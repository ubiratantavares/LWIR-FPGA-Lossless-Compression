from abc import ABC, abstractmethod
import numpy as np

class IImageLoader(ABC):
    @abstractmethod
    def load(self, filepath: str) -> np.ndarray:
        pass

class IPredictor(ABC):
    @abstractmethod
    def predict(self, image: np.ndarray) -> np.ndarray:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass

class IEncoder(ABC):
    @abstractmethod
    def encode(self, data: np.ndarray) -> bytes:
        pass

class IView(ABC):
    @abstractmethod
    def show_message(self, message: str):
        pass
    
    @abstractmethod
    def show_progress(self, current: int, total: int):
        pass
    
    @abstractmethod
    def show_results(self, results: dict):
        pass
