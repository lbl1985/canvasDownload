import sys, os, unittest
repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'coursera')
sys.path.append(repo_root)
from CourseraDownloaderUtil import CourseraDownloaderUtil

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class UtilTest(unittest.TestCase):
    def setUp(self):
        self.util = CourseraDownloaderUtil()
        self.buttons_text = [
            'Open Coursera membership menu',
            'Search',
            'English',
            'B\nBinlong Li',
            'Course Material',
            'Get started',
            'Course Orientation\nComplete',
            'About the Course\nComplete',
            'Get started',
            'About Excel\nComplete',
            'About Your Classmates\nComplete',
            'Module 1: Hypothesis Testing\nComplete',
            'Show more',
            'Module 1 Information\nComplete',
            'Lesson 1-1: Formulating the Hypothesis\nComplete',
            'Lesson 1-2: Analyzing the Result\nComplete',
            'Lesson 1-3: Two-Tail Test for Mean\nComplete',
            'Lesson 1-4: One-Tail Test for Mean\nComplete',
            'Lesson 1-5: Testing the Proportion\nComplete',
            'Module 1 Graded Activities\nComplete'
        ]
        self.uls_text = [
            'Welcome to Inferential and Predictive Statistics for Business!\nVideo•\n. Duration: 5 minutes\n5 min\nGet started\n. Click to get started\nSyllabus\nReading•\n. Duration: 10 minutes\n10 min\nePub\nReading•\n. Duration: 10 minutes\n10 min\nAbout the Discussion Forums\nReading•\n. Duration: 4 minutes\n4 min\nGlossary\nReading•\n. Duration: 15 minutes\n15 min\nOrientation Quiz\nPractice Quiz•5 questions',
            'Using Excel for this Course\nReading•\n. Duration: 10 minutes\n10 min\nExcel Data Analysis Toolpak\nVideo•\n. Duration: 1 minute\n1 min',
            'Updating Your Profile\nReading•\n. Duration: 10 minutes\n10 min\nGetting to Know Your Classmates\nDiscussion Prompt•\n. Duration: 10 minutes\n10 min',
            'Module 1 Overview\nReading•\n. Duration: 3 minutes\n3 min\nModule 1 Readings\nReading•\n. Duration: 1 hour\n1h',
            '1-1.1. Formulating the Hypothesis\nVideo•\n. Duration: 13 minutes\n13 min\nLesson 1-1 Practice Quiz\nPractice Quiz•3 questions',
            '1-2.1. Analyzing the Result\nVideo•\n. Duration: 8 minutes\n8 min\nLesson 1-2 Practice Quiz\nPractice Quiz•3 questions',
            '1-3.1. Two-Tail Test for Mean\nVideo•\n. Duration: 10 minutes\n10 min\n1-3.2. Two-Tail Test for Mean in Excel\nVideo•\n. Duration: 4 minutes\n4 min\nLesson 1-3 Practice Quiz\nPractice Quiz•3 questions',
            '1-4.1. One-Tail Test for Mean\nVideo•\n. Duration: 5 minutes\n5 min\n1-4.2. Left-Tail Test for Mean in Excel\nVideo•\n. Duration: 3 minutes\n3 min\n1-4.3. Right-Tail Test for Mean in Excel\nVideo•\n. Duration: 6 minutes\n6 min\nLesson 1-4 Practice Quiz\nPractice Quiz•3 questions',
            '1-5.1. Testing the Proportion\nVideo•\n. Duration: 12 minutes\n12 min\n1-5.2. Left-Tail Test for Proportion in Excel\nVideo•\n. Duration: 5 minutes\n5 min\n1-5.3. Right-Tail Test for Proportion in Excel\nVideo•\n. Duration: 3 minutes\n3 min\n1-5.4. Two-Tail Test for Proportion in Excel\nVideo•\n. Duration: 5 minutes\n5 min\nLesson 1-5 Practice Quiz\nPractice Quiz•3 questions'
        ]
        self.downloads_text = [
            "Lecture Video (360p) mp4",
            "Lecture Video (720p) mp4",
            "Subtitles (English) WebVTT",
            "Transcript (English) txt", 
            "Module 1 Lesson 1 Slides pdf"
        ]

        self.opt = Options()
        self.driver = webdriver.Edge(options=self.opt)

        self.test_data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'data')
        self.overview_file_gt = os.path.join(self.test_data_folder, 'overview.md')
        self.reading_file_gt = os.path.join(self.test_data_folder, 'reading.md')

        self.temp_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'test', 'temp')
        CourseraDownloaderUtil.check_folder(self.temp_folder)
        self.overview_file = os.path.join(self.temp_folder, 'overview.md')
        # if os.path.exists(self.overview_file):
        #     os.remove(self.overview_file)
        self.reading_file = os.path.join(self.temp_folder, 'reading.md')
        if os.path.exists(self.reading_file):
            os.remove(self.reading_file)

    def tearDown(self):
        """tear down the test"""
        pass
    

    def test_CourseraDownloaderUtil(self):
        """
        test for get_video_download_link
        """
        arr = []
        self.buttons_text = [text for text in self.buttons_text if not ('Grade' in text)]
        index = 0
        while index < len(self.uls_text):
            if self.uls_text[index].startswith('Module'):
                break
            index += 1
        self.uls_text = self.uls_text[index:]


        for test in self.uls_text:
            h1_text = self.util.find_header(test, self.buttons_text)
            if test == "Module 1 Overview": 
                self.assertEqual(h1_text, "Module 1 Information")
            elif test == "1-1.1. Formulating the Hypothesis":
                self.assertEqual(h1_text, "Lesson 1-1: Formulating the Hypothesis")
            elif test == "1-2.1. Analyzing the Result":
                self.assertEqual(h1_text, "Lesson 1-2: Analyzing the Result")
            elif test == "1-3.1. Two-Tail Test for Mean":
                self.assertEqual(h1_text, "Lesson 1-3: Two-Tail Test for Mean")
            elif test == "1-4.1. One-Tail Test for Mean":
                self.assertEqual(h1_text, "Lesson 1-4: One-Tail Test for Mean")
            elif test == "1-5.1. Testing the Proportion":
                self.assertEqual(h1_text, "Lesson 1-5: Testing the Proportion")
            arr = []

    def test_find_higher_resolution(self):
        """
        test for find_higher_resolution
        """
        self.assertEqual(self.util.find_higher_resolution(self.downloads_text, "highest"), 1)
        self.assertEqual(self.util.find_higher_resolution(self.downloads_text, "lowest"), 0)

    def test_get_md_path(self):
        self.assertEqual(self.util.get_md_path("./Downloads/Inferential/Week1/Business/WelcometoInferential/subtitles-en.vtt"), "./Week1/Business/WelcometoInferential/subtitles-en.vtt")
        self.assertEqual(self.util.get_md_path("./Downloads/Inferential/Week1/Business/WelcometoInferential/subtitles-en.vtt", 1), "./Inferential/Week1/Business/WelcometoInferential/subtitles-en.vtt")
        self.assertEqual(self.util.get_md_path("./Downloads/Inferential/Week1/Business/WelcometoInferential/subtitles-en.vtt", 0), "./Downloads/Inferential/Week1/Business/WelcometoInferential/subtitles-en.vtt")
    
    def test_get_clean_name(self):
        self.assertEqual(self.util.get_clean_name("Lecture Video (360p) mp4"), "Lecture_Video_360p_Mp4")
        self.assertEqual(self.util.get_clean_name("Lecture Video (720p) mp4"), "Lecture_Video_720p_Mp4")
        self.assertEqual(self.util.get_clean_name("Subtitles (English) WebVTT"), "Subtitles_English_WebVTT")
        self.assertEqual(self.util.get_clean_name("Welcome to Inferential and Predictive Statistics for Business!"), "Welcome_To_Inferential_And_Predictive_Statistics_For_Business")

    # index = 9; print(f"index{index}: tag_name: {elements[index].tag_name}, text = {elements[index].text}")
    # l = [f"index{index}, tag_name: {elements[index].tag_name}, text = {elements[index].text}" for index in range(len(elements))]
    # print('\n'.join(l))
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