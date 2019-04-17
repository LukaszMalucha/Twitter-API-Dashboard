from behave import *
from selenium import webdriver

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.common_trends_page import CommonTrendsPage
from tests.acceptance.page_model.login_page import LoginPage
from tests.acceptance.page_model.manage_db_page import ManageDBPage
from tests.acceptance.page_model.register_page import RegisterPage
from tests.acceptance.page_model.retweets_page import RetweetsPage
from tests.acceptance.page_model.sentiment_page import SentimentPage
from tests.acceptance.page_model.trend_search_page import TrendSearchPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')  ## path to chromedriver
    page = BasePage(context.driver)
    context.driver.get(page.url)


@given('I am on the register page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = RegisterPage(context.driver)
    context.driver.get(page.url)


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/chromedriver.exe')
    page = LoginPage(context.driver)
    context.driver.get(page.url)




@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url


@then('I am on the register page')
def step_impl(context):
    expected_url = RegisterPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the trend search page')
def step_impl(context):
    expected_url = TrendSearchPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the manage db page')
def step_impl(context):
    expected_url = ManageDBPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the sentiment analysis page')
def step_impl(context):
    expected_url = SentimentPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the common trends page')
def step_impl(context):
    expected_url = CommonTrendsPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am on the popular retweets page')
def step_impl(context):
    expected_url = RetweetsPage(context.driver).url
    assert context.driver.current_url == expected_url