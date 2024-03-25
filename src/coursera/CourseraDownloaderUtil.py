from difflib import SequenceMatcher

class CourseraDownloaderUtil:
    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()