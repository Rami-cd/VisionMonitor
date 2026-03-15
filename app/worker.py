import time
import redis
import json

worker = redis.Redis(host="redis", port=6379)


while True:
    job = worker.brpop("video-jobs")
    job_data = json.loads(job[1])

    video_path = job_data["video-path"]

    print(video_path)