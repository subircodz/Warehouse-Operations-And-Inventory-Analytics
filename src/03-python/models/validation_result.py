"""
Validation Result Model

Represents the output of a validation step.

Author: Subir Sutradhar
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class WaveResult:
    """
    Represents the result of a validation.
    """

    validation_name: str
    data: Any
    status: str | None = None