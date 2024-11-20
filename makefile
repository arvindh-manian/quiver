setup:
	docker network create quiver-net
	docker pull arvindhmanian/quiver-ingestion:latest
	docker pull arvindhmanian/quiver-edge:latest

up:
	docker run --rm -d --name ingestion-server -p 1935:1935 --network quiver-net arvindhmanian/quiver-ingestion:latest
	docker run --rm -d --name edge-server -p 8080:8080 --network quiver-net arvindhmanian/quiver-edge:latest

push:
	docker push arvindhmanian/quiver-ingestion:1.0.2
	docker push arvindhmanian/quiver-edge:1.0.2
	docker tag arvindhmanian/quiver-ingestion:1.0.2 arvindhmanian/quiver-ingestion:latest
	docker tag arvindhmanian/quiver-edge:1.0.2 arvindhmanian/quiver-edge:latest
	docker push arvindhmanian/quiver-ingestion:latest
	docker push arvindhmanian/quiver-edge:latest

down:
	docker stop ingestion-server
	docker stop edge-server