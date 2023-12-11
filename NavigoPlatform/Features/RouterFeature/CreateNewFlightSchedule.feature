Feature: Create New Flight Schedules

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

    @CreateNewFlightSchedule @Sanity
    Scenario: Create New Flight Schedule
      And Click on Flight Schedule Tab
      And Click on Create New Flight Schedule Btn
      And Select the suitable Air Route from the dropdown
      And Enter the Suitable Title
      And Select the Available Dates
      And Check if Prices matches or not
      And Click on Next btn
      And Add Purchaser Details
      And Click on Complete Purchase
      And Check for the Confirmation
      And Close the Confirmation Overlay

    @AssignPaidStatus @Sanity
    Scenario: Make Flight Schedule Payment Status Paid
      And Click on Flight Schedule Tab
      Then Click on Action icon
      And Select Flight Status dropdown as "On Time"
      And Select Payment Status as "Paid"
      Then Save the Status
