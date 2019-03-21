from sudoku_gen import main as sudoku_gen
from difficult_sudoku_gen import main as diff_gen
from sudoku_solver import main as sudoku_solver
from fpdf import FPDF
import utils
from graphics_app import main as GA


def gen_pdf(field_rows:list):
    new_rows = []
    c = 0
    for row in field_rows:
        c += 1
        row.insert(6, '  ')
        row.insert(3, '  ')
        new_rows.append(' '.join(list(map(str, row))))
        if c % 3 == 0:
            new_rows.append('')

    pdf = FPDF(unit='mm')
    pdf.add_font('BPmono', '', 'BPmonoItalics.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('BPmono', size=16)
    ln = 0
    for row in new_rows:
        ln += 1
        pdf.cell(200, 10, txt=row+'\n', ln=1, align='L')
    pdf.output('the_field.pdf')


if __name__ == '__main__':
    print('''
    1: Генератор расстановки для судоку + PDF
    2: Генератор поля судоку по сложности
    3: Решатель судоку по полю (автоматически генерируется поле, а затем решается)
    4: Графическое судоку
    ''')
    program = int(input('Выберите программу (1-4):'))
    if program == 1:
        sudoku_gen()
    elif program == 2:
        diff_gen(int(input('Введите сложность (1-3):')))
    elif program == 3:
        diff_gen(1)
        sudoku_solver()
    elif program == 4:
        GA(1)


    f = utils.read_field('new_field.txt')
    gen_pdf(f)
