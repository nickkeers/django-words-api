from rest_framework import generics, viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied


from .models import Word, Language
from .serializers import WordSerializer, LanguageSerializer, UserSerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class WordsAPIViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer

    def destroy(self, request, *args, **kwargs):
        word = Word.objects.get(id=kwargs["pk"])
        if not request.user == word.created_by:
            raise PermissionDenied("You can not delete this word")
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        # we set language_id earlier
        language_id = self.kwargs["language_id"]
        return Word.objects.filter(language_id=language_id)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
