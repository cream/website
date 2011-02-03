Skins
-----

Now comes the interesting part. As told before the widget is just a html page rendered by webkit.
A widget can have different skins and each skin consists of these files:
    * *index.html*
        This is the HTML page which is displayed on the desktop.
    * *manifest.xml*
        See previous chapter.

Additionally you can add any other file, which can be included in the HTML page such as CSS and JS files, images, fonts, etc.

So let us begin:

In ``<head>`` we include all neccessary scripts and stylesheets. We should also give our widget a nice title.

The style definition of each theme is specified in ``melange.css``. Furthermore we have to include ``mootools`` and ``cream.js``, which is important when we want to use python inside the widget:


.. code-block:: html

    <head>
        <title>Tutorial widget</title>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        <!-- Melange's style definitions. -->
        <link rel="stylesheet" type="text/css" href="/common/ui/melange.css" media="screen" />
        <!-- The JavaScript framework we are using. -->
        <script type="text/javascript" src="/common/core/mootools.js"></script>
        <!-- The JavaScript for setting up the api -->
        <script type="text/javascript" src="/common/core/cream.js"></script>
    </head>


The ``<body>`` is even easier. The only thing needed is a div-element which class ist ``widget`` and the rest is up to your creativity :)

It is though recommended to use a background, which can easilly be achieved by adding the ``background`` class to the ``widget`` div.

Our widget should display the city and the current temperature there, so we just add some ``<span>`` elements, which then can be filled with data.

This is how the body should look like:

.. code-block:: html

    <body>
        <div class="widget background" style="width: 180px;">
            <span id="location">Berlin, Germany</span>:<span id="temperature"></span><span id="celsius">°C.</span>
        </div>
    </body>

That is, so far, not much code, and if you run melange you can add the widget to your desktop.
But so far it looks a bit boring, so let us continue with the magic of :doc:`Python <python>`
