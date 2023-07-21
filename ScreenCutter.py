import cv2 as cv
from classes import Point, Rect


class ScreenCutter:
    def __init__(self, configuration_path: str):
        self.players_locations = []
        with open(configuration_path) as config:
            for i in range(14):
                player_location = list(map(int, config.readline().split()))
                player_nickname = Rect(Point(player_location[0], player_location[1]),
                                       Point(player_location[2], player_location[3]))
                player_tank_id = Rect(Point(player_location[4], player_location[5]),
                                      Point(player_location[6], player_location[7]))
                self.players_locations.append({'nick': player_nickname, 'tank_id': player_tank_id})

    def get_players_images(self, image):
        allies_team = []
        for i in range(7):
            allies_team.append({'nick': self.get_image_by_coordinates(image, self.players_locations[i]['nick']),
                                'tank_id': self.get_image_by_coordinates(image, self.players_locations[i]['tank_id'])})

        enemies_team = []
        for i in range(7, 14):
            enemies_team.append({'nick': self.get_image_by_coordinates(image, self.players_locations[i]['nick']),
                                 'tank_id': self.get_image_by_coordinates(image, self.players_locations[i]['tank_id'])})
        for i in range(7):
            for j in range(len(enemies_team[i]['tank_id'])):
                enemies_team[i]['tank_id'][j] = enemies_team[i]['tank_id'][j][::-1]
        return {'allies': allies_team, 'enemies': enemies_team}

    def get_image_by_coordinates(self, image, position: Rect):
        cropped_image = image[position.pt1.y:position.pt2.y, position.pt1.x:position.pt2.x]
        return cropped_image
