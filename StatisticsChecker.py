import cv2 as cv
from ScreenCutter import ScreenCutter
from DataRecognizer import DataRecognizer
from RequestHandler import RequestHandler

class StatisticsChecker:
    @staticmethod
    def get_players_statistics(config: str, image_filename: str):
        screenshot = cv.imread(image_filename)
        cutter = ScreenCutter(config)
        players_images = cutter.get_players_images(screenshot)
        scanned_data = DataRecognizer.get_scanned_data(players_images)
        players_stats = RequestHandler.get_all_players_stats(scanned_data)
        return players_stats