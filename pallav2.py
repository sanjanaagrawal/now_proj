import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('/home/pallav/Downloads/chromedriver')

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()
    
    def search(self, text, connect,message):
        """ Search execeuted from home screen """
        # self._nav(self.feed_url)
        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
        # Waiting for search results to load
        time.sleep(10)
        formal = message
        self.driver.find_element_by_xpath("//button[@class='search-vertical-filter__filter-item-button artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view' and @aria-label='View only People results']").click()
                                            
        # if connect:
        self._search_connect(formal)
    
    def _search_connect(self,message):
        """ Called after search method to send connections to all on page """
        time.sleep(2)
        unorder_list = self.driver.find_elements_by_tag_name('search-results__list list-style-none')
        li=[]
        li = self.driver.find_elements_by_tag_name('li')
        for i in range(len(li)):
            time.sleep(5)
            self.driver.execute_script("document.getElementsByClassName('search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary')["+str(i)+"].click()")
            try:
                element = self.driver.find_element_by_xpath("//textarea[@class='send-invite__custom-message mb3 ember-text-area ember-view' and @name='message']")
            except NoSuchElementException:
                continue
            element.send_keys(message)
            self.driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view' and @aria-label='Send invitation']").click()
            time.sleep(5)
        time.sleep(2)


if __name__ == '__main__':

    username = ''
    password = ''
    search_text = 'airbnb'

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    message = "Respected recruiter im pallav agarwal a 3rd year (I.T) student at iet lucknow. I want to request you for a referal for an internship oppurtinity at airbnb. I have strong data structures and algorithms fundamentals"
    bot.search(search_text, True,message)
