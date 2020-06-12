import cv2
import numpy as np


async def gaussian_blur(img: np.ndarray) -> np.ndarray:
    res = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    return res


async def edge_detect(img: np.ndarray) -> np.ndarray:
    edges = cv2.Canny(img, 100, 300)
    return edges


async def vintage(img: np.ndarray) -> np.ndarray:
    rows, cols = img.shape[:2]
    # Create gaussian filter
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    _filter = 255 * kernel / np.linalg.norm(kernel)
    for i in range(3):
        img[:, :, i] = img[:, :, i] * _filter
    return img


filter_map = {
    "gaussian": gaussian_blur,
    "edge": edge_detect,
    "vintage": vintage
}
