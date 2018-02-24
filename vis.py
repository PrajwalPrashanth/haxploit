import requests
import json
import sume


def ocr_space_file(filename, overlay=False, api_key='a311ed074988957', language='eng'):
    

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='a311ed074988957', language='eng'):
   

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()



test_file = ocr_space_file(filename='j.jpg', language='eng')

loaded_json = json.loads(test_file)

f=loaded_json['ParsedResults']
x=f[0]
l=x['ParsedText'].encode('ascii','replace').decode('ascii','replace')


sume.smmm(l)




