# setting for nginx

sudo rm -r /etc/nginx/sites-enabled/*
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart


# settings for gunicorn

# --- for stepic ---
# sudo rm -r /etc/gunicorn.d/*
# sudo ln -sf /home/box/web/etc/gunicorn-stepic.py   /etc/gunicorn.d/gunicorn.py
# sudo ln -sf /home/box/web/etc/qa-stepic.py         /etc/gunicorn.d/qa.py
# cd /home/box/web/ask
# sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
# sudo /etc/init.d/gunicorn restart

# --- for local ---
gunicorn -c /home/box/web/etc/gunicorn.py  hello:application 
gunicorn -c /home/box/web/etc/qa.py        ask.wsgi:application


# setting for mysql

# --- for local ---
# for: ERROR 1698 (28000): Access denied for user 'root'@'localhost'
# http://qaru.site/questions/161543/error-1698-28000-access-denied-for-user-rootlocalhost


# --- for all ---
 sudo /etc/init.d/mysql restart
 mysql -uroot -e "DROP DATABASE IF EXISTS ASK"
 mysql -uroot -e "DROP USER IF EXISTS sa@localhost"
 mysql -uroot -e "CREATE DATABASE ASK"
 mysql -uroot -e "CREATE USER 'sa'@'localhost' IDENTIFIED BY 'sa'"
 mysql -uroot -e "GRANT ALL PRIVILEGES ON ASK.* TO 'sa'@'localhost'"
# sudo service mysql stop


# --- for stepic ---
# python3 /home/box/web/ask/manage.py makemigrations qa
# python3 /home/box/web/ask/manage.py migrate qa

# --- for local ---
 python /home/box/web/ask/manage.py makemigrations qa
 python /home/box/web/ask/manage.py migrate qa


