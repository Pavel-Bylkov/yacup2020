import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def main():
    from sys import stdin
    url_server = stdin.readline().strip()
    port = stdin.readline().strip()
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    urlData = f"{url_server}:{port}?a={a}&b={b}"
    jsonData = getResponse(urlData)
    print(sum(jsonData))

main()