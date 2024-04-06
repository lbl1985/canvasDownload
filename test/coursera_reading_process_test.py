import sys, os, unittest
repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'coursera')
sys.path.append(repo_root)
from CourseraDownloaderUtil import CourseraDownloaderUtil

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

import difflib

class UtilTest(unittest.TestCase):
    def setUp(self):
        self.util = CourseraDownloaderUtil()
        
        self.opt = Options()
        self.driver = webdriver.Edge(options=self.opt)

        self.test_data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'data')
        self.overview_file_gt = os.path.join(self.test_data_folder, 'overview_win.md') if os.name == 'nt' else os.path.join(self.test_data_folder, 'overview.md')
        self.reading_file_gt = os.path.join(self.test_data_folder, 'reading_win.md') if os.name == 'nt' else os.path.join(self.test_data_folder, 'reading.md')

        self.temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'temp')
        CourseraDownloaderUtil.check_folder(self.temp_folder)
        self.overview_file = os.path.join(self.temp_folder, 'overview.md')
        if os.path.exists(self.overview_file):
            os.remove(self.overview_file)
        self.reading_file = os.path.join(self.temp_folder, 'reading.md')
        if os.path.exists(self.reading_file):
            os.remove(self.reading_file)

        self.maxDiff = None

    def tearDown(self):
        """tear down the test"""
        pass
    
    def test_process_overview(self):
        webpage = "file://" + os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'data', 'coursera_li_reading.html'))

        self.driver.get(webpage)
        viewers = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1kgqbsw")
        if len(viewers) == 1:
            viewer = viewers[0]
            elements = viewer.find_elements(By.XPATH, "./*")
            for element in elements:
                with open(self.overview_file, 'a') as f:
                    f.write(self.util.process_reading_elements(element, "./Downloads/Course/week1/", is_test=True))
        with open(self.overview_file_gt, 'r') as file1, open(self.overview_file, 'r') as file2:
            contents_gt = file1.read()
            contents = file2.read()

            self.assertEqual(contents_gt, contents)

    def test_process_reading(self):
        webpage = "file://" + os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'data', 'coursera_li_modual_reading.html'))

        self.driver.get(webpage)
        viewers = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1kgqbsw")
        if len(viewers) == 1:
            viewer = viewers[0]
            elements = viewer.find_elements(By.XPATH, "./*")
            for element in elements:
                with open(self.reading_file, 'a') as f:
                    f.write(self.util.process_reading_elements(element, "./Downloads/Course/week1/", is_test=True))
        with open(self.reading_file_gt, 'r') as file1, open(self.reading_file, 'r') as file2:
            contents_gt = file1.read()
            contents = file2.read()
            self.assertEqual(contents_gt, contents)

if __name__ == '__main__':
    unittest.main()