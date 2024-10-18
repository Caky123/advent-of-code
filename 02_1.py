from util import read_file_by_line as read_file

class Present:
    def __init__(self, data):

        try:
            self.l = int(data[0])
            self.w = int(data[1])
            self.h = int(data[2])
            self.surface_area = 0
            self.calc_dimension()
        except Exception as e:
            print(e)
            exit(0)
    
    def calc_dimension(self):
        lw = self.l*self.w
        wh = self.w*self.h
        hl = self.h*self.l

        self.surface_area = 2*lw + 2*wh + 2*hl + min(lw, wh, hl)

total = 0
for line in read_file('data/day02/input.txt'):
    present = Present(line.split("x"))
    total += present.surface_area

print(f"Result is <{total}>")