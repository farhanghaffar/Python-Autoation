import time

from behave import *
from NavigoPlatform.PageObjects.Router.FlightScheduleListPage import FlightScheduleListPage
from NavigoPlatform.Configurations import Config


logs = Config.get_logs()

@then(u'Click on Tabs Flight Schedule List')
def click_on_tabs_flight_schedule_list(Context):
    Context.FlightSchedulePage = FlightScheduleListPage(Context.driver)
    Context.FlightSchedulePage.click_on_flight_schedules_tab()
    logs.info("Clicked on Flight Schedule List Tab")


@then(u'Create the New Flight Schedule')
def create_the_new_flight_schedule(Context):
    Context.FlightSchedulePage.click_on_create_new_flight_schedule_btn()
    logs.info("Clicked on New Flight Schedule button")
    Context.FlightSchedulePage.click_on_drop_menu_btn()
    logs.info("Clicked on drop down")
    Context.FlightSchedulePage.input_title()
    logs.info("Input Title")
    Context.FlightSchedulePage.click_on_swipe_right_btn()
    logs.info("Swipe Right")
    Context.FlightSchedulePage.click_on_date()
    logs.info("Select the date")
    Context.FlightSchedulePage.click_on_next_btn()
    logs.info("Next Button")
    Context.FlightSchedulePage.input_purchaser()
    logs.info("Input Purchase")


@then(u'Verify Flight Created or not')
def verify_flight_created(Context):
    Context.FlightSchedulePage.verify_flight_created()

