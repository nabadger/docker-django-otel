# Sleep for db ;)
sleep 15

export DJANGO_SETTINGS_MODULE=project.settings
export PYTHONPATH="/app:/opt/venv"
export OTEL_METRICS_EXPORTER=none
export OTEL_TRACES_EXPORTER=console

/opt/venv/bin/python manage.py makemigrations
/opt/venv/bin/python manage.py migrate
/opt/venv/bin/python manage.py loaddata initialstrings

# Dump out traces locally to console (disable metrics_exporter else it crashes out)

# Test runserver
/opt/venv/bin/opentelemetry-instrument /opt/venv/bin/python manage.py runserver 0.0.0.0:8000 --noreload


# Test gunicorn
#/opt/venv/bin/opentelemetry-instrument --log_level=debug /opt/venv/bin/gunicorn -c ./gunicorn_conf.py wsgi:application -b "0.0.0.0:8000"
