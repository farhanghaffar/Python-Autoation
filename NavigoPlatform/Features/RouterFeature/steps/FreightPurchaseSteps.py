import time

from behave import *
from NavigoPlatform.PageObjects.Router.FreightPurchasePage import FreightPurchasePage
from NavigoPlatform.Configurations import Config

logs = Config.get_logs()


@when(u'Click on Tab Freight Purchase')
def click_on_tab_freight_purchase(context):
    context.freight_purchase = FreightPurchasePage(context.driver)
    context.freight_purchase.click_on_freight_purchase_tab()
    logs.info("Clicked on the Freight Purchase Tab")


@then(u'Create record if it is not available')
def create_record_if_not_available(context):
    context.record = context.freight_purchase.check_records()
    if not context.record:
        context.freight_purchase.purchase_new_freight_btn()
        context.freight_purchase.create_new_freight_purchase()


@then(u'Verify the Flights are available')
def check_the_flights(context):
    context.freight_purchase.purchase_new_freight_btn()
    context.freight_purchase.check_flights()


@then(u'Select the shipment date')
def shipment_date(context):
    context.freight_purchase.purchase_new_freight_btn()
    context.freight_purchase.shipment_date()
    logs.info("Clicked on the Freight Purchase Tab")


@then(u'get the old shipment load')
def get_old_shipment_load(context):
    context.old_weight = context.freight_purchase.get_shipment_load_weight()
    context.old_status = context.freight_purchase.get_shipment_load()
    logs.info(f"{context.old_status} {context.old_weight}")


@then(u'Change the weight unit')
def change_weight_unit(context):
    context.convert_to_imperial_unit = False
    context.convert_to_metric_unit = False
    logs.info(f'{context.old_weight}')
    if "kg" in context.old_weight:
        context.convert_to_imperial_unit = True
    if "lbs" in context.old_weight:
        context.convert_to_metric_unit = True
    if context.convert_to_imperial_unit:
        logs.info("imperial")
        context.freight_purchase.change_to_imperial_unit()
    if context.convert_to_metric_unit:
        logs.info("metric")
        context.freight_purchase.change_to_metric_unit()


@then(u'get the new shipment load')
def get_new_shipment_load(context):
    context.new_status = context.freight_purchase.get_shipment_load()


@then(u'is shipment load changed or not')
def is_shipment_changed(context):
    logs.info(f"{context.old_status} and {context.new_status}")
    assert context.old_status != context.new_status


@then(u'purchase new freight btn')
def purchase_new_freight_btn(context):
    context.freight_purchase.purchase_new_freight_btn()


@then(u'verify the purchase new freight popup')
def verify_purchase_freight_popup(context):
    assert context.freight_purchase.verify_purchase_freight_popup()


@then(u"verify the measurement")
def verify_measurement(context):
    context.freight_purchase.verify_measurement()


@then(u'add the package')
def add_package(context):
    context.freight_purchase.add_package()
    logs.info("Added the package")


@then(u'verify cargo details')
def verify_cargo_details(context):
    context.freight_purchase.verify_cargo_details_valid()


@then(u'click on next flight btn')
def click_on_next_btn(context):
    context.freight_purchase.next_btn()


@then(u'enter the cargo details')
def add_cargo_details(context):
    context.freight_purchase.add_cargo_details()
    logs.info("Entered the cargo details")


@then(u'delete the package')
def delete_package(context):
    context.freight_purchase.delete_package()
    logs.info("Deleted the package")


@then(u'verify package deleted or not')
def verify_delete_package(context):
    context.is_package_available = context.freight_purchase.verify_package_deleted()
    if not context.is_package_available:
        logs.info("Package deleted successfully")
        assert True


@then(u'verify the item added or not')
def verify_item_added(context):
    context.is_package_available = context.freight_purchase.verify_package_deleted()
    if context.is_package_available:
        logs.info("Package Added successfully")
        assert True


@then(u'Check the cargo details')
def cargo_details(context):
    context.is_measurement_valid = context.freight_purchase.verify_measurement_details()
    if context.is_measurement_valid:
        context.is_shipment_type_valid = context.freight_purchase.verify_shipment_type_details()
        if context.is_shipment_type_valid:
            if context.freight_purchase.add_item_visible():
                assert context.freight_purchase.back_btn_visible()
            else:
                context.freight_purchase.screenshot()
                assert False, "Add item button is not available"
        else:
            context.freight_purchase.screenshot()
            assert False, "Shipment Type is not valid"
    else:
        context.freight_purchase.screenshot()
        assert False, "Measurement is not valid"


@then(u'Check the cargo item details')
def cargo_items_details(context):
    if context.freight_purchase.is_measurement_visible():
        if context.freight_purchase.is_weight_visible():
            if context.freight_purchase.is_item_size_visible():
                assert True
            else:
                context.freight_purchase.screenshot()
                assert False, "Item size is not visible"
        else:
            context.freight_purchase.screenshot()
            assert False, "Weight box is not visible"
    else:
        context.freight_purchase.screenshot()
        assert False, "Measurement is not visible"


@then(u'Add item')
def add_item(context):
    context.freight_purchase.add_package()


@then(u'Enter the next item details')
def enter_next_item_details(context):
    context.freight_purchase.add_next_item_details()
    context.freight_purchase.next_btn()


@then(u'calculate weight and items')
def calculate_weight_item(context):
    context.number_of_items, context.calculated_weight = context.freight_purchase.calculate_weight_item()


@then(u'check weight and items')
def check_weight_items(context):
    context.total_items, context.total_weight = context.freight_purchase.get_total_weight_items()
    if context.number_of_items == context.total_items and context.total_weight == context.calculated_weight:
        logs.info("Weight and items Matched successfully")
        assert True
    else:
        context.freight_purchase.screenshot()
        assert False, "Weight and items did not matched"


@then(u'add more then 20 items')
def add_more_20_items(context):
    try:
        for iterate in range(0, 23):
            context.freight_purchase.add_package()
        logs.info("Added the items successfully")
    except:
        context.freight_purchase.screenshot()
        logs.info("Failed to add items")


@then(u'input multiple items data')
def input_multiple(context):
    try:
        context.freight_purchase.input_multiple_records()
        context.freight_purchase.next_btn()
        logs.info("Enter multiple items details successfully")
        assert True
    except:
        context.freight_purchase.screenshot()
        logs.info("Failed to enter multiple items details")
        assert False


@then(u'Select Use Metric Units Weight')
def select_use_metric_unit(context):
    assert context.freight_purchase.select_metric_unit()


@then(u'get the tab names')
def tab_names(context):
    context.tabs_name = context.freight_purchase.get_tab_names()
    logs.info(f"{context.tabs_name}")
    if "Shipment Date" in context.tabs_name and "Cargo Details" in context.tabs_name and \
            "Invoice Summary" in context.tabs_name and "Purchaser" in context.tabs_name \
            and "Terms & Conditions" in context.tabs_name and "Confirmation" in context.tabs_name:
        assert True
    else:
        context.freight_purchase.screenshot()
        logs.info("Tabs names are different")
        assert False


@then(u'view the freights purchase table')
def Freight_purchase_table(context):
    context.check = context.freight_purchase.check_records()
    if context.check:
        logs.info("Freight Purchase Records are visible")
        assert True
    else:
        context.freight_purchase.screenshot()
        logs.info("Freight Purchase Records are not visible")
        assert False


@then(u'Verify Metric unit')
def metric_unit(context):
    assert context.freight_purchase.verify_metric_unit()


@then(u'Freight Purchase complete table with records')
def verify_table_and_records(context):
    context.air_route_column = context.freight_purchase.verify_airroute_column()
    if len(context.air_route_column.split('-')) == 2:
        context.flight_schedule_column = context.freight_purchase.verify_flight_schedule_column()
        if len(context.flight_schedule_column.split(',')) == 3:
            context.date_column = context.freight_purchase.verify_date_column()
            if len(context.date_column.split("-")) == 3:
                if context.freight_purchase.verify_flight_status_column():
                    if context.freight_purchase.verify_aircraft_column():
                        if context.freight_purchase.verify_weight_column():
                            if context.freight_purchase.verify_shipment_type_column():
                                if context.freight_purchase.verify_freight_status_column():
                                    if context.freight_purchase.verify_invoice_column():
                                        assert True
                                    else:
                                        context.freight_purchase.screenshot()
                                        logs.info("Freight Purchase Invoice are invalid")
                                        assert False
                                else:
                                    context.freight_purchase.screenshot()
                                    logs.info("Freight Purchase Freight status are invalid")
                                    assert False
                            else:
                                context.freight_purchase.screenshot()
                                logs.info("Freight Purchase Shipment items are invalid")
                                assert False
                        else:
                            context.freight_purchase.screenshot()
                            logs.info("Freight Purchase Weight are invalid")
                            assert False
                    else:
                        context.freight_purchase.screenshot()
                        logs.info("Freight Purchase Air Crafts are invalid")
                        assert False
                else:
                    context.freight_purchase.screenshot()
                    logs.info("Freight Purchase Flights status are invalid")
                    assert False
            else:
                context.freight_purchase.screenshot()
                logs.info("Freight Purchase Dates are invalid")
                assert False
        else:
            context.freight_purchase.screenshot()
            logs.info("Freight Purchase Flight Schedule are invalid")
            assert False
    else:
        context.freight_purchase.screenshot()
        logs.info("Freight Purchase Air Router are invalid")
        assert False


