Documentation for the module `cream.gui`
========================================

Using the Timeline
------------------

When creating an animation you just define a timeline with a given curve
as a transition. You can connect to the curve's `update` signal and animate
your object according to the second paramter given to your callback function.

Here is an example how to use the timeline::

 from cream.gui import Timeline, CURVE_SINE

 def update(timeline, state):
     print state

 def completed(timeline):
     print "The timeline has finished!"

 my_timeline = Timeline(1000, CURVE_SINE)
 my_timeline.connect('update', update)
 my_timeline.connect('completed', completed)
 my_timeline.run()

API Documentation
-----------------

.. automodule:: cream.gui
    :members:
