Feature: Freight Purchase

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

    Scenario: Create Freight if not available
        When Click on Tab Freight Purchase
        Then Create record if it is not available
        Then Close the browser

    Scenario: Check Flight are available
        When Click on Tab Freight Purchase
        Then Verify the Flights are available
        Then Close the browser

    Scenario: Check the cargo measurement
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then verify the measurement
        Then Close the browser

    Scenario: Check the cargo details
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then enter the cargo details
        Then click on next flight btn
        Then verify cargo details
        Then Close the browser

    Scenario: Delete the package
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then enter the cargo details
        Then delete the package
        Then verify package deleted or not
        Then Close the browser

    Scenario: Add the package item
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then enter the cargo details
        Then delete the package
        Then add the package
        Then verify the item added or not
        Then Close the browser

    Scenario: Verify Freight Purchase Screen Units Dropdown
        When Click on Tab Freight Purchase
        Then get the old shipment load
        Then Change the weight unit
        Then get the new shipment load
        Then is shipment load changed or not
        Then Close the browser

    Scenario: Purchase New Freight Button behavior
        When Click on Tab Freight Purchase
        Then purchase new freight btn
        Then verify the purchase new freight popup
        Then Close the browser

    Scenario: Cargo Details - Cargo Details section
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then Check the cargo details
        Then Close the browser

    Scenario: Cargo Details - Cargo  Items Details
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then Check the cargo item details
        Then Close the browser

    Scenario: Cargo List Items number and weights
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then enter the cargo details
        Then Add item
        Then Enter the next item details
        Then calculate weight and items
        Then check weight and items
        Then Close the browser

    Scenario: Cargo List Items- Pagination
        When Click on Tab Freight Purchase
        Then Select the shipment date
        Then enter the cargo details
        Then add more then 20 items
        Then input multiple items data
        Then Close the browser

    Scenario: Select the use metric units
        When Click on Tab Freight Purchase
        Then Select Use Metric Units Weight
        Then Close the browser

    Scenario: Freight Purchase Tabs
        When Click on Tab Freight Purchase
        Then purchase new freight btn
        Then get the tab names
        Then Close the browser

    Scenario: view the listing of freight purchasers
        When Click on Tab Freight Purchase
        Then view the freights purchase table
        Then Close the browser

    Scenario: Freight Purchase Flight are available
        When Click on Tab Freight Purchase
        Then Verify the Flights are available
        Then Close the browser

    Scenario: Verify the TAB Details
        When Click on Tab Freight Purchase
        Then Verify Metric unit
        Then Freight Purchase complete table with records
        Then Close the browser



