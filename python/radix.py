from __future__ import annotations
from dataclasses import dataclass, field
        
@dataclass
class Node:
    word: str
    is_final: bool
    children: [Node] = field(default_factory=list)



