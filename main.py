from fastapi import FastAPI

app = FastAPI()

bot_running = False

@app.get("/")
def home():
    return {"message": "Trading Bot API Running"}

@app.get("/start")
def start():
    global bot_running
    bot_running = True
    return {"status": "started"}

@app.get("/stop")
def stop():
    global bot_running
    bot_running = False
    return {"status": "stopped"}

@app.get("/status")
def status():
    return {"running": bot_running}
