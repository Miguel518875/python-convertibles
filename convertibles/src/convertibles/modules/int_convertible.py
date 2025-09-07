from typing import Any

class convertibleToInt:
    def __init__(self, texto: Any) -> None:
        try:
            self._value = int(texto)
        except Exception:
            raise ValueError(f"'{texto}' is not convertible to int")
        self.texto = texto

    def __int__(self) -> int:
        return self._value

    def __index__(self) -> int:
        return self._value  # permite usar como índice em listas

    def __float__(self) -> float:
        return float(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"convertibleToInt({self.texto!r} -> {self._value})"

    def __eq__(self, other: Any) -> bool:
        return self._value == int(other)

    def __lt__(self, other: Any) -> bool:
        return self._value < int(other)

    def __gt__(self, other: Any) -> bool:
        return self._value > int(other)

    def __add__(self, other: Any):
        return self._value + int(other)

    def __sub__(self, other: Any):
        return self._value - int(other)

    def __mul__(self, other: Any):
        return self._value * int(other)

    def __truediv__(self, other: Any):
        return self._value / int(other)

    def __call__(self) -> int:
        return self._value
