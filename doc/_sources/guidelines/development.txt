Guidelines for Development
--------------------------

Micro Commits
~~~~~~~~~~~~~

There has always been a discussion on how to commit code changes. Some people tend to commit huge patches fixing a bug or implementing a new feature and some others try to keep their commits small. From a bigger project's point of view it's a lot easier to work with small and easy to follow commits than to review huge patches and get lost in tons of changes.

Therefore we would recommend a higher frequency of smaller commits than just a single commit every few days. For more reasons for this recommendation please refer to Lucas Rocha's great blog article `Micro Commits`_ on the very same topic.

Commit Messages
~~~~~~~~~~~~~~~

Let's make this one short and clear:

Good Commit Message
+++++++++++++++++++

::

 Added class `Bar` to `cream.foo`, fixing http://bit.ly/fLxmLN.

A good commit message should

- consist of a complete (although maybe elliptic) and grammatically correct English sentence,
- refer to the changed code in a correct and easy to follow way and
- make clear what you intended with the commit.
- The title should be max 80 chars long. If your commit needs more explanation, then use a short title and put the explanation into the body of the commit.

Bad Commit Message
++++++++++++++++++

::

 added class bar to cream.foo




.. _`Micro Commits`: http://lucasr.org/2011/01/29/micro-commits/
