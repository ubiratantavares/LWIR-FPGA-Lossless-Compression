import numpy as np
from src.interfaces.base import IPredictor

class DPCMFixedPredictor(IPredictor):
    def get_name(self) -> str:
        return "DPCM_Fixed"

    def predict(self, image: np.ndarray) -> np.ndarray:
        """
        Fixed DPCM: Left Neighbor Prediction.
        """
        img_int = image.astype(np.int32)
        prediction = np.roll(img_int, 1, axis=1)
        prediction[:, 0] = 0
        residual = img_int - prediction
        return residual.flatten()

class AdaptiveMEDPredictor(IPredictor):
    def get_name(self) -> str:
        return "Adaptive_MED"

    def predict(self, image: np.ndarray) -> np.ndarray:
        """
        Adaptive DPCM: Median Edge Detection (MED) / LOCO-I.
        """
        img_int = image.astype(np.int32)
        rows, cols = img_int.shape
        
        padded = np.zeros((rows + 1, cols + 1), dtype=np.int32)
        padded[1:, 1:] = img_int
        
        A = padded[1:, :-1] # Left
        B = padded[:-1, 1:] # Up
        C = padded[:-1, :-1] # Up-Left
        
        max_ab = np.maximum(A, B)
        min_ab = np.minimum(A, B)
        
        pred = np.zeros_like(img_int)
        
        mask1 = C >= max_ab
        pred[mask1] = min_ab[mask1]
        
        mask2 = C <= min_ab
        pred[mask2] = max_ab[mask2]
        
        mask3 = ~(mask1 | mask2)
        pred[mask3] = A[mask3] + B[mask3] - C[mask3]
        
        residual = img_int - pred
        return residual.flatten()
