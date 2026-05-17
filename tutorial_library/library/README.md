# Data Library

A modern Python library for processing, analyzing and validating data with ease.

## Installation

### From PyPI (when published)
```bash
pip install data
```

### Installation in development from GitHub
```bash
git clone https://github.com/mdfjbotss/data.git
cd data
pip install -e .
```

## Quick Start

```python
import data

# Load data
data_loaded = data.load_data("data.json")

# Process data
processor = data.DataProcessor(data_loaded)
filtered = processor.filter_by_key("status", "active")

# Analyze data
analyzer = data.DataAnalyzer(data_loaded)
statistics = analyzer.get_statistics()

# Validate data
schema = {"name": str, "age": int}
data.validate_schema({"name": "John", "age": 30}, schema)

# Save data
data.save_data(filtered, "output.json")
```

## Features

### 🔧 Data Processing
- `DataProcessor`: Filters, transforms and summarizes data
- Support for lists of dictionaries
- Custom transformation functions

### 📊 Data Analysis
- `DataAnalyzer`: Generates statistics
- Item counting
- Value frequency
- Schema information

### ✅ Data Validation
- Schema validation
- Required fields validation
- Email validation
- Custom validators

### 📁 Input/Output
- Load data from JSON and CSV
- Save in JSON and CSV
- Merge multiple datasets
- Data cleaning

## Examples

### Load and process data
```python
import data

# Load CSV data
users = data.load_data("users.csv")

# Create processor
proc = data.DataProcessor(users)

# Filter by age
adults = proc.filter_by_key("age", 18)

# Save results
data.save_data(adults, "adults.json")
```

### Validate data
```python
from data import validate_schema, ValidationError

schema = {
    "id": int,
    "name": str,
    "email": str,
    "age": int
}

user = {
    "id": 1,
    "name": "John Smith",
    "email": "john@example.com",
    "age": 30
}

try:
    validate_schema(user, schema)
    print("Data is valid!")
except ValidationError as e:
    print(f"Error: {e}")
```

### Analyze data
```python
import data

# Load data
employees = data.load_data("employees.json")

# Analyze
analyzer = data.DataAnalyzer(employees)
print(f"Total employees: {analyzer.count_items()}")
print(f"Statistics: {analyzer.get_statistics()}")

# Frequency of departments
freq_depts = analyzer.get_value_frequency("department")
print(f"Employees by department: {freq_depts}")
```

### Transform data
```python
import data

products = data.load_data("products.json")

proc = data.DataProcessor(products)

# Apply transformation (apply 10% discount)
with_discount = proc.map_transform(
    lambda p: {**p, "price": p["price"] * 0.9}
)

data.save_data(with_discount, "products_discount.json")
```

## API Reference

### DataProcessor
```python
processor = data.DataProcessor(data)

# Filter elements
result = processor.filter_by_key("key", "value")

# Transform data
transformed = processor.map_transform(function)

# Get summary
summary = processor.get_summary()
```

### DataAnalyzer
```python
analyzer = data.DataAnalyzer(data)

# Count items
total = analyzer.count_items()

# Get keys
keys = analyzer.get_keys()

# Value frequency
frequency = analyzer.get_value_frequency("key")

# Statistics
stats = analyzer.get_statistics()
```

### Utility Functions
```python
# Load data
data_loaded = data.load_data("file.json")

# Save data
data.save_data(data_loaded, "output.csv")

# Clean data
clean = data.clean_data(data_loaded)

# Merge data
result = data.merge_data(data1, data2, data3)
```

### Validators
```python
# Validate with schema
data.validate_schema(data, schema)

# Validate required fields
data.validate_required_fields(data, ["id", "name"])

# Validate emails
data.validate_email_field(data, "email")

# Custom validator
data.validate_data(data, lambda d: len(d) > 0)
```

## Requirements

- Python 3.8 or higher

## License

MIT License - See LICENSE for details

## Contributing

Contributions are welcome. Please:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

If you have questions or issues, open an issue in the repository.
