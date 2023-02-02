# Docker Django Otel

Spin up a minimal compose stack with django and a db.

## Usage

```
docker-compose up
```

Browse to http://localhost:8000 - you should see output from a few db-selects

## Notes

`run.sh` starts django using `runserver` and applies auto-instrumentation. Spans are dumped to console.



