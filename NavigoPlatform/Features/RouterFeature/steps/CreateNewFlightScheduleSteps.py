from behave import *
from NavigoPlatform.Configurations import Config
from NavigoPlatform.PageObjects.Router.CreateNewFlightSchedulePage import CreateNewFlightSchedulePage

logs = Config.get_logs()


@then(u'Click on Flight Schedule Tab')
def click_on_flight_schedule_tab(context):
    context.NewFlightSchedule = CreateNewFlightSchedulePage(context.driver)
    context.NewFlightSchedule.click_on_flight_schedule_tab()
    logs.info("Clicked on Flight Schedule Tab")


@then(u'Click on Create New Flight Schedule Btn')
def click_on_create_new_flight_schedule_btn(context):
    context.NewFlightSchedule.click_on_create_new_flight_schedule_btn()
    logs.info("Clicked on Create New Flight Schedule Btn")


@then(u'Select the suitable Air Route from the dropdown')
def select_air_route_drop_down(context):
    context.NewFlightSchedule.click_on_air_route_drop_down()
    logs.info("Select the suitable Air Route from the dropdown")


@then(u'Enter the Suitable Title')
def enter_title_for_air_route(context):
    context.NewFlightSchedule.add_title_for_the_air_route()
    logs.info("Entered the Suitable Title")


@then(u'Select the Available Dates')
def select_the_available_dates(context):
    context.NewFlightSchedule.click_on_calendar_nxt_arrow()
    context.NewFlightSchedule.click_on_calendar_date()
    logs.info("Entered the available dates")


@then(u'Check if Prices matches or not')
def check_for_prices(context):
    context.NewFlightSchedule.check_for_total_value()
    logs.info("Total value checked")


@then(u'Click on Next btn')
def click_on_next_btn(context):
    context.NewFlightSchedule.click_on_next()
    logs.info("Clicked on Next btn")


@then(u'Add Purchaser Details')
def add_purchaser_details(context):
    context.NewFlightSchedule.enter_purchaser_details()
    logs.info("Added Purchaser Details")


@then(u'Click on Complete Purchase')
def click_on_complete_purchase(context):
    context.NewFlightSchedule.click_on_complete_purchase()
    logs.info("Clicked on Complete Purchase")


@then(u'Check for the Confirmation')
def check_confirmation(context):
    context.NewFlightSchedule.check_for_confirmation()
    logs.info("Checked for the Confirmation")


@then(u'Close the Confirmation Overlay')
def close_the_dialog(context):
    context.NewFlightSchedule.close_conformation_dialog()
    logs.info("Checked for the Confirmation")


@then(u'Click on Action icon')
def click_on_action_icon(context):
    context.NewFlightSchedule.click_on_action_icon()
    logs.info("Clicked on Action icon")


@then(u'Select Flight Status dropdown as "On Time"')
def select_flight_status(context):
    context.NewFlightSchedule.select_flight_status_drop_down()
    logs.info("Select Flight Status dropdown as 'On Time'")


@then(u'Select Payment Status as "Paid"')
def select_payment_status(context):
    context.NewFlightSchedule.select_payment_status_drop_down()
    logs.info("Selected Payment Status as 'Paid'")


@then(u'Save the Status')
def Save_the_status(context):
    context.NewFlightSchedule.click_on_flight_schedule_save_btn()
    logs.info("Saved the Status")
