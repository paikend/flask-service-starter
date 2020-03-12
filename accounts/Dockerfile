FROM python:3.6
LABEL maintainer="paikend@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /accounts
WORKDIR /accounts
COPY requirements.txt /accounts/
RUN pip install -r requirements.txt
COPY . /accounts/
EXPOSE 5000

