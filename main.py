from src.controllers.simulation import SimulationController
from src.services.loader import TiffImageLoader
from src.services.predictors import DPCMFixedPredictor, AdaptiveMEDPredictor
from src.services.encoders import ZlibEncoder
from src.views.console import ConsoleView

class Main:
    """
    Main entry point for the Mass Simulation Activity (Sprint 0, Step 1.1).
    Orchestrates the setup and execution of the simulation pipeline.
    """
    DATA_DIR = "/home/bira/github/LWIR-FPGA-Lossless-Compression/data/thermal_16_bit"

    def __init__(self):
        # Initialize Services (Dependency Injection)
        self.loader = TiffImageLoader()
        self.predictors = [DPCMFixedPredictor(), AdaptiveMEDPredictor()]
        self.encoder = ZlibEncoder()
        self.view = ConsoleView()
        
        # Initialize Controller
        self.controller = SimulationController(
            data_dir=self.DATA_DIR,
            loader=self.loader,
            predictors=self.predictors,
            encoder=self.encoder,
            view=self.view
        )

    def run(self):
        """Executes the simulation pipeline."""
        self.controller.run()

if __name__ == "__main__":
    app = Main()
    app.run()
