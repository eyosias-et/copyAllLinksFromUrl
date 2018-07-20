import urllib3
import re
import sys
import pyperclip

http = urllib3.PoolManager()
if len(sys.argv) > 0:
    urls=""
    for url in sys.argv[1:]:
        req = http.request("GET", url)

        for match in re.finditer("<a href=[\'|\"]([^\'\"<>]*)[\'|\"]>", str(req.data)):
            print(url + match.group(1))
            urls += url + match.group(1) + "\n"
    pyperclip.copy(urls)
else:        
    url = input("Input URL")
    req = http.request("GET", "")

    urls = ""
    for match in re.finditer("<a href=[\'|\"]([^\'\"<>]*)[\'|\"]>", str(req.data)):
        print(url + match.group(1))
        urls += url + match.group(1) + "\n"
    pyperclip.copy(urls)
print("Parsed URLs copied to clipboard. Open a download manager start a \"Batch Download from Clipbaord\" or Something simillar. however it is Done on your specific Download Manager.")