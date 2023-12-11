from behave import *
from NavigoPlatform.Configurations import Config
from NavigoPlatform.PageObjects.Router.LoginPage import LoginPage
from NavigoPlatform.PageObjects.Router.AirRoutesPage import AirRoutesPage

logs = Config.get_logs()


@then(u'click on Create New Route button')
def click_on_create_new_btn(context):
    try:
        context.loginPage = LoginPage(context.driver)
        context.airRoutePage = AirRoutesPage(context.driver)
        context.airRoutePage.click_on_create_new_route_btn()
        logs.info("clicked on Create New btn")
    except:
        assert False, "Not able to click on Create New button"


@then(u'Enter all the details of Origin Airport')
def origin_airport_details(context):
    context.airRoutePage.fill_all_origin_details()
    logs.info("filling origin Details")


@then(u'Enter all the details of Destination Airport')
def destination_airport_details(context):
    context.airRoutePage.fill_all_destination_details()
    logs.info("filling Destination Details")


@then(u'Enter the pricing details')
def enter_price_detaila(context):
    context.airRoutePage.enter_price_details()
    logs.info("Entered Pricing Details")


@then(u'Click on Save Btn to create new AirRoute')
def create_new_air_route(context):
    context.airRoutePage.click_on_create_air_route_btn()
    logs.info("Created NEw Air Route")


@then(u'Delete the AirRoute')
def delete_air_route(context):
    deleted_route_name = context.airRoutePage.click_on_delete_icon()
    logs.info("Deleted the AirRoute. AirRoute name is mentioned below: ")
    logs.info(deleted_route_name)
