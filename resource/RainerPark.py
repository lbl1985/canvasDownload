from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time, os, sys, json, math
import datetime
import urllib.request
from pync import Notifier



WEB_PAGE = "https://www.recreation.gov/timed-entry/10101917/ticket/10101919"

PROCESS_READ = "Reading"
PROCESS_VIDEO = "Video"

class NationalParkChecker:
    def __init__(self):
        self.opt = Options()
        self.video_name = ""
        # object saving path would be 
        # default_saving_path/courser_saving_path/week_saving_path/video_name
        self.week_saving_path = ""
        self.video_list = []
        self.index_file_name = ""
        self.webpage = ""
        self.buttons_text = []
        self.driver = webdriver.Edge(options = self.opt)
        self.dates = []

    def open_page(self, webpage: str):
        self.webpage = webpage
        self.driver.get(self.webpage)
        self.action = ActionChains(self.driver)

    def check_dates_available(self, dates):
        # check if the page is available
        # if the page is not available, then we should return False
        # otherwise, we should return True
        self.dates = dates
        for date in self.dates:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
            print(f"Checking {date}")
            date_picker = self.driver.find_elements(By.CSS_SELECTOR, "div.date-segment")[0]
            date_picker.click()
            self.action.send_keys(date_obj.strftime("%m")).perform()
            # self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(date_obj.strftime("%d")).perform()
            # self.action.send_keys(Keys.TAB).perform()
            self.action.send_keys(date_obj.strftime("%Y")).perform()
            self.action.send_keys(Keys.RETURN).perform()
            time.sleep(1)
            self.check_entry_window(date)

    def check_entry_window(self, date):
        times = self.driver.find_elements(By.CSS_SELECTOR, "div.sarsa-inline.xs.y-center.left")[0].find_element(By.TAG_NAME, "div").find_elements(By.XPATH, "./*")
        for time in times:
            time_class = time.get_attribute("class")
            print(f"{time.text} is {time_class}")
            if not (time_class == "disabled"):
                notification_str = f"Available time slot: {date} for {time.text}"
                Notifier.notify(notification_str, open=self.webpage)
                print(notification_str)

if __name__ == "__main__":
    park = NationalParkChecker()
    park.open_page(WEB_PAGE)
    park.check_dates_available(["2024-09-01", "2024-09-02"])
    while True:
        time.sleep(60)
        park.check_dates_available(["2024-09-01", "2024-09-02"])
    print("Done!")