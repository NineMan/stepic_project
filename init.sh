# setting for nginx

#sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart



# settings for gunicorn

sudo ln -s /home/box/web/etc/gunicorn.py /etc/gunicorn.d/gunicorn.py

# sudo gunicorn -b 0.0.0.0:8080 gunicorn hello:application

cd /home/box/web
sudo gunicorn -c /home/box/web/etc/gunicorn.py hello:application


# setting for mysql

