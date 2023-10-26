from django.conf import settings
from profiles.decorators import load_profile_when_im_authenticated

import os

class LanguageObject(object):
    def __init__(self, language: str) -> None:
        """
            @description: The language class objects.
        """
        self.language = language

    def get_index_src(self):
        """
            @description: 
        """
        language_path = self.language
        if self.language == 'en':
            language_path = 'en-US'
        return os.path.join(language_path, 'index.html') 

def __loadlanguage_authenticated(request):
    """
        @description: 
    """
    if not request.user.is_authenticated:
        return
        
    load_profile_when_im_authenticated(request)
    if request.profile is None:
        return
    request.language = LanguageObject(request.profile.language)

def __loadlanguage_not_authenticated(request):
    """
        @description: 

    """
    if request.user.is_authenticated:
        return
    
    request.language = LanguageObject('en')
    request.META['HTTP_ACCEPT_LANGUAGE']
    HTTP_ACCEPT_LANGUAGE = request.META['HTTP_ACCEPT_LANGUAGE'].split(',')
    language = ''

    if 'language' in request.COOKIES:
        language = request.COOKIES['language']
        if language not in settings.LANGUAGE_LIST:
            language = settings.DEFAULT_LANGUAGE
        request.language = LanguageObject(language)
        return
        
    for line in HTTP_ACCEPT_LANGUAGE:
        line = line.split('-')
        if len(line) == 1:
            continue

        language = line[1].split(';')[0].lower()
        break

    if language not in settings.LANGUAGE_LIST:
        request.language = LanguageObject(settings.DEFAULT_LANGUAGE)
        return
    
    request.language = LanguageObject(language)


def load_languages(function):
    """
        @description: Charger la bonne langue au bon moment.
    """
    def wrap(request, *args, **kwargs):
        """
            @description: Est destiner à la récupérations automatique des informations concernants le group zone demander.
        """
        __loadlanguage_not_authenticated(request)        
        __loadlanguage_authenticated(request)
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap