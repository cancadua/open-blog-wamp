import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/adek/AppData/Local/Programs/Python/Python311/Lib/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Adek/Projekty/open-blog-wamp')
sys.path.append('C:/Adek/Projekty/open-blog-wamp/app')

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
