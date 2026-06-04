from __future__ import annotations
from dataclasses import dataclass
        
@dataclass
class Node:
    word: str
    children: [Node]
    is_final: bool


