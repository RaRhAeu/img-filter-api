import cv2
import pytest
import requests

from api import apply_filters
from api.filters import filter_map


def test_filters_are_callabe():
    assert len(filter_map) >= 1
    for filter_name, _filter in filter_map.items():
        assert isinstance(filter_name, str)
        assert callable(_filter)


def test_apply_filters():
    response = requests.get("https://picsum.photos/200/200")
    all_filters = filter_map.keys()
    test_img = response.content
    assert isinstance(test_img, bytes)
    for _filter in all_filters:
        test_res = apply_filters(test_img, _filter)
        assert isinstance(test_res, bytes)


def test_apply_filters_fail():
    with pytest.raises(cv2.error):
        apply_filters(b"asd", [])
