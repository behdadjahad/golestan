from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.faculty.models import Faculty

from golestan.account.services.faculties import *
from golestan.account.selectors.faculties import *

from drf_spectacular.utils import extend_schema

class FacultiesApi(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputFacultiesSerialiser(serializers.Serializer):

        name = serializers.CharField(max_length=100)


    class OutputFacultiesSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Faculty
            # fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            fields = "__all__"
        
    @extend_schema(request=InputFacultiesSerialiser, responses=OutputFacultiesSerialiser)
    def post(self, request):
        
        serializer = self.InputFacultiesSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_faculty(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputFacultiesSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputFacultiesSerialiser)
    def get(self, request):
        query = get_faculties()
        return Response(self.OutputFacultiesSerialiser(query, context={"request":request}, many=True).data)



class FacultyDetailApi(APIView):

    class OutputFacultySerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Faculty
            fields = ("name",)
            # fields = "__all__"
        

    @extend_schema(responses=OutputFacultySerialiser)
    def get(self, request, id):

        try:
            query = get_faculty_detail(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputFacultySerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputFacultySerialiser)
    def put(self, request, id):
        pass

    @extend_schema(responses=OutputFacultySerialiser)
    def delete(self, request, id):
        try:
            query = delete_faculty(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputFacultySerialiser(query, context={"request":request}).data)