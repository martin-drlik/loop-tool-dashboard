from rest_framework.serializers import ModelSerializer

from olap.models import FactCourseVisit


class FactCourseVisitSerializer(ModelSerializer):
    class Meta:
        model = FactCourseVisit
        fields = '__all__' # TODO: Update this to specify exact fields to return