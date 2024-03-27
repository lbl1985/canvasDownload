import sys, os, unittest
repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'coursera')
sys.path.append(repo_root)
from CourseraDownloaderUtil import CourseraDownloaderUtil

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
            test = test.split('\n')[0]
            for text in self.buttons_text:
                ratio = self.util.similar(test, text)
                arr.append(ratio)
            # print(arr)
            max_index = arr.index(max(arr))
            h1_text = self.buttons_text[max_index].split('\n')[0]
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


            # print(f"{test} ===> {h1_text}")
            arr = []