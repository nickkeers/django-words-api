from .apiviews import WordsList, LanguageList, WordsAPIViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"languages/(?P<language_id>\d+)/words",
                WordsAPIViewSet, basename="words")


urlpatterns = [
    path("languages/", LanguageList.as_view(), name="language_list"),
]

urlpatterns += router.urls
