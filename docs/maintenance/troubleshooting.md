# Troubleshooting

## Logging

In its default configuration your auth project logs INFO and above messages to myauth/log/allianceauth.log. If you're encountering issues it's a good idea to view DEBUG messages as these greatly assist the troubleshooting process. These are printed to the console with manually starting the webserver via `python manage.py runserver`.

To record DEBUG messages in the log file, alter a setting in your auth project's settings file: `LOGGING['handlers']['log_file']['level'] = 'DEBUG'`. After restarting gunicorn and celery your log file will record all logging messages.

## Common Problems

### I'm getting an error 500 trying to connect to the website on a new install

*Great.* Error 500 is the generic message given by your web server when *anything* breaks. The actual error message is hidden in one of your auth project's log files. Read them to identify it.

### Failed to configure log handler

Make sure the log directory is writeable by the allianceserver user: `chmown -R allianceserver:allianceserver /path/to/myauth/log/`, then restart the auth supervisor processes.

### Groups aren't syncing to services

Make sure the background processes are running: `supervisorctl status myauth:`. If `myauth:worker` or `myauth:beat` do not show `RUNNING` read their log files to identify why.

### Task queue is way too large

Stop celery workers with `supervisorctl stop myauth:worker` then clear the queue:

```bash
    redis-cli FLUSHALL
    celery -A myauth worker --purge
```

Press Control+C once.

Now start the worker again with `supervisorctl start myauth:worker`

### Proxy timeout when entering email address

This usually indicates an issue with your email settings. Ensure these are correct and your email server/service is properly configured.

### No images are available to users accessing the website

This is likely due to a permissions mismatch. Check the setup guide for your web server. Additionally ensure the user who owns `/var/www/myauth/static` is the same user as running your webserver, as this can be non-standard.

### Unable to execute 'gunicorn myauth.wsgi' or ImportError: No module named 'myauth.wsgi'

Gunicorn needs to have context for its running location, `/home/alllianceserver/myauth/gunicorn myauth.wsgi` will not work, instead `cd /home/alllianceserver/myauth` then `gunicorn myauth.wsgi` is needed to boot Gunicorn. This is handled in the Supervisor config, but this may be encountered running Gunicorn manually for testing.

### Specified key was too long error

Migrations may about with the following error message:

```bash
Specified key was too long; max key length is 767 bytes
```

This error will occur if one is trying to use Maria DB prior to 10.2.x, which is not compatible with Alliance Auth.

Install a never Maria DB version to fix this issue another DBMS supported by Django 2.2.
