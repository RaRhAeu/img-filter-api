from aiohttp import ClientSession
import cv2
import numpy as np
from typing import List, Union

from api.filters import filter_map


async def apply_filters(img: Union[bytes, str],
                        filter_list: List[str] = None) -> bytes:
    np_arr_img = np.frombuffer(img, np.uint8)
    img = cv2.imdecode(np_arr_img, cv2.IMREAD_COLOR)
    print(type(img))
    if filter_list:
        for _filter in filter_list:
            if _filter in filter_map:
                img = await filter_map[_filter](img)
    success, encoded_img = cv2.imencode('.jpg', img)
    if not success:
        return b''
    return encoded_img.tobytes()


async def get_img_from_url(url: str) -> bytes:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.read()
            return data
