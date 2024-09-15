release: python3 manage.py collectstatic --noinput && python3 manage.py migrate --noinput
web: gunicorn <nama_project>.wsgi