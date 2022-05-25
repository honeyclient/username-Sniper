import requests, threading, random, time, os
from keep_alive import keep_alive
from discordwebhook import Discord
def check():
    try:
        users = ""
        for x in range(5):
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            users = users + str(random.choice(letters))
        print(users)
        username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={users}')
        if username.json()['message'] == "Username is valid":
           discord = Discord(url="https://discord.com/api/webhooks/978843703475064874/F77Z0XYSRnIcJmZWfu6tczM0EBmkZWDJ0LsZlBOVa2Lt7VIeC8ySgmo6CMgVg6mZ59eP")
           discord.post(
    embeds=[
        {
            "title": "BLOX USERNAME SNIPER",
            "fields": [
                {"name": "Letters:", "value": 5},
                {"name": "Username:", "value": users},
            ],
            "footer": {
                "text": "BLOX | Username Sniper | dsc.gg/synapse",
                "icon_url": "https://cdn.discordapp.com",
            },
        }
    ],
)
           open("available.txt", "a").write(users + '\n')
           time.sleep(1)
    except:
        pass
keep_alive()

while True:
    threading.Thread(target=check,).start()