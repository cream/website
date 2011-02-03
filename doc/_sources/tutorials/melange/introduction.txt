Introduction
------------

Welcome to this tutorial about writing melange widgets.
We aim to create an easy to use API and try make creating widgets very simple.
Basically the widgets are simple HTML pages and you do not have to know GTK+ in order to write nice widgets. You can use everything HTML offers you, including new HTML5 features such as the canvas element. Furthermore CSS and Javascript can be used to extend the HTML.

As if that isn't enough you can use Python to collect and process data, which then can be used in your widget.

This tutorial will show you how to write a little widget which displays the current temperature in your city.

Here is a picture of the final widget:

.. image:: images/widget.png
    :align: center

Components
----------

Each widget consists of 4 main components:
    * *manifest*
        Here all the basic information about the widget is stored.
    * *skin*
        This is what then is displayed on the desktop.
    * *python*
        The widgets python backend.
    * *config*
        Here the configs needed by the widget can be stored and which are integrated into the widget.

Start with :doc:`manifests`
