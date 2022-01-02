# Author
# Praneet Kumar, B.Tech CSE
# NIT Silchar, Class of 2019
# Editor
# Rakesh Reddy, B.Tech PET
# GIET College of Engineering(JNTUK)

import os
import requests
from zipfile import ZipFile
import time
import re
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# ------------------  OS FOLDER CREATE  -------------------- #

# Python program to explain os.mkdir() method
# importing os module
#importing requests
# importing required modules

# Directory
directory = "Chromedriver"

# Parent Directory path
parent_dir = "c:/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'Chromedriver' in
# 'c:/'
try: 
    os.mkdir(path) 
except OSError as error: 
    print(Dirctory alredy exit going to next step!)

print('Downloading all the files now...')
print('Downloading ...............0%')
print('Downloading ...............5%')
print('Downloading ...............38%')
print('Downloading ...............54%')
print('Downloading ...............98%')
print('Downloading ...............99%')
print('Downloading ...............100%')

url = 'https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_win32.zip'

myfile = requests.get(url, allow_redirects=True)

print('Downloading Completed')

open('c:/Chromedriver/chromedriver_win32.zip', 'wb').write(myfile.content)



# specifying the zip file name
file_name = "c:/Chromedriver/chromedriver_win32.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
	# printing all the contents of the zip file
	zip.printdir()

	# extracting all the files
	print('Extracting all the files now...')
try:
    zip.extractall('c:/Chromedriver/')
except:
    print('Extraction already Completed!')


# ------------------  USER INPUT -------------------- #

url = ""

''' How frequently you want the updates. Basically the script will crawl the page after every 'time_interval' seconds
    specified. Recommended to keep >= 10. '''
time_interval = '15'

''' Set either 'Y' or 'N' for the below five options. '''

show_match_status = ''
show_fours = ''
show_sixes = ''
show_wickets = ''
show_EndOfOver = ''
show_singles = ''
show_dot = ''
show_Balls = ''

''' Stores the runs, wickets and overs scored before and after a ball. '''
prev_numbers = [0, 0, 0, 0]                           # Do not change


# ---------------------  INITIALIZE CHROMEDRIVER  ---------------------- #

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"                     # Enable explicit wait.
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')             # Start Chrome maximized.
driver = webdriver.Chrome('C:\Chromedriver\chromedriver.exe', desired_capabilities=capa, chrome_options=options)  # Arguments
driver.get(url)

time.sleep(15)


# --------------- GET MATCH DETAILS ----------------- #

while 0 == 0:                                                                       # For infinite loop

    ''' Find the title, i.e., the names of the teams playing the match. '''
    title_element = driver.find_element_by_css_selector(".cb-nav-hdr.cb-font-18.line-ht24")
    title_complete = title_element.text
    title_partial = title_complete.split(",")[0]

    ''' Get the current score '''
    score_element = driver.find_element_by_css_selector(".cb-font-20.text-bold.inline-block.ng-binding")
    current_score = score_element.text

    ''' Create two empty lists which will contain the details of the players, i.e., their names, runs scored and 
    balls consumed '''
    player_1 = [[] for i in range(3)]
    player_2 = [[] for i in range(3)]

    ''' Get the names of the current batsmen. '''
    player_names = driver.find_elements_by_xpath('//a[@ng-bind="batsmen.full_name"]')
    try:
        player_1[0] = player_names[0].text
        player_2[0] = player_names[1].text
    except:
        player_2[0] = ""

    ''' Get the runs scored by the two batsmen. '''
    player_runs = driver.find_elements_by_xpath('//div[@ng-bind="batsmen.r"]')
    try:
        player_1[1] = player_runs[0].text
        player_2[1] = player_runs[1].text
    except:
        player_2[1] = ""

    ''' Get the balls consumed by the two batsmen. '''
    player_balls = driver.find_elements_by_xpath('//div[@ng-bind="batsmen.b"]')
    try:
        player_1[2] = player_balls[0].text
        player_2[2] = player_balls[1].text
    except:
        player_2[2] = ""

    ''' Get the match status. '''
    try:
        match_status = driver.find_element_by_xpath('//div[@ng-bind="match.status"]').text
    except:
        match_status = ""

    ''' Stores the runs, wickets and overs from current_score in a list.
    0th element : runs
    1st element : wickets
    2nd element : over
    3rd element : balls
    Eg. if current_score == 125/5 (43.1 Ovs), the list will contain [125, 5, 43, 1]. '''
    curr_numbers = re.findall(r'\d+', current_score)

    ''' Delete any extra information if present to make the size of list as four '''
    if len(curr_numbers) == 5:
        del curr_numbers[0]
    elif len(curr_numbers) == 6:
        del curr_numbers[0]
        del curr_numbers[0]
    curr_numbers = list(map(int, curr_numbers))         # Convert the data into a list of integers.

    ''' Form the string with the scores of the batsmen and their names. '''
    batsmen_1 = str(player_1[0]) + " " + str(player_1[1]) + "(" + str(player_1[2]) + ")"
    if player_2[0] != '':
        batsmen_2 = str(player_2[0]) + " " + str(player_2[1]) + "(" + str(player_2[2]) + ")"
    else:
        batsmen_2 = ""

    toaster = ToastNotifier()                       # Create an instance of Windows 10 notifications.

    ''' Show the Win10 notifications for base case. '''
    if prev_numbers == [0, 0, 0, 0]:
        toaster.show_toast(title_partial,
                           current_score + "\n" + batsmen_1 + "\n" + batsmen_2,
                           icon_path="Cricket.ico")
        if show_match_status == 'Y':
            toaster.show_toast(title_partial,
                               match_status,
                               icon_path="Cricket.ico")
    else:
        info, flag = "", 0
        if curr_numbers[0] == prev_numbers[0] + 4 and show_fours == 'Y':      # If there is an increment of 4 runs.
            info = "It's a FOUR!! "
            flag = 1
        if curr_numbers[0] == prev_numbers[0] + 6 and show_sixes == 'Y':      # If there is an increment of 6 runs.
            info = "It's a SIX!! "
            flag = 1
        if curr_numbers[0] == prev_numbers[0] + 1 and show_singles == 'Y':      # If there is an increment of 1 run.
            info = "It's a SINGLE!! "
            flag = 1
        if curr_numbers[0] == prev_numbers[0] + 0 and show_dot == 'Y':      # If there is no change with 0 run.
            info = "It's a DOT BALL!! "
            flag = 1
        if curr_numbers[1] == prev_numbers[1] + 1 and show_wickets == 'Y':    # If there is an increment of 1 wicket.
            info += "It's a WICKET!! "
            flag = 1
        if curr_numbers[2] == prev_numbers[2] + 1 and show_EndOfOver == 'Y':  # If there is an increment of 1 over.
            info += "END OF OVER!!"
            flag = 1
        if curr_numbers[3] == prev_numbers[3] + 1 and show_Balls == 'Y':  # If there is an increment of 1 ball.
            info += "Ball!!"
            flag = 1

        ''' If any of the above conditions are true, show the Win10 notifications. '''
        if flag == 1:
            toaster.show_toast(title_partial,
                               current_score + "\n" + batsmen_1 + "\n" + batsmen_2 + "\n" + info,
                               icon_path="Cricket.ico")
            if show_match_status == 'Y':
                toaster.show_toast(title_partial,
                                   match_status,
                                   icon_path="Cricket.ico")

        if info != "":
            print(title_partial + "\n" + current_score + "\n" + batsmen_1 + "\n" + batsmen_2 + "\n" + match_status
                  + "\n" + info + "\n")

    prev_numbers = curr_numbers                  # Keep track of score before and after a ball.
    time.sleep(int(time_interval))               # Crawl again after the given time interval.

driver.quit()                                    # Quit the browser.


