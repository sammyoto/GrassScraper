#API must take data from the VR and transmit it to the Raspberry Pi
#Simple instructions like moving and turning are fine

import json
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

class Instruction(BaseModel):
    handy: str
    stickX: str
    stickY: str
    trigger: str
    x1: str
    x2: str

#TODO create POST method to add to instruction queue and GET method to take from queue and reset it
instructionQueue = []


@app.get("/piGet")
async def root():
    if len(instructionQueue) > 0:
        item = instructionQueue.pop()
        return json.dumps(item.__dict__)
    else:
        return {"message: No item in queue!"}

@app.post("/vrPost")
async def vrPost(instruction: Instruction):
    #directional input
    instructionQueue.append(instruction)
    print(instructionQueue)
