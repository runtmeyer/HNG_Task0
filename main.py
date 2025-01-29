from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.responses import JSONResponse

app = FastAPI()
iso_timestamp = datetime.now(timezone.utc).isoformat(timespec='minutes')

port = 5000


@app.get("/")
def read_root():
    data=  {
        "email": "muobotone@gmail.com",
        "current_datetime": iso_timestamp,
        "github_url": "https://github.com/runtmeyer/HNG_Task0"
        }

    return JSONResponse(content=data)







