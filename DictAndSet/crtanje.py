import turtle
import webbrowser
from time import sleep

# turtle.circle(75.00)
# sleep(4)

# turtle.done()

# help(turtle)

url = 'https://www.rezultati.com/tenis/'
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(url)
