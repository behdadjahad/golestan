from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from golestan.api.pagination import LimitOffsetPagination
from golestan.term.models import Term

from golestan.account.services.terms import *
from golestan.account.selectors.terms import *

from drf_spectacular.utils import extend_schema

class TermsApi(APIView):


    class Pagination(LimitOffsetPagination):
        pass


    class InputTermsSerialiser(serializers.Serializer):

        term_name = serializers.CharField(max_length=100)
        unit_selection_start_time = serializers.DateTimeField()
        unit_selection_end_time = serializers.DateTimeField()
        courses_start_time = serializers.DateField()
        courses_end_time = serializers.DateField()
        repairing_unit_selection_start_time = serializers.DateTimeField()
        repairing_unit_selection_end_time = serializers.DateTimeField()
        emergency_deletion_start_time = serializers.DateTimeField()
        emergency_deletion_end_time = serializers.DateTimeField()
        exams_start_time = serializers.DateField()
        term_end_time = serializers.DateField()

        

    class OutputTermsSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Term
            # fields = ("first_name", "last_name", "email", "account_number", "national_id", "gender", "created_at", "updated_at")
            fields = "__all__"
        
    @extend_schema(request=InputTermsSerialiser, responses=OutputTermsSerialiser)
    def post(self, request):
        
        serializer = self.InputTermsSerialiser(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            query = create_term(term_name=serializer.validated_data.get("term_name"),
                                unit_selection_start_time=serializer.validated_data.get("unit_selection_start_time"),
                                unit_selection_end_time=serializer.validated_data.get("unit_selection_end_time"),
                                courses_start_time=serializer.validated_data.get("courses_start_time"),
                                courses_end_time=serializer.validated_data.get("courses_end_time"),
                                repairing_unit_selection_start_time=serializer.validated_data.get("repairing_unit_selection_start_time"),
                                repairing_unit_selection_end_time=serializer.validated_data.get("repairing_unit_selection_end_time"),
                                emergency_deletion_start_time=serializer.validated_data.get("emergency_deletion_start_time") ,
                                emergency_deletion_end_time=serializer.validated_data.get("emergency_deletion_end_time"),
                                exams_start_time=serializer.validated_data.get("exams_start_time"),
                                term_end_time=serializer.validated_data.get("term_end_time"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputTermsSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputTermsSerialiser)
    def get(self, request):
        query = get_terms()
        return Response(self.OutputTermsSerialiser(query, context={"request":request}, many=True).data)



class TermDetailApi(APIView):

    class OutputTermSerialiser(serializers.ModelSerializer):
        
        class Meta:
            model = Term
            fields = ("term_name",)
            # fields = "__all__"
        

    @extend_schema(responses=OutputTermSerialiser)
    def get(self, request, id):

        try:
            query = get_term_detail(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputTermSerialiser(query, context={"request":request}).data)
    
    @extend_schema(responses=OutputTermSerialiser)
    def put(self, request, id):
        pass

    @extend_schema(responses=OutputTermSerialiser)
    def delete(self, request, id):
        try:
            query = delete_term(id=id)
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutputTermSerialiser(query, context={"request":request}).data)