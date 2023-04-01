'''
This program takes the search string from user and search it over the url mentioned
We used webbrowser module which lets us put URL and user query/

'''

import webbrowser
user_input= input("Enter what do you want to search")
webbrowser.open_new_tab("https://www.google.co.in/search?q="+user_input)