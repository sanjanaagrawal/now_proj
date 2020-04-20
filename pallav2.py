import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:
    def _init_(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('')

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
# mentions-texteditor__content
    def post(self, text):
        """ Make a text post """
        self.driver.find_element_by_class_name('share-box__open').click()
        self.driver.find_element_by_class_name('ql-editor ql-blank').send_keys(text)
        self.driver.find_element_by_class_name('share-actions__primary-action').click()
    
    def search(self, text, connect):
        """ Search execeuted from home screen """
        # self._nav(self.feed_url)
        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
        # Waiting for search results to load
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@class='search-vertical-filter__filter-item-button artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view' and @aria-label='View only People results']").click()
                                            
        # if connect:
        self._search_connect()
    
    def _search_connect(self):
        """ Called after search method to send connections to all on page """
        # print("agya")
        time.sleep(2)
        # search = self.driver.find_element_by_class_name('search-result_actions')
        unorder_list = self.driver.find_element_by_xpath("//ul[@class='search-results__list list-style-none']")
        for div in unorder_list.find_all('li'):
            self.driver.find_element_by_xpath("//div[@class='ember-view']/button[@class='search-result_action-button search-result_actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary']").click()
            time.sleep(2)
        # self.driver.find_element_by_xpath("//div[@class='search-result_actions']/button[@class='message-anywhere-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary']").click()
        time.sleep(2)
        # self.driver.find_element_by_class_name('ml1').click()


if _name_ == '_main_':

    username = ''
    password = ''
    # post_text = 'nothing'
    search_text = 'amazon'

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    # bot.post(post_text)
    bot.search(search_text, True)