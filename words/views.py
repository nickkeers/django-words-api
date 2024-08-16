from django.shortcuts import render
from django.views import View
from .models import Language, Word
from django.db.models import Count

class LanguageListView(View):
    def get(self, request):
        languages = Language.objects.annotate(word_count=Count('word'))
        context = {
            'languages': languages
        }
        return render(request, 'language_list.html', context)
