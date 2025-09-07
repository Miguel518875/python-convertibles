from typing import Any

class convertibleToBool:
    def __init__(self, texto: Any) -> None:
        try:
            self._value = bool(texto)
        except Exception:
            raise ValueError(f"'{texto}' is not convertible to bool")
        self.texto = texto

    def __bool__(self) -> bool:
        return self._value

    def __repr__(self) -> str:
        return f"convertibleToBool({self.texto!r} -> {self._value})"

    def __eq__(self, other: Any) -> bool:
        return self._value == bool(other)

    def __invert__(self) -> bool:
        return not self._value

    def __and__(self, other: Any) -> bool:
        return self._value and bool(other)

    def __or__(self, other: Any) -> bool:
        return self._value or bool(other)

    def __call__(self) -> bool:
        return self._value
