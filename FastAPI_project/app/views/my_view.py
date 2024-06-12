from fastapi import APIRouter, HTTPException
from typing import List
from app.models.my_model import Payload, Output
from app.controllers.my_controller import MyController
from app.utils import logger
from datetime import datetime

router = APIRouter()

@router.post("/process_addition", response_model=Output)
def process_addition(request: Payload):
    try:
        start_time = datetime.now()
        logger.debug(f"Starting addition process: {start_time}")
        logger.debug(f"Calling addition controller")
        result = MyController.add_list(request.payload)
        logger.debug(f"Result: {result}")
        end_time = datetime.now()
        logger.debug(f"Finished addition process: {end_time}")
        
        if not isinstance(result, list):
            raise ValueError("Result is not a list")
        response = Output(batchid=request.batchid, response=result, status="complete", started_at=start_time, completed_at = end_time)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))