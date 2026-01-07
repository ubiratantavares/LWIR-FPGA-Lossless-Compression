from src.interfaces.base import IView
import numpy as np

class ConsoleView(IView):
    def show_message(self, message: str):
        print(message)

    def show_progress(self, current: int, total: int):
        if current % 50 == 0 or current == total:
            print(f"Processed {current}/{total} images...")

    def show_results(self, results: dict):
        print("\n=== Simulation Results ===")
        for name, stats in results.items():
            avg_ent = np.mean(stats.entropies)
            avg_cr_ent = np.mean(stats.cr_entropies)
            avg_cr_deflate = np.mean(stats.cr_deflates)
            
            print(f"\nMethod: {name}")
            print(f"  Avg Entropy: {avg_ent:.4f} bits/pixel")
            print(f"  Avg CR (Entropy-based): {avg_cr_ent:.4f}:1")
            print(f"  Avg CR (Deflate/LZW proxy): {avg_cr_deflate:.4f}:1")
