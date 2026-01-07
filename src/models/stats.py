from dataclasses import dataclass, field
from typing import List

@dataclass
class MethodStats:
    name: str
    entropies: List[float] = field(default_factory=list)
    cr_entropies: List[float] = field(default_factory=list)
    cr_deflates: List[float] = field(default_factory=list)

    def add_result(self, entropy: float, cr_entropy: float, cr_deflate: float):
        self.entropies.append(entropy)
        self.cr_entropies.append(cr_entropy)
        self.cr_deflates.append(cr_deflate)
