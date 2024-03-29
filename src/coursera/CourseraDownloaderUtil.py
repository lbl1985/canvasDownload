from difflib import SequenceMatcher

class CourseraDownloaderUtil:
    @staticmethod
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()
    
    @staticmethod
    def find_header(ul_text, headers):
        arr = []
        ul_text = ul_text.split('\n')[0]
        for header in headers:
            ratio = CourseraDownloaderUtil.similar(ul_text, header)
            arr.append(ratio)
        max_index = arr.index(max(arr))
        return headers[max_index]
