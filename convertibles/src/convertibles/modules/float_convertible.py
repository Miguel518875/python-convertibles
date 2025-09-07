from typing import Any

class convertibleToFloat:
    def __init__(self, texto: Any) -> None:
        try:
            self._value = float(texto)
        except Exception:
            raise ValueError(f"'{texto}' is not convertible to float")
        self.texto = texto

    def __float__(self) -> float:
        return self._value

    def __int__(self) -> int:
        return int(self._value)

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return f"convertibleToFloat({self.texto!r} -> {self._value})"

    # Comparações
    def __eq__(self, other: Any) -> bool:
        return self._value == float(other)

    def __lt__(self, other: Any) -> bool:
        return self._value < float(other)

    def __gt__(self, other: Any) -> bool:
        return self._value > float(other)

    # Operações matemáticas
    def __add__(self, other: Any) -> float:
        return self._value + float(other)

    def __sub__(self, other: Any) -> float:
        return self._value - float(other)

    def __mul__(self, other: Any) -> float:
        return self._value * float(other)

    def __truediv__(self, other: Any) -> float:
        return self._value / float(other)

    def __floordiv__(self, other: Any) -> int:
        return self._value // float(other)

    def __mod__(self, other: Any) -> float:
        return self._value % float(other)

    def __pow__(self, other: Any) -> float:
        return self._value ** float(other)

    def __neg__(self) -> float:
        return -self._value

    def __abs__(self) -> float:
        return abs(self._value)

    def __call__(self) -> float:
        return self._value
