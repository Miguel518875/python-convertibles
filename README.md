# python-convertibles  

Wrapper for Python native types (`int`, `float`, `str`, `bool`, `complex`)  
with **automatic validation** and support for a wide range of **magic methods (dunder methods)**.  

---

## 📦 Installation

Clone this repository and install in editable mode:

```bash
git clone https://github.com/YOUR_USER/python-convertibles.git
cd python-convertibles
python -m pip install -e .
```

---

## ✨ Features

- ✅ Safe conversion with `ValueError` for invalid inputs  
- ✅ Operator support (`+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `<`, `>`, etc.)  
- ✅ Integration with native functions (`len`, `abs`, `bool`, `int`, `float`, `complex`, etc.)  
- ✅ Friendly representation via `__repr__` and `__str__`  
- ✅ Almost identical behavior to native types, but with explicit validation  
- ✅ Unified interface:  
  - `convertibleToInt`  
  - `convertibleToFloat`  
  - `convertibleToStr`  
  - `convertibleToBool`  
  - `convertibleToComplex`  

---

## 🚀 Usage Examples

### Integers
```python
from convertibles import convertibleToInt

x = convertibleToInt("42")
print(x > 30)          # True
print(x * 2)           # 84
```

### Strings
```python
from convertibles import convertibleToStr

y = convertibleToStr(123)
print(y + "abc")       # "123abc"
print(len(y))          # 3
print("2" in y)        # True
```

### Floats
```python
from convertibles import convertibleToFloat

z = convertibleToFloat("3.14")
print(float(z) * 2)    # 6.28
print(abs(-z))         # 3.14
print(z ** 2)          # 9.8596
```

### Booleans
```python
from convertibles import convertibleToBool

b = convertibleToBool("hello")
print(bool(b))         # True
print(~b)              # False
print(b and True)      # True
```

### Complex numbers
```python
from convertibles import convertibleToComplex

c = convertibleToComplex("1+2j")
print(c + (2+3j))      # (3+5j)
print(abs(c))          # 2.23606797749979
print(str(c))          # "(1+2j)"
```

---

## 📘 Class Details

### 🔹 `convertibleToInt`
- Converts values to integer with validation  
- Implements:  
  - `__int__`, `__index__`, `__float__`  
  - Comparisons (`__eq__`, `__lt__`, `__gt__`)  
  - Math operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`)  
  - `__neg__`, `__abs__`, `__repr__`, `__call__`  

### 🔹 `convertibleToFloat`
- Converts values to float with validation  
- Implements:  
  - `__float__`, `__int__`, `__str__`  
  - Comparisons (`__eq__`, `__lt__`, `__gt__`)  
  - Full math operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`)  
  - `__neg__`, `__abs__`, `__repr__`, `__call__`  

### 🔹 `convertibleToStr`
- Converts values to string with validation  
- Implements:  
  - `__str__`, `__repr__`  
  - Comparisons (`__eq__`, `__lt__`, `__gt__`)  
  - Concatenation (`__add__`)  
  - `__len__`, `__getitem__`, `__contains__`  
  - `__call__`  

### 🔹 `convertibleToBool`
- Converts values to boolean with validation  
- Implements:  
  - `__bool__`, `__repr__`, `__eq__`  
  - Logical operators (`__invert__`, `__and__`, `__or__`)  
  - `__call__`  

### 🔹 `convertibleToComplex`
- Converts values to complex numbers with validation  
- Implements:  
  - `__complex__`, `__float__`, `__int__`, `__str__`, `__repr__`  
  - Comparisons (`__eq__`)  
  - Math operations (`+`, `-`, `*`, `/`)  
  - `__neg__`, `__abs__`, `__call__`  

---

## 🧩 Magic Methods Table

| Type       | Main implemented methods |
|------------|---------------------------|
| **Int**    | `__int__`, `__index__`, `__float__`, `__eq__`, `__lt__`, `__gt__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__neg__`, `__abs__`, `__repr__`, `__call__` |
| **Float**  | `__float__`, `__int__`, `__eq__`, `__lt__`, `__gt__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__neg__`, `__abs__`, `__repr__`, `__call__` |
| **Str**    | `__str__`, `__repr__`, `__len__`, `__getitem__`, `__contains__`, `__eq__`, `__lt__`, `__gt__`, `__add__`, `__call__` |
| **Bool**   | `__bool__`, `__repr__`, `__eq__`, `__invert__`, `__and__`, `__or__`, `__call__` |
| **Complex**| `__complex__`, `__float__`, `__int__`, `__str__`, `__repr__`, `__eq__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__neg__`, `__abs__`, `__call__` |

---

## 💡 Additional Information
- This project is ideal for **learning Python's magic methods (dunder methods)**.  
- Useful for understanding how Python's native types work “under the hood”.  
- Can be extended to support other types (`Decimal`, `Fraction`, `datetime`, etc.).  
- Not a replacement for native types in production — this is an **educational tool**.  

---

## 🏷️ License
[MIT](LICENSE) © Miguel
