from dataclasses import dataclass


@dataclass(frozen=True)
class TopologyState:
    n3: int
    n4: int
    n5: int
    n6: int = 0


@dataclass(frozen=True)
class TopologyDescriptor:
    values: tuple[int, ...]
    labels: tuple[str, ...]
