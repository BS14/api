import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response, status

state = {"started": False, "ready": False}


@asynccontextmanager
async def lifespan(app: FastAPI):
    state["started"] = True
    state["ready"] = True
    yield
    state["ready"] = False


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "hello", "epoch": int(time.time())}


@app.get("/healthz")
def liveness():
    return {"status": "alive"}


@app.get("/readyz")
def readiness(response: Response):
    if not state["ready"]:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not ready"}
    return {"status": "ready"}


@app.get("/startupz")
def startup(response: Response):
    if not state["started"]:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "starting"}
    return {"status": "started"}
