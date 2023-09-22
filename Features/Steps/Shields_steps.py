from behave import *

from Ship.Shield import Shield

use_step_matcher("parse")


class Ship:
    def __init__(self, shield):
        self.shield = shield

@given("Shield level is at {shieldlevel}")
def step_impl(context, shieldlevel):
    context.shield = Shield(shieldlevel)
    context.ship = Ship(context.shield)

@step('Shield is "raised"')
def step_impl(context):
    context.shield.be_raised()


@when("Ship is hit with a 1000 energy attack")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Ship is hit with a 1000 energy attack')


@then("we expect Shield level to be 0")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then we expect Shield level to be 0')


@step('Shield should be "down"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Shield should be "down"')


@step("no subsystems are damaged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And no subsystems are damaged')