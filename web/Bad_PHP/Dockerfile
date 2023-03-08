FROM php:5.6.40-apache

COPY challenge/App/ /var/www/html/
RUN mkdir -p /var/www/html/uploads
RUN chmod -R 777 /var/www/html/uploads/
EXPOSE 80

RUN sed -i 's/index.html/index.php index.html/g' /etc/apache2/mods-enabled/dir.conf
RUN adduser --disabled-password --force-badname alphaCTF
USER alphaCTF