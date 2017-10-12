from behave import *
use_step_matcher('re')

@given('I open the url "([^"]*)?"')
def open_url(context, url):
    context.behave_driver.open_url(url)


@given('the element "([^"]*)?" is( not)* visible')
def element_visible(context, negative, element):
    visible = context.behave_driver.element_visible(element)
    if negative:
        assert not visible
    else:
        assert visible


@given('the element "([^"]*)?" is( not)* enabled')
def element_enabled(context, element, negative):
    enabled = context.behave_driver.element_enabled(element)
    if negative:
        assert not enabled
    else:
        assert enabled


@given('the element "([^"]*)?" is( not)* selected')
def element_selected(context, element, negative):
    selected = context.behave_driver.element_selected(element)
    if negative:
        assert not selected
    else:
        assert selected


@given('the checkbox "([^"]*)?" is( not)* checked')
def element_checked(context, element, negative):
    # should this check that the element is, in fact, a checkbox?
    checked = context.behave_driver.element_selected(element)
    if negative:
        assert not checked
    else:
        assert checked


@given('there is (an|no) element "([^"]*)?" on the page')
def element_exists(context, an_no, element):
    negative = an_no == 'no'
    exists = context.behave_driver.element_exists(element)
    if negative:
        assert not exists
    else:
        assert exists


@given('the title is( not)* "([^"]*)?"')
def title(context, negative, value):
    if negative:
        assert context.behave_driver.title != value
    else:
        assert context.behave_driver.title == value


@given('the element "([^"]*)?" contains( not)* the same text as element "([^"]*)?"')
def elements_same_text(context, first_element, negative, second_element):
    first_elem_text = context.behave_driver.get_element_text(first_element)
    second_elem_text = context.behave_driver.get_element_text(second_element)
    same =  first_elem_text == second_elem_text
    if negative:
        assert not same
    else:
        assert same


@given('the element "([^"]*)?"( not)* matches the text "([^"]*)?"')
def element_matches_text(context, element, negative, text):
    matches = context.behave_driver


@given('the element "([^"]*)?"( not)* contains the text "([^"]*)?"')
def step_impl(context, element, negative, text):
    pass


@given('the element "([^"]*)?"( not)* contains any text')
def step_impl(context, element, negative):
    pass


@given('the element "([^"]*)?" is( not)* empty')
def step_impl(context, element, negative):
    pass


@given('the page url is( not)* "([^"]*)?"')
def step_impl(context, negative, value):
    page_url = context.behave_driver.current_url
    if negative:
        assert not page_url == value
    else:
        assert page_url == value


@given('the( css)* attribute "([^"]*)?" from element "([^"]*)?" is( not)* "([^"]*)?"')
def step_impl(context, is_css, attr, element, negative, value):
    pass


@given('the cookie "([^"]*)?" contains( not)* the value "([^"]*)?"')
def step_impl(context, cookie_key, negative, value):
    pass


@given('the cookie "([^"]*)?" does( not)* exist')
def step_impl(context, cookie_key, negative):
    pass


@given('the element "([^"]*)?" is( not)* ([\d]+)px (broad|tall)')
def step_impl(context, element, negative, pixels, axis):
    pass


@given('the element "([^"]*)?" is( not)* positioned at ([\d]+)px on the (x|y) axis')
def step_impl(context, element, negative, pos, axis):
    pass


@given('I have a screen that is ([\d]+) by ([\d]+) pixels')
def step_impl(context, x, y):
    pass


@given('I have closed all but the first (window|tab)')
def step_impl(context, window_or_tab):
    pass


@given('a (alertbox|confirmbox|prompt) is( not)* opened')
def step_impl(context, modal, negative):
    pass
