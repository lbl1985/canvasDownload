from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time, os, sys
import urllib.request
import CourseraDownloaderUtil



# WEB_PAGE = "https://www.coursera.org/learn/marketing-digital/home/week/2"
WEB_PAGE = "https://www.coursera.org/learn/business-statistics/home/week/1"
# WEB_PAGE = "file://" + os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..', 'test', 'data', 'courseraWeekPage.html'))

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

    def open_page(self, webpage: str):
        # driver_path = "~/Downloads/edgedriver_mac64_m1/msedgedriver"  # Replace with the actual path to your Microsoft Edge WebDriver executable
        # service = Service(driver_path)
        # driver = webdriver.Edge(service=service, options=self.opt)
        self.driver = webdriver.Edge(options = self.opt)
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
        self.index_file_name = os.path.join(self.default_saving_path, self.get_course_name() + ".md")
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
            content = viewer[0].text
            if len(content) > 0:
                with open(self.index_file_name, "a") as f:
                    f.write(f"{content}\n")

    def process_li_video(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        download_buttons =[button for button in buttons if button.text == "Downloads"]

        while len(download_buttons) == 0:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            download_buttons =[button for button in buttons if button.text == "Downloads"]
            time.sleep(2)

        download_button = download_buttons[0]
        download_button.click()
        time.sleep(0.2)

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
            with open(self.index_file_name, "a") as f:
                f.write(f"#### {li_text}\n")

            li.click()
            time.sleep(0.5)

            if process_type == PROCESS_READ:
                self.process_li_read()
            else:
                self.process_li_video()

            self.driver.back()
            time.sleep(0.5)
    
    def process_week(self, week_index: int):
        weeks_li = self.get_weeks_li()
        week = weeks_li[week_index]
        week_text = week.text
        self.week_saving_path = os.path.join(self.default_saving_path, week_text)
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
                    f.write(f"## {header}\n")
                    f.write(f"### {ul_text}\n")
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
        self.set_buttons_text()

        weeks_li = self.get_weeks_li()
        
        index_week = 0
        while index_week < len(weeks_li):
            self.process_week(index_week)
            index_week = index_week + 1

        # uls = self.driver.find_elements(By.TAG_NAME, "ul")
        # weeks = [ul for ul in uls if ('Course Material' in ul.text)]
        # contents = self.get_content_in_week()
        # for index_content in range(len(contents)):
        #     videos = self.get_video_in_content(index_content)
        #     for index_video in range(len(videos)):
        #         videos = self.get_video_in_content(index_content)
        #         video = videos[index_video]
        #         self.video_name = self.utility.get_video_name(video.text)
        #         video.click()
        #         time.sleep(3)

        #         buttons = self.driver.find_elements(By.TAG_NAME, "button")
        #         download_buttons =[button for button in buttons if button.text == "Downloads"]

        #         while len(download_buttons) == 0:
        #             buttons = self.driver.find_elements(By.TAG_NAME, "button")
        #             download_buttons =[button for button in buttons if button.text == "Downloads"]
        #             time.sleep(2)

        #         download_button = download_buttons[0]
        #         download_button.click()
        #         time.sleep(0.2)

        #         self.process_download()

        #         self.driver.back()
        #         time.sleep(2)
        #         index_video = index_video + 1
        #     index_content = index_content + 1

        return;

    def get_download_items(self):
        tags = self.driver.find_elements(By.TAG_NAME, "ul")
        download_list = [tag for tag in tags if ('Video' in tag.text)] # find the download button
        download_ul = download_list[-1]
        download_ul.click()
        time.sleep(0.2)
        return download_ul.find_elements(By.TAG_NAME, "li")

    def process_download(self):
        download_items = self.get_download_items()
        index = self.util.find_higher_resolution([item.text for item in download_items])
        current_saving_paths = ''
        while index < len(download_items):
            download_items = self.get_download_items()
            download_item = download_items[index]
            a = download_item.find_element(By.TAG_NAME, "a")
            object_name = a.get_attribute("download")
            
            if 'mp4' in object_name:
                current_saving_paths = os.path.join(self.week_saving_path, object_name[:-4])
                self.util.check_folder(current_saving_paths)
            
            object_path = os.path.join(current_saving_paths, object_name)
            video_url = a.get_attribute("href")
            urllib.request.urlretrieve(video_url, object_path)
            print(f"Downloaded {object_name}")
            with open(self.index_file_name, "a") as f:
                    f.write(f"[{object_name}]({object_path})\n")
            
            index = index + 1
        return;


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _ = input(f"Please provide the webpage. Otherwise, we will use the default webpage: {WEB_PAGE}\n Press enter to confirm to use the default.")
        if len(_) > 0:
            WEB_PAGE = _
    else:
        WEB_PAGE = sys.argv[1]
        
    downloader = CourseraDownloader()
    while len(WEB_PAGE) > 0:
        downloader.open_page(WEB_PAGE)
        _ = input("Please press enter once you have finished sign in")
        downloader.process()
        print(f"{WEB_PAGE} is done")
        WEB_PAGE = ""
        
        WEB_PAGE = input("If you want to go with another class. Please input for another page.")