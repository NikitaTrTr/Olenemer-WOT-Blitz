import cv2 as cv

def get_nicknames_images(filename, configuration):
    img = load_image(filename)
    players_coordinates = get_coordinates(configuration)
    green_team = [img[x[1]:x[3], x[0]:x[2]] for x in players_coordinates[0:7]]
    red_team = [img[x[1]:x[3], x[0]:x[2]] for x in players_coordinates[7:14]]
    return green_team, red_team


def load_image(filename):
    img = cv.imread(filename)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray


def get_coordinates(configuration):
    with open(configuration, 'r') as coordinates_file:
        coordinates = map(lambda x: x.split(), coordinates_file.read().split(sep='\n'))
        players = [tuple(map(int, x)) for x in coordinates]
    return players
