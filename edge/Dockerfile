FROM python:3.12.7-slim-bookworm

LABEL maintainer="arvindh.manian@gmail.com"
LABEL description="Dockerfile for edge server"

WORKDIR /app
EXPOSE 8080

ENV FLASK_APP=edge_server.py
ENV FLASK_RUN_PORT=8080

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:8080/healthz || exit 1

CMD ["flask", "run", "--host=0.0.0.0"]

# COPY nginx.conf /etc/nginx/nginx.conf

# EXPOSE 1935 8080

# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:8080/healthz || exit 1

# CMD ["nginx", "-g", "daemon off;"]