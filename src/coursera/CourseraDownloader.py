from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time
import pyperclip



# WEB_PAGE = "https://www.coursera.org/learn/marketing-digital/home/week/2"
WEB_PAGE = "https://www.coursera.org/learn/business-statistics/home/"

class Utility:
    def get_video_name(self, name:str):
        return name.split('\n')[0]

class CourseraDownloader:
    def __init__(self):
        self.opt = Options()
        self.utility = Utility()
        self.video_name = ""

    def open_page(self, webpage: str):
        # driver_path = "~/Downloads/edgedriver_mac64_m1/msedgedriver"  # Replace with the actual path to your Microsoft Edge WebDriver executable
        # service = Service(driver_path)
        # driver = webdriver.Edge(service=service, options=self.opt)
        self.driver = webdriver.Edge(options = self.opt)
        self.driver.get(webpage)
        self.action = ActionChains(self.driver)

    def get_content_in_week(self):
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        return [ul for ul in uls if ('Duration' in ul.text)]

    def get_video_in_content(self, index_content: int):
        contents = self.get_content_in_week()
        ul = contents[index_content]
        lis = ul.find_elements(By.TAG_NAME, "li")
        return [li for li in lis if ('Video' in li.text)]

    def process(self): 
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        weeks = [ul for ul in uls if ('Course Material' in ul.text)]
        contents = self.get_content_in_week()
        for index_content in range(len(contents)):
            videos = self.get_video_in_content(index_content)
            for index_video in range(len(videos)):
                videos = self.get_video_in_content(index_content)
                video = videos[index_video]
                self.video_name = self.utility.get_video_name(video.text)
                video.click()
                time.sleep(3)

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

                self.driver.back()
                time.sleep(0.2)
                index_video = index_video + 1
            index_content = index_content + 1

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
        for index in range(len(download_items)):
            download_items = self.get_download_items()
            download_item = download_items[index]
            if 'mp4' in download_item.text:
                self.video_name = self.video_name + '_' + download_item.text.replace(" mp4", "")
                pyperclip.copy(self.video_name)
                self.download(download_item) # download the video operations
            index = index + 1
        return;

    def download(self, obj):
        obj.click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        video = self.driver.find_element(By.TAG_NAME, "video")
        _ = input("Please press enter once finish downloading the video")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(0.2)
        # self.action.context_click(video).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
        return;




if __name__ == "__main__":
    downloader = CourseraDownloader()
    downloader.open_page(WEB_PAGE)
    _ = input("Please press enter once you have finished sign in")

    courser_page = ""
    downloader.process()
    _ = input("Another pause ")


    