from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.account.models import Student

from golestan.account.services.students import create_student
from golestan.account.selectors.students import get_students

from drf_spectacular.utils import extend_schema

class StudentApiForItManager(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputSerialiser(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField(max_length=255)
        last_name = serializers.CharField(max_length=255)
        account_number = serializers.CharField(max_length=9)
        phone_number = serializers.CharField(max_length=11)
        national_id = serializers.CharField(max_length=10)
        birth_date = serializers.DateField()
        gender = serializers.CharField(max_length=1)
        intrance_year = serializers.DateField()
        militery_service_status = serializers.CharField(max_length=20)

    class OutputSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Student
            fields = ("first_name", "last_name", "email", "account_number", "national_id", "created_at", "updated_at")
        
    @extend_schema(request=InputSerialiser, responses=OutputSerialiser)
    def post(self, request):
        
        serializer = self.InputSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_student(serializer.validated_data.get("first_name"),
                                   serializer.validated_data.get("last_name"),
                                   serializer.validated_data.get("account_number"),
                                   serializer.validated_data.get("national_id"),
                                   serializer.validated_data.get("birth_date"),
                                   serializer.validated_data.get("gender"),
                                   serializer.validated_data.get("militery_service_status"),
                                   serializer.validated_data.get("intrance_year"),
                                   serializer.validated_data.get("email"),
                                   serializer.validated_data.get("phone_number"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputSerialiser)
    def get(self, request):
        query = get_students()
        return Response(self.OutputSerialiser(query, context={"request":request}, many=True).data)

    def put(self, request):
        pass
    
    def delete(self, request):
        pass