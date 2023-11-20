from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.account.models import Professor

from golestan.account.services.professors import *
from golestan.account.selectors.professors import *

from drf_spectacular.utils import extend_schema

class ProfessorApi(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputProfessorsSerialiser(serializers.Serializer):
        password = serializers.CharField(max_length=255)
        email = serializers.EmailField()
        first_name = serializers.CharField(max_length=255)
        last_name = serializers.CharField(max_length=255)
        account_number = serializers.CharField(max_length=9)
        phone_number = serializers.CharField(max_length=11)
        national_id = serializers.CharField(max_length=10)
        birth_date = serializers.DateField()
        gender = serializers.CharField(max_length=1)
        faculty = serializers.IntegerField()
        major = serializers.IntegerField()
        expertise = serializers.CharField(max_length=100)
        degree = serializers.CharField(max_length=100)


    class OutputProfessorsSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Professor
            # fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            fields = "__all__"
        
    @extend_schema(request=InputProfessorsSerialiser, responses=OutputProfessorsSerialiser)
    def post(self, request):
        
        serializer = self.InputProfessorsSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_professor(first_name=serializer.validated_data.get("first_name"),
                                     last_name=serializer.validated_data.get("last_name"),
                                     account_number=serializer.validated_data.get("account_number"),
                                     phone_number=serializer.validated_data.get("phone_number"),
                                     national_id=serializer.validated_data.get("national_id"),
                                     birth_date=serializer.validated_data.get("birth_date"),
                                     gender=serializer.validated_data.get("gender"),
                                     email=serializer.validated_data.get("email"),
                                     password=serializer.validated_data.get("password"),
                                     faculty=serializer.validated_data.get("faculty"),
                                     major=serializer.validated_data.get("major"),
                                     expertise=serializer.validated_data.get("expertise"),
                                     degree=serializer.validated_data.get("degree"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputProfessorsSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputProfessorsSerialiser)
    def get(self, request):
        query = get_professors()
        return Response(self.OutputProfessorsSerialiser(query, context={"request":request}, many=True).data)



class ProfessorDetailApi(APIView):

    class OutputProfessorSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Professor
            fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            # fields = "__all__"
        

    @extend_schema(responses=OutputProfessorSerialiser)
    def get(self, request, id):

        try:
            query = get_professor_detail(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputProfessorSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputProfessorSerialiser)
    def put(self, request, id):
        pass

    @extend_schema(responses=OutputProfessorSerialiser)
    def delete(self, request, id):
        try:
            query = delete_professor(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputProfessorSerialiser(query, context={"request":request}).data)