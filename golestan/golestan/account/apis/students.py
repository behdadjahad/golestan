from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.account.models import Student

from golestan.account.services.students import *
from golestan.account.selectors.students import *

from drf_spectacular.utils import extend_schema

class StudentApi(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputSerialiser(serializers.Serializer):
        password = serializers.CharField(max_length=255)
        email = serializers.EmailField()
        first_name = serializers.CharField(max_length=255)
        last_name = serializers.CharField(max_length=255)
        account_number = serializers.CharField(max_length=9)
        phone_number = serializers.CharField(max_length=11)
        national_id = serializers.CharField(max_length=10)
        birth_date = serializers.DateField()
        gender = serializers.CharField(max_length=1)
        entrance_year = serializers.DateField()
        entrance_term = serializers.CharField(max_length=225)
        military_service_status = serializers.CharField(max_length=20)
        faculty = serializers.IntegerField()
        major = serializers.IntegerField()

    class OutputSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Student
            # fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            fields = "__all__"
        
    @extend_schema(request=InputSerialiser, responses=OutputSerialiser)
    def post(self, request):
        
        serializer = self.InputSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_student(first_name=serializer.validated_data.get("first_name"),
                                   last_name=serializer.validated_data.get("last_name"),
                                   account_number=serializer.validated_data.get("account_number"),
                                   phone_number=serializer.validated_data.get("phone_number"),
                                   national_id=serializer.validated_data.get("national_id"),
                                   birth_date=serializer.validated_data.get("birth_date"),
                                   gender=serializer.validated_data.get("gender"),
                                   military_service_status=serializer.validated_data.get("military_service_status"),
                                   entrance_year=serializer.validated_data.get("entrance_year"),
                                   entrance_term=serializer.validated_data.get("entrance_term"),
                                   email=serializer.validated_data.get("email"),
                                   password=serializer.validated_data.get("password"),
                                   faculty=serializer.validated_data.get("faculty"),
                                   major=serializer.validated_data.get("major"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputSerialiser)
    def get(self, request):
        query = get_students()
        return Response(self.OutputSerialiser(query, context={"request":request}, many=True).data)

class StudentDetailApi(APIView):

    class OutputSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Student
            fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            # fields = "__all__"
        

    @extend_schema(responses=OutputSerialiser)
    def get(self, request, id):

        try:
            query = get_student_detail(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputSerialiser)
    def put(self, request, id):
        pass

    @extend_schema(responses=OutputSerialiser)
    def delete(self, request, id):
        try:
            query = delete_student(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputSerialiser(query, context={"request":request}).data)