[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/LMS/lms-project
/ExecStart=/home/ubuntu/LMS/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          LMS.wsgi:application

[Install]
WantedBy=multi-user.target


[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

server {
    listen 80;
    server_name 13.127.240.19 ;

    location = /favicon.ico { access_log off; log_not_found off; }
  
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    location /static/ {
        root /home/ubuntu/LS/lms-project/staticfiles;
    }
}


[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/LMS/lms-project
ExecStart=/home/ubuntu/LMS/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          LMS.wsgi:application

[Install]
WantedBy=multi-user.target