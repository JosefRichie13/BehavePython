@AutomatedTests
@ProductCheckout

Feature: Product Checkout Scenarios

  @cleanappstate
  Scenario: I can buy a product and checkout
    Given I open the web page
    When I login as a "standard" user
    And I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Onesie" to the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    And I confirm my order
    Then I should see "Thank you for your order!" after the order is placed

  @cleanappstate
  Scenario: Tax is calculated at 8%
    Given I open the web page
    When I login as a "standard" user
    And I add "Test.allTheThings() T-Shirt (Red)" to the cart
    And I add "Sauce Labs Onesie" to the cart
    And I add "Sauce Labs Fleece Jacket" to the cart
    And I add "Sauce Labs Bolt T-Shirt" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    And I add "Sauce Labs Backpack" to the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    Then I confirm that the tax is calculated at 8 percent

  @cleanappstate
  Scenario: Total price decreases when a product is removed from the cart
    Given I open the web page
    When I login as a "standard" user
    And I add "Sauce Labs Backpack" to the cart
    And I add "Sauce Labs Bike Light" to the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    And I get the total price in the cart
    And I go to the main page
    And I remove "Sauce Labs Bike Light" from the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    Then I confirm that the price is "decreased"

  @cleanappstate
  Scenario: Total price increases when a product is added to the cart
    Given I open the web page
    When I login as a "standard" user
    And I add "Sauce Labs Backpack" to the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    And I get the total price in the cart
    And I go to the main page
    And I add "Sauce Labs Bike Light" to the cart
    And I click on the cart
    And I checkout
    And I enter my information to continue
      | FirstName | LastName | Zip   |
      | John      | Doe      | 37188 |
    Then I confirm that the price is "increased"