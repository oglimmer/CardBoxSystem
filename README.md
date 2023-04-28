# start server & client with docker

```bash
docker compose up --build
```

Access to UI at http://localhost:8080/

# start server locally

The REST API is implemented in [server.py](server/server.py) and is using the Python framework FastAPI.

To start the server:

```bash
cd server
pip install fastapi "uvicorn[standard]" pydantic
uvicorn server:app --reload
```

You can test this with

```bash
curl http://localhost:8000/cards
```

# start client locally

To start the client in dev mode:

```bash
cd client
npm i
npm run dev
```

Access to UI at http://localhost:5173/
