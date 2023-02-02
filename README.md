# Docker Django Otel

Spin up a minimal compose stack with django and a db.

## Usage

```
docker-compose up
```

Browse to http://localhost:8000 - you should see output from a few db-selects

## Testing MySQL Bug

Currently manage.py tries to init mysql tracing in `__main__`.

The goal here is to trace mysql calls using `mysqlclient` rather than the python-native mysql db-api (for performance reasons)

This fails straight away:

```
trace_integration(MySQLdb, "connect", "mysql")
```

```
webapp_1  |     self.connection.autocommit(autocommit)
webapp_1  |   File "/opt/venv/lib/python3.9/site-packages/django/db/utils.py", line 91, in __exit__
webapp_1  |     raise dj_exc_value.with_traceback(traceback) from exc_value
webapp_1  |   File "/opt/venv/lib/python3.9/site-packages/django/db/backends/mysql/base.py", line 289, in _set_autocommit
webapp_1  |     self.connection.autocommit(autocommit)
webapp_1  |   File "/opt/venv/lib/python3.9/site-packages/MySQLdb/connections.py", line 238, in autocommit
webapp_1  |     if self.get_autocommit() != on:
webapp_1  | django.db.utils.OperationalError: (2006, '')
```

## Notes

`run.sh` starts django using `runserver` and applies auto-instrumentation. Spans are dumped to console.



