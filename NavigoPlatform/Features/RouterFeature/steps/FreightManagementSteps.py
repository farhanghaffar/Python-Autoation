import time

from behave import *
from NavigoPlatform.PageObjects.Router.FreightManagementPage import FreightManagementPage
from NavigoPlatform.Configurations import Config

logs = Config.get_logs()


@then(u'Click on Tab Freight Management')
def click_on_tab_freight_purchase(context):
    context.freight_management = FreightManagementPage(context.driver)
    context.freight_management.click_on_freight_management_tab()
    logs.info("Clicked on Freight Management Tab")


@then(u'Verify the Freight Management Tab')
def click_on_tab_freight_management(context):
    verify_tab = context.freight_management.freight_management_tab()
    assert verify_tab


@then(u'Click on edit btn')
def click_on_edit_btn(context):
    context.freight_management.click_on_edit_btn()
    logs.info("Clicked on Edit button")


@then(u'Click on Contact Info btn')
def click_on_contact_info_btn(context):
    context.freight_management.click_on_contact_btn()
    logs.info("Clicked on Contact Info button")


@then(u'Is Contact info visible')
def click_on_contact_info_btn(context):
    context.freight_management.verify_contact_btn()


@when(u'Freight Management records available')
def freight_management_records_available(context):
    verify_tab = context.freight_management.verify_freight_management_tab()
    assert verify_tab


@then(u'Verify the Select dropdown')
def verify_select_dropdown(context):
    element = context.freight_management.verify_select_drop_down()
    assert element


@then(u'logout the old account')
def logout_account(context):
    context.freight_management = FreightManagementPage(context.driver)
    context.freight_management.logout()
    logs.info("Logged out the acocunt")


@then(u'Click on status')
def click_on_status(context):
    context.freight_management.click_on_flight_status()
    logs.info("Clicked on Status button")


@then(u'Verify the Status Popup')
def verify_status_popup(context):
    context.freight_management.verify_status_popup()


@then(u'Click on cancel btn')
def click_on_cancel_btn(context):
    context.freight_management.click_on_cancel_btn()
    logs.info("Clicked on Cancel button")


@then(u'Click on save btn')
def click_on_save_btn(context):
    context.freight_management.click_on_save_btn()
    logs.info("Clicked on Save Button")


@then(u'Get the old status')
def get_old_status(context):
    context.old_status = context.freight_management.get_the_status()
    time.sleep(2)


@then(u'Check the Status Changed or not "{Status}"')
def check_status(context, Status):
    context.new_status = context.freight_management.get_the_status()
    time.sleep(2)
    if Status == "Cancel":
        assert context.old_status == context.new_status
        logs.info(f"{context.new_status} are matched to {context.old_status}")
    if Status == "Save":
        assert context.old_status != context.new_status
        logs.info(f"{context.new_status} are not matched to {context.old_status}")


@then(u'Check the Freight Management Tab')
def verify_freight_management_tab(context):
    assert context.freight_management.verify_freight_management_tab()


@then(u'Click on Tab Freight Purchases')
def click_on_tab_freight_purchase(context):
    context.freight_management = FreightManagementPage(context.driver)
    context.freight_management.click_on_freight_purchase_tab()
    logs.info("Clicked on Tab Freight Purchase")


@then(u'Click on the Purchase new Freight')
def click_on_purchase_new_freight(context):
    context.freight_management.click_on_purchase_btn()
    logs.info("Clicked on Purchase new Freight button")


@then(u'Select Available Flight')
def click_on_select_flight(context):
    context.freight_management.click_on_select_flight()
    context.freight_management.verify_select_available_flight()


@then(u'Verify the Freight Table columns')
def verify_freight_table_columns(context):
    context.freight_management.verify_table_view()


@then(u'verify it is in table format')
def verify_freight_table_view(context):
    context.freight_management.verify_table_view()


@then(u'click on delete btn')
def delete_btn(context):
    context.freight_management.delete_btn()


@then(u'verify pop up appears')
def verify_pop_up(context):
    assert context.freight_management.delete_popup_text()
