# Checky: a runtime type-checking decorator for Python

## About

Checky lets you dynamically type-check your code at runtime, raising an error
if a function is called with or returns an unexpected type

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

## Changelog

0.1.0
-----
 * Support for simple builtin data types e.g. str, int
