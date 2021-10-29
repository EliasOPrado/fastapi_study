## Technologies used 

- FastAPI with Uvicorn
- SQLAlchemy + Alembic
- PostgreSQL + PGAdmin
- Docker/Docker-compose
- Configuring Environment Variables


### Command to run the applicantion

`(venv)$ uvicorn app.main:app`

- To run the applicantion:
   - `$ docker-compose build` 
   - `$ docker compose up`

- After running the application test if the db connection was done correctly:
   - `$ docker-compose exec db psql --username=fastapi_traefik --dbname=fastapi_traefik`
   - `fastapi_traefik=# \l`
   - To leave: `fastapi_traefik=# \q`

- Check if the volume was done right:
   - `$ docker volume inspect fastapi-docker-traefik_postgres_data`

- Navigate to `127.0.0.1:8008`:
```
    {
        "id": 1,
        "email": "test@test.com",
        "active": true
    }
```

