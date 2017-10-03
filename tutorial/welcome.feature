Feature: Welcome page

  As a user
  I want to navigate to the welcome page
  So that I can purchase lotsss of stuff

  Scenario: Without Login
    Given I am on the home page
    When I click on the welcome link
    Then I should see the welcome page
