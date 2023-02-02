import os

projdir = os.environ.get("PROJDIR")
logdir = os.environ.get("LOGDIR")
pidfile = os.environ.get("PIDFILE")

name = "django-otel"

worker_class = os.getenv("GUNICORN_WORKER_CLASS", "sync")
workers = int(os.getenv("GUNICORN_WORKER_COUNT", 2))
threads = int(os.getenv("GUNICORN_WORKER_THREADS", 1))
worker_connections = int(os.getenv("GUNICORN_WORKER_CONNECTIONS", 1000))
worker_tmp_dir = "/dev/shm/"  # nosec B108

from socket import gethostname  # noqa: E402 isort:skip

hostname = gethostname()
preload = True

timeout = int(os.environ.get("GUNICORN_TIMEOUT", 300))
graceful_timeout = int(os.environ.get("GUNICORN_GRACEFUL_TIMEOUT", 30))
max_requests = int(os.environ.get("GUNICORN_MAX_REQ", 1000))

#def post_worker_init(worker):
#    import MySQLdb
#    from opentelemetry.instrumentation.auto_instrumentation import sitecustomize
#    from opentelemetry.instrumentation.dbapi import trace_integration
##   trace_integration(MySQLdb, "connect", "mysql")
