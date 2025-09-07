from typing import Any

class convertibleToComplex:
    def __init__(self, texto: Any) -> None:
        try:
            self._value = complex(texto)
        except Exception:
            raise ValueError(f"'{texto}' is not convertible to complex")
        self.texto = texto

    def __complex__(self) -> complex:
        return self._value

    def __float__(self) -> float:
        # Se for puramente real, funciona
        if self._value.imag == 0:
            return float(self._value.real)
        raise TypeError("Cannot convert non-real complex to float")

    def __int__(self) -> int:
        if self._value.imag == 0:
            return int(self._value.real)
        raise TypeError("Cannot convert non-real complex to int")

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"convertibleToComplex({self.texto!r} -> {self._value})"

    # Comparações
    def __eq__(self, other: Any) -> bool:
        return self._value == complex(other)

    # Operações matemáticas
    def __add__(self, other: Any) -> complex:
        return self._value + complex(other)

    def __sub__(self, other: Any) -> complex:
        return self._value - complex(other)

    def __mul__(self, other: Any) -> complex:
        return self._value * complex(other)

    def __truediv__(self, other: Any) -> complex:
        return self._value / complex(other)

    def __neg__(self) -> complex:
        return -self._value

    def __abs__(self) -> float:
        return abs(self._value)

    def __call__(self) -> complex:
        return self._value
