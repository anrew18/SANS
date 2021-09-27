from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class Test():
    def testAddMovie(self):

        driver = webdriver.Firefox(executable_path="/Users/andrew.alexander/PycharmProjects/drivers/geckodriver")
        driver.get("file:///C:/Users/andrew.alexander/PycharmProjects/SANS/venv/LogIn.html")


        title = "Impossible"
        date = "12122020"
        rating = "4"


        target = driver.find_element_by_id("title")
        target.send_keys(title)
        target = driver.find_element_by_id("releaseDate")
        ActionChains(driver).move_to_element(target).click().send_keys(date).perform()
        target = driver.find_element_by_id("rating")
        target.send_keys(rating)
        time.sleep(5)
        target = driver.find_element_by_id("submit")
        target.click()

        # obviously ths is a better test to take place on the form submission code. we could also query the results from the DB to see if they matched the submission.
        if len(title) > 200:
            print("fail")
        else:
            print("pass")


        driver.close()

    def testaddMovieFail(self):
        driver = webdriver.Firefox(executable_path="/Users/andrew.alexander/PycharmProjects/drivers/geckodriver")
        driver.get("file:///C:/Users/andrew.alexander/PycharmProjects/SANS/venv/LogIn.html")

        title = ""
        date = "12122020"
        rating = "4"

        target = driver.find_element_by_id("title")
        target.send_keys(title)
        target = driver.find_element_by_id("releaseDate")
        ActionChains(driver).move_to_element(target).click().send_keys(date).perform()
        target = driver.find_element_by_id("rating")
        target.send_keys(rating)
        time.sleep(5)
        target = driver.find_element_by_id("submit")
        target.click()

        if len(title) < 1:
            print("fail, title too short")
        else:
            print("pass")

        """connect to DB"""

        """
        def queryCheck(conn):
            cur= conn.cursor()
            cur.execute("SELECT * FROM movies")
            
            rows = cur.fetchall()
            
            for row in rows:
                if row = title:
                    print("pass")
                else:
                    print("fail")
                    
        """

        driver.close()

testRunner = Test()
testRunner.testAddMovie()
testRunner.testaddMovieFail()
