import glob
import os
from typing import List

from src.interfaces.base import IImageLoader, IPredictor, IEncoder, IView
from src.models.stats import MethodStats
from src.services.metrics import MetricsCalculator

class SimulationController:
    def __init__(self, 
                 data_dir: str, 
                 loader: IImageLoader, 
                 predictors: List[IPredictor], 
                 encoder: IEncoder, 
                 view: IView):
        self.data_dir = data_dir
        self.loader = loader
        self.predictors = predictors
        self.encoder = encoder
        self.view = view
        self.stats = {p.get_name(): MethodStats(p.get_name()) for p in predictors}

    def run(self):
        files = sorted(glob.glob(os.path.join(self.data_dir, "*.tiff")))
        if not files:
            self.view.show_message("No TIFF files found.")
            return

        self.view.show_message(f"Starting simulation on {len(files)} images...")
        
        for i, f in enumerate(files):
            try:
                img = self.loader.load(f)
            except Exception as e:
                self.view.show_message(str(e))
                continue
            
            original_bytes_len = img.nbytes
            
            for predictor in self.predictors:
                # Prediction
                residuals = predictor.predict(img)
                
                # Metrics: Entropy
                entropy = MetricsCalculator.calculate_entropy(residuals)
                cr_entropy = MetricsCalculator.calculate_cr_entropy(entropy)
                
                # Metrics: Compression (Deflate as proxy)
                compressed = self.encoder.encode(residuals)
                cr_deflate = MetricsCalculator.calculate_cr_size(original_bytes_len, len(compressed))
                
                # Record Stats
                self.stats[predictor.get_name()].add_result(entropy, cr_entropy, cr_deflate)
            
            self.view.show_progress(i + 1, len(files))
        
        self.view.show_results(self.stats)
