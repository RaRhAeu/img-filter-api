import io
from typing import List

from fastapi import FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from api import apply_filters, get_img_from_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/image")
async def filter_img(filters: List[str] = Query(None),
                     file: UploadFile = File(...)):
    img = await file.read()
    try:
        img = apply_filters(img, filters)
    except Exception:
        raise HTTPException(status_code=415,
                            detail="Unable to process the image")
    return StreamingResponse(io.BytesIO(img), media_type="image/jpeg")


@app.get("/image_from_url")
async def filter_from_url(filters: List[str] = Query(None),
                          url: str = Query(...)):
    img = await get_img_from_url(url)
    img = apply_filters(img, filters)
    return StreamingResponse(io.BytesIO(img), media_type="image/jpeg")
