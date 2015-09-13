# Deploys pyip-reflector on Ubuntu 14.04 using gunicorn, listening on 0.0.0.0
# This is meant as a reference and/or shortcut for deployment.

FROM ubuntu:14.04

RUN apt-get update && apt-get install -y --force-yes python-flask gunicorn

ADD . /opt/pyip-reflector
WORKDIR /opt/pyip-reflector

EXPOSE 10704
ENTRYPOINT gunicorn pyip_reflector:app -b 0.0.0.0:10704
