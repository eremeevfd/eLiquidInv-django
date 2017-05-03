FROM ubuntu:16.04
MAINTAINER eLiquidInventory team
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
    curl \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*
RUN pip3 install uwsgi
COPY eLiquidInv/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt
COPY uwsgi.ini /home/docker/code/app/
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY eLiquidInv/ /home/docker/code/app/
WORKDIR /home/docker/code/app/
EXPOSE 8000
CMD ["uwsgi", "--http", ":8000", "--module", "eLiquidInv.wsgi"]
#CMD ["uwsgi", "--ini", "/home/docker/code/app/uwsgi.ini"]


