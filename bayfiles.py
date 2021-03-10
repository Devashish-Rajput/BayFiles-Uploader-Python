import requests
import sys
import json
import os
path = "/Your Path to files/"
url = 'https://api.bayfiles.com/upload'
#url = 'https://api.anonfiles.com/upload'
filepaths = [os.path.join(path, file) for file in os.listdir(path)]
print(filepaths)
for x in filepaths:
    try:
        files = {'file': (open(x, 'rb'))}
    except FileNotFoundError:
        print(f'[ERROR] The file "{x}" doesn\'t exist!')
    except IsADirectoryError:
        print('[ERROR] You cannot upload a directory!')
    r = requests.post(url, files=files)
    print("[UPLOADING]", x)
    resp = json.loads(r.text)
    if resp['status']:
        urlshort = resp['data']['file']['url']['short']
        urllong = resp['data']['file']['url']['full']
        print(f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
    else:
        message = resp['error']['message']
        errtype = resp['error']['type']
        print(f'[ERROR] {message}\n{errtype}')
#upload()
