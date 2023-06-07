#!/user/bin/python3
# Script: Ops 401 Class 36 Code Challenge
# Deontae Carter
# 6/7/2023
# Purpose: Cookie Capture Capades



# The below Python script shows one possible method to return the cookie from a site that supports cookies.

# import requests

# # targetsite = input("Enter target site:") # Uncomment this to accept user input target site
# targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
# response = requests.get(targetsite)
# cookie = response.cookies

# def bringforthcookiemonster(): # Because why not!
#     print('''

#               .---. .---.
#              :     : o   :    me want cookie!
#          _..-:   o :     :-.._    /
#      .-''  '  `---' `---' "   ``-.
#    .'   "   '  "  .    "  . '  "  `.
#   :   '.---.,,.,...,.,.,.,..---.  ' ;
#   `. " `.                     .' " .'
#    `.  '`.                   .' ' .'
#     `.    `-._           _.-' "  .'  .----.
#       `. "    '"--...--"'  . ' .'  .'  o   `.

#         ''')

# bringforthcookiemonster()
# print("Target site is " + targetsite)
# print(cookie)

# # Add here some code to make this script perform the following:
# # - Send the cookie back to the site and receive a HTTP response
# # - Generate a .html file to capture the contents of the HTTP response
# # - Open it with Firefox



#!/usr/bin/python3

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Sending the cookie back to the site and receiving a HTTP response
response = requests.get(targetsite, cookies=cookie)
html_content = response.text

# Generating a .html file to capture the contents of the HTTP response
file_name = "response.html"
with open(file_name, "w") as file:
    file.write(html_content)

# Opening the file with Firefox
webbrowser.register('firefox', None, webbrowser.GenericBrowser('firefox'), 1)
webbrowser.get("firefox").open(file_name)
