import requests, json

url = 'https://languagetool.org/api/v2/check'

def checkGrammar(text):
    data = {
        'text': text,
        'language': 'en-US',
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent':'python',
    }
    r = requests.post(url, data=data, headers=header)
    response = r.json()
    if len(response['matches']):
        error = response['matches'][0]['message']
        t = list(text)
        offset = response['matches'][0]['offset']
        length = response['matches'][0]['length']
        for i in range(offset, offset+length):
            t.pop(offset)
        insert = response['matches'][0]['replacements'][0]['value']
        for s in insert:
            t.insert(offset, s)
            offset+=1    
        correct = ''.join(t)
        result = error+'\n'+"The correct sentence could be: "+correct
        return result
    else:
        return "No grammatical errors found."    
    