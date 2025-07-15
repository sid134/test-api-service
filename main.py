from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

# Prometheus counter
REQUEST_COUNT = Counter("request_count", "Total request count")

@app.api_route("/api", methods=["GET", "POST"])
async def echo_request(request: Request):
    REQUEST_COUNT.inc()
    headers = dict(request.headers)
    method = request.method
    body = await request.body()
    
    return {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": headers,
        "method": method,
        "body": body.decode()
    }

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest().decode("utf-8"))

