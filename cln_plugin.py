#!/usr/bin/env python3
from pyln.client import Plugin
import time

plugin = Plugin()


def hello(plugin, name="world"):
    """This is the documentation string for the hello-function.

    It gets reported as the description when registering the function
    as a method with `lightningd`.

    """
    greeting = plugin.get_option('greeting')
    s = '{} {}'.format(greeting, name)
    plugin.log(s)
    return s


def bye(plugin, name, **kwargs):
    """This method requires {name} to be set by the caller !"""
    return "Bye {}".format(name)


def init(options, configuration, plugin, **kwargs):
    plugin.log("Plugin helloworld.py initialized")


def on_connect(plugin, id, address, **kwargs):
    plugin.log("Received connect event for peer {}".format(id))


def on_disconnect(plugin, id, **kwargs):
    plugin.log("Received disconnect event for peer {}".format(id))


def on_payment(plugin, invoice_payment, **kwargs):
    plugin.log("Received invoice_payment event for label {label}, preimage {preimage},"
               " and amount of {msat}".format(**invoice_payment))


def on_invoice_creation(plugin, invoice_creation, **kwargs):
    plugin.log("Received invoice_creation event for label {label}, preimage {preimage},"
               " and amount of {msat}".format(**invoice_creation))


def on_htlc_accepted(onion, htlc, plugin, **kwargs):
    plugin.log('on_htlc_accepted called')
    time.sleep(20)
    return {'result': 'continue'}


plugin.add_option('greeting', 'Hello', 'The greeting I should use.')
plugin.run()