from bs4 import BeautifulSoup
from urllib.request import*
import winsound


def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html


def main():
    url = "https://radiomayak.ru/podcasts/archive/"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    _list = soup.find_all(class_="b-podcast__block-link")
    link_dict = {}
    output_txt_file = open('links.txt', mode='w', encoding='utf8')
    indx = 0
    for a in _list:
        second_html = get_html('https://radiomayak.ru'+a['href'])
        second_soup = BeautifulSoup(second_html, "html.parser")
        sound = second_soup.find_all(class_= "b-podcast__records-listen")
        for b in sound:
            indx += 1
            link_dict[b['data-title']] = b['data-url']
            print(b['data-title'], b['data-url'], file=output_txt_file)
    output_txt_file.close()


if __name__ == '__main__':
    main()
    print('Done!')
    try:
        winsound.PlaySound('C:/Windows/Media/Alarm03.wav', winsound.SND_ALIAS)
    except:
        pass
