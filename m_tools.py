import requests
import shutil
import urllib3


# Downloaden plaatje
def downloadImage(url, filename):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
    else:
        print("Downloaden van plaatje %s is niet gelukt." % url)


# Downloaden tekstbestand
def downloadText(url, filename):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    txt_str = str(r.data)
    # Fix voor fout in lezen (utf-8 error...)
    txt_str = txt_str[2:-1]
    lines = txt_str.split('\\n')
    f = open(filename, 'w')
    for line in lines:
        new_line = line.replace('\\t', '    ')
        f.write(new_line + '\n')
    f.close()
