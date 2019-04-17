Feature: Test navigation between pages

  Scenario: Home can go to Login
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log In" dropdown link
    Then I am on the login page

  Scenario: Home can go to Logout
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log Out" dropdown link
    Then I am on the login page

  Scenario: Home can go to Register
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Sign In" dropdown link
    Then I am on the register page


  Scenario: Home can go to Trend Search
    Given I am on the homepage
    Given I wait for the page to load
    When I click on the "TRENDS" link
    Then I am on the trend search page

  Scenario: Home can go to Manage DB
    Given I am on the homepage
    Given I wait for the page to load
    When I click on the "MANAGE" link
    Then I am on the manage db page

  Scenario: Home can go to Sentiment Analysis
    Given I am on the homepage
    Given I wait for the page to load
    When I click on the "ANALYSIS" link
    Then I am on the sentiment analysis page

  Scenario: Home can go to Tale of Two Cities
    Given I am on the homepage
    Given I wait for the page to load
    When I click on the "COMMON" link
    Then I am on the common trends page

  Scenario: Home can go to Popular Retweets
    Given I am on the homepage
    Given I wait for the page to load
    When I click on the "RETWEETS" link
    Then I am on the popular retweets page
