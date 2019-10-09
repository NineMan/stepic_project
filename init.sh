# setting for nginx

sudo rm -r /etc/nginx/sites-enabled/*
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart


# settings for gunicorn

# ----------------- Ver 5 -------------------------
sudo rm -r /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/gunicorn.py   /etc/gunicorn.d/gunicorn.py
sudo ln -sf /home/box/web/etc/qa.py         /etc/gunicorn.d/qa.py
cd /home/box/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
# sudo /etc/init.d/gunicorn restart


# setting for mysql

sudo /etc/init.d/mysql restart
mysql -uroot -e "DROP DATABASE ASK"
mysql -uroot -e "DROP USER sa@localhost"
mysql -uroot -e "CREATE DATABASE ASK"
mysql -uroot -e "CREATE USER 'sa'@'localhost' IDENTIFIED BY 'sa'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ASK.* TO 'sa'@'localhost'"

python3 /home/box/web/ask/manage.py makemigrations qa
# python /home/box/web/ask/manage.py makemigrations qa
python3 /home/box/web/ask/manage.py migrate qa
# python /home/box/web/ask/manage.py migrate qa




# ----------------- setting for gunicorn
# ----------------- Ver 1 -------------------------
# sudo ln -s       /home/box/web/etc/gunicorn.py /etc/gunicorn.d/gunicorn.py
# cd /home/box/web
# sudo gunicorn -c /home/box/web/etc/gunicorn.py hello:application
# ----------------- Ver 2 -------------------------
# sudo gunicorn -b 0.0.0.0:8080 hello:application
# ----------------- Ver 3 -------------------------
# cd /home/box/web
# gunicorn --bind='0.0.0.0:8080' hello:application
# ----------------- Ver 4 -------------------------
# sudo ln -s       /home/box/web/etc/gunicorn1.py /etc/gunicorn.d/gunicorn.py
# sudo gunicorn -c /home/box/web/etc/gunicorn1.py
# ----------------- Ver 5 -------------------------
# sudo rm -r /etc/gunicorn.d/*
# sudo ln -sf /home/box/web/etc/gunicorn.py   /etc/gunicorn.d/gunicorn.py
# sudo ln -sf /home/box/web/etc/qa.py         /etc/gunicorn.d/qa.py
# sudo /etc/init.d/gunicorn restart

