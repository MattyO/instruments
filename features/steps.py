import lettuce
import pqaut.client


@lettuce.step(u'Given the app is running')
def given_the_app_is_running(step):
    pass

@lettuce.step(u'Then I can see the heading')
def then_i_can_see_the_heading(step):
    pqaut.client.assert_is_visible('Heading')
@lettuce.step(u'And the heading is 100')
def and_the_heading_is_100(step):
    pqaut.client.assert_is_visible(u'100')
