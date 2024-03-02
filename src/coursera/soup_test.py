from bs4 import BeautifulSoup
import requests
# If the website needs login
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(EdgeChromiumDriverManager().install())

url = "https://www.coursera.org"  # replace with your URL

# username = getpass('Enter your username: ')
# password = getpass('Enter your password: ')

# Create a session
session = requests.Session()

# Define the login data
# login_data = {
#     'username': r'herbert19lee@gmail.com',
#     'password': r'OCamps@2013'
# }

# Post the login data to the website
# session.post(url, data=login_data)

# Use the session to get access to the website
# response = session.get('https://www.coursera.org/learn/risk-management-empathy-data/home/week/4')

# response = requests.get(url, auth=(username, password))

# Save the response content as a .html file
# with open("response.html", "w", encoding='utf-8') as file:
#     file.write(response.text)

    # If the website has two-factor authentication, you might need to handle it here
    # This is a simple example and might not work for all websites
    # You would need to know the exact process the website uses for two-factor authentication

# Get the two-factor code
# two_factor_code = getpass('Enter your two-factor code: ')

# Define the two-factor data
# two_factor_data = {
#     'username': r'herbert19lee@gmail.com',
#     'password': r'OCamps@2013',
#     'code': two_factor_code
# }

# Post the two-factor data to the website
# session.post(url, data=two_factor_data)

# Now you should be logged in and can continue to get the page you want
# response = session.get('https://www.coursera.org/learn/risk-management-empathy-data/home/week/4')

# Save the response content as a .html file
# with open("response.html", "w", encoding='utf-8') as file:
#     file.write(response.text)

# print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')

# paragraphs = soup.find_all('p')

# for p in paragraphs:
#     print(p.get_text())
    
# Define the URL you want to visit
url = 'https://www.coursera.org/learn/risk-management-empathy-data/home/week/4'

# Define the path to the Edge user data directory

edge_user_data_dir = r'C:\Users\herbe\AppData\Local\Microsoft\Edge\User Data'


# Define Chrome options
options = Options()
options.add_argument(f'user-data-dir={edge_user_data_dir}')

driver = webdriver.Edge(options=options)
# Start the Chrome driver with the specified options
# driver = webdriver.Chrome(options=options)

# Visit the URL
driver.get(url)

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')
with open("response.html", "w", encoding='utf-8') as file:
    file.write(response.text)

# Find all paragraph elements
paragraphs = soup.find_all('p')

# Print the text of each paragraph
for p in paragraphs:
    print(p.get_text())
