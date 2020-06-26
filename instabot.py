from selenium import webdriver
from info import password as pw, username as user 
import time
class InstaBot:
    def __init__(self, user, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("http://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)

    def get_unf(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(user)).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href, 'following')]").click()
        following = self._get_names()
        following.sort()
        self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]").click()
        followers = self._get_names()
        followers.sort()
        print(followers, following)
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        time.sleep(2)
        box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last, cur = 0,1
        while last != cur:
            last = cur
            time.sleep(1)
            cur = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, box)
        links = box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text!='']
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        time.sleep(1)
        return names


myBot = InstaBot(user, pw)
myBot.get_unf()
