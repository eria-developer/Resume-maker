from django.urls import path
from .views import (
    ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView,
    EducationListCreateAPIView, EducationRetrieveUpdateDestroyAPIView,
    ExperienceListCreateAPIView, ExperienceRetrieveUpdateDestroyAPIView,
    SkillListCreateAPIView, SkillRetrieveUpdateDestroyAPIView,
    LeadershipListCreateAPIView, LeadershipRetrieveUpdateDestroyAPIView,
    ReferenceListCreateAPIView, ReferenceRetrieveUpdateDestroyAPIView,
    CertificationListCreateAPIView, CertificationRetrieveUpdateDestroyAPIView,
    ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView,
    LanguageListCreateAPIView, LanguageRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # profile urls 
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),

    # education urls 
    path('educations/', EducationListCreateAPIView.as_view(), name='education-list-create'),
    path('educations/<int:pk>/', EducationRetrieveUpdateDestroyAPIView.as_view(), name='education-detail'),

    # experience urls 
    path('experiences/', ExperienceListCreateAPIView.as_view(), name='experience-list-create'),
    path('experiences/<int:pk>/', ExperienceRetrieveUpdateDestroyAPIView.as_view(), name='experience-detail'),

    # skills urls 
    path('skills/', SkillListCreateAPIView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyAPIView.as_view(), name='skill-detail'),

    # leadership urls 
    path('leaderships/', LeadershipListCreateAPIView.as_view(), name='leadership-list-create'),
    path('leaderships/<int:pk>/', LeadershipRetrieveUpdateDestroyAPIView.as_view(), name='leadership-detail'),

    # references urls 
    path('references/', ReferenceListCreateAPIView.as_view(), name='reference-list-create'),
    path('references/<int:pk>/', ReferenceRetrieveUpdateDestroyAPIView.as_view(), name='reference-detail'),

    # certifications urls 
    path('certifications/', CertificationListCreateAPIView.as_view(), name='certification-list-create'),
    path('certifications/<int:pk>/', CertificationRetrieveUpdateDestroyAPIView.as_view(), name='certification-detail'),

    # projects urls 
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),

    # language urls 
    path('languages/', LanguageListCreateAPIView.as_view(), name='language-list-create'),
    path('languages/<int:pk>/', LanguageRetrieveUpdateDestroyAPIView.as_view(), name='language-detail'),
]
