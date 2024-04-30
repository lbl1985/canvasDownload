from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time, os, sys, json, math
import urllib.request
import CourseraDownloaderUtil



WEB_PAGE = "https://www.coursera.org/learn/country-level-economics/home/week/1"

PROCESS_READ = "Reading"
PROCESS_VIDEO = "Video"

class Utility:
    def get_video_name(self, name:str):
        return name.split('\n')[0]

class CourseraDownloader:
    def __init__(self):
        self.opt = Options()
        self.utility = Utility()
        self.video_name = ""
        # object saving path would be 
        # default_saving_path/courser_saving_path/week_saving_path/video_name
        self.default_saving_path = "./Downloads/"
        self.course_saving_path = ""
        self.week_saving_path = ""
        self.video_list = []
        self.index_file_name = ""
        self.webpage = ""
        self.buttons_text = []
        self.util = CourseraDownloaderUtil.CourseraDownloaderUtil()
        if os.path.exists(self.default_saving_path) == False:
            os.mkdir(self.default_saving_path)
        self.driver = webdriver.Edge(options = self.opt)

    def open_page(self, webpage: str):
        
        self.webpage = webpage
        self.driver.get(self.webpage)
        self.action = ActionChains(self.driver)


    def get_course_name(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, "h2.css-6ecy9b")
        if len(items) == 1:
            return items[0].text
        else:
            items = self.webpage.split("/")
            index = items.index("learn")
            return items[index + 1]

    def get_week_number(self):
        items = self.webpage.split("/")
        return items[-1]

    def initial_index_file(self):
        course_name = self.get_course_name()
        course_name = self.util.get_clean_name(course_name)
        self.course_saving_path = os.path.join(self.default_saving_path, course_name)
        self.util.check_folder(self.course_saving_path)
        self.index_file_name = os.path.join(self.course_saving_path, course_name + ".md")

        with open(self.index_file_name, "a") as f:
            course_name = self.get_course_name()
            week_number = self.get_week_number()
            f.write(f"# {course_name} Week {week_number}\n")


    def get_content_in_week(self):
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        return [ul for ul in uls if ('Duration' in ul.text)]

    def get_video_in_content(self, index_content: int):
        contents = self.get_content_in_week()
        ul = contents[index_content]
        lis = ul.find_elements(By.TAG_NAME, "li")
        return [li for li in lis if ('Video' in li.text)]

    def get_reading_and_video_content_in_week(self):
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        uls = [ul for ul in uls if (PROCESS_VIDEO in ul.text or PROCESS_READ in ul.text)]
        # Skip the uls not related to class. 
        index = 0
        # uls_text = [ul.text for ul in uls]
        # while index < len(uls_text):
        #     if uls_text[index].startswith('Module'):
        #         break
        #     index += 1
        return uls[index:]

    def set_buttons_text(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        self.buttons_text =  [button.text.split('\n')[0] for button in buttons if len(button.text) > 0 and not ('Grade' in button.text)]

    def get_lis(self, ul):
        lis = ul.find_elements(By.TAG_NAME, "li")
        return [li for li in lis if ('Video' in li.text or 'Reading' in li.text)]
    
    def process_li_read(self):
        viewer = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1kgqbsw")
        if len(viewer) == 1:
            viewer = viewer[0]
            elements = viewer.find_elements(By.XPATH, "./*")
            for element in elements:
                with open(self.index_file_name, 'a', encoding='utf-8', errors='ignore') as f:
                    text = self.util.process_reading_elements(element, self.week_saving_path)
                    if text is not None:
                        f.write(text)

    def process_li_video(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        download_buttons =[button for button in buttons if button.text == "Downloads"]

        locks = self.driver.find_elements(By.CSS_SELECTOR, "div.rc-ItemLockedCover")
        if len(locks) > 0:
            print("The video is locked")
            return
        
        counter = 0
        while len(download_buttons) == 0 and counter < 5:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            download_buttons =[button for button in buttons if button.text == "Downloads"]
            time.sleep(2)
            counter = counter + 1

        if len(download_buttons) == 0:
            print("No download button found")
            return
        
        download_button = download_buttons[0]
        download_button.click()
        time.sleep(3)

        self.process_download()

    def process_ul(self, ul_index: int):
        uls = self.get_reading_and_video_content_in_week()
        ul = uls[ul_index]
        lis = ul.find_elements(By.TAG_NAME, "li")
        index = 0
       
        for index in range(len(lis)):
            uls = self.get_reading_and_video_content_in_week()
            ul = uls[ul_index]

            lis = ul.find_elements(By.TAG_NAME, "li")
            li = lis[index]

            process_type = ""
            if PROCESS_READ in li.text:
                process_type = PROCESS_READ
            elif PROCESS_VIDEO in li.text:
                process_type = PROCESS_VIDEO
            
            if len(process_type) == 0:
                continue

            li_text = li.text.split('\n')[0]
            # if 'Honor' in li_text: # skip the honor related contents
            #     continue

            with open(self.index_file_name, "a") as f:
                f.write(f"### {li_text}\n")

            li.click()
            time.sleep(0.5)

            honor = self.driver.find_elements(By.CSS_SELECTOR, "div.honors-modal-content")
            if len(honor) > 0:
                buttons = honor[0].find_elements(By.CSS_SELECTOR, "button")
                continue_button = [button for button in buttons if button.text == "Continue"]
                if len(continue_button) == 1:
                    continue_button[0].click()
                    time.sleep(0.5)

            if process_type == PROCESS_READ:
                self.process_li_read()
            else:
                self.process_li_video()

            self.driver.back()
            time.sleep(0.5)
    
    def process_week(self, week_index: int):
        self.set_buttons_text()

        weeks_li = self.get_weeks_li()
        week = weeks_li[week_index]
        week_text = week.text
        self.week_saving_path = os.path.join(self.course_saving_path, self.util.get_clean_name(week_text))
        self.util.check_folder(self.week_saving_path)
        week.click()
        time.sleep(3)

        uls = self.get_reading_and_video_content_in_week()
        current_header = ""
        index = 0
        while index < len(uls):
            uls = self.get_reading_and_video_content_in_week()
            ul = uls[index]
            ul_text = ul.text.split('\n')[0]
            header = self.util.find_header(ul_text, self.buttons_text) 
            if header != current_header:
                with open(self.index_file_name, "a") as f:
                    f.write(f"## {ul_text}\n")
            current_header = header
            self.process_ul(index)
            index = index + 1
    
    def get_weeks_li(self):
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        week_ul = [ul for ul in uls if ('Course Material' in ul.text)][0]
        weeks_li = week_ul.find_elements(By.TAG_NAME, "li")
        weeks_li = [li for li in weeks_li if 'Week' in li.text and not ("\n" in li.text)]
        return weeks_li

    def process(self): 
        # Initial the index .md file
        self.initial_index_file()

        weeks_li = self.get_weeks_li()
        
        index_week = 0
        while index_week < len(weeks_li):
            self.process_week(index_week)
            index_week = index_week + 1

        return;

    def get_download_items(self):
        tags = self.driver.find_elements(By.TAG_NAME, "ul")
        download_list = [tag for tag in tags if ('Video' in tag.text)] # find the download button
        download_ul = download_list[-1]
        return download_ul.find_elements(By.TAG_NAME, "li")

    def process_download(self):
        download_items = self.get_download_items()
        index = self.util.find_higher_resolution([item.text for item in download_items])
        current_saving_paths = ''
        truncate = 0
        while index < len(download_items):
            download_items = self.get_download_items()
            download_item = download_items[index]
            a = download_item.find_element(By.TAG_NAME, "a")
            object_name = a.get_attribute("download")
            if len(object_name) == 0: # skip empty download link
                index = index + 1
                continue
            file_name, ext = os.path.splitext(object_name)
            
            if len(ext) == 0 and object_name.endswith('Slides'):
                ext = '.pdf'

            clean_name = self.util.get_clean_name(file_name)
            if truncate != 0:
                # clean the previous folder first
                previous_clean_name = clean_name[:math.floor(len(clean_name) / pow(2, truncate - 1))]
                if os.path.exists(os.path.join(self.week_saving_path, previous_clean_name)):
                    os.rmdir(os.path.join(self.week_saving_path, previous_clean_name))
                # setup new clean name
                truncate_len = math.floor(len(clean_name) / pow(2, truncate))
                clean_name = clean_name[:truncate_len]
            
            object_name = clean_name + ext
            
            if 'mp4' in object_name:
                folder_name, _ = os.path.splitext(object_name)
                current_saving_paths = os.path.join(self.week_saving_path, folder_name)
                self.util.check_folder(current_saving_paths)
            
            object_path = os.path.join(current_saving_paths, object_name)
            video_url = a.get_attribute("href")
            print(f'Downloading {object_name}')
            try:
                urllib.request.urlretrieve(video_url, object_path)
            except Exception as e:
                print(f"Error in downloading {object_name}, {video_url}, {object_path}")
                print(e)
                if 'No such file or directory' in str(e):
                    truncate = truncate + 1
                    print(f"object name too long, set up truncate to {truncate} ")

                continue

            if truncate != 0:
                truncate = 0 # reset the truncate once download successfully
            
            print(f"Downloaded {object_name}")
            with open(self.index_file_name, "a") as f:
                    file_name, _ = os.path.splitext(object_name)
                    object_path_md = self.util.get_md_path(object_path)
                    f.write(f"\n[{file_name}]({object_path_md})\n")
            
            index = index + 1
        return;


if __name__ == "__main__":
    downloader = CourseraDownloader()
    init = True
    if len(sys.argv) == 1:
        _ = input(f"Please provide the webpage. Otherwise, we will use the default webpage: {WEB_PAGE}\n Press enter to confirm to use the default.")
        if len(_) > 0:
            WEB_PAGE = _
    elif len(sys.argv) == 2:
        if downloader.util.is_url(sys.argv[1]):
            WEB_PAGE = sys.argv[1]
        else:
            if os.path.exists(sys.argv[1]) and os.path.splitext(sys.argv[1])[1] == '.json':
                web_pages = json.load(open(sys.argv[1]))
                for page in web_pages:
                    WEB_PAGE = page
                    if (WEB_PAGE == web_pages[-1]): # last course break to get into regular cycle
                        break
                    print(f"Processing {WEB_PAGE}")
                    downloader.open_page(WEB_PAGE)
                    time.sleep(5)
                    if init:
                        _ = input("Please press enter once you have finished sign in")
                        init = False
                    downloader.process()
                    print(f"{WEB_PAGE} is done")

    while len(WEB_PAGE) > 0:
        print(f"Processing {WEB_PAGE}")
        downloader.open_page(WEB_PAGE)
        time.sleep(3)
        if init:
            _ = input("Please press enter once you have finished sign in")
            init = False
        downloader.process()
        print(f"{WEB_PAGE} is done")
        WEB_PAGE = ""
        
        WEB_PAGE = input("If you want to go with another class. Please input for another page.")


'''
Knowledge for zsh
# find all the files with Slides in the name
find . -type f -iname "*Slides" 
# find all the files with Slides in the name and rename them to pdf
find . -type f -name "*Slides" -exec sh -c 'mv "$0" "${0}.pdf"' {} \; 
# find all the files with xlsx in the name
find . -type f -iname "*xlsx"
# find all the files with xlsx in the name and rename them to .xlsx
find . -type f -name "*xlsx" -exec sh -c 'mv "$0" "${0%xlsx}.xlsx"' {} \;
'''