Feature: Test that forms work correctly


  Scenario: Signup page registers user
    Given I am on the register page
    When I enter "tester" in the "username" field
    And I enter "tester@gmail.com" in the "email" field
    And I enter "12341234" in the "password" field
    And I press the submit button
    Then I am on the login page


  Scenario: Login page login user
    Given I am on the login page
    When I enter "tester" in the "username" login field
    And I enter "12341234" in the "password" login field
    And I press the submit button
    Then I am on the homepage


