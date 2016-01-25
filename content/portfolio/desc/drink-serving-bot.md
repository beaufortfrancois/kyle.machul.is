title: Drink Bot/Bartris/Adult Mario
slug: drink-serving-bot
template: project

# Description

The Drink Serving Robot was built as part of a residency at
MuseumsQuartier in Vienna, Austria, October-December 2009, to be shown
at the [Roboexotica](http://roboexotica.org) exhibition. It consists
of 3 drink serving lines, which are controlled via computer. The
software for the controlling drink mixtures is based on video games
such as Super Mario Brothers and Tetris. It is also controllable over
the internet via Second Life.

The video game interfaces introduce a feedback loop into the
system. The better a player does, the stronger the drink they
mix. Therefore, the more they play, the more they drink, and the worse
they will play in future sessions. This allows the bot to be self
regulating for alcohol resources.

# Drink Pouring System

Originally designed by Mitch Heinrich and Chris Vogel for the 2009
Roboexotica bot workshop, the drink pouring system for the robot is a
combination of simplicity and clever design, resulting in a system
that is cheap to build and control. It consists of 3 chopsticks nailed
to a wooden plank. Tubes for liquid flow are fed under the
chopsticks. Servos are mounted to the board, and the chopsticks are
tied to the rotating heads. To constrict the flow of liquid, the
servos are simply turned to a point where they will be pulling down on
the chopsticks. Releasing the servos lets liquid flow through the
system.

The "active-off" nature of the system does mean there are issues when
the controller board reboots or power is removed from the
system. However, when weighed against the price and complexity of
pumps, along with no real accuracy requirements for pouring amounts,
this system fulfills the needs of the project.

## Computer Control

Computer control for the drink serving bot happens via a python server
process. The python server receives OpenSoundControl messages, which
it parses and sends the resulting command to the controller
board. This control layer gives a developer the ability to quickly and
easily build a drink serving interface into any program that can
access the network and send OpenSoundControl messages.

## Environmental Feedback

To immerse players in the games more as they drank, the amBX gaming
environment system is used. The system consists of controllable RGB
lights, fans which blow at the player, and a rumble bar.

For haptic feedback, the Rez Trancevibrator is used. It allows the
user to feel vibration whenever the game state triggers it.

# Game and Interaction Modes

## Tetris

The tetris interface to the drink serving robot was a python
implementation adapted from a PyGame example. The rules for drink
mixing were based around the colors of pieces in play. 

- Gray: Rum Piece
- Brown: Coke Piece
- Blue: Water Piece

As players created lines in the game, the color makeup of the line
determined the drink to be made. So, if a line (each of which have 10
segments) was 4 brown pieces, 4 gray pieces, and 2 blue pieces, the
bot would mix a 4/4/2 coke/rum/water shot for the drink. The game
could either be played for 10 lines (at which the cup was full), or an
"infinite" game where the drink had to be consumed while the game was
being played. The losing state for the infinite mode was either the
usual lines filling up the game grid, or the drink overfilling.

## Super Mario Brothers

The Super Mario Brothers interface for the drink bot uses the original
Super Mario Brothers game for the NES. The ROM is played through the
FCEUX emulator on a PC. FCEUX not only emulates the ROM, but it allows
for developers to modify games via a LUA scripting engine that has
access to the RAM/ROM of the game as it is being played. Through this
interface, information about game state (coins collected, enemies
killed, level endings, etc...) can be monitored, and events can be
sent to outside programs via IPC or network.

For the drink bot installation, the following rules were applied:

- Getting a coin: Coke added to drink
- Killing an enemy: Rum added to drink
- Mario dies: Water added to drink

The amBX system is used to immerse the player in mario's world. The
fans from the system blow in the player's face at different speeds as
mario runs, and the vibrator speed is set for the length of time mario
spends sliding down the flag pole at the end of the level.

## Second Life

As a last minute addition for the Second Life version of Roboexotica,
a module was added to the drink serving bot that allows it to be
controlled via Second Life. An object in Second Life, which clicked,
makes an HTTP call to the same python server that the two game control
methods call, allowing SL users all over the world to mix drinks for
the attendees at the exhibition.
