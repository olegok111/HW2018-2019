from sudoku_gen import main as sudoku_gen
from difficult_sudoku_gen import main as diff_gen, read_field
from fpdf import FPDF


def gen_pdf(field_rows:list):
    new_rows = []
    c = 0
    for row in field_rows:
        c += 1
        row.insert(6, '   ')
        row.insert(3, '   ')
        new_rows.append(''.join(list(map(str, row))))
        if c % 3 == 0:
            new_rows.append('')

    pdf = FPDF(unit='mm')
    pdf.add_font('BPmono', '', 'BPmonoItalics.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('Helvetica', size=16)
    ln = 0
    for row in new_rows:
        ln += 1
        pdf.cell(200, 10, txt=row+'\n', ln=1, align='L')
    pdf.output('the_field.pdf')


if __name__ == '__main__':
    sudoku_gen()
    diff_gen()
    f = read_field('new_field.txt')
    gen_pdf(f)
