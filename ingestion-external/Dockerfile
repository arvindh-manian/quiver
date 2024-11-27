FROM ubuntu:18.04

LABEL maintainer="arvindh.manian@gmail.com"
LABEL description="Dockerfile for ingestion server"

RUN apt-get update && \
    apt-get install -y nginx=1.14.0-0ubuntu1.11 libnginx-mod-rtmp=1.14.0-0ubuntu1.11 curl=7.58.0-2ubuntu3.24 && \
    apt-get clean

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 1935

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:8080/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]