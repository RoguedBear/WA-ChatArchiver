# RUN CHROME AS  google-chrome --remote-debugging-port=9222
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
from sys import stdout
# Start script by setting chromedriver in the environmental PATH variable

#Hello message:
print("\t\x1b[1;31m Script created by \x1b[1m\x1b[5;32;40mROGUEDBEAR\x1b[0m")

def archive():
    #driver.implicitly_wait(5)
    drop_menu = driver.find_element_by_class_name("_3Bxar")

    try:
        print("Hope you dont do something on the web rn.😒")
        hover = ActionChains(driver).move_to_element(drop_menu)
        hover.perform()


        z = driver.find_element_by_class_name("ZR5SB")
        z.click()

    except:
        print("error while run, retrying")
        return 0
    # sleep(5)
    while True:
        try:
            archive_button = driver.find_element_by_class_name("_167q")
            archive_button.click()
            print("FOUND: Archive button.")
            return 1
        except:
            print("NOT FOUND")
            return 0


# initialising webdriver
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Firefox()
#driver.get("https://web.whatsapp.com")
# Input: number/name
stdout.write("Enter number: ")
sleep(2)
id = input("You Enter: ")
for i in id:
    stdout.flush()
    stdout.write(i)
    sleep(0.2)
sleep(1)
print()
# Since I know its gonna be WA, so check that the current url is WA

if driver.current_url == 'https://web.whatsapp.com/':
    print(f"[{datetime.now().strftime('%H:%M')}]", "URL already opened.")
    pass
else:
    print(f"[{datetime.now().strftime('%H:%M')}]", "URL not opened, opening one...")
    driver.get("https://web.whatsapp.com")

# Wait for the page to load
search_bar = WebDriverWait(driver, 60).until(lambda r: driver.find_element_by_class_name("selectable-text"))

# select search if not; retrieve the current number and clear and all
print(f"[{datetime.now().strftime('%H:%M')}]", "Search Bar Found")
if search_bar.text in id:
    print(f"[{datetime.now().strftime('%H:%M')}]", "id already in search bar, commencing archive checks 🤖BEEPBOOP🤖")
else:
    print(f"[{datetime.now().strftime('%H:%M')}]", "Typing in id...")
    search_bar.clear()
    search_bar.send_keys(id)


# Ensuring only one chat is there:
# if more chats are there, redo the search thingy
while True:
    if len(driver.find_elements_by_class_name('_2wP_Y')) == 2:
        print(f"[{datetime.now().strftime('%H:%M')}]", "Only one chat found. Very good😏...")
        break
    else:
        print(f"[{datetime.now().strftime('%H:%M')}]", "More than one chat present. re-searching...")
        search_bar.clear()
        search_bar.send_keys(id)

# TODO: archive test(); imp:
try:
    while True:
        if len(driver.find_elements_by_class_name('_2wP_Y')) == 2:
            try: # If archive element is present or not
                # driver.implicitly_wait(5)
                if_archived = driver.find_element_by_class_name("_3JEcM")
                if if_archived.text == 'Archived':
                    print(f"[{datetime.now().strftime('%H:%M')}]", "archived...", end='\r')
                    continue
            except:
                if len(driver.find_elements_by_class_name("_2wP_Y")) == 2:
                    print(f"[{datetime.now().strftime('%H:%M')}]", "Archived Box not found; Archiving...")

                    result = archive()
                    # wait until archive is visible
                    if result == 1:
                        try:
                            WebDriverWait(driver, 10).until(lambda r: driver.find_element_by_class_name("_3JEcM"))
                            print(f"[{datetime.now().strftime('%H:%M')}]", "Archive CONFIRMED")
                        except:
                            continue
                    elif result ==0:
                        continue
                else:
                    continue
        else:
            print(f"[{datetime.now().strftime('%H:%M')}]", "More than one chat, probably on homescreen. Researching...")
            search_bar.clear()
            search_bar.send_keys(id)
            sleep(0.5)
except KeyboardInterrupt:
    print("Bye Bye!")
    driver.quit()
