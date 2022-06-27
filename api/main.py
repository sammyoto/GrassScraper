#API must take data from the VR and transmit it to the Raspberry Pi
#Simple instructions like moving and turning are fine

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Instruction(BaseModel):
    handy: str
    stickX: str
    stickY: str
    trigger: str
    x1: str
    x2: str

#TODO create POST method to add to instruction queue and GET method to take from queue and reset it
instructionQueue = []

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post("/vrPost")
async def vrPost(instruction: Instruction):
    instructionQueue.clear()
    #directional input
    print(instruction.handy)
    print(instruction.stickX)
    print(instruction.stickY)
    print(instruction.trigger)
    print(instruction.x1)
    print(instruction.x2)
    
    print(instructionQueue)
