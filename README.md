# Docker Volume Logger

A beginner-friendly Docker project built to deeply understand **volumes**, **bind mounts**, **named volumes**, and **healthchecks** in Docker.

This project runs a Python app inside a Docker container that reads and writes timestamped logs to a file — and uses Docker volumes to persist that data even after the container is destroyed.

---

## What This Project Does

- Reads existing log entries on startup
- Appends a new timestamped log entry every 10 seconds
- Persists log data using Docker volumes (survives container restarts and removals)
- Uses a Docker healthcheck to monitor if the app is running correctly

---

## Project Structure

```
volume-logger/
├── app.py                  ← Python app that reads/writes logs
├── Dockerfile              ← How to build the image
├── docker-compose.yml      ← How to run the container with volumes
├── .gitignore              ← Ignores the data/ folder
└── data/                   ← Created at runtime, holds log.txt
```

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Your Machine                  │
│                                                 │
│   volume-logger/                                │
│   └── data/                                     │
│       └── log.txt  ◄──── Bind Mount ────►  /app/data/log.txt  │
│                                                 │
│              ┌──────────────────────┐           │
│              │   Docker Container   │           │
│              │                      │           │
│              │   python app.py      │           │
│              │   ↓                  │           │
│              │   /app/data/log.txt  │           │
│              │                      │           │
│              │   Healthcheck ✓      │           │
│              │   (every 30s)        │           │
│              └──────────────────────┘           │
└─────────────────────────────────────────────────┘
```

### Volume Types Used

| Type | Syntax | Use Case |
|------|--------|----------|
| Bind Mount | `./data:/app/data` | You control the path, files visible on your machine |
| Named Volume | `data:/app/data` | Docker manages storage, best for databases |

---

## How to Run

### Clone the repo

```bash
git clone https://github.com/gunjanjain24/volume-logger.git
cd volume-logger
```

### Run with Docker Compose

```bash
docker compose up --build
```

### View live logs

```bash
docker logs -f volume-logger-app-1
```

### Check container health

```bash
docker ps
```

You should see `(healthy)` in the STATUS column.

### Stop and remove the container

```bash
docker compose down
```

### Check that logs persisted

```bash
cat data/log.txt
```

The log file will still be there even after the container is removed.

---

## Key Concepts Demonstrated

### Bind Mount
Maps a folder on your machine directly into the container. Two-way live sync — changes on either side are instantly reflected on the other.

```yaml
volumes:
  - "./data:/app/data"
```

### Named Volume
Docker manages the storage location. Data persists but you don't control the path. Best for databases and production data.

```yaml
volumes:
  - "data:/app/data"

volumes:
  data:
```

### Healthcheck
Docker runs a test every 30 seconds to verify the app is working. If the log file exists, the container is marked healthy.

```yaml
healthcheck:
  test: ["CMD-SHELL", "test -f /app/data/log.txt"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### Python Unbuffered Output (`-u` flag)
Without `-u`, Python buffers print output and `docker logs` shows nothing. Always use unbuffered mode in Docker.

```dockerfile
CMD ["python", "-u", "app.py"]
```

---

## Docker Hub

The image is available on Docker Hub. Pull and run it directly without cloning the repo:

```bash
docker run -v "./data:/app/data" gunjanjain24/volume-logger:v1
```

---

## Technologies Used

- Python 3.11
- Docker
- Docker Compose
- Bind Mounts & Named Volumes
- Docker Healthchecks

---

## What I Learned

- How bind mounts and named volumes work and when to use each
- Container paths vs machine paths
- Why data is lost without volumes and how to fix it
- How Docker healthchecks work in real world containers
- How to debug a running container using `docker exec` and `docker logs`
- Why Python needs the `-u` flag inside Docker containers

---

## Author

Gunjan Jain
Learning Docker, DevOps, and Infrastructure.
