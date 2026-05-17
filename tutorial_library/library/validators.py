"""
Data validators module
"""

from typing import Any, Dict, List, Union, Callable


class ValidationError(Exception):
    """Exception for validation errors"""
    pass


def validate_data(data: Any, validator_func: Callable[[Any], bool]) -> bool:
    """
    Validates data using a custom validator function
    
    Args:
        data: Data to validate
        validator_func: Function that returns True if data is valid
        
    Returns:
        True if the data is valid
        
    Raises:
        ValidationError: If data is not valid
    """
    if not validator_func(data):
        raise ValidationError(f"Data does not pass validation: {data}")
    return True


def validate_schema(data: Union[Dict, List], schema: Dict) -> bool:
    """
    Validates that data complies with a specific schema
    
    Args:
        data: Data to validate
        schema: Schema with required keys and expected types
        
    Returns:
        True if data complies with the schema
        
    Raises:
        ValidationError: If data does not comply with the schema
        
    Example:
        schema = {
            "name": str,
            "age": int,
            "email": str
        }
        validate_schema({"name": "John", "age": 30, "email": "john@example.com"}, schema)
    """
    if isinstance(data, dict):
        # Validate that all required keys are present
        for key, expected_type in schema.items():
            if key not in data:
                raise ValidationError(f"Missing required key: {key}")
            
            # Validate the data type
            if not isinstance(data[key], expected_type):
                raise ValidationError(
                    f"Key '{key}' has type {type(data[key]).__name__}, "
                    f"expected {expected_type.__name__}"
                )
        return True
    
    elif isinstance(data, list):
        # Validate each element in the list
        for item in data:
            validate_schema(item, schema)
        return True
    
    else:
        raise ValidationError(f"Data must be a dictionary or list")


def validate_required_fields(data: Dict, required_fields: List[str]) -> bool:
    """
    Validates that a dictionary contains the required fields
    
    Args:
        data: Dictionary to validate
        required_fields: List of required fields
        
    Returns:
        True if it contains all required fields
        
    Raises:
        ValidationError: If any required field is missing
    """
    missing = [field for field in required_fields if field not in data]
    
    if missing:
        raise ValidationError(f"Missing fields: {missing}")
    
    return True


def is_valid_email(email: str) -> bool:
    """Validates that a string is a valid email"""
    import re
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_email_field(data: Union[Dict, List], email_field: str = "email") -> bool:
    """
    Validates that the email field is valid in the data
    
    Args:
        data: Data to validate
        email_field: Name of the field containing the email
        
    Returns:
        True if the email is valid
        
    Raises:
        ValidationError: If the email is not valid
    """
    if isinstance(data, dict):
        if email_field in data and not is_valid_email(data[email_field]):
            raise ValidationError(f"Invalid email: {data[email_field]}")
    
    elif isinstance(data, list):
        for item in data:
            validate_email_field(item, email_field)
    
    return True
