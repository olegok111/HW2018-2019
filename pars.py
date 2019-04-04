import fpdf
import requests as rq
import os

pdf = fpdf.FPDF()

for i in range(4,10):
    r = rq.get(f'http://arch.rgdb.ru/xmlui/bitstream/handle/123456789/43489/Image0000{i}.jpg?sequence={i-2}')
    #print(type(r.content))
    with open(f'{i}.jpg', 'wb') as outfile:
        outfile.write(r.content)
    pdf.add_page('L')
    pdf.image(f'{i}.jpg', w=200)



for i in range(11, 51):
    r = rq.get(f'http://arch.rgdb.ru/xmlui/bitstream/handle/123456789/43489/Image000{i}.jpg?sequence={i - 2}')
    #print(type(r.content))
    with open(f'{i}.jpg', 'wb') as outfile:
        outfile.write(r.content)
    pdf.add_page('L')
    pdf.image(f'{i}.jpg', w=200)

pdf.output('diafilm.pdf', 'F')

for file in os.listdir(os.getcwd()):
    if file.endswith('.jpg'):
        os.remove(file)
