@AutomatedTests
@APIDelete

Feature: API Delete Scenarios

  Scenario: Delete to Verify login
    Given I make a DELETE call to the "Verify login" endpoint
    Then I verify that the method is not supported