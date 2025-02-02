import os.path

import requests

__dir__ = os.path.dirname(__file__)
urls = ['https://zh.kcwiki.cn/index.php?title=%E4%BB%BB%E5%8A%A1&action=raw',
        'https://zh.kcwiki.cn/index.php?title=%E4%BB%BB%E5%8A%A1/%E6%9C%9F%E9%97%B4%E9%99%90%E5%AE%9A%E4%BB%BB%E5%8A%A1'
        '&action=raw',
        'https://zh.kcwiki.cn/index.php?title=%E4%BB%BB%E5%8A%A1/%E6%9C%80%E6%96%B0%E4%BB%BB%E5%8A%A1&action=raw',
        ]  # 三个需要抓取的网站
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.104 Safari/537.36',
    'cookie': "_ga=GA1.2.1881705690.1629543107; VEE=wikitext; vector-nav-p-.E5.B8.B8.E7.94.A8.E9.80.9F.E6.9F.A5=true; "
              "vector-nav-p-.E5.87.BA.E5.87.BB.E6.B5.B7.E5.9F.9F=true; vector-nav-p-tb=true; "
              "vector-nav-p-.E5.8F.82.E4.B8.8E.E7.BC.96.E5.86.99kcwiki=true; vector-nav-p-.E6.B2.99.E7.9B.92=true; "
              "vector-nav-p-.E6.B8.B8.E6.88.8F.E6.96.87.E5.8C.96=true; "
              "vector-nav-p-kcwiki.E6.97.97.E4.B8.8B.E9.A1.B9.E7.9B.AE=true; vector-nav-p-.E9.81.93.E5.85.B7=true; "
              "vector-nav-p-.E5.85.A5.E6.B8.A0.E3.83.BB.E8.A1.A5.E7.BB.99=true; "
              "vector-nav-p-.E6.94.B9.E8.A3.85.E3.83.BB.E5.B7.A5.E5.8E.82=true; kcwiki_UserName=Callofblood; "
              "kcwiki_UserID=5277; kcwiki_Token=a696414057db9b77a8a4472b77eeaf90; _gid=GA1.2.1109110936.1631275946; "
              "kcwiki__session=1tin18vua2u0c4nmk9i511h50fbbsqm7; vector-nav-p-.E4.BB.BB.E5.8A.A1=true "
}


def save(text, index):
    pages = text.split('页首}}\n')
    for page_index, page in enumerate(pages[1:]):
        with open('{}/../rs/{}-{}.txt'.format(__dir__, index, page_index), 'w', encoding='utf-8') as f:
            f.write(page.split('{{页尾')[0])


def run():
    session = requests.Session()
    session.headers = headers
    print(__dir__)
    for index, url in enumerate(urls):
        result = session.get(url)
        # with open('{}/../AllTasks.txt'.format(__dir__), 'w+', encoding='utf-8') as f:
        #     f.write(result.text)
        save(result.text, index)


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    # run()
