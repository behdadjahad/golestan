from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.account.models import EducationalAssistant

from golestan.account.services.assistants import *
from golestan.account.selectors.assistants import *

from drf_spectacular.utils import extend_schema

class AssistantApi(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputAssistantsSerialiser(serializers.Serializer):
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

    class OutputAsistantsSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = EducationalAssistant
            # fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            fields = "__all__"
        
    @extend_schema(request=InputAssistantsSerialiser, responses=OutputAsistantsSerialiser)
    def post(self, request):
        
        serializer = self.InputAssistantsSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_assistant(first_name=serializer.validated_data.get("first_name"),
                                     last_name=serializer.validated_data.get("last_name"),
                                     account_number=serializer.validated_data.get("account_number"),
                                     phone_number=serializer.validated_data.get("phone_number"),
                                     national_id=serializer.validated_data.get("national_id"),
                                     birth_date=serializer.validated_data.get("birth_date"),
                                     gender=serializer.validated_data.get("gender"),
                                     email=serializer.validated_data.get("email"),
                                     password=serializer.validated_data.get("password"),
                                     faculty=serializer.validated_data.get("faculty"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputAsistantsSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputAsistantsSerialiser)
    def get(self, request):
        query = get_assistants()
        return Response(self.OutputAsistantsSerialiser(query, context={"request":request}, many=True).data)



class AsistantDetailApi(APIView):

    class OutputAssistantSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = EducationalAssistant
            fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            # fields = "__all__"
        

    @extend_schema(responses=OutputAssistantSerialiser)
    def get(self, request, id):

        try:
            query = get_assistant_detail(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputAssistantSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputAssistantSerialiser)
    def put(self, request, id):
        pass

    @extend_schema(responses=OutputAssistantSerialiser)
    def delete(self, request, id):
        try:
            query = delete_assistant(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputAssistantSerialiser(query, context={"request":request}).data)