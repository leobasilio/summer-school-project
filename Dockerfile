FROM ubuntu:bionic

WORKDIR /root

ADD dana.tar.gz .

EXPOSE 8080

ENV DANA_HOME="/root/dana"
ENV PATH="$PATH:$DANA_HOME"

COPY ./application ./application
COPY ./pal ./pal
COPY entrypoint.sh ./

RUN chmod +x entrypoint.sh && \
    cd application && \
    dnc . && \
    cd ../pal && \
    dnc . -sp ../application/

CMD ./entrypoint.sh
