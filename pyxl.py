import numpy as np
import xlsxwriter

workbook = xlsxwriter.Workbook('./files/arrays3.xlsx')
worksheet = workbook.add_worksheet()

cells_number = 25
rows = 5
cols = 5
array = np.random.choice(cells_number, (rows, cols), replace=False)

col = 0

middle_row = rows % 2 + 1
middle_col = cols % 2 + 1


class Board:

    def __init__(self, middle_number):
        self.middle_number = middle_number

    def draw_board(self):
        for row, data in enumerate(array):
            print('TEST')
            print(data)
            # middle_number = 0
            if row == middle_row:
                self.middle_number = data[middle_col]
                print(self.middle_number)
                data[middle_col] = 0
            worksheet.write_row(row, col, data)

    def swap_cells(self):
        for row, data in enumerate(array):
            new_data = [self.middle_number if i == 0 else i for i in data]  # -->
            worksheet.write_row(row, col, new_data)

    # def set_joker(self, data, middle_number):
    #     print(middle_number)
    #     new_data = [middle_number if i == 0 else i for i in data]  # -->
    #     return new_data


b1 = Board(1)
b1.draw_board()
b1.swap_cells()

workbook.close()
