from difflib import SequenceMatcher
import re, os
import urllib.request

class CourseraDownloaderUtil:

    def __init__(self):
        self.skip_list = [
            "Getting and Giving Help",
            "Many of the"
        ]

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
    
    @staticmethod
    def get_md_path(path:str, spaces = 2):
        return '/'.join(['.'] + path.split('/')[(1+spaces):])
    
    @staticmethod
    def get_clean_name(name: str):
        s = re.sub(r'[^\w\s-]', '', name).strip()
        return re.sub(r"(?<=\b)\w", lambda match: match.group(0).upper(), s).replace(' ', '_')
    
    def process_reading_elements(self, element, saving_path:str=".", path_level:int=2, is_test:bool=False):
        if element.text in self.skip_list:
            return ''        
        elif element.tag_name in ['h1', 'h2', 'h3']:
            return f"**{element.text}**\n"
        elif element.tag_name == 'p':
            if '.pdf' in element.text:
                return self.process_pdf(element, saving_path, path_level, is_test)
            return f"{element.text}\n"
    
    # Example saving_path = "./Downloads/Course/week1/"
    def process_pdf(self, element, saving_path:str=".", path_level:int = 2, is_test:bool=False):
        text = [file for file in element.text.split('\n') if '.pdf' in file][0]
        
        url = element.get_attribute('href')

        object_name = self.get_clean_name(text[:-4]) + text[:-4]
        object_path = os.path.join(saving_path, object_name)

        if not is_test:
            urllib.request.urlretrieve(url, object_path)
        print(f"Downloaded {object_name}")

        object_path_md = self.get_md_path(object_path, path_level)

        return f"[{object_name}]({object_path_md})\n"

    @staticmethod
    def download_file(url:str, file_name:str, saving_path:str, path_level:int=2):

        urllib.request.urlretrieve(url, file_name)
        return file_name