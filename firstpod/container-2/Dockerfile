FROM ubuntu:latest
RUN apt-get update && apt-get -y install cron
COPY . /
RUN (crontab -l ; echo "* * * * * python backup_code.py") | crontab
CMD ["cron","-f"]

EXPOSE 80