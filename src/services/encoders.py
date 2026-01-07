import zlib
import numpy as np
from src.interfaces.base import IEncoder

class ZlibEncoder(IEncoder):
    def encode(self, data: np.ndarray) -> bytes:
        """
        Encodes data using ZigZag encoding followed by zlib compression.
        """
        # ZigZag encoding to map signed residuals to unsigned
        zigzag = (data << 1) ^ (data >> 31)
        zigzag_uint16 = zigzag.astype(np.uint16)
        return zlib.compress(zigzag_uint16.tobytes())
