import os
import sys
import site

# Należy zmienić ścieżkę konfiguracji do site-packages na własną według wzoru
site.addsitedir('C:/Users/adek/AppData/Local/Programs/Python/Python311/Lib/site-packages')

# Należy zmienić ścieżkę konfiguracji do projektu i folderu app w projekcie na własną według wzoru
sys.path.append('C:/Adek/Projekty/open-blog-wamp')
sys.path.append('C:/Adek/Projekty/open-blog-wamp/app')

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
