import io
from typing import List
from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import StreamingResponse

from api import apply_filters, get_img_from_url

app = FastAPI()


@app.post("/images")
async def filter_img(filters: List[str] = Query(None),
                     file: UploadFile = File(...)):
    img = await file.read()
    img = await apply_filters(img, filters)
    return StreamingResponse(io.BytesIO(img), media_type="image/jpeg")


@app.get("/from_url")
async def filter_from_url(filters: List[str] = Query(None),
                          url: str = Query(...)):
    img = await get_img_from_url(url)
    img = await apply_filters(img, filters)
    return StreamingResponse(io.BytesIO(img), media_type="image/jpeg")
