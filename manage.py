#!/usr/bin/env python
import os
import sys

import MySQLdb
from opentelemetry.instrumentation.dbapi import trace_integration

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Causes 2006 server gone away as autocommit does not appear to be handled correctl
    # Idea is to use this in conjunction with 'django.db.backends.mysql' that we make use of 
    # C extension for DB calls (otherwise there will be a significant perf. hit if we switch
    # to the python native impl.)


    argv = sys.argv
    cmd = argv[1] if len(argv) > 1 else None
    if cmd == "runserver":
        trace_integration(MySQLdb, "connect", "mysql")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
