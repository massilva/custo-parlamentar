FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y libgeos-c1
RUN apt-get update -y --fix-missing
RUN apt-get install -y libproj-dev libfreexl-dev libgdal-dev gdal-bin

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . /usr/src/app
