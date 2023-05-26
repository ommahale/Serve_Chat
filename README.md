# Serve_Chat
## Run with docker compose (Recommended for testing)
In order to run the application as isolated docker container network run following command in terminal of your project directory.
Migration scripts:
```powershell
docker-compose run app python manage.py migrate
```
Run containers
```powershell
docker-compose up
```
The server is now up and running in http://localhost:8000/
the mapped database volume directory will be created as "data" in your project directory.
