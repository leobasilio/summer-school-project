FROM ubuntu:bionic

ADD dana.tar.gz /root

EXPOSE 8080

ENV DANA_HOME="/root/dana"
ENV PATH="$PATH:$DANA_HOME"
