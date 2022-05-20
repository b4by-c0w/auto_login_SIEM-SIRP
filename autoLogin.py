from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import requests


dict_button = {
	"submit_ELK": """//button[@type="submit"][@data-test-subj="loginSubmit"]""",
	"userName_SIRP": """//input[@ng-model="params.username"]""",
	"password_SIRP": """//input[@ng-model="params.password"]""",
	"submit_SIRP": """//button[@type="submit"][@ng-click="login()"]"""
}

def init_browser(URI):
	global browser
	gecko = r'.\webdrivers\msedgedriver.exe'
	browser = webdriver.Edge(executable_path=gecko)
	browser.get(URI)
	browser.implicitly_wait(30)

def login_siem(username, passwd):
	email_box = browser.find_element_by_name('username')
	email_box.send_keys(username)
	# print("Email {} entered!".format(username))

	pass_box = browser.find_element_by_name('password')
	pass_box.send_keys(passwd)
	# print("Password entered!")

	button_login = browser.find_element_by_xpath(dict_button["submit_ELK"])
	print(button_login)
	button_login.click()

	# print("Cookie: {}".format(browser.get_cookies()))
	browser.implicitly_wait(30)

def login_sirp(username,passwd):

	email_box = browser.find_element_by_xpath(dict_button["userName_SIRP"])
	email_box.send_keys(username)
	# print("Email {} entered!".format(username))

	pass_box = browser.find_element_by_xpath(dict_button["password_SIRP"])
	pass_box.send_keys(passwd)
	# print("Password entered!")

	button_login = browser.find_element_by_xpath(dict_button["submit_SIRP"])
	print(button_login)
	button_login.click()

	# print("Cookie: {}".format(browser.get_cookies()))
	browser.implicitly_wait(30)



if __name__ == "__main__":
	# init functions
	init_browser('linkSIEMELK') #https://siem.vn
	login_siem('','') #Fill usrname và passwd
	browser.execute_script("window.open('');")# Switch to the new window and open URL SIRP
	browser.switch_to.window(browser.window_handles[1])
	browser.get('linkSIRP') #https://sirp.vn 
	login_sirp('','') #Fill usrname và passwd



