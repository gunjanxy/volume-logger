
# 🐳 Docker Volume Logger

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Docker Hub](https://img.shields.io/badge/Docker_Hub-gunjanjain24-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> A hands-on Docker project to deeply understand **volumes**, **bind mounts**, **named volumes**, and **healthchecks** — the way real DevOps engineers use them.

---

## 📌 What This Project Does

A Python app runs inside a Docker container and:

- 📖 Reads existing log entries on startup
- ✍️ Appends a new timestamped log entry **every 10 seconds**
- 💾 Persists all log data using Docker volumes — survives container restarts and removals
- ❤️ Uses a Docker **healthcheck** to monitor container health every 30 seconds

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        Your Machine                          │
│                                                              │
│   volume-logger/                                             │
│   └── data/                                                  │
│       └── log.txt ◄──── Bind Mount (two-way sync) ────►     │
│                                                              │
│              ┌───────────────────────────────┐              │
│              │        Docker Container        │              │
│              │                               │              │
│              │   🐍 python -u app.py         │              │
│              │          ↓                    │              │
│              │   /app/data/log.txt           │              │
│              │                               │              │
│              │   ❤️  Healthcheck             │              │
│              │   test -f /app/data/log.txt   │              │
│              │   interval: 30s               │              │
│              └───────────────────────────────┘              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
volume-logger/
│
├── app.py                  ← Python app that reads and writes logs
├── Dockerfile              ← How to build the image
├── docker-compose.yml      ← How to run the container with volumes
├── .gitignore              ← Ignores the data/ folder
└── data/                   ← Created at runtime, stores log.txt
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/gunjanjain24/volume-logger.git
cd volume-logger
```

### 2. Run with Docker Compose

```bash
docker compose up --build
```

### 3. View live logs

In a new terminal:

```bash
docker logs -f volume-logger-app-1
```

### 4. Check container health

```bash
docker ps
```

You should see `(healthy)` in the STATUS column.

### 5. Stop the container

```bash
docker compose down
```

### 6. Verify data persisted

```bash
cat data/log.txt
```

The log file is still there — even after the container was destroyed. That's the power of volumes. ✅

---

## 🧠 Key Concepts Explained

### 🔗 Bind Mount

Maps a folder on your machine directly into the container. Two-way live sync — changes on either side are instantly visible on the other.

```yaml
volumes:
  - "./data:/app/data"
#    ↑              ↑
# your machine   container
```

### 📦 Named Volume

Docker manages the storage location. You don't control the path but the data persists safely. Best for databases and production data.

```yaml
services:
  app:
    volumes:
      - "data:/app/data"

volumes:
  data:
```

### ❤️ Healthcheck

Docker runs a test every 30 seconds to verify the app is actually working — not just running.

```yaml
healthcheck:
  test: ["CMD-SHELL", "test -f /app/data/log.txt"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### 🐍 Python Unbuffered Output

Without `-u`, Python buffers print output and `docker logs` shows nothing. Always use unbuffered mode in Docker containers.

```dockerfile
CMD ["python", "-u", "app.py"]
```

---

## 🔄 Volume Types Comparison

| Feature | Bind Mount | Named Volume |
|---|---|---|
| You control the path | ✅ Yes | ❌ Docker manages it |
| Files visible on your machine | ✅ Yes | ❌ Hidden in Docker storage |
| Easy to inspect/edit | ✅ Yes | Harder |
| Best for | Logs, code, configs | Databases, production data |
| Syntax | `./data:/app/data` | `data:/app/data` |

---

## 🐳 Docker Hub

The image is available on Docker Hub. Run it directly without cloning:

```bash
docker run -v "./data:/app/data" gunjanjain24/volume-logger:v1
```

🔗 [gunjanjain24/volume-logger on Docker Hub](https://hub.docker.com/r/gunjanjain24/volume-logger)

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.11 | App that reads and writes logs |
| Docker | Containerization |
| Docker Compose | Multi-config container management |
| Bind Mount | Two-way file sync between host and container |
| Named Volume | Persistent Docker-managed storage |
| Docker Healthcheck | Container health monitoring |

---

## 📚 What I Learned

- ✅ How bind mounts and named volumes work and when to use each
- ✅ Container paths vs machine paths — and why they're different
- ✅ Why data is lost without volumes and how to fix it
- ✅ How Docker healthchecks work in real world containers
- ✅ How to debug a running container using `docker exec` and `docker logs`
- ✅ Why Python needs the `-u` flag inside Docker containers
- ✅ How Docker layer caching works and when to use `--no-cache`
- ✅ Full workflow: build → run → push to Docker Hub → push to GitHub

---

## 🔍 Useful Commands

```bash
# Build and run
docker compose up --build

# Force rebuild ignoring cache
docker compose build --no-cache
docker compose up

# View live container logs
docker logs -f volume-logger-app-1

# Check container health status
docker ps

# Go inside the running container
docker exec -it volume-logger-app-1 bash

# Stop and remove container
docker compose down

# View log file on your machine
cat data/log.txt
```

---

## 📁 Related Projects

| Project | Concepts |
|---|---|
| [linux-server-bootstrap](https://github.com/gunjanxy/linux-server-bootstrap) | Linux automation, Bash scripting, server provisioning |
| volume-logger *(this project)* | Docker volumes, healthchecks, bind mounts |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Gunjan Jain**

Learning Docker, Linux, and DevOps — one project at a time.

[![GitHub](https://img.shields.io/badge/GitHub-gunjanxy-181717?style=flat&logo=github)](https://github.com/gunjanxy)
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-gunjanjain24-2496ED?style=flat&logo=docker)](https://hub.docker.com/u/gunjanjain24)
