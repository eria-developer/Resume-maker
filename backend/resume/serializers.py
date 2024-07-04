from rest_framework import serializers
from . import models
from rest_framework.response import Response
from django.contrib.auth import get_user_model




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


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