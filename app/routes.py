from fastapi import APIRouter, UploadFile
import redis
import json
import uuid

router = APIRouter()

worker = redis.Redis(host="redis", port=6379)

@router.post("/analyze-video")
async def analyze_video():
    
    job = {
        "video-path": "path..."
    }

    worker.lpush("video-jobs", json.dumps(job))

    return {"job_id": "01"}

@router.get("/redis-health-checkup")
def ping_redis():
    response = worker.ping()
    return {"redis response": response}