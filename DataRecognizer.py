import cv2 as cv
from pytesseract import image_to_string
from decoding_dictionary import decoding_dictionary


class ScannedPlayer:
    def __init__(self, nickname: str, tank_id: int):
        self.nickname = nickname
        self.tank_id = tank_id
    def __str__(self):
        return f'{self.nickname} {self.tank_id}'
    def __repr__(self):
        return f'{self.nickname} {self.tank_id}'

class DataRecognizer:

    @staticmethod
    def return_scanned_data(players):
        scanned_allies = []
        scanned_enemies = []
        for player in players['allies']:
            scanned_nickname = DataRecognizer.scan_nickname(player['nick'])
            scanned_tank_id = DataRecognizer.scan_tank_id(player['tank_id'])
            scanned_player = ScannedPlayer(scanned_nickname, scanned_tank_id)
            scanned_allies.append(scanned_player)
        for player in players['enemies']:
            scanned_nickname = DataRecognizer.scan_nickname(player['nick'])
            scanned_tank_id = DataRecognizer.scan_tank_id(player['tank_id'])
            scanned_player = ScannedPlayer(scanned_nickname, scanned_tank_id)
            scanned_enemies.append(scanned_player)
        return {'allies': scanned_allies, 'enemies': scanned_enemies}


    @staticmethod
    def scan_nickname(nick_image):
        nick_image_gray = cv.cvtColor(nick_image, cv.COLOR_BGR2GRAY)
        nick_image_gray_resized = cv.resize(nick_image_gray, None, fx=2.3, fy=2.2, interpolation=cv.INTER_LINEAR)
        nick_image_binary = cv.threshold(nick_image_gray_resized, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        nickname_string = image_to_string(nick_image_binary, config="-c tessedit_char_whitelist=0123456789")[0:-1]

        #print(nickname_string)
        #cv.imshow('1', cv.resize(nick_image_binary, None, fx=0.33, fy=0.33, interpolation=cv.INTER_LINEAR))
        #cv.waitKey()

        nickname_decoded = DataRecognizer.decode(nickname_string)
        return nickname_decoded

    @staticmethod
    def scan_tank_id(image):
        tank_id_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        tank_id_gray_resized = cv.resize(tank_id_gray, None, fx=1.8, fy=1.8, interpolation=cv.INTER_LINEAR)
        tank_id_binary = cv.threshold(tank_id_gray_resized, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        tank_id_string = image_to_string(tank_id_binary, config="-c tessedit_char_whitelist=0123456789")[0:-1]

        #print(tank_id_string)
        #cv.imshow('1', tank_id_binary)
        #cv.waitKey()

        return tank_id_string

    @staticmethod
    def decode(nickname_string: str):
        if len(nickname_string) < 4 or len(nickname_string) % 2 != 0:
            return ""
        nickname_decoded = ""
        for i in range(0, len(nickname_string), 2):
            if nickname_string[i:i + 2] in decoding_dictionary:
                nickname_decoded += decoding_dictionary[nickname_string[i:i + 2]]
            else:
                nickname_decoded += '#'
        nickname_decoded_without_clantag = DataRecognizer.remove_clantag(nickname_decoded)
        return nickname_decoded_without_clantag

    @staticmethod
    def remove_clantag(nickname: str):
        if not ('[' in nickname):
            return nickname
        if nickname.index('[') == 0:
            return nickname[nickname.index(']') + 1:]
        else:
            return nickname[0:nickname.index('[')]
