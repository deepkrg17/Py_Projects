from dataclasses import dataclass


@dataclass
class chr_range:
    """Inclusive range for characters"""

    start: str
    stop: str
    step: int = 1

    def __new__(cls, start, stop, step=1):
        if len(start + stop) != 2:
            raise ValueError("Expected two characters as start and end")
        if any([start < stop, start > stop and step < 0]):
            return super().__new__(cls)
        return None

    def __iter__(self):
        start = ord(self.start)
        stop = ord(self.stop)
        for i in range(start, stop + 1, self.step):
            yield (chr(i))
