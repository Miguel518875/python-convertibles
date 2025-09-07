from typing import Any

class convertibleToStr:
    def __init__(self, texto: Any) -> None:
        try:
            self._value = str(texto)
        except Exception:
            raise ValueError(f"'{texto}' is not convertible to str")
        self.texto = texto

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"convertibleToStr({self.texto!r} -> {self._value!r})"

    def __eq__(self, other: Any) -> bool:
        return self._value == str(other)

    def __lt__(self, other: Any) -> bool:
        return self._value < str(other)

    def __gt__(self, other: Any) -> bool:
        return self._value > str(other)

    def __add__(self, other: Any) -> str:
        return self._value + str(other)

    def __len__(self) -> int:
        return len(self._value)

    def __getitem__(self, index: int) -> str:
        return self._value[index]

    def __contains__(self, item: Any) -> bool:
        return str(item) in self._value

    def __call__(self) -> str:
        return self._value
