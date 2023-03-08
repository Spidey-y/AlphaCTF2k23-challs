FROM php:5.6-apache  
COPY . /var/www/html
RUN adduser --disabled-password --force-badname alphaCTF
USER alphaCTF

COPY php.ini /usr/local/etc/php