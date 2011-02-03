Python
------

Writing a python API for your widget is very simple too.

You just create a subclass of :mod:`cream.contrib.api.API` and the methods of this class can then be accessed from the javascript.

But you certainly don't want every method to be accessible, so you have to decorate these methods with ``@api.expose`` and they can be used from the JS.

This is actually everything you have to know about the API, so lets have a look on the whole code:

.. code-block:: python

    # modules needed to download and parse the data
    import urllib
    from contextlib import closing
    from lxml.etree import parse

    # the api for the widget
    from cream.contrib.melange import api

    # the url which will be queried to get the weather data
    URL = 'http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query={location}'

    # This will register the API-class as `widget.api.tutorial`
    # accessable from your JavaScript code.
    @api.register('tutorial')
    class Tutorial(api.API):

        def __init__(self):
            api.API.__init__(self)

        # This exposes the method which can be called in your JavaScript code as
        # `widget.api.tutorial.get_temperature(callback(temperature);`
        @api.expose
        def get_temperature(self):
            location = 'Berlin, Germany'
            url = URL.format(location=location)
            with closing(urllib.urlopen(url)) as xml:
                weather_data = parse(xml)

            return weather_data.find('temp_c').text

We use a hardcoded location right now, but in the :doc:`config section <config>` I'll show you something better.

In the next section we'll glue python and javascript together: :doc:`Accessing python from javascript <python-js>`
