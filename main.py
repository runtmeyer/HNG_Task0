from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.responses import JSONResponse
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    iso_timestamp = datetime.now(timezone.utc).isoformat(timespec='minutes')
    data = {
        "email": "muobotone@gmail.com",
        "current_datetime": iso_timestamp,
        "github_url": "https://github.com/runtmeyer/HNG_Task0"
    }
    return JSONResponse(content=data)

if __name__ == "__main__":
    # Get port from environment variable or use 5000 as default
    port = int(os.getenv("PORT", 5000))
    
    # Run the app with uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",  # Bind to all available network interfaces
        port=port,
        reload=True  # Enable auto-reload during development
    )







