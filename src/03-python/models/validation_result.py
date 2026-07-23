"""
Validation Result Model

Represents the output of a validation step.

Author: Subir Sutradhar
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:
    """
    Represents the result of a validation.
    """

    validation_name: str
    status: str
    data: Any