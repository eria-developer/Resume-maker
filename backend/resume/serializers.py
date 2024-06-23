from rest_framework import serializers
from . import models
from rest_framework.response import Response


def create_standard_response(status, message, data=None):
    response = {
        'status': status,
        'message': message,
    }
    if data is not None:
        response['data'] = data
    return Response(response)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification
        fields = "__all__"


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = "__all__"


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leadership
        fields = "__all__"