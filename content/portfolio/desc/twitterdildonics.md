title: Twitterdildonics
slug: twitterdildonics
template: project

Twitterdildonics is a python script that retrieves twitter messages
from the public timeline, breaks them down into characters, and uses
the resulting values to set the vibration on a Rez TranceVibrator.
This allows viewers to actually /feel/ twitter messages versus simply
reading them.

As unintended side effect, the vibrator would move at far higher
speeds when it would hit a message written in a foreign language. This
is because the original software was written to expect only ASCII
values, which are common for languages using roman character sets.
Languages like Russian, Japanese, and others that use different
character sets would cause the program to return far higher values.
This made it seem as if the program itself had a foreign language
fetish.
