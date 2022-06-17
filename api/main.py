#API must take data from the VR and transmit it to the Raspberry Pi
#Simple instructions like moving and turning are fine

from fastapi import FastAPI
app = FastAPI()

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