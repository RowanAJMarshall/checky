# Checky: a runtime type-checking decorator for Python

## Usage

```python

@check(args = (int, int), returns = int)
def add(num1, num2):
    return num1 + num2

```

```python

@check(kwargs = {"name": str}, returns = str)
def greet(name="Rowan"):
    return "Hello " + name + "!"

```
