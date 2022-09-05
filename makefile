start:
	docker-compose up -d 

stop:
	docker-compose down 

console:

	docker exec -it redis-services redis-cli