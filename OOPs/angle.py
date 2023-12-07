from __future__ import annotations


class Angle:
    def __init__(self, deg: int, mint: int, sec: int):
        ext_mint, self.sec = divmod(sec, 60)
        ext_deg, self.mint = divmod(mint + ext_mint, 60)
        self.deg = deg + ext_deg

    @staticmethod
    def avg(*args: Angle):
        deg = mint = sec = 0
        n = len(args)
        for ang in args:
            deg += ang.deg
            mint += ang.mint
            sec += ang.sec

        deg, ext_deg = divmod(deg, n)
        mint, ext_mint = divmod(mint + (ext_deg * 60), n)
        sec = (sec + (ext_mint * 60)) // n

        return Angle(deg, mint, sec)

    def __add__(self, other: Angle):
        return Angle(self.deg + other.deg, self.mint + other.mint, self.sec + other.sec)

    def __str__(self):
        return f"{self.deg}°{self.mint}'{self.sec}\""
