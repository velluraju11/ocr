import os
from fastapi import FastAPI, WebSocket, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.core.orchestrator import Orchestrator

app = FastAPI(title="Ryha AI Builder")

# Mount static files
app.mount("/static", StaticFiles(directory="src/ui/static"), name="static")

@app.get("/")
async def get():
    with open("src/ui/static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.websocket("/ws/build")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    orchestrator = Orchestrator()

    try:
        while True:
            data = await websocket.receive_text()
            # Expecting just the idea string for now
            idea = data

            # Run the build process and stream events
            for event in orchestrator.build_software_generator(idea):
                await websocket.send_json(event)

            await websocket.send_json({"type": "done"})

    except Exception as e:
        print(f"WebSocket Error: {e}")
        try:
            await websocket.close()
        except:
            pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
