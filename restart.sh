kill -TERM $(cat 1.pid)
kill -TERM $(cat 2.pid)

gunicorn -c /home/box/web/etc/gunicorn.py  hello:application
gunicorn -c /home/box/web/etc/qa.py        ask.wsgi:application
