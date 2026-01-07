import numpy as np
from PIL import Image
from src.interfaces.base import IImageLoader

class TiffImageLoader(IImageLoader):
    def load(self, filepath: str) -> np.ndarray:
        try:
            img = Image.open(filepath)
            return np.array(img, dtype=np.uint16)
        except Exception as e:
            raise IOError(f"Failed to load image {filepath}: {e}")
