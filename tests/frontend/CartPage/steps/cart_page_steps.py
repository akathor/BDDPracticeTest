from behave import then, when, given
from BDDCommon.CommonConfigs.locatorsconfig import CART_PAGE_LOCATORS
from BDDCommon.CommonFuncs import webcommon

import time

@when("I select 'Free shipping' option")
def i_select_free_shipping_option(context):
    """

    """

    free_ship = CART_PAGE_LOCATORS['free_shipping_radio']
    webcommon.click(context, free_ship['type'], free_ship['locator'])

    webcommon.assert_radio_is_selected(context, free_ship['type'], free_ship['locator'])


@when("I click on 'Proceed to checkout' button in the cart page")
def i_click_on_proceed_to_checkout_button_in_the_cart_page(context):
    """

    """
    proceed_button = CART_PAGE_LOCATORS['proceed_to_checkout_btn']

    max_try = 3
    try_count = 0
    while try_count < max_try:
        try:
            webcommon.click(context, proceed_button['type'], proceed_button['locator'])
            break
        except Exception as e:
            try_count += 1
            print(f"Failed to click on 'Proceed to checkout' Retry number: {try_count}")
    else:
        raise Exception(f"Failed to click on 'Proceed to checkout' after retrying '{max_try}' times.")


