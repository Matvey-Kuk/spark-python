# Cspark-python is a [cisco spark](https://www.ciscospark.com/) library for bots

[![Build](https://travis-ci.org/Matvey-Kuk/cspark-python.svg?branch=master)](https://travis-ci.org/Matvey-Kuk/cspark-python)
[![Downloads](https://img.shields.io/pypi/dm/cspark-python.svg)](https://pypi.python.org/pypi/cspark-python)
[![Version](https://img.shields.io/pypi/v/cspark-python.svg)](https://pypi.python.org/pypi/cspark-python)

### Why?

1. Spark API provides only one mechanism to notify bot about updates: Webhooks.
"Webhooks require that the Cisco Spark Cloud be able to reach your backend over HTTP" 
[(link)](https://developer.ciscospark.com/webhooks-explained.html#auth)
It's not comfortable to develop and test bots on public server so Cspark-python
emulates update mechanism using REST API.
2. Class-based routers and request handlers allow you to use Django-style project 
structure for complex projects.