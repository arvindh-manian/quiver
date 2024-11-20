# Quiver

A simple real-time streaming solution with a single ingestion server and multiple load-balanced edge servers. Built using Nginx, Docker, and Python.

TODO:
- Deploy onto k8s
- Adaptive bitrate
- Caching layer

## Usage

The development environment uses Docker Compose. `docker compose up` and `docker compose down` should bring the server up and down respectively.

Stream to `rtmp://localhost:1935/show/<streamkey>`.

Pull from `http://localhost:8080/hls/<streamkey>.m3u8`.