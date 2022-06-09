from django.test import TestCase

# Create your tests here.

import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

#korisnik sa username filip treba da postoji u bazi

#lara
def testUspjesnaRegistracija():
    chrome_driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_driver.get('http://127.0.0.1:8000/register/')
    chrome_driver.maximize_window();
    username= chrome_driver.find_element(by=By.NAME, value="username");
    password1= chrome_driver.find_element(by=By.NAME, value="password1");
    password2= chrome_driver.find_element(by=By.NAME, value="password2");
    firstName= chrome_driver.find_element(by=By.NAME, value="first_name");
    lastName= chrome_driver.find_element(by=By.NAME, value="last_name");
    email= chrome_driver.find_element(by=By.NAME, value="email");
    phone= chrome_driver.find_element(by=By.NAME, value="phone");
    instagram= chrome_driver.find_element(by=By.NAME, value="instagram");
    snapchat= chrome_driver.find_element(by=By.NAME, value="snapchat");
    facebook =  chrome_driver.find_element(by=By.NAME, value="facebook");
    experience= chrome_driver.find_element(by=By.NAME, value="experience");
    date= chrome_driver.find_element(by=By.NAME, value="birthdate");
    button=chrome_driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div[2]/div/form/button");

    username.send_keys("nikola");
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

    username.send_keys("nikola10");
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


