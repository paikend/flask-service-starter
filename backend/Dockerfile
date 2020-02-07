FROM python:3.6
LABEL maintainer="paikend@gmail.com"
RUN apt update && apt install python-dev -y
COPY . /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/
EXPOSE 8000

