from fastapi import FastAPI
import threading
import time

app = FastAPI()

bot_running = False

# === YOUR BOT LOOP ===
def bot_loop():
    global bot_running
    while bot_running:
        print("Bot running...")

        # 👉 Here you will later plug ICT strategy + trading logic

        time.sleep(60)

# === ROUTES ===

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/start")
def start_bot():
    global bot_running
    if not bot_running:
        bot_running = True
        thread = threading.Thread(target=bot_loop)
        thread.start()
    return {"message": "Bot started"}

@app.get("/stop")
def stop_bot():
    global bot_running
    bot_running = False
    return {"message": "Bot stopped"}

@app.get("/status")
def status():
    return {"running": bot_running}
