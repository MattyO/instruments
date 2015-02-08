import lettuce
import pqaut.client
from lettuce import *
import time

@lettuce.step(u'Given the app is running')
def given_the_app_is_running(step):
    pass

@lettuce.step(u'Then I can see the speed')
def then_i_can_see_the_heading(step):
    pqaut.client.assert_is_visible('Speed')

@lettuce.step(u'And the speed is 0')
def the_heading_is_100(step):
    pqaut.client.assert_is_visible(u'0')

@step(u'And my position is 81.6697 W 41.4822 N')
def and_my_position_is_81_23_w_41_123_n(step):
    lettuce.world.qtapp.call.change_position({'lat': 41.123, 'lng':-81.23})

@step(u'And I press the GOTO button')
def and_i_press_the_goto_button(step):
    pqaut.client.tap("goto")

@step(u'And I enter the new mark')
def and_i_enter_the_new_mark(step):
    if step.hashes > 0:
        new_mark = step.hashes[0]
        pqaut.client.input("lat_text", new_mark['latatude'])
        pqaut.client.input("lng_text", new_mark['longitude'])

@step(u'And I press Submit')
def and_i_press_group1(step):
    pqaut.client.tap("Submit")
    time.sleep(2)

@step(u'Then I see the bearing ([0-9]+)')
def then_i_see_the_bearing_234(step, bearing):
    pqaut.client.assert_is_visible(bearing)

