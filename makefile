setup:
	docker pull arvindhmanian/quiver-ingestion:latest
	docker pull arvindhmanian/quiver-edge:latest

up:
	docker compose up -d

push:
	docker push arvindhmanian/quiver-ingestion:1.0.2
	docker push arvindhmanian/quiver-edge:1.0.2
	docker tag arvindhmanian/quiver-ingestion:1.0.2 arvindhmanian/quiver-ingestion:latest
	docker tag arvindhmanian/quiver-edge:1.0.2 arvindhmanian/quiver-edge:latest
	docker push arvindhmanian/quiver-ingestion:latest
	docker push arvindhmanian/quiver-edge:latest

down:
	docker compose down