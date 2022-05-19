from fastapi import APIRouter, Request
from celery_worker import detectPerfectCycles
from typing import List
from pydantic import BaseModel

router = APIRouter()


class body(BaseModel):
   list1: List = []


# Kick off a new job by adding it to the work queue
@router.post("/detectperfectcycles")
async def addJob(request: Request): 
    lists = await request.json()
    task = detectPerfectCycles.delay(lists)     
    return {"Message": "Thank you for submitting your data", 
            "Task ID": task.id}

# Allows the client to query the state of a background job
@router.get("/detectperfectcycles/{task_id}")
def get_status(task_id):
    task_result = detectPerfectCycles.AsyncResult(task_id)
    print(task_result)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result
