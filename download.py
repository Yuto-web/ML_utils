from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys


#API key の情報

key = "4af7b175f60ddc32f5ad34d27ade870e"
secret = "966a132ba38ec6d5"
wait_time = 1

#保存フォルダの指定
animalnames = [sys.argv[1], sys.argv[2]]

for animalname in animalnames:
    savedir = "./" + animalname
    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text = animalname,
        per_page = 400,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        extras = 'url_q, licence'
    )

    photos = result['photos']
    #pprint(photos)

    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        filepath = savedir + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath): continue
        urlretrieve(url_q, filepath)
        time.sleep(wait_time)
