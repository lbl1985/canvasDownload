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
* The download would be triggered automatically. You could monitor the behavior in your command line area. 

# Usage for the downloads
The major benefits of using the tool are not only about automatic downloading, but also using markdown files to organize the downloaded contents. 

When we download the files, the corresponding information such as the the Course name, Modual name, week topic and extra information, etc.. The markdown file and the corresponding .mp4 video files are all saved in relative folder paths. If in Visual Code, users could directly click on the hyper link to watch the videos. 

# msedge driver
This current implementation is use the selenium for msedge. Therefore, you may have to go [msedgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH) to download the latest version of msedgedriver and put into your local machine location. 
On my machine the location is **C:\Tools\edgedriver_win64**
Of course, you would have to add the **C:\Tools\edgedriver_win64** location into your local environment path. 

# Declaration
All operations in software are allowed by Coursera. The program author is free of any related liabilities related to the usage of the software. The users should take full responsibilities. Meanwhile, the goal for the software is to help users ease up the burden of saving materials for them to go over offline or for later references. Please do not copy or propogate the information for whatever unlawful behaviors. 