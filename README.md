# Cspark-python [![Build](https://travis-ci.org/Matvey-Kuk/cspark-python.svg?branch=master)](https://travis-ci.org/Matvey-Kuk/cspark-python) [![Downloads](https://img.shields.io/pypi/dm/cspark-python.svg)](https://pypi.python.org/pypi/cspark-python) [![Version](https://img.shields.io/pypi/v/cspark-python.svg)](https://pypi.python.org/pypi/cspark-python) [![Updates](https://pyup.io/repos/github/matvey-kuk/cspark-python/shield.svg)](https://pyup.io/repos/github/matvey-kuk/cspark-python/) [![Python 3](https://pyup.io/repos/github/matvey-kuk/cspark-python/python-3-shield.svg)](https://pyup.io/repos/github/matvey-kuk/cspark-python/) [![codecov](https://codecov.io/gh/Matvey-Kuk/cspark-python/branch/master/graph/badge.svg)](https://codecov.io/gh/Matvey-Kuk/cspark-python)

Cspark-python is a [cisco spark](https://www.ciscospark.com/) library for simple or complex bots.


### Why Cspark-python?

1. Spark API provides only one mechanism to notify bot about updates: Webhooks.
"Webhooks require that the Cisco Spark Cloud be able to reach your backend over HTTP" 
[(link)](https://developer.ciscospark.com/webhooks-explained.html#auth)
It's not comfortable to develop and test bots on public server so Cspark-python
emulates update mechanism using REST API.
2. Class-based routers and request handlers allow you to use Django-style project 
structure for complex projects.
3. Event-based callbacks allows you to build prototype fast.

### Howto:

1. Install with PIP:
```
pip install cspark-python
```

2. Then go to developer website, [create new bot](https://developer.ciscospark.com/apps.html) and achieve **Access Token**. 
Be careful and don't copy your own **Access Token** it will cause funny situation.  

> If you stacked with icon uploading mechanism (as I always do), you can use random photo of a cat: https://pbs.twimg.com/profile_images/562466745340817408/_nIu8KHX.jpeg 

3. Use examples to start your first bot. Don't forget to change **Access Token**.

> Currently only 0_simple_echo.py example works, others are concepts.

Keywords: Cisco Spark team use term "SDK" for libraries which use their API... Ok. That's **Cisco Spark Python SDK**.   