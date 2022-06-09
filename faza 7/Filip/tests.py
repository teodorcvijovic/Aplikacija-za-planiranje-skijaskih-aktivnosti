from django.test import TestCase

# Create your tests here.
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "otvorena" == chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[2]').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_foggy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "maglovito" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_busy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "ima gužve" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    chrome_driver.find_element(by=By.NAME, value='is_busy').click()
    chrome_driver.find_element(by=By.NAME, value='is_foggy').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "ima gužve", "maglovito" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('test komentar')

    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "test komentar" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('123456')

    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "123456" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('#$&!')

    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "#$&!" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    chrome_driver.find_element(by=By.NAME, value='comment').send_keys('novi komentar')
    chrome_driver.find_element(by=By.NAME, value='is_busy').click()

    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "#$&!" in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[3]').text
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

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)
    chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/form/div[3]/div/div[1]/label/input').click()

    button = chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div/div/div[2]/form/button')
    chrome_driver.execute_script("arguments[0].click();", button)

    assert "Poljice" not in chrome_driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]').text
    sleep(2)
    chrome_driver.close()
