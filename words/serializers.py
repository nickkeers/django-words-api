from rest_framework import serializers
from .models import Word, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"