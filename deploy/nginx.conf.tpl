server {
    listen ${nginx:port}
    server_name ${buildout:domain};
    location /s/ {
        root ${buildout:directory}/${config:DJ_PROJECT}/static/;
        expires 30d;
        access_log off;
        rewrite ^/s/(.*) /\$1 break;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass ${uwsgi:connection};
        root ${buildout:directory};
    }

    charset utf-8;
    access_log  ${nginx:access_log}
    error_log   ${nginx:error_log}
    client_max_body_size 300m;
}
