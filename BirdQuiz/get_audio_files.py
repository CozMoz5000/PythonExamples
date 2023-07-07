import pathlib
import re
import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
BASE_URL = 'https://www.bird-sounds.net/'
BIRDS = ['American Robin', 'Blue Jay', 'Western Kingbird']

DIRECTORY = pathlib.Path('D:\\Music\\Bird Sounds')
DIRECTORY.mkdir(parents=True, exist_ok=True)

for bird in BIRDS:
    sanitzed_name = bird.replace(' ', '-').lower()
    url = f'{BASE_URL}{sanitzed_name}'
    print(f'Requesting: {url}')

    r = requests.get(
        url=url,
        headers={'User-Agent': USER_AGENT},
    )
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    for element in soup.find_all(name='source', src=re.compile(r'.*\.mp3')):
        mp3_file = requests.get(
            url=f'{BASE_URL}{element["src"]}',
            headers={'User-Agent': USER_AGENT},
        )
        with (DIRECTORY / f'{sanitzed_name}.mp3').open(mode='wb') as f:
            f.write(mp3_file.content)
