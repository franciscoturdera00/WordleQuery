# Containerization

This repository includes a `Dockerfile` and a `docker-compose.yml` to run the API in a container.

- Build the Docker image locally:

```bash
docker build -t wordlequery:latest .
```

- Run the container (single command):

```bash
docker run --rm -p 6767:6767 -v "$(pwd)":/app wordlequery:latest
```

Notes:

- The Flask app in this project listens on port `6767` (the container maps host port `6767`).
- The `-v "$(pwd)":/app` mount keeps the container synced with your local files for development; omit it for an immutable production container.

- Using Docker Compose (recommended for local development):

```bash
docker-compose up --build
```

- After the container starts, point Postman or `curl` at `http://localhost:6767` (this is the default `baseUrl` in the provided Postman collection).

- If you want a production-ready container, consider using a production WSGI server (e.g., `gunicorn`) and pinning dependency versions in `requirements.txt`.
