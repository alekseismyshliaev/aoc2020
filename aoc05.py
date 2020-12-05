import sys


class Seat:
    __slots__ = ('row', 'col')

    def __init__(self, row, col):
        self.row = row
        self.col = col

    @property
    def seat_id(self):
        '''Calculate seat id number'''
        return self.row * 8 + self.col

    @classmethod
    def from_string(cls, data):
        '''Convert from a 10-digit binary string

        :param data: string, first 7 characters describe the row number,
            last 3 characters describe column number
        :returns: Seat instance
        '''
        rowdata = data[:7]
        coldata = data[7:10]

        rownum = int(rowdata.replace('F', '0').replace('B', '1'), base=2)
        colnum = int(coldata.replace('L', '0').replace('R', '1'), base=2)
        return cls(rownum, colnum)


if __name__ == '__main__':
    scanned_passes = []
    for line in sys.stdin:
        scanned_passes.append(Seat.from_string(line.rstrip('\n')))

    print(max(seat.seat_id for seat in scanned_passes))
