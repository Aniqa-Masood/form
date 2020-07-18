from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime 
import dateutil.relativedelta

from flask import Flask, request, render_template,jsonify
app = Flask(__name__)
def do_something(text1,text2):
    elementlist = []
    dlist=[]
    driver=webdriver.Chrome(executable_path='./drivers/chromedriver')
    driver.implicitly_wait(5)
    driver.get(text1)
    time.sleep(5)
    myString=text2
    elementlist=driver.find_elements_by_xpath("//*[contains(text(),'%s')]" % (myString))
    for element in elementlist:
        attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
        dlist.append(attrs)

    print(dlist)
    return dlist
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    result = do_something(text1,text2)
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)