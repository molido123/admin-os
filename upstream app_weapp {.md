upstream app_weapp {
    server localhost:5000;
    keepalive 8;
server {
    listen      80;
    #=====需要修改=========替换成自己的域名
    server_name yakui114514.xyz;
    #服务器自动把 HTTP 的请求重定向到 HTTPS
    rewrite ^(.*)$ https://$server_name$1 permanent;
}

server {
    listen      443;
    #=====需要修改=========替换成自己的域名
    server_name yakui114514.xyz;
    ssl on;
    #=====需要修改=========下面两行替换成自己SSL文件的路径
    ssl_certificate           /etc/nginx/ssl/yakui114514.xyz_bundle.crt;
    ssl_certificate_key       /etc/nginx/ssl/yakui114514.xyz.key;
    ssl_session_timeout       5m;
    ssl_protocols             TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers               ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA;
    ssl_session_cache         shared:SSL:50m;
    ssl_prefer_server_ciphers on;
    location / {
        proxy_pass http://app_weapp;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

