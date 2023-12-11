import os
from behave import *
from NavigoPlatform.Configurations.Config import TestConfig
from NavigoPlatform.Configurations import Config
from NavigoPlatform.PageObjects.Router.LoginPage import LoginPage
from NavigoPlatform.PageObjects.Router.DashboardPage import DashboardPage

logs = Config.get_logs()


@given(u'Launch the browser')
def launch_browser(context):
    # Config.headless_chrome_browser(context)
    # Config.chrome_browser(context)
    # this is the logoic to access whether we want to execute chrome with non-headless or headless by running first
    # By Default it runs in headless and running export HEADLESS=false before behave cmd will run in non-headless mode
    headless_mode = os.environ.get("HEADLESS", "false").lower() == "true"
    context.driver = Config.chrome_with_param_browser(context, headless_mode)
    context.driver.get(TestConfig.URL)
    logs.info("Launch the Chrome browser")


@when(u'Open the router app https://qa2-platform.navigo.global/apps/router/')
def open_login_page(context):
    logs.info("Opening login page")
    context.loginPage = LoginPage(context.driver)
    logs.info("Opened the router app login page in QA3 ENV")


@then(u'The login portal has been opened')
def validate_login_page(context):
    try:
        context.loginPage.validate_title()
        logs.info("Validating the title page")
    except:
        assert False, "Test is failed in validate login page title"


@then(u'Provide valid username and password')
def enter_login_creds(context):
    context.loginPage.enter_login_credentials()
    logs.info("Login creds are entered")


@then(u'click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
        logs.info("Login button is clicked")
    except:
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    context.DashboardPage = DashboardPage(context.driver)
    context.DashboardPage.validate_router_pageLoaded()
    logs.info("Login is successful and dashboard is opened")


@then(u'Provide the username "{User}" and password "{Pwd}"')
def validate_multiple_login_creds(context, User, Pwd):
    try:
        context.loginPage.enter_username(User)
        context.loginPage.enter_password(Pwd)
    except:
        logs.critical("Login is Failed")
        assert False, "Test is failed in validating invalid login"


@then(u'Login is failed and invalid credential error is displayed')
def validate_invalid_login(context):
    try:
        context.loginPage.validate_invalid_creds()
        logs.critical("Login is Failed")
    except:
        assert False, "Test is failed in validating invalid login"


@then(u'Provide the password "{Pwd}"')
def enter_login_creds(context, Pwd):
    try:
        context.loginPage.enter_password(Pwd)
    except:
        assert False, "Test is failed in enter password"


#
# @then(u'Provide the username "{user}"')
# def enter_login_creds(context, user):
#     try:
#         context.loginPage.enter_username(user)
#     except:
#         context.driver.close()
#         assert False, "Test is failed in enter username"
#
#
@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        context.loginPage.validate_empty_username()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty username"

#
#
# @then(u'Login is failed and empty password error is displayed')
# def validate_empty_passeword(context):
#     try:
#         context.loginPage.validateEmptyPassword()
#     except:
#         context.driver.close()
#         assert False, "Test is failed in validate empty password"


@then(u'Close the browser')
def close_browser(context):
    context.driver.close()
