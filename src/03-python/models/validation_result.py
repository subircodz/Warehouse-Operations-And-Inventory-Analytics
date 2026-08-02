"""
Common return object for all profiling and validation modules.

Author: Subir Sutradhar
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WaveResult:
    """
    Represents the output of a profiling or validation module.
    """

    validation_name: str
    data: Any
    summary: dict[str, Any] = field(default_factory=dict)
    status: str | None = None