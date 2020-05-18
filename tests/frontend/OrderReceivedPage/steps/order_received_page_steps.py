from behave import then, when, given
from BDDCommon.CommonConfigs.locatorsconfig import ORDER_RECEIVED_LOCATORS
from BDDCommon.CommonFuncs import webcommon

@then("order received page should load with correct data")
def order_received_page_should_load_with_correct_data(context):

    context.execute_steps("""
        then Order received heading should be displayed
        then Thank you message should be displayed
    """)



@then("Order received heading should be displayed")
def order_received_heading_should_be_displayed(context):

    header_locator = ORDER_RECEIVED_LOCATORS['page_header']
    webcommon.element_contains_text(context, 'Order received', header_locator['type'], header_locator['locator'])

@then("Thank you message should be displayed")
def thank_you_message_should_be_displayed(context):

    header_locator = ORDER_RECEIVED_LOCATORS['page_header']
    webcommon.element_contains_text(context, 'Order received', header_locator['type'], header_locator['locator'])
