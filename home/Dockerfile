FROM python:3.6
LABEL maintainer="paikend@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /home
WORKDIR /home
COPY requirements.txt /home/
RUN pip install -r requirements.txt
COPY . /home/
EXPOSE 5000

