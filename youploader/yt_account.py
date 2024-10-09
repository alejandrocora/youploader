from youploader.constants import *
from youploader.utils.selaux import *
from youploader.utils.logging import  *

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *


class YT_Account():
    def __init__(self, driver, output):
        self.driver = driver
        self.output = output
        self.channel_code = ''

    def login(self, username, password):
        print_save('[i] Login with ' + username + '...', self.output)
        self.driver.get(YT_LOGIN)
        try:
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='identifier']")))
            self.driver.find_element(By.XPATH, "//input[@name='identifier']").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@name='identifier']").send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']")))
            self.driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys(Keys.ENTER)
            wait_return(self.driver, "/html/body/div[4]/header/div[2]/div[1]/div[4]/div/a", False, False, 15)
            print_save('[i] Login successful.', self.output)
            return True
        except TimeoutException:
            print_save('[!] An error occurred during login, input not found.', self.output)
            return False

    def report_video(self, video_url, n_reason):
        reasons = n_reason.split(',')
        self.driver.get(video_url)
        sleep(2)
        wait_return(self.driver, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]", True, False, 30).click()
        wait_return(self.driver, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[2]/tp-yt-paper-item", True, True, 30).click()
        elems = wait_return(self.driver, "//tp-yt-paper-radio-button", False, False, 15)[int(reasons[0])-1].click()
        if len(n_reason) > 1:
            wait_return(self.driver, "//tp-yt-paper-dropdown-menu", False, True, 15)[int(reasons[0])-1].click()
            wait_return(self.driver, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-dropdown-menu[1]/tp-yt-paper-menu-button/tp-yt-iron-dropdown/div/div/tp-yt-paper-listbox/tp-yt-paper-item", False, True, 15)[int(reasons[1])+1].click()
            wait_return(self.driver, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/div/yt-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]", True, False, 15).click()
            wait_return(self.driver, "//*[@id='submit-button']/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]", True, False, 15).click()
            print_save('[+] Video reported!', self.output)

    def get_channel_code(self):
        self.driver.get(YT_MAIN)
        channel = wait_return(self.driver, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[2]/button/yt-img-shadow/img", True, True, 30).click()
        channel = wait_return(self.driver, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[2]/ytd-active-account-header-renderer/div/yt-formatted-string[4]/a", True, False, 30).get_attribute('href').split('/')[-1]
        return channel

    def upload(self, file_path, title, description):
        if not self.channel_code:
            self.channel_code = self.get_channel_code()
        self.driver.get(YT_UPLOAD.replace('$code', self.channel_code))
        wait_return(self.driver, "//ytcp-button[@id='create-icon']", True, True, 15).click()
        wait_return(self.driver, "//tp-yt-paper-item[@id='text-item-0']", True, True, 15).click()
        wait_return(self.driver, "//input[@type='file']", True, False, 15).send_keys(file_path)
        #wait_return(self.driver, "//ytcp-button[@id='select-files-button']", True, True, 15).send_keys(file_path)
        #pyperclip.copy(file_path)
        #pyautogui.hotkey("ctrl", "v")
        #pyautogui.press('enter')
        try:
            WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-iron-icon[@class='error-icon']")))
            return 1
        except TimeoutException:
            pass
        title_input = wait_return(self.driver, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-video-title/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div", True, False, 30)
        title_input.clear()
        title_input.send_keys(title)
        wait_return(self.driver, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-video-description/div/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div", True, False, 30).send_keys(description)
        try:
            self.driver.find_elements(By.XPATH, "//div[@id='offRadio']")[1].click()
        except ElementClickInterceptedException:
            print_save('[!] An error ocurred while uploading video. Perhaps the file path ' + file_path + ' is incorrect?', self.output)
            return False
        for n in range(0, 3):
            self.driver.find_element(By.XPATH, "//ytcp-button[@id='next-button']").click()
        wait_return(self.driver, "//div[@id='radioContainer']", False, True, 30)[2].click()
        try:
            wait_return(self.driver, "//ytcp-button[@id='got-it-button']", True, True, 30)
        except TimeoutException:
            pass
        self.driver.find_element(By.XPATH, "//ytcp-button[@id='done-button']").click()
        try:
            video_url = wait_return(self.driver, "/html/body/ytcp-video-share-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/div/div/a", True, False, 60).get_attribute('href').split('?')[0]
        except TimeoutException:
            return 2
        return video_url
