from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProfileViewSet, EducationViewSet, ExperienceViewSet, SkillViewSet,
                    LeadershipViewSet, ReferenceViewSet, CertificationViewSet, ProjectViewSet, LanguageViewSet, UserRegistrationView, UserLoginView)

router = DefaultRouter()
# router.register(r"register", UserRegistrationView)
# router.register(r"login", UserLoginView)
router.register(r'profiles', ProfileViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'leaderships', LeadershipViewSet)
router.register(r'references', ReferenceViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'languages', LanguageViewSet)



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]

urlpatterns += router.urls
