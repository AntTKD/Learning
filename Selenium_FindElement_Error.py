# I am attempting to follow Chapter 12 of Automate the Boring Stuff with Python (ATBSwP).
# Changes to Selenium and ChromeDriver means that the code doesn't work as written.

from selenium import webdriver
# The below is needed so I can tell webdriver where 'chromedriver.exe' is.
from selenium.webdriver.chrome.service import Service 
# The below is needed because the listed 'find_element_*' methods or depreciated. 
from selenium.webdriver.common.by import By

# Pointing towards chromedriver 102 on my PC. 
s=Service(r'C:\Users\antse\AppData\Local\Chrome_WebDriver\chromedriver.exe')

# These lines prevent certain messages from clogging up the interpreter with faulty device messages. 
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])

def FNC_GET_CLASS_ELEMENT_FROM_PAGE(URL, CLASSNAME):       
    # Open webdriver with Chrome.
    browser = webdriver.Chrome(service = s, options = op)
    # Connect to URL.
    browser.get(URL)
    try:
        # Use the find_element() function to find an element with the chosen class name.
        # In ATBSwP, the method used is 'find_element_by_class_name(classname)', but on attempting to run it this
        #   way the error message says this method has depreciated and to use 'find_element() instead.'  
        elem = browser.find_element(By.CLASS_NAME, CLASSNAME)
        # Print the tag with the call name. 
        print('Found <%s> element with that class name!' % (elem.tag_name))
    except:
        print('Was not able to find an element with that name.')
    # I have tried taking the 'find_element()' function out of the try/except statement to view its error message, 
    #   but this error message also just satates that it can't find a matching class.

# To let people test the code quickly. 
while True:
    print('Choose which code to run:')
    print('(1) = Faulty Code -> FNC_GET_CLASS_ELEMENT_FROM_PAGE(\'https://inventwithpython.com\', \'card-img-top cover-thumb\')')
    print('(2) = Functional Code -> FNC_GET_CLASS_ELEMENT_FROM_PAGE(\'https://en.wikipedia.org/wiki/Tyrannosaurus\',\'image\')')
    print('(3) = Custom Code -> Choose your own URL and Class Name')
    choice = input('> ')
    if choice == '1':
        # Problematic code: I know that an <img> tag where class = 'card-img-top cover-thumb' exists 
        #   at the above url but the Python code says that it can't find it.
        print('\n')
        print('Running faulty code...')
        FNC_GET_CLASS_ELEMENT_FROM_PAGE('https://inventwithpython.com', 'card-img-top cover-thumb')
        print('\n')
        continue
    elif choice == '2':
        # Trying the code on a different url works. 
        print('Running functioning code...')
        print('\n')
        FNC_GET_CLASS_ELEMENT_FROM_PAGE('https://en.wikipedia.org/wiki/Tyrannosaurus','image') # Dinosaurs are awesome
        print('\n')
        continue
    elif choice == '3':
        # Let the user try thweir own arguments. 
        print('Running custom code...')
        user_url = input('Type your URL: ')
        user_class = input('Type the element\'s class name: ')
        FNC_GET_CLASS_ELEMENT_FROM_PAGE(user_url,user_class) 
        print('\n')
        continue
    else:
        print('\n')
        print('Please enter either \'1\' or \'2\'.')
        print('\n')
        continue