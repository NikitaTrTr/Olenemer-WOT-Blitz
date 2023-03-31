from PIL import ImageGrab
from screen_cutter import get_nicknames_images
import cv2 as cv
from pytesseract import image_to_string
from classes import player_stats
import urllib.request, json

class statistic_checker():
    def __init__(self):
        self.screen_config = "configs/1920.1080.125.txt"

    def return_olenei(self):
        screen_size_x, screen_size_y = self.screen_config[8:].split(sep='.')[0:2]
        self.take_screenshot(int(screen_size_x), int(screen_size_y))
        souz, vragi = get_nicknames_images("out/oleni.png", self.screen_config)
        souz_nicknames, vragi_nicknames, team_size = self.scan_olenei(souz, vragi)
        dictionary = self.load_dictionary()
        decoded_souz_team = [self.decode(nick, dictionary) for nick in souz_nicknames]
        decoded_vragi_team = [self.decode(nick, dictionary) for nick in vragi_nicknames]

        souz_team_responses = [self.send_request(nick) for nick in decoded_souz_team]
        vragi_team_responses = [self.send_request(nick) for nick in decoded_vragi_team]

        souz_player_stats = [self.parse_response(player) for player in souz_team_responses]
        vragi_player_stats = [self.parse_response(player) for player in vragi_team_responses]
        return souz_player_stats, vragi_player_stats, team_size



    def scan_olenei(self, souz, vragi):
        souz_nicknames = []
        vragi_nicknames = []
        for i in range(7):
            img = cv.resize(souz[i], None, fx=2.3, fy=2, interpolation=cv.INTER_LINEAR)
            img = cv.threshold(img, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
            nickname = image_to_string(img, config="-c tessedit_char_whitelist=0123456789")[0:-1]
            if len(nickname.split())>1:
                souz_nicknames.append(nickname.split()[0])
            else:
                souz_nicknames.append(nickname)
        for i in range(7):
            img = cv.resize(vragi[i], None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)
            img = cv.threshold(img, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
            nickname = image_to_string(img, config="-c tessedit_char_whitelist=0123456789")[0:-1]
            if len(nickname.split()) > 1:
                vragi_nicknames.append(nickname.split()[1])
            else:
                vragi_nicknames.append(nickname)
        team_size = 7
        for i in range(7):
            if len(''.join(list(filter(lambda x: x != ' ', souz_nicknames[i])))) == 0:
                team_size = i + 1
        return souz_nicknames, vragi_nicknames, team_size


    def send_request(self, nickname):
        if nickname == "":
            return 0, -1
        url = f"https://api.wotblitz.ru/wotb/account/list/?application_id=f35eae96ca784b31d1a85c258e31eab9&search={nickname}&type=exact"
        id_data = json.load(urllib.request.urlopen(url))
        if id_data['status'] == 'error':
            return 0, -1
        if id_data['meta']['count']!=0:
            id = id_data['data'][0]['account_id']
            url = f"https://api.wotblitz.ru/wotb/account/info/?application_id=f35eae96ca784b31d1a85c258e31eab9&account_id={id}&fields=statistics.all.wins%2C+statistics.all.battles"
            data = json.load(urllib.request.urlopen(url))
        else:
            data = 0
            id = -1
        return data,id

    def parse_response(self, data):
        id = data[1]
        if data[0] == 0:
            win_rate = 0
            tank_win_rate = 0
            tank_damage = 0
        else:
            wins = data[0]["data"][str(id)]["statistics"]["all"]["wins"]
            battles = data[0]["data"][str(id)]["statistics"]["all"]["battles"]
            if battles !=0:
                win_rate = wins/battles*100
            else:
                win_rate = 0
            tank_win_rate = 0
            tank_damage = 0
        player = player_stats(id, win_rate, tank_win_rate, tank_damage)
        return player


    def take_screenshot(self, screen_size_x, screen_size_y):
        image = ImageGrab.grab(bbox=(0, 0, screen_size_x, screen_size_y))
        image.save('out/oleni.png')

    def load_dictionary(self):
        dct = {}
        with open("source/encoding_dictionary.txt", 'r') as dictionary:
            number_of_lines = 66
            for i in range(number_of_lines):
                character = dictionary.readline().split()
                dct[character[1]] = character[0]
        return dct

    def decode(self, number, dct):
        if len(number) < 4:
            return ""
        nickname = ""
        for i in range(0, len(number), 2):
            if number[i:i + 2] in dct:
                nickname += dct[number[i:i + 2]]
            else:
                nickname += '#'
        nickname_without_clantag = self.remove_clantag(nickname)
        return nickname_without_clantag

    def remove_clantag(self, nickname):
        if not ('[' in nickname):
            return nickname
        if nickname.index('[') == 0:
            return nickname[nickname.index(']') + 1:]
        else:
            return nickname[0:nickname.index('[')]
