from typing import List, Union

import cv2  # type: ignore
import numpy as np  # type: ignore
from aiohttp import ClientSession

from api.filters import filter_map


def apply_filters(img: Union[bytes, str],
                  filter_list: List[str] = None) -> bytes:
    np_arr_img = np.frombuffer(img, np.uint8)
    img = cv2.imdecode(np_arr_img, cv2.IMREAD_COLOR)
    if filter_list:
        for _filter in filter_list:
            if _filter in filter_map:
                img = filter_map[_filter](img)
    _, encoded_img = cv2.imencode('.jpg', img)
    return encoded_img.tobytes()


async def get_img_from_url(url: str) -> bytes:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            url_image = await resp.read()
            return url_image
