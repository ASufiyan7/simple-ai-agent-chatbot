from fastapi import APIRouter
from .model import RequestModel
from Agent.an_agent import get_response

router = APIRouter()

@router.post("/get_response")
async def get_response_endpoint(request: RequestModel):
    response = get_response(
        llm_id=request.model_name,
        query_history=request.messages,
        use_search=request.search,
        system_prompt=request.system_prompt,
    )

    return {"response": response}