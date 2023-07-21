import requests
from DataRecognizer import ScannedPlayer
from classes import PlayerStats


class RequestHandler:
    @staticmethod
    def get_token():
        with open("configs/token") as token_file:
            token = token_file.readline()
        return token

    @staticmethod
    def get_all_players_stats(players):
        allies = []
        for player in players['allies']:
            allies.append(RequestHandler.get_player_stats(player))
        enemies = []
        for player in players['enemies']:
            enemies.append(RequestHandler.get_player_stats(player))
        return {'allies': allies, 'enemies': enemies}

    @staticmethod
    def get_player_stats(player: ScannedPlayer):
        token = RequestHandler.get_token()
        url = f'https://api.wotblitz.ru/wotb/account/list/?application_id={token}&search={player.nickname}&type=exact'
        response = requests.get(url).json()
        if response['status'] == 'error':
            print('not found')
            return PlayerStats("Not found", 0, 0, 0)
        player_id = response['data'][0]['account_id']
        url = f'https://api.wotblitz.ru/wotb/account/info/?application_id={token}&account_id={player_id}' \
              f'&fields=statistics.all.wins%2C+statistics.all.battles'
        response = requests.get(url).json()
        number_of_battles = response['data'][str(player_id)]['statistics']['all']['battles']
        number_of_wins = response['data'][str(player_id)]['statistics']['all']['wins']
        if number_of_battles != 0:
            common_winrate = number_of_wins / number_of_battles * 100
        else:
            common_winrate = 0

        url = f'https://api.wotblitz.ru/wotb/account/tankstats/?application_id={token}&account_id={player_id}&' \
              f'tank_id={player.tank_id}&fields=all.wins%2C+all.battles%2C+all.damage_dealt'
        response = requests.get(url).json()
        if response['data'][str(player_id)]:
            tank_number_of_battles = response['data'][str(player_id)]['all']['battles']
            tank_number_of_wins = response['data'][str(player_id)]['all']['wins']
            if tank_number_of_battles != 0:
                tank_winrate = tank_number_of_wins / tank_number_of_battles * 100
                tank_damage = int(response['data'][str(player_id)]['all']['damage_dealt'] / tank_number_of_battles)
            else:
                tank_winrate = 0
                tank_damage = 0
        else:
            tank_winrate = 0
            tank_damage = 0
        player_stats = PlayerStats(player.nickname, common_winrate, tank_winrate, tank_damage)
        return player_stats
