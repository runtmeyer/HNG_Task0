from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.responses import JSONResponse
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    iso_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {
        "email": "muobotone@gmail.com",
        "current_datetime": iso_timestamp,
        "github_url": "https://github.com/runtmeyer/HNG_Task0"
    }
    return JSONResponse(content=data)

if __name__ == "__main__":
    
    port = int(os.getenv("PORT", 5000))
    
    # Run the app with uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",  
        port=port,
        reload=True 
    )







