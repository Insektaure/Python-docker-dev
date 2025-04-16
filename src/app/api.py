from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.app.utils import greet
from src.app.rabbitmq_utils import publish_message
from src.models.models import PublishRequest

app = FastAPI()

@app.get("/greet/{name}")
def greet_endpoint(name: str):
    """
    Endpoint to greet a user by name using the greet function.
    """
    greet(name)  # call the utility function to print the greeting in console
    return JSONResponse(content={"message": f"Hello, {name}!"})


@app.post("/publish/{queue_name}")
def publish_to_queue(queue_name: str, request: PublishRequest):
    """
    Endpoint to publish a message to a RabbitMQ queue.
    """
    try:
        publish_message(queue_name, request.message)
        return JSONResponse(content={"message": f"Message published to queue '{queue_name}'"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))