# instamarket
اپ فروش آنلاین


create a venv:
```bash
python -m venv venv
```
activate it in linux:
```bash
source ./venv/bin/avtivate
```
activate it in windows:
```bash
./venv/Scripts/avtivate.bat
```
install requirement:
```python
pip install -r requirements.txt
```

put your site root address,'/' , '/instamarket/' eg:
```python
echo "SITE_URL='/'" >> instamarket/server_settings.py
```
or

```python
echo "SITE_URL='/instamarket/'" >> instamarket/server_settings.py
```
generate and view secret key:
```python
rm instamarket/secret_key.py
echo "SECRET_KEY='INITIAL_VALUE'" >> instamarket/secret_key.py
python manage.py djecrety
```
put it in specific file:
```bash
echo "SECRET_KEY='put_generated_secret_key_here'" >> instamarket/secret_key.py
```


put my sql db credential in files like right below:

```
[client]
database = your_database_name
host = your_host_name
user = your_user_name
password = your_password
default-character-set = utf8
```
for production:
```bash
rm instamarket/secret_my_sql.cnf
echo "[client]">> instamarket/secret_my_sql.cnf
echo "database = your_database_name">> instamarket/secret_my_sql.cnf
echo "host = your_host_name">> instamarket/secret_my_sql.cnf
echo "user = your_user_name">> instamarket/secret_my_sql.cnf
echo "password = your_password">> instamarket/secret_my_sql.cnf
echo "default-character-set = utf8" >> instamarket/secret_my_sql.cnf
```



migrate : 
```python
python manage.py migrate
```

create superuser : 
```python
python manage.py createsuperuser
```

collectstatic : 
```python
python manage.py collectstatic
```
