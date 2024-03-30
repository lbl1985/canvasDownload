from difflib import SequenceMatcher
import re, os

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
    
    @staticmethod
    # downloads is list of string from download selenium elements' text format
    # we should return the index for the mode specified index
    def find_higher_resolution(downloads, mode = "highest"):
        resolution_search = re.compile(r'(\d+)p(?=.*mp4)')
        # downloads_text = [download.text for download in downloads]
        default_value = 0 if mode == "highest" else 100000
        arr = []
        for download in downloads:
            match = resolution_search.search(download)
            if match:
                resolution = int(match.group(1))
                arr.append(resolution)
            else:
                arr.append(default_value)

        if mode == "highest":
            return arr.index(max(arr))
        elif mode == "lowest":
            return arr.index(min(arr))
        
    @staticmethod
    def check_folder(folder: str):
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder