Feature: Create New AirCrafts

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

    @CreateAircraft
    Scenario: Create New AirCraft
        And Click on Tabs Aircraft and Available Aircraft
        And Click on Create New Aircraft Btn
        And Enter all Aircraft Details
        And Upload Seat Schematics file
        And Goto Seat Availability Tab and upload Seat which is less than total number of available Seats
        Then Save Aircraft
        Then Verify its been Create or not

    @CreateAircraftWithFreight @Sanity
    Scenario: Create New AirCraft with Freight Capacity
        And Click on Tabs Aircraft and Available Aircraft
        And Click on Create New Aircraft Btn
        And Enter all Aircraft Details
        And Upload Seat Schematics file
        And Goto Seat Availability Tab and upload Seat which is less than total number of available Seats
        And Click on Freight Tab
        And Select Freight Space Availability to Yes
        And Enter Maximum Payload
        And Fill all the deck details
        And Save the Aircraft with Freight

    @Assign_AirCraft
    Scenario: Assign Aircraft to the Paid Route
        When Click on Aircraft Tabs and then Aircraft Assignment Tabs
        And Click on Assign Action Button
        And Select available AirCraft from Dropdown
        And Click on Assign Button to assign the Aircaft to the Route


    @Change_Unit
    Scenario: Change Units under Aircraft Screen
        And Click on Tabs Aircraft and Available Aircraft
        And Select the Imperical Unit
        And Verify if it has been applied or not
