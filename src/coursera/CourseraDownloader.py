from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


WEB_PAGE = "https://www.coursera.org/learn/marketing-digital/home/week/1"

class CourseraDownloader:
    def __init__(self):
        self.opt = Options()
        

    def open_page(self, webpage: str):
        # driver_path = "~/Downloads/edgedriver_mac64_m1/msedgedriver"  # Replace with the actual path to your Microsoft Edge WebDriver executable
        # service = Service(driver_path)
        # driver = webdriver.Edge(service=service, options=self.opt)
        self.driver = webdriver.Edge(options = self.opt)
        self.driver.get(webpage)
        self.action = ActionChains(self.driver)

    def process(self): 
        uls = self.driver.find_elements(By.TAG_NAME, "ul")
        weeks = [ul for ul in uls if ('Course Material' in ul.text)]
        contents = [ul for ul in uls if ('Duration' in ul.text)]
        for index_content in range(len(contents)):
            ul = contents[index_content]
            lis = ul.find_elements(By.TAG_NAME, "li")
            videos = [li for li in lis if ('Video' in li.text)]
            for index_video in range(len(videos)):
                video = videos[index_video]
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

                tags = self.driver.find_elements(By.TAG_NAME, "ul")
                download_list = [tag for tag in tags if ('Video' in tag.text)] # find the download button
                self.process_download(download_list[-1])

                self.driver.back()
                break

        return;

    def process_download(self, download_list):
        download_list.click()
        download_items = download_list.find_elements(By.TAG_NAME, "li")
        for index in range(len(download_items)):
            download_item = download_items[index]
            self.download(download_item) # download the video operations
            break
        return;

    def download(self, obj):
        obj.click()
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        video = self.driver.find_element(By.TAG_NAME, "video")
        self.action.context_click(video).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
        return;




if __name__ == "__main__":
    downloader = CourseraDownloader()
    downloader.open_page(WEB_PAGE)
    _ = input("Please press enter once you have finished sign in")

    courser_page = ""
    downloader.process()
    _ = input("Another pause ")


    