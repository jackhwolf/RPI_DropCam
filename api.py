from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from dropcam import DropCam

app = FastAPI()
cam = DropCam()

@app.get('/dropcam/healthcheck')
async def dc_healtcheck():
    return {"status": "healthy!"}

@app.get('/dropcam/file')
async def dc_file():
    return FileResponse(cam.pic_to_file())

@app.get('/dropcam/stream')
async def dc_stream():
    stream, ext = cam.pic_to_stream()
    stream.seek(0)
    return StreamingResponse(stream, media_type=ext)


