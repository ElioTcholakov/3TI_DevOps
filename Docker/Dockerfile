FROM ubuntu:latest

CMD [ "a2enmod", "rewrite" ]

CMD [ "systemctl", "restart", "apache2" ]  

CMD [ "sed", "'s/^Listen 80$/Listen 8081/'", "/etc/apache2/ports.conf" ]

CMD [ "sed", "'s/^<VirtualHost \*:80>$/<VirtualHost \*:8021>/'", "/etc/apache2/sites-available/000-default.conf " ]

CMD [ "/etc/init.d/apache2", "restart " ]

CMD [ "echo", "Success" ]


