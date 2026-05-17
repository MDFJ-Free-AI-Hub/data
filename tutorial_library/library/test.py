"""
Basic tests for the data library
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

import data
from data import ValidationError


def test_data_processor():
    """Test the DataProcessor class"""
    print("Testing DataProcessor...")
    
    data_list = [
        {"id": 1, "name": "John", "status": "active"},
        {"id": 2, "name": "Mary", "status": "inactive"},
        {"id": 3, "name": "Carlos", "status": "active"},
    ]
    
    proc = data.DataProcessor(data_list)
    
    # Test filter
    active = proc.filter_by_key("status", "active")
    assert len(active) == 2, "Filter did not work correctly"
    
    # Test summary
    summary = proc.get_summary()
    assert summary["count"] == 3, "Summary is not correct"
    
    print("✓ DataProcessor working correctly")


def test_data_analyzer():
    """Test the DataAnalyzer class"""
    print("Testing DataAnalyzer...")
    
    data_list = [
        {"id": 1, "name": "John", "department": "IT"},
        {"id": 2, "name": "Mary", "department": "HR"},
        {"id": 3, "name": "Carlos", "department": "IT"},
    ]
    
    analyzer = data.DataAnalyzer(data_list)
    
    # Test count
    assert analyzer.count_items() == 3, "Count is not correct"
    
    # Test keys
    keys = analyzer.get_keys()
    assert "name" in keys, "Keys not obtained correctly"
    
    # Test frequency
    freq = analyzer.get_value_frequency("department")
    assert freq["IT"] == 2, "Frequency not calculated correctly"
    
    print("✓ DataAnalyzer working correctly")


def test_validators():
    """Test validators"""
    print("Testing Validators...")
    
    schema = {"name": str, "age": int}
    
    # Test valid data
    try:
        data.validate_schema({"name": "John", "age": 30}, schema)
        print("✓ Schema validation correct")
    except ValidationError:
        raise AssertionError("Validation failed on valid data")
    
    # Test invalid data
    try:
        data.validate_schema({"name": "John", "age": "thirty"}, schema)
        raise AssertionError("Validation should have failed")
    except ValidationError:
        print("✓ Invalid data detection correct")


def test_utils():
    """Test utility functions"""
    print("Testing Utils...")
    
    # Test merge
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3}
    merged = data.merge_data(dict1, dict2)
    assert merged == {"a": 1, "b": 2, "c": 3}, "Merge does not work"
    
    # Test clean
    dirty = {"a": 1, "b": None, "c": ""}
    clean = data.clean_data(dirty)
    assert len(clean) == 1, "Clean does not work"
    
    print("✓ Utility functions working correctly")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Data Library Tests")
    print("=" * 50)
    print()
    
    try:
        test_data_processor()
        test_data_analyzer()
        test_validators()
        test_utils()
        
        print()
        print("=" * 50)
        print("✓ All tests passed successfully!")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\n✗ Test error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
