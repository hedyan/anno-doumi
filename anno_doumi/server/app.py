from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
stored_commands = []


class CommandItem(BaseModel):
    command: str


@app.post("/store_command")
async def store_command(commands: List[CommandItem]):
    global stored_commands
    stored_commands.extend(commands)
    return {"message": "Commands stored successfully", "count": len(commands)}


@app.get("/get_commands")
async def get_commands():
    return {"commands": stored_commands}


@app.delete("/clear_commands")
async def clear_commands():
    global stored_commands
    stored_commands = []
    return {"message": "Commands cleared"}
