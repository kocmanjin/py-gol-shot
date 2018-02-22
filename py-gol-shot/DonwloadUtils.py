import urllib.request



def download_data(url: str):
    print(url)
    url_link = urllib.request.urlopen(url)
    return url_link