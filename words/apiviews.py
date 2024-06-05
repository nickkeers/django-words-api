from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Word, Language
from .serializers import WordSerializer, LanguageSerializer


class WordsList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = "language_id"


class CreateWord(APIView):
    def post(self, request, language_id):
        language = get_object_or_404(Language, id=language_id)
        data = request.data
        data["language"] = language.id
        serializer = WordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    serializer_class = WordSerializer



class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class WordsAPIViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer

    def get_queryset(self):
        # we set language_id earlier
        language_id = self.kwargs["language_id"]
        return Word.objects.filter(language_id=language_id)
