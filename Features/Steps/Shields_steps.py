from behave import *
import unittest

from Ship.Shield import Shield

use_step_matcher("parse")


class Ship:
    def __init__(self, shield):
        self.shield = shield

    def attacked(self, attack_strength):
        pass

@given("Shield level is at {shieldlevel}")
def step_impl(context, shieldlevel):
    context.shield = Shield(shieldlevel)
    context.ship = Ship(context.shield)

@step('Shield is "raised"')
def step_impl(context):
    context.shield.be_raised()

@when("Ship is hit with a {attack_strength} energy attack")
def step_impl(context, attack_strength):
    context.ship.attacked(attack_strength)

@then("we expect Shield level to be {expected_shield_level}")
def step_impl(context, expected_shield_level):
    t = unittest.TestCase()
    t.assertEquals(expected_shield_level, context.shield.check_level())

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