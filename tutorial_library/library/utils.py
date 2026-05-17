"""
Utility module for manipulating data files
"""

import json
import csv
from pathlib import Path
from typing import Any, Dict, List, Union


def load_data(filepath: str) -> Union[Dict, List]:
    """
    Loads data from a JSON or CSV file
    
    Args:
        filepath: Path to the file
        
    Returns:
        Loaded data (dictionary or list)
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the format is not supported
    """
    path = Path(filepath)
    
    if not path.exists():
        raise FileNotFoundError(f"The file {filepath} does not exist")
    
    if path.suffix == ".json":
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    
    elif path.suffix == ".csv":
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    else:
        raise ValueError(f"Unsupported format: {path.suffix}")


def save_data(data: Union[Dict, List], filepath: str, format: str = None) -> None:
    """
    Saves data to a JSON or CSV file
    
    Args:
        data: Data to save
        filepath: Path to the destination file
        format: Format ('json' or 'csv'). If None, it is deduced from the extension
        
    Raises:
        ValueError: If the format is not supported
    """
    path = Path(filepath)
    
    # Deduce format if not specified
    if format is None:
        format = path.suffix.lstrip(".")
    
    if format == "json":
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    elif format == "csv":
        if not isinstance(data, list) or not data:
            raise ValueError("For CSV, data must be a list of dictionaries")
        
        keys = data[0].keys() if isinstance(data[0], dict) else []
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    
    else:
        raise ValueError(f"Unsupported format: {format}")


def clean_data(data: Union[Dict, List]) -> Union[Dict, List]:
    """
    Cleans data by removing empty or None values
    
    Args:
        data: Data to clean
        
    Returns:
        Cleaned data
    """
    if isinstance(data, list):
        return [clean_data(item) for item in data if item]
    
    elif isinstance(data, dict):
        return {k: v for k, v in data.items() if v is not None and v != ""}
    
    return data


def merge_data(*datasets: Union[Dict, List]) -> Union[Dict, List]:
    """
    Combines multiple datasets
    
    Args:
        datasets: Datasets to combine
        
    Returns:
        Combined data
    """
    if all(isinstance(d, dict) for d in datasets):
        result = {}
        for dataset in datasets:
            result.update(dataset)
        return result
    
    elif all(isinstance(d, list) for d in datasets):
        result = []
        for dataset in datasets:
            result.extend(dataset)
        return result
    
    else:
        raise ValueError("All datasets must be of the same type")
