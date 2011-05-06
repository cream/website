Using the Development Environment
=================================

Installation
------------

You can find instructions for installing Cream from Git here: http://cream-project.org/install/


Activating the Development Environment
--------------------------------------

You need to run the following command in every console window you want to use the development environment in:

.. code-block:: bash
 
 $ source dev/bin/activate

This will prepend ``(dev)`` to your bash prompt to show you, that you are working in a development environment.


Running Modules
---------------

Modules don't get installed in your development environment. Commands like ``melange`` won't work -- unless you have modules installed in your system, too.

Instead, you may find the modules in ``src/modules``. Just change into the particular directory and run the module like this:

.. code-block:: bash

 $ cd src/modules/melange/src
 $ ./melange.py
