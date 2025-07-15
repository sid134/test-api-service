# test-api-service


## FastAPI Demo API

A simple, cloud-native API service built with FastAPI, Dockerized and deployable to Kubernetes via Helm, integrated with GitHub Actions CI/CD.

---

## Features

- HTTP API that prints request headers, method, and body
- Containerized using Docker
- Packaged using Helm for Kubernetes deployment
- CI/CD via GitHub Actions
- Optional Prometheus instrumentation

---

## Tech Stack

- FastAPI
- Python 3.9+
- Docker
- Kubernetes
- Helm 3.x
- GitHub Actions

---

##  Project Structure


.
├── app/
│   └── main.py                   # FastAPI app entry
├── Dockerfile                    # Docker image definition
├── requirements.txt              # Python dependencies
├── .github/workflows/ci.yml      # GitHub Actions workflow
├── fastapi-chart/                # Helm chart
│   ├── templates/
│   └── values.yaml
├── README.md

