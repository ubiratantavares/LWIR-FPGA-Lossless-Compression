import numpy as np

class MetricsCalculator:
    @staticmethod
    def calculate_entropy(data: np.ndarray) -> float:
        if len(data) == 0:
            return 0.0
        unique, counts = np.unique(data, return_counts=True)
        probs = counts / len(data)
        return -np.sum(probs * np.log2(probs))

    @staticmethod
    def calculate_cr_entropy(entropy: float, bit_depth: int = 16) -> float:
        return bit_depth / entropy if entropy > 0 else 0.0

    @staticmethod
    def calculate_cr_size(original_size: int, compressed_size: int) -> float:
        return original_size / compressed_size if compressed_size > 0 else 0.0
