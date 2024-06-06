# Introduction
This repor contains two major funcitonalities: 
1. Help UIUC iMBA students to download the videos from Canvas. They are available for you to download and use for later on references. 
2. Help any Coursera users to download Coursera materials, including PDF, video, etc. 

# Installation
1. Install selenium by using **pip install**
Please do not use conda install. Conda version would not install the necessary browser drivers automatically. 

# Instructions for Coursera Downloader
* Go to path: src/coursera
* Run: 
  * python CourseraDownloader.py <address to your class>
  Example: python CourseraDownloader.py https://www.coursera.org/learn/country-level-economics/home/week/1
  * python CourseraDownload.py <address to a json file, which contains a list of coursers>
  Example python CourseraDownloader.py ../../courses.json
  Where the courses.json contains a list of strings, each string is the address to the Coursera class. 
* Input your Coursera username and password. 
* Once signed-in and to your class home page. Press Enter in the command line. 
* The download would triggered automatically. You could monitor the behavior in your command line area. 