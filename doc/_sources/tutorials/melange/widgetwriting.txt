Melange: Widget Writing Guide
=============================

Introduction
------------

Writing widgets for melange is really easy. The UI is simply a renderd html-page which can be extended by javascript and python.

In this tutorial we will create a little widget which displays the current time.

Basic Setup
-----------

At first we will create some files in the widgets basedirectory:
    * *manifest.xml*
        Here all the basic information about the widget is located
    * *__init__.py*
        This is the widgets python-backend
    * *skins/default/index.html*
        This is the html-file which is then renderd to the desktop
    * *skins/default/manifest.xml*
        Here some basic information about the skin is located

Manifests
---------

Every widget has to have a *manifest.xml* file in its rootdirectory. It looks like this:

.. code-block:: html

    <?xml version="1.0" ?>
    <manifest namespace='org.cream.melange' version="1.0">
        <component name="Digital-clock Widget" id=".digital-clockWidget" version="1.0" type=".Widget">
            <license title="GPL" version="3+"/>
            <description lang="en" content="A nice little clock widget" />
            <author name="Your Name" type="developer" />
        </component>
    </manifest>

There has to be a *manifest.xml* in every skindirectory too, so let us add this to *skins/default/manifest.xml*:

.. code-block:: html

    <?xml version="1.0" ?>
    <manifest namespace='org.cream.melange' version="1.0">
        <component name="Default" id=".digitalclock-widget.DefaultSkin" version="1.0" type=".Skin">
            <license title="GPL" version="3+" />
            <description lang="en" content="A default skin for the Digital-Clock widget." />
            <author name="Your Name" type="developer" />
        </component>
    </manifest>

For further information on the manifests please consult the documentation of :mod:`cream.manifest`.

Python backend
--------------

With melange it is very easy to interact between python and javascript so this gives us the possibility to do complex tasks within python and hand the result over to javascript.

In order to do so, we have to import the API from :mod:`cream.contrib.melange` and create a subclass of :class:`api.API`.
But lets see how it looks like:

.. code-block:: python

    import time
    from cream.contrib.melange import api

    # This will register the API-class as `widget.api.digitalclock`
    # accessable from your JavaScript code.
    @api.register('digitalclock')
    class DigitalClock(api.API):

        def __init__(self):
            api.API.__init__(self)

        # This exposes the method which can be called in your JavaScript code as
        # `widget.api.digitalclock.get_current_time();`
        @api.expose
        def get_current_time(self):
            # Get the time in this format hours:minutes:seconds
            current_time = time.asctime().split()[3]
            return current_time

With :func:`api.register` we tell melange to instance the *class* and make it public in the js.
By decorating the method with :func:`api.expose` we can acces it from the javascript and get the return value.
This is actually all magic that happens here. Easy isn't it?

Creating the interface
----------------------

Now we are ready to design the widget. As mentioned above this is done by one html-file.

In ``<head>`` we import the stylesheet used for all widgets (``melange.css``) which gives all widgets their style according to the used theme:

.. code-block:: html

    <link rel="stylesheet" type="text/css" href="/common/ui/melange.css" media="screen" />

Now we need to import mootools and the cream-js-framework:

.. code-block:: html

    <script type="text/javascript" src="/common/core/mootools.js" />
    <script type="text/javascript" src="/common/core/cream.js" />

Now we need some widget-spezific style to make it look nice by adding some css. You could also load the css from a file:

.. code-block:: html

    <style type="text/css">

    </style>

Now comes the interesting part: The bridge to our python-backend.
We define a function ``main`` which automatically gets called when the widget is initialized. We set an intervall in order to update the time every second.
Then we call our python method und as a argument it expects a callback which is called when the method finishes.
The return value is stored in the argument of the callback and now we can set the text of our *clock* div to the current time:

.. code-block:: html

    <script type="text/javascript">
        function main(){
            setIntervall(update, 1000);
        }

        function update(){
            widget.api.digitalclock.get_current_time(function(time) {
                $('clock').innerHTML = time;
            });
        }

    </script>

Last but not least we still need a body, so here it comes:

.. code-block:: html

    <body>
        <div class="widget" style="width: 100px;">
            <div class="background">
                <div id="clock">
                    00:00
                </div>
            </div>
        </div>
    </body>


If you put everything together it should look like this and you're ready to load this widget:

.. code-block:: html

    <!doctype html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    
        <head>
            <title>DigitalClock widget</title>
            <meta http-equiv="content-type" content="text/html;charset=utf-8" />
            <!-- Melange's style definitions. -->
            <link rel="stylesheet" type="text/css" href="/common/ui/melange.css" media="screen" />
            <!-- The JavaScript framework we are using. -->
            <script type="text/javascript" src="/common/core/mootools.js"></script>
            <!-- The JavaScript for setting up the api -->
            <script type="text/javascript" src="/common/core/cream.js"></script>
            <style type="text/css">
    
            </style>
            <script type="text/javascript">
                function main(){
                    setIntervall(update, 1000);
                }
    
                function update(){
                    widget.api.digitalclock.get_current_time(function(time) {
                        $('clock').innerHTML = time;
                    });
                }
    
            </script>
        </head>
    
        <body>
            <div class="widget" style="width: 100px;">
                <div class="background">
                    <div id="clock">
                        00:00
                    </div>
                </div>
            </div>
        </body>
    </html>

