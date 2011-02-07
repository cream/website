Widget Configuration
--------------------

All widgets have a nice integrated configuration, which can be accessed by right-clicking on the widget and selecting *Configure*.
You can add your own field there and it will be integrated in the dialog and the can easily be changed there.


All there is to do, is to create a file *scheme.xml* in ``widget_root/configuration``

Remember the hardcoded location in our python backend? Time to move it to the config:

.. code-block:: xml

    <configuration>
        <location label="Location" type="char">Berlin, Germany</location>
    </configuration>

.. seealso::

   Module :mod:`cream.config`

Now lets see how we can use this data:

Access from python
------------------

Your widget class has the configuration saved in ``self.config``.
Fields have read and write access.

In our example we can get the location like this:

.. code-block:: python

    def get_temperature(self):
        location = self.config.location
        url = URL.format(location=location)
        with closing(urllib.urlopen(url)) as xml:
            weather_data = parse(xml)

        return weather_data.find('temp_c').text


Access from javascript
----------------------

You can also get and set the config values from javascript like this:

.. code-block:: javascript

    var location = widget.config.get('location'); //get the value

    widget.config.set('location', new_value); // set `location` to new_value
