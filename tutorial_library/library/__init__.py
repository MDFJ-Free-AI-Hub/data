"""
Data Library - A library for manipulating and processing data
"""

from .core import DataProcessor, DataAnalyzer
from .utils import load_data, save_data, clean_data, merge_data
from .validators import (
    validate_data,
    validate_schema,
    validate_required_fields,
    validate_email_field,
    ValidationError,
)

__version__ = "1.0.0"
__author__ = "Your Name"
__all__ = [
    "DataProcessor",
    "DataAnalyzer",
    "load_data",
    "save_data",
    "clean_data",
    "merge_data",
    "validate_data",
    "validate_schema",
    "validate_required_fields",
    "validate_email_field",
    "ValidationError",
]
