# Open-blog
 
 Klient aplikacji blog dla stosu technologicznego WAMP (Windows, Apache, MySQL, Python) napisany w języku Python na platformie programistycznej Django
 
### Wymagania
 - Python 3+
 - Platforma Django
 - WampServer (należy po uruchomieniu, pod adresem ```http://localhost/phpmyadmin/``` utworzyć bazę danych o nazwie ```chat```)
 - Visual Studio for C++ (najnowsze wersje)

### Uruchomienie
 Należy uruchomić komendę ```python manage.py migrate``` w głównym folderze projektu, następnie zainstalować mod_wsgi. Komendą w wierszu polecenia ```set MOD_WSGI_APACHE_ROOTDIR=C:\wamp64\bin\apache\apache2.4.46``` ustawiamy miejsce instalacji apache (miejsce oraz wersja mogą się różnić), następnie zatwierdzamy ```pip install mod-wsgi```.
 
Należy zmienić konfigurację  ```...open-blog-wamp/app/wsgi.py``` według zawartych instrukcji
 
Następnie do pliku konfiguracyjnego w miejscu instalacji WampServer ``/wamp64/bin/apache/apache2.4.46/conf/httpd.conf``` na końcu pliku dodajemy 
```
LoadFile "<ścieżka pliku Python, np .../Python311/python311.dll"
LoadModule wsgi_module "<ścieżka instalacji wsgi np ...Python/Python311/Lib/site-packages/mod_wsgi/server/mod_wsgi.cp311-win_amd64.pyd>"
WSGIPythonHome "<ścieżka instalacji Python np ...AppData/Local/Programs/Python/Python311>"
WSGIPythonPath "<ścieżka do folderu głównego projektu np ...open-blog-wamp/>"
WSGIScriptAlias / "<ścieżka do konfiguracji wsgi w projekcie np ...open-blog-wamp/app/wsgi.py>"

<Directory "<ścieżka do głównego folderu projektu np ...open-blog-wamp>">
	<Files wsgi.py>
		Require all granted
	</Files>
	Order deny,allow
	Allow from all
</Directory>

<Directory "<ścieżka do konfiguracji w projekcie np ...open-blog-wamp/app>">
   Allow from all
   Order allow,deny
</Directory>

Alias /static/ "<ścieżka do plików statycznych w projekcie np ...open-blog-wamp/chat/static/>"

<Directory "<cieżka do plików statycznych w projekcie np ...open-blog-wamp/chat/static>">
    Require all granted
</Directory>

Alias /favicon.ico "<cieżka do pliku favicon.ico w projekcie np ...open-blog-wamp/chat/static/favicon/favicon.ico>"

<Directory "<cieżka do plików CSS w projekcie np ...open-blog-wamp/chat/static/css/>">
    <Files *.css>
        Header set Content-type "text/css"
    </Files>
</Directory>
```

Po uruchomieniu WampServer aplikacja znajdować się będzie pod adresem ```localhost```
