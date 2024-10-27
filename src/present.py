from typing import List


class Present:
    def __init__(self, dim_data: List[int]):

        try:
            self.dimensions: List[int] = dim_data

        except ValueError as e:
            print(e)
    
    def calc_surface_area(self):
        l, w, h = self.dimensions
        lw: int = l*w
        wh: int = w*h
        hl: int = h*l

        return 2*lw + 2*wh + 2*hl + min(lw, wh, hl)
    
    def feet_of_ribbon(self):
        try:
            d1, d2, d3 = sorted(self.dimensions)
            return d1 * 2 + d2 * 2 + (d1 * d2 * d3)
        except Exception as e:
            print(e)
