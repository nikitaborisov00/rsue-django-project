from venv import create
from rest_framework import serializers

from .models import GradeItem, GradeResult


class GradeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeItem
        fields = ('date',)


class GradeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeResult
        fields = '__all__'
        validators = []

    def create(self, validated_data):
        student = validated_data['student']
        grade_item = validated_data['grade_item']
        score = validated_data['score']
        grade_result, created = GradeResult.objects.update_or_create(
            student=student,
            grade_item=grade_item,
            defaults={'score': score}
        )
        return grade_result

class ResultSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    grade_item__grade_service_set__check_point = serializers.IntegerField()
    result = serializers.DecimalField(max_digits=3, decimal_places=1)
