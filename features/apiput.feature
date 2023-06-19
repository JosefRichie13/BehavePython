@AutomatedTests
@APIPut

Feature: API Put Scenarios

  Scenario: Put to All Brands
    Given I make a PUT call to the "All brands" endpoint
    Then I verify that the method is not supported