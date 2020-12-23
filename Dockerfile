FROM python:2.7

MAINTAINER yuf1sher

RUN apt-get update && apt-get install -y \
                gcc \
                gettext \
                mariadb-server \
                wget \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

#RUN wget https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/cp27/mysqlclient-1.4.6-cp27-cp27m-win_amd64.whl

#RUN pip install mysqlclient-1.4.6-cp27-cp27m-win_amd64.whl && rm -rf mysqlclient-1.4.6-cp27-cp27m-win_amd64.whl

ENV DJANGO_VERSION 1.9.8

RUN python -m pip install --upgrade pip
 
RUN pip install mysqlclient django=="$DJANGO_VERSION"

ADD web_dionaea /opt/web_dionaea
WORKDIR /opt/web_dionaea

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
