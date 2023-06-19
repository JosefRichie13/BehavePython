@AutomatedTests
@APIPost

Feature: API Post Scenarios

  Scenario: Post to All Products
    Given I make a POST call to the "All products" endpoint
    Then I verify that the method is not supported

  Scenario: Post to Search Product
    Given I make a POST call to the "Search product" endpoint
      | Product         |
      | Fancy Green Top |
    Then I verify if I get the correct search result with "Fancy Green Top"

  Scenario: Post to Search Product without search parameter
    Given I make a POST call to the "Search product no param" endpoint
      | Product |
      | Blue    |
    Then I verify that I get a Bad request response

  Scenario: Post to Verify login without email parameter
    Given I make a POST call to the "Login no email" endpoint
    Then I verify that I get a Bad request response