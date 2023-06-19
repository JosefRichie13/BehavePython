@AutomatedTests
@APIGet

Feature: API Get Scenarios

  Scenario: Get All Products
    Given I make a GET call to the "All products" endpoint
    Then I verify that I get all the products are returned

  Scenario: Get All Brands
    Given I make a GET call to the "All brands" endpoint
    Then I verify that all the brands are returned