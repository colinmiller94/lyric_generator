from bs4 import BeautifulSoup
import requests
import random



user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'

artist_url = 'https://genius.com/artists/Young-thug'

def get_song_url(artist_url):
    #get random album
    response = requests.get(artist_url, headers={'User-Agent': user_agent})

    soup = BeautifulSoup(response.text, "lxml")
    #print(soup)

    album_url_list =[]


    for link in soup.find_all('a', class_ = 'vertical_album_card'):
        if link.has_attr('href'):
            album_url_list.append(link['href'])


    album_url = random.choice(album_url_list)

    #Now get random song
    response = requests.get(album_url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.text, 'lxml')
    song_url_list = []


    for link in soup.find_all('a', class_ = 'u-display_block'):
        if link.has_attr('href'):
            if 'lyrics' in str(link['href']):
                song_url_list.append(link['href'])


    song_url = random.choice(song_url_list)
    return song_url


def get_lyric():

    song_url = get_song_url(artist_url)

    response = requests.get(song_url, headers = {'User_Agent' : user_agent})
    soup = BeautifulSoup(response.text, 'lxml')
    lyrics = soup.find('div', class_ = 'lyrics').text.strip()


    lst = lyrics.split('\n')


    newLyric = True

    while newLyric:
        i = random.randint(1,len(lst)-2)
        if len(lst[i]) > 10 and "[" not in lst[i] and ":" not in lst[i] and len(lst[i+1]) > 10 and "[" not in lst[i+1] and ":" not in lst[i+1]:
            lyric = lst[i] + "\n" + lst[i+1]
            newLyric = False

    return lyric

for i in range(100):
    print(get_lyric())
    print('-------------')