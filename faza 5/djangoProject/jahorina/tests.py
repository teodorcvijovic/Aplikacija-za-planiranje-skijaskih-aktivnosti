
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By


# Create your tests here.

# uslov za izvrsenje svih ovih testova je da se
# u sistemu nalazi moderator filip sa lozinkom 123
# i da se u sistemu nalazi makar jedna staza

# filip
def testviewTracks():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/')
    chrome_driver.maximize_window()

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    assert "Ski-staze Jahorine" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# filip
def testTrackEdit():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Jahorina - Ko preživi, pričaće!" == chrome_driver.title
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditOpen():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "otvorena" == chrome_driver.find_element(by=By.XPATH,
                                                    value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[2]').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditFoggy():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_foggy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "maglovito" in chrome_driver.find_element(by=By.XPATH,
                                                     value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditBusy():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_busy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "ima gužve" in chrome_driver.find_element(by=By.XPATH,
                                                     value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditBusyAndFoggy():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_busy').click()
    chrome_driver.find_element(by=By.NAME, value='is_foggy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "ima gužve", "maglovito" in chrome_driver.find_element(by=By.XPATH,
                                                                  value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditCommentChar():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('test komentar')

    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "test komentar" in chrome_driver.find_element(by=By.XPATH,
                                                         value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditCommentNum():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('123456')

    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "123456" in chrome_driver.find_element(by=By.XPATH,
                                                  value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditCommentSpec():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('#$&!')

    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "#$&!" in chrome_driver.find_element(by=By.XPATH,
                                                value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
    sleep(2)
    chrome_driver.close()


# filip
def testTrackEditDiscard():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('novi komentar')
    chrome_driver.find_element(by=By.NAME, value='is_busy').click()

    chrome_driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "#$&!" in chrome_driver.find_element(by=By.XPATH,
                                                value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
    sleep(2)
    chrome_driver.close()


# filip
# NAPOMENA - u bazi mora postojati makar jedna staza
def testTrackEditDelete():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://localhost:8000/login/')
    chrome_driver.maximize_window()

    # login as filip with password 123

    username = chrome_driver.find_element(by=By.NAME, value="username")
    password = chrome_driver.find_element(by=By.NAME, value="password")

    username.send_keys("filip")
    password.send_keys("123")

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    allTracksBtn = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div/ul/li[3]/a')
    chrome_driver.execute_script("arguments[0].click();", allTracksBtn)

    button = chrome_driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/div/div[2]/div[6]/div/div[1]/div[2]/form')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Olimpijski Veleslalom" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]').text
    chrome_driver.close()



# lara
def testUspjesnaRegistracija():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola58");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Jahorina - Ko preživi, pričaće!" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testKorisnickoImePostojiUBazi():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("filip");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testLozinkaIPotvrdaLozinkeSeNePoklapaju():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola1");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("123");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNegativneGodineIskustva():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola2");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("-1");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testDatumRodjenjaULosemFormatu():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola101");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("10");
    date.send_keys("01011999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenoKorisnickoIme():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenaLozinka():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola3");
    password1.send_keys("");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenaPotvrdaLozinke():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola4");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenoIme():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola5");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenoPrezime():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola6");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenaEmailAdresa():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola6");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenBrojTelefona():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola7");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testNijeUnesenoIskustvo():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola9");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()


# lara
def testKorisnickoImePostojiUBazi():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username = chrome_driver.find_element(by=By.NAME, value="username");
    password1 = chrome_driver.find_element(by=By.NAME, value="password1");
    password2 = chrome_driver.find_element(by=By.NAME, value="password2");
    firstName = chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName = chrome_driver.find_element(by=By.NAME, value="last_name");
    email = chrome_driver.find_element(by=By.NAME, value="email");
    phone = chrome_driver.find_element(by=By.NAME, value="phone");
    instagram = chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat = chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook = chrome_driver.find_element(by=By.NAME, value="facebook");
    experience = chrome_driver.find_element(by=By.NAME, value="experience");
    date = chrome_driver.find_element(by=By.NAME, value="birthdate");
    button = chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("filip");
    password1.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    password2.send_keys("pbkdf2_sha256$320000$WD4xM2OBg4jiISOlm0ORTs$roNb4HbetXYqOAHHiChwef/9wdGyvnxoNYRv9E5OQNc=");
    firstName.send_keys("Nikola");
    lastName.send_keys("Jovanovic");
    email.send_keys("dzoni1@gmail.com");
    phone.send_keys("+381652090657");
    experience.send_keys("5");
    date.send_keys("01/01/1999");
    button = chrome_driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/form/button")
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Registracija" == chrome_driver.title

    sleep(2)
    chrome_driver.close()



