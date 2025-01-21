#!/usr/bin/python
# -------------------------------------------------
__AUTHOR__ = 'Moj'
__TELEGRAM_ID__ = '@iranLwner'
__INSTAGRAM_ID__ = '@MJi_Devil'
__GITHUB__ = 'https://github.com/C4ssif3r'
__COMMENT__ = '''plz get me Star ⭐ :)'''

# -------------------------------------------------
# import mudules                                  |
# -------------------------------------------------
import os
import time
import sys
import concurrent.futures
from datetime import datetime
# ------------------------------------------------
try:
    import requests as req
except:
    os.system('pip install requests')
#--------------------------------------------
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
#--------------------------------------------
try:
    from colored import fg, bg, attr
except:
    os.system('pip install colored')
#--------------------------------------------
try:
    import pyuseragents as agent
except:
    os.system('pip install pyuseragents')
#--------------------------------------------
os.system('clear')
class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'
    white = '\033[00m'
def banner():
    print(f'''


{color.red}██   ██▄   █▀▄▀█ ▄█    ▄       {color.white}█ ▄▄  ██      ▄   ▄███▄   █         {color.green}▄████  ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄ 
{color.red}█ █  █  █  █ █ █ ██     █      {color.white}█   █ █ █      █  █▀   ▀  █         {color.green}█▀   ▀ ██     █  █  █  █▀   ▀  █  ▄▀ 
{color.red}█▄▄█ █   █ █ ▄ █ ██ ██   █     {color.white}█▀▀▀  █▄▄█ ██   █ ██▄▄    █         {color.green}█▀▀    ██ ██   █ █   █ ██▄▄    █▀▀▌  
{color.red}█  █ █  █  █   █ ▐█ █ █  █     {color.white}█     █  █ █ █  █ █▄   ▄▀ ███▄      {color.green}█      ▐█ █ █  █ █  █  █▄   ▄▀ █  █  
{color.red}   █ ███▀     █   ▐ █  █ █     {color.white} █       █ █  █ █ ▀███▀       ▀     {color.green} █      ▐ █  █ █ ███▀  ▀███▀     █   
{color.red}  █          ▀      █   ██     {color.white}  ▀     █  █   ██                   {color.green}  ▀       █   ██                ▀    
{color.red} ▀                             {color.white}       ▀                                        {color.green}

''')

banner()

print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Enter target url example: google.com (without http or https or www !)')

target_url = input('TARGET [URL] '+Fore.RED+'>_'+Fore.GREEN+' ')


print(Fore.RESET+'')

if 'http://' or 'https://' in target_url:
    pass


if 'http://' or 'https://' not in target_url:
    target_url = 'http://'+target_url

test = req.get(target_url)

time.sleep(5)

if test.status_code == 200:
    pass

else:
    print(Fore.RED+'cant connect to target '+Fore.WHITE+'> '+Fore.YELLOW+''+target_url)
    sys.exit()
target_url = target_url.replace('http://', '').replace('https://','')
print (f'''
methods:

    method 1 :
        the subdomains searcher for find subdamins from {target_url}
        example test with sub_manual:
        target > {target_url}
        example[1] > admin.{target_url}
        example[2] > cpanel.{target_url}
    
    method 2 :
        
        the manual list search admin panels with [patch(dirs)]
        example search with manual list:
        target > {target_url}
        example[1] > {target_url}/admin
        example[2] > {target_url}/cpanel


''')

select_method = input('Select [method]: 1[subdomain[finder]] —— 2[patch-dirs[finder]] '+Fore.RED+'>_'+Fore.WHITE+' ')

def log_output(message, logfile):
    print(message)
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

def sub_manual():

    '''
    the sub_manual for find subdamins 
    example test with sub_manual:
        target > test.com
        to > admin.test.com 
        to2 > cpanel.test.com
    '''
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    logfile = f'admin_finder_subdomains_{timestamp}.txt'
    log_output(f'[{Fore.GREEN}*{Fore.WHITE}] TARGET >>> {Fore.GREEN}{target_url}', logfile)

    links = open('.sub.txt', 'r').read().split()

    def heders():
        hd = agent.random()
        return hd

    heders1 = {
        'User-Agent': heders()
    }

    def check_link(link):
        try:
            url = ('http://'+link+'.'+target_url)
            get_req = req.get(url, timeout=20, headers=heders1)
            msg = f'[{Fore.GREEN}OK{Fore.WHITE}] founded a page - URL > %s%s {url} %s' % (fg('black'), bg('green'), attr('reset'))
            log_output(msg, logfile)
        
        except Exception:
            msg = f'[{Fore.RED}NOT{Fore.WHITE}] cant found page - URL > %s%s {url} %s' % (fg('black'), bg('red'), attr('reset'))
            log_output(msg, logfile)
    
        except KeyboardInterrupt:
            msg = '\nBye !'
            log_output(msg, logfile)
            time.sleep(3)
            sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_link, links)

def manual_list():
    '''
    the manual_list search admin panels with [patch{dirs}]
    example search with manual_list:
        target > test.com
        to > test.com/admin
        to2 > test.com/cpanel
    '''
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    logfile = f'admin_finder_paths_{timestamp}.txt'
    log_output(f'[{Fore.GREEN}*{Fore.WHITE}] TARGET >>> {Fore.GREEN}{target_url}', logfile)

    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    link_file = os.path.join(script_dir, '.link.txt')

    # Try different encodings if one fails
    encodings = ['utf-8', 'latin-1', 'cp1252', 'ascii']
    links = None

    for encoding in encodings:
        try:
            if not os.path.exists(link_file):
                print(Fore.RED + '[ERROR]' + Fore.WHITE + f' .link.txt file not found in {script_dir}')
                print(Fore.YELLOW + '[INFO]' + Fore.WHITE + ' Please create .link.txt file with list of paths to check')
                sys.exit(1)
                
            with open(link_file, 'r', encoding=encoding) as f:
                links = f.read().strip().split()
                break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(Fore.RED + '[ERROR]' + Fore.WHITE + f' Failed to read .link.txt: {str(e)}')
            sys.exit(1)

    if links is None:
        print(Fore.RED + '[ERROR]' + Fore.WHITE + ' Could not read .link.txt with any supported encoding')
        sys.exit(1)

    if not links:
        print(Fore.RED + '[ERROR]' + Fore.WHITE + ' .link.txt file is empty')
        sys.exit(1)

    def heders():
        hd = agent.random()
        return hd

    heders1 = {
        'User-Agent': heders()
    }

    def check_link(link):
        try:
            url = ('http://'+target_url+'/'+link)
            get_req = req.get(url, timeout=20, headers=heders1)
            sisad = 399
            charsad = 400
            charnono = 499

            if get_req.status_code < sisad:
                msg = f'[{Fore.GREEN}OK{Fore.WHITE}] founded a page - URL > %s%s {url} %s' % (fg('black'), bg('green'), attr('reset'))
                log_output(msg, logfile)
            
            if get_req.status_code > charsad:
                msg = f'[{Fore.RED}NOT{Fore.WHITE}] cant found page - URL > %s%s {url} %s' % (fg('black'), bg('red'), attr('reset'))
                log_output(msg, logfile)
    
            if get_req.status_code > charnono:
                msg = f'[{Fore.YELLOW}Server-ERROR{Fore.WHITE}] SERVER ERROR - URL > %s%s {url} %s' % (fg('white'), bg('yellow'), attr('reset'))
                log_output(msg, logfile)
    
        except KeyboardInterrupt:
            msg = '\nBye !'
            log_output(msg, logfile)
            time.sleep(3)
            sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_link, links)

if select_method == '1':
    sub_manual()
elif select_method == '2':
    manual_list()
else:
    print (Fore.RED+'[ERROR]'+Fore.WHITE+' please enter valid method (1) or (2) ! \n enter for exit .')
    input ('')
    sys.exit(1)

