from time import sleep

classmates = [
    736419735,
    5200613842,
    769261945,
    1129340099,
    1013678603,
    878679344,
    732773897,
    792643492,
    631487736,
    1260207019,
    2023501286,
    717628531,
    493205532,
    796941936,
    1290382750,
    642098524
]

def mafia(client, message):
    text = message.text.split("#mafia ")[-1]
    for i in classmates:
        try:
            client.send_message(i, text)
        except:
            print("mafia bad")
        sleep(0.2)