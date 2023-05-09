import sys
from urllib.request import urlopen
def check_website_st(yoururls):
    for url in yoururls:
        try:
            response = urlopen(url)
            if response.getcode() == 200 or response.getcode() == 302:
                print(f"{url} - OK")
            else:
                print(f"{url} - FAIL")
        except:
            print(f"{url} - FAIL")
def main():
    while True:
        yoururls=[input("Enter your url:")]
        check_website_st(yoururls)
        yourchoice=input("Do you want to continue?Y/N: ")
        if yourchoice=="Y" or yourchoice=="y":
            main()
        if yourchoice=="N" or yourchoice=="n":
            sys.exit()
        else:
            print("There is no such symbol")
            
main()