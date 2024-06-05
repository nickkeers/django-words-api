from .apiviews import UserCreate, LanguageList, WordsAPIViewSet, LoginView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"languages/(?P<language_id>\d+)/words",
                WordsAPIViewSet, basename="words")


urlpatterns = [
    path("languages/", LanguageList.as_view(), name="language_list"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]

urlpatterns += router.urls
