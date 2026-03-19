from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import threading
import time

app = FastAPI()

bot_running = False

# ================= BOT LOOP =================
def bot_loop():
    global bot_running
    while bot_running:
        print("Bot running...")
        # 👉 ICT trading logic will go here later
        time.sleep(60)

# ================= DASHBOARD UI =================
dashboard_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Trading Bot Dashboard</title>
    <style>
        body { font-family: Arial; text-align: center; background: #0f172a; color: white; }
        button { padding: 10px 20px; margin: 10px; font-size: 16px; cursor: pointer; }
        .start { background: green; color: white; }
        .stop { background: red; color: white; }
        .status { margin-top: 20px; font-size: 18px; }
    </style>
</head>
<body>

    <h1>📊 Trading Bot Dashboard</h1>

    <button class="start" onclick="startBot()">Start Bot</button>
    <button class="stop" onclick="stopBot()">Stop Bot</button>

    <div class="status" id="status">Status: Unknown</div>

    <script>
        async function startBot() {
            await fetch('/start');
            checkStatus();
        }

        async function stopBot() {
            await fetch('/stop');
            checkStatus();
        }

        async function checkStatus() {
            const res = await fetch('/status');
            const data = await res.json();
            document.getElementById('status').innerText =
                "Status: " + (data.running ? "Running ✅" : "Stopped ⛔");
        }

        setInterval(checkStatus, 3000);
        checkStatus();
    </script>

</body>
</html>
"""

# ================= ROUTES =================

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return dashboard_html

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
