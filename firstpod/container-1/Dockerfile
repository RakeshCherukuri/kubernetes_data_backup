FROM ubuntu:latest
RUN apt-get update && apt-get install -y apache2 && apt-get -y install cron

RUN (crontab -l ; echo "* * * * * python writelog.py") | crontab
CMD ["cron","-f"]
COPY index.html /var/www/html/
CMD [“/usr/sbin/apache2”, “-D”, “FOREGROUND”]
EXPOSE 80