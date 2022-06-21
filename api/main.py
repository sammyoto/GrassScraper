#API must take data from the VR and transmit it to the Raspberry Pi
#Simple instructions like moving and turning are fine

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Instruction(BaseModel):
    left: str
    right: str
    forward: str
    back: str
    lookLeft: str
    lookRight: str
    lookDown: str
    lookUp: str

#TODO create POST method to add to instruction queue and GET method to take from queue and reset it
instructionQueue = []

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/alexSucks")
async def alexSucks():
    return {"message": "API works, Alex doesn't understand it at all lol."}

@app.get("/noahsGirlfriend")
async def noahsGirlfriend():
    return {"message": "I love Noah so much, he's all mine no other girl can have him."}

@app.post("/vrPost")
async def vrPost(instruction: Instruction):
    instructionQueue.clear()
    #directional input
    if instruction.left == "true":
        instructionQueue.append("left")
    if instruction.right == "true":
        instructionQueue.append("right")
    if instruction.forward == "true":
        instructionQueue.append("forward")
    if instruction.back == "true":
        instructionQueue.append("back")

    #camera input
    if instruction.lookLeft == "true":
        instructionQueue.append("lookLeft")
    if instruction.lookRight == "true":
        instructionQueue.append("lookRight")
    if instruction.lookDown == "true":
        instructionQueue.append("lookDown")
    if instruction.lookUp == "true":
        instructionQueue.append("lookUp")
    
    print(instructionQueue)
