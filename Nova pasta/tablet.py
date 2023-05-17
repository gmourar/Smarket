import smtplib
import schedule
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from cx_Freeze import setup, Executable



chrome_options = Options()

nav = webdriver.Chrome(options= chrome_options)

sighramanager = ('http://187.61.13.196/mn00000/login.jsf')

def tab():
    nav.get(sighramanager)
    time.sleep(10)

tab()
 