# 📚 Complete Guide: Python Library `data`

## 📋 Overview

A complete, modular and professional Python library called **`data`** has been created that works as an importable package. The library allows:

✅ **Process** data (filtering, transformation)
✅ **Analyze** data (statistics, frequencies)
✅ **Validate** data (schemas, required fields)
✅ **Load/Save** data (JSON, CSV)
✅ **Merge and clean** data

---

## 📁 Folder Structure

```
data/
├── data/                    # Main package
│   ├── __init__.py         # Package initializer
│   ├── core.py             # DataProcessor and DataAnalyzer classes
│   ├── utils.py            # Utility functions
│   └── validators.py       # Validators and schemas
├── setup.py                # Installation configuration
├── LICENSE                 # MIT License
├── README.md               # Complete documentation
├── .gitignore             # Files to ignore in git
├── tests.py               # Unit tests
└── example_usage.py       # Practical examples
```

---

## 🚀 Installation

### Option 1: Install in development mode (recommended)

```bash
# Clone the repository
git clone https://github.com/mdfjbotss/data.git
cd data

# Install in development mode
pip install -e .
```

### Option 2: Install from local file

```bash
cd path/to/data
pip install .
```

### Option 3: Add to PYTHONPATH

```bash
# On Linux/Mac
export PYTHONPATH="${PYTHONPATH}:/path/to/data"

# On Windows (PowerShell)
$env:PYTHONPATH += ";C:\path\to\data"
```

### Option 4: Install directly from GitHub

```bash
pip install git+https://github.com/mdfjbotss/data.git
```

---

## 📖 Basic Usage

After installation, import and use the library:

```python
import data

# 1. Create data
employees = [
    {"id": 1, "name": "John", "department": "IT"},
    {"id": 2, "name": "Mary", "department": "HR"},
]

# 2. Process
processor = data.DataProcessor(employees)
it_staff = processor.filter_by_key("department", "IT")

# 3. Analyze
analyzer = data.DataAnalyzer(employees)
print(f"Total: {analyzer.count_items()}")

# 4. Validate
schema = {"id": int, "name": str, "department": str}
data.validate_schema(employees[0], schema)

# 5. Save
data.save_data(employees, "output.json")
```

---

## 🔧 Main Classes and Functions

### DataProcessor

**Purpose**: Process and transform data

```python
processor = data.DataProcessor(data)

# Filter by key and value
filtered = processor.filter_by_key("status", "active")

# Transform data
transformed = processor.map_transform(lambda item: {...})

# Get summary
summary = processor.get_summary()
```

### DataAnalyzer

**Purpose**: Analyze and generate statistics

```python
analyzer = data.DataAnalyzer(data)

# Count items
count = analyzer.count_items()

# Get available keys
keys = analyzer.get_keys()

# Get frequency of values
frequency = analyzer.get_value_frequency("department")

# Get statistics
stats = analyzer.get_statistics()
```

### Utility Functions

```python
# Load from JSON or CSV
data = data.load_data("file.json")

# Save to JSON or CSV
data.save_data(data, "output.csv")

# Remove None and empty values
clean = data.clean_data(data)

# Merge multiple datasets
merged = data.merge_data(data1, data2, data3)
```

### Validators

```python
# Validate schema
data.validate_schema(data, schema)

# Validate required fields
data.validate_required_fields(data, ["id", "name"])

# Validate email field
data.validate_email_field(data, "email")

# Custom validator
data.validate_data(data, lambda d: len(d) > 0)
```

---

## 💡 Practical Examples

### Example 1: Process employee data

```python
import data

# Load data
employees = data.load_data("employees.json")

# Filter active employees
processor = data.DataProcessor(employees)
active = processor.filter_by_key("status", "active")

# Save filtered data
data.save_data(active, "active_employees.json")
```

### Example 2: Analyze sales data

```python
import data

# Load sales data
sales = data.load_data("sales.csv")

# Create analyzer
analyzer = data.DataAnalyzer(sales)

# Get statistics
print(f"Total sales: {analyzer.count_items()}")
print(f"Sales per region: {analyzer.get_value_frequency('region')}")
```

### Example 3: Validate user data

```python
import data

# Define schema
user_schema = {
    "id": int,
    "name": str,
    "email": str,
    "age": int
}

# Load users
users = data.load_data("users.json")

# Validate each user
for user in users:
    try:
        data.validate_schema(user, user_schema)
        data.validate_email_field(user, "email")
        print(f"✓ {user['name']} is valid")
    except data.ValidationError as e:
        print(f"✗ {user['name']}: {e}")
```

### Example 4: Transform and save data

```python
import data

# Load products
products = data.load_data("products.json")

# Create processor
proc = data.DataProcessor(products)

# Apply 20% discount
discounted = proc.map_transform(
    lambda p: {**p, "price": p["price"] * 0.8}
)

# Save discounted products
data.save_data(discounted, "products_discounted.json")
```

### Example 5: Clean and merge data

```python
import data

# Load two datasets
data1 = data.load_data("customers1.csv")
data2 = data.load_data("customers2.csv")

# Merge
merged = data.merge_data(data1, data2)

# Clean
clean = data.clean_data(merged)

# Save
data.save_data(clean, "all_customers.json")
```

---

## 🧪 Running Tests

```bash
cd data
python tests.py
```

Expected output:
```
==================================================
Running Data Library Tests
==================================================

Testing DataProcessor...
✓ DataProcessor working correctly
Testing DataAnalyzer...
✓ DataAnalyzer working correctly
Testing Validators...
✓ Schema validation correct
✓ Invalid data detection correct
Testing Utils...
✓ Utility functions working correctly

==================================================
✓ All tests passed successfully!
==================================================
```

---

## 🎯 Running Examples

```bash
cd data
python example_usage.py
```

This will run 10 practical examples demonstrating all features of the library.

---

## 📦 Integration with GitHub

### Push to GitHub

```bash
# Navigate to your repository
cd /path/to/data

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Data library v1.0.0"

# Add remote repository
git remote add origin https://github.com/mdfjbotss/data.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Clone from GitHub

```bash
git clone https://github.com/mdfjbotss/data.git
cd data
pip install -e .
```

---

## 🔐 Using in Your Projects

### After installation, use in any Python file:

```python
# my_script.py
import data

def process_company_data():
    # Load data
    employees = data.load_data("employees.json")
    
    # Process
    processor = data.DataProcessor(employees)
    active = processor.filter_by_key("status", "active")
    
    # Analyze
    analyzer = data.DataAnalyzer(active)
    stats = analyzer.get_statistics()
    
    # Validate
    schema = {"id": int, "name": str}
    for emp in active:
        data.validate_schema(emp, schema)
    
    # Save
    data.save_data(active, "output.json")
    
    return stats

if __name__ == "__main__":
    stats = process_company_data()
    print(stats)
```

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Make your changes
4. Run tests: `python tests.py`
5. Commit: `git commit -m "Add YourFeature"`
6. Push: `git push origin feature/YourFeature`
7. Open a Pull Request

---

## 📋 API Quick Reference

### DataProcessor Methods
- `filter_by_key(key, value)` - Filter items by key
- `map_transform(function)` - Apply transformation
- `get_summary()` - Get data summary

### DataAnalyzer Methods
- `count_items()` - Count total items
- `get_keys()` - Get available keys
- `get_value_frequency(key)` - Get value frequency
- `get_statistics()` - Get general statistics

### Utility Functions
- `load_data(filepath)` - Load from JSON/CSV
- `save_data(data, filepath)` - Save to JSON/CSV
- `clean_data(data)` - Remove empty values
- `merge_data(*datasets)` - Merge datasets

### Validator Functions
- `validate_data(data, func)` - Custom validation
- `validate_schema(data, schema)` - Schema validation
- `validate_required_fields(data, fields)` - Required fields
- `validate_email_field(data, field)` - Email validation

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🆘 Support and Issues

- **Documentation**: Check README.md
- **Examples**: Run example_usage.py
- **Tests**: Run tests.py
- **Issues**: Open an issue on GitHub

---

## ✨ Features Summary

| Feature | Description |
|---------|-------------|
| 🔧 Data Processing | Filter, transform, and summarize data |
| 📊 Data Analysis | Generate statistics and frequencies |
| ✅ Data Validation | Validate schemas and required fields |
| 📁 File I/O | Load/save JSON and CSV files |
| 🧹 Data Cleaning | Remove empty and None values |
| 🔀 Data Merging | Combine multiple datasets |
| 🎯 Custom Validators | Create custom validation functions |
| 📧 Email Validation | Built-in email validation |
| 🧪 Fully Tested | Comprehensive test suite included |
| 📖 Well Documented | Clear examples and API reference |

---

**Ready to use! Happy data processing! 🚀**
