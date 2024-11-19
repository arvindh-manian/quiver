up:
	docker run -d --name ingestion-server -p 1935:1935 --network quiver-net arvindhmanian/quiver-ingestion:1.0.1
	docker run -d --name edge-server -p 8080:8080 --network quiver-net arvindhmanian/quiver-edge:1.0.1