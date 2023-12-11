from behave import *
from NavigoPlatform.Configurations import Config
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.PageObjects.Router.AirRoutesPage import AirRoutesPage
from NavigoPlatform.PageObjects.Router.LoginPage import LoginPage
from NavigoPlatform.PageObjects.Router.CreateAircraftPage import CreateAirCraftPage

logs = Config.get_logs()


@then(u'Click on Tabs Aircraft and Available Aircraft')
def click_onTab_Aircraft_and_Available_Aircrafts(context):
    context.AirCraftPage = CreateAirCraftPage(context.driver)
    context.AirCraftPage.click_On_Aircraft_Tab()
    context.AirCraftPage.click_On_Available_Aircraft_Tab()
    logs.info("clicked on Tabs Aircraft")


@when(u'Click on Tabs Aircraft and Available Aircraft')
def click_onTab_Aircraft_and_Available_Aircrafts(context):
    context.AirCraftPage = CreateAirCraftPage(context.driver)
    context.AirCraftPage.click_On_Aircraft_Tab()
    context.AirCraftPage.click_On_Available_Aircraft_Tab()
    logs.info("clicked on Tabs Aircraft")


@then(u'click on Create New Aircraft Btn')
def click_OnCreate_NewAircraft_btn(context):
    context.AirCraftPage.click_On_Create_New_Aircraft_Btn()
    logs.info("clicked on Create New Aircraft Btn")


@then(u'Enter all Aircraft Details')
def fill_aircraft_data(context):
    context.AirCraftPage.fill_aircraft_details()
    logs.info("Filled all the details of the aircraft")


@then(u'Upload Seat Schematics file')
def upload_seat_schematics_file(context):
    context.AirCraftPage.upload_seat_schematics()
    logs.info("Uploaded the Seat Schematics")


@then(u'Goto Seat Availability Tab and upload Seat which is less than total number of available Seats')
def upload_seats_file(context):
    context.AirCraftPage.upload_seats()
    logs.info("Uploaded the Seats txt file")


@then(u'Save Aircraft')
def save_aircraft_btn(context):
    context.AirCraftPage.click_On_Save_Aircraft()
    logs.info("clicked on the Save Btn")


@then(u'Verify its been Create or not')
def verify_created_aircraft(context):
    context.AirCraftPage.verify_created_aircraft()
    logs.info("Verified that the aircraft has created")


@then(u'Click on Freight Tab')
def click_freight_tab(context):
    context.AirCraftPage.click_on_freight_tab()
    logs.info("Click on Freight Tab")


@then(u'Select Freight Space Availability to Yes')
def select_space_freight_availability(context):
    context.AirCraftPage.select_freight_space_available()
    logs.info("Selected YES from space available dropdown")


@then(u'Enter Maximum Payload')
def enter_max_payload_cap(context):
    context.AirCraftPage.add_max_payload_cap()
    logs.info("Entered Max payload")


@then(u'Fill all the deck details')
def add_all_deck_details(context):
    context.AirCraftPage.enable_main_deck_toggle()
    logs.info("Enabled main deck toggle btn")
    context.AirCraftPage.add_overhead_bin_box_dimensions()
    logs.info("Added overhead bin box dimensions")
    context.AirCraftPage.enable_lower_deck_forward_toggle()
    logs.info("Enabled lower deck forward btn")
    context.AirCraftPage.add_lower_deck_forward_details()
    logs.info("Added lower deck forward details")
    context.AirCraftPage.enable_lower_deck_aft_toggle()
    logs.info("Enabled lower deck aft btn")
    context.AirCraftPage.add_lower_deck_aft_details()
    logs.info("Added lower deck aft details")


@then(u'Save the Aircraft with Freight')
def save_aircraft_with_freight(context):
    context.AirCraftPage.save_aircraft_freight()
    logs.info("Clicked on Save button to Save the Aircraft with Freight Cap")


@when(u'Click on Aircraft Tabs and then Aircraft Assignment Tabs')
def click_on_aircrafts_and_assignment_tabs(context):
    context.AirCraftPage = CreateAirCraftPage(context.driver)
    context.AirCraftPage.click_On_Aircraft_Tab()
    logs.info("Clicked on Tabs Aircraft")
    context.AirCraftPage.click_on_aircraft_assignment_tab()
    logs.info("Clicked on Aircraft Assignment Tab")


@when(u'Click on Assign Action Button')
def get_assign_action_btn(context):
    context.AirCraftPage.click_on_assign_action_btn()
    logs.info('Clicked on Assign Action Button')


@when(u'Select available AirCraft from Dropdown')
def get_air_route(context):
    context.AirCraftPage.select_available_air_craft_from_dropdown()
    logs.info('Selected available AirRoute from Dropdown')


@when(u'Click on Assign Button to assign the Aircaft to the Route')
def assign_aircraft_to_the_route(context):
    context.AirCraftPage.click_on_assign_save_btn()
    logs.info('Clicked on Assign Button')


@when(u'Select the Imperical Unit')
def select_imperical_unit(context):
    context.AirCraftPage.change_the_aircraft_metric_unit()
    logs.info('Clicked on Unit changed dropdown')


@when(u'Verify if it has been applied or not')
def check_unit_change(context):
    context.AirCraftPage.verify_metric_unit_change()
    logs.info('Verified Unit Change')
