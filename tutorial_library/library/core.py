"""
Core module with the main classes of the library
"""

import json
import csv
from typing import Any, Dict, List, Union


class DataProcessor:
    """Processes and transforms data"""
    
    def __init__(self, data: Union[Dict, List] = None):
        """
        Initializes the data processor
        
        Args:
            data: Initial data (dictionary or list)
        """
        self.data = data or {}
    
    def filter_by_key(self, key: str, value: Any) -> List[Dict]:
        """Filters data by key and value"""
        if isinstance(self.data, list):
            return [item for item in self.data if isinstance(item, dict) and item.get(key) == value]
        return []
    
    def map_transform(self, transform_func) -> Any:
        """Applies a transformation function to the data"""
        if isinstance(self.data, list):
            return [transform_func(item) for item in self.data]
        return transform_func(self.data)
    
    def get_summary(self) -> Dict:
        """Gets a summary of the data"""
        if isinstance(self.data, list):
            return {
                "type": "list",
                "count": len(self.data),
                "sample": self.data[0] if self.data else None
            }
        else:
            return {
                "type": "dict",
                "keys": list(self.data.keys()) if isinstance(self.data, dict) else []
            }


class DataAnalyzer:
    """Analyzes data and generates statistics"""
    
    def __init__(self, data: Union[Dict, List]):
        """
        Initializes the data analyzer
        
        Args:
            data: Data to analyze
        """
        self.data = data
    
    def count_items(self) -> int:
        """Counts the number of items"""
        if isinstance(self.data, list):
            return len(self.data)
        elif isinstance(self.data, dict):
            return len(self.data)
        return 0
    
    def get_keys(self) -> List[str]:
        """Gets the available keys"""
        if isinstance(self.data, dict):
            return list(self.data.keys())
        elif isinstance(self.data, list) and self.data and isinstance(self.data[0], dict):
            return list(self.data[0].keys())
        return []
    
    def get_value_frequency(self, key: str) -> Dict[Any, int]:
        """Gets the frequency of values for a specific key"""
        frequency = {}
        if isinstance(self.data, list):
            for item in self.data:
                if isinstance(item, dict) and key in item:
                    value = item[key]
                    frequency[value] = frequency.get(value, 0) + 1
        return frequency
    
    def get_statistics(self) -> Dict:
        """Generates general statistics"""
        return {
            "total_items": self.count_items(),
            "keys": self.get_keys(),
            "data_type": type(self.data).__name__
        }
