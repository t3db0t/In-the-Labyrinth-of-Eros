*"In the Labyrinth of Eros" is a text-adventure sonnet.*

...what?

Instead of a pre-written text, this poem comes in the form of an "interactive fiction" text adventure in the grand tradition of Zork and countless others.

To read the poem, play the game (`python3 eros.py`). Each "room" in the game is a line of the poem, and by walking through 14 rooms you will have generated a sonnet (3 quatrains and a couplet):

```
You've entered Room No. 0

When we had opened all the doors

Destinations:
SW S SE 
-->
```

As in pretty much all text adventures, you'll need to type something like "go sw" to proceed.

![The room graph of "In the Labyrinth of Eros"](graph.jpg "The room graph of "In the Labyrinth of Eros"")

The rooms of the game form a directed graph that constrain what order you can walk through them in. A principal concern while writing this, of course, was that it would be a good and interesting poem in any of the possible resulting patterns.  I'll leave that to you to decide.

To quit, type Ctrl+D or Ctrl+C. There's also a little easter egg hidden in the script.