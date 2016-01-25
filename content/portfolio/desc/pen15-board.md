title: Pen15 Board
slug: pen15-board
template: project

Arduino shield built specifically for controlling small vibrators via
computers. The board only contains 5 components:

- Resistors/Capacitors
- A MOSFET
- 2.5mm Mono Audio Jack, a common connector for modular vibrators
- Passthru pins to other arduino ports not in use by the shield

The board works as a simple, single direction motor driver, driven by
the PWM pins on the arduino, and powered by the USB power supply. This
allows the user to create control interfaces to vibrators using
whatever language/interface they like, be it software or via hardware
interfaces hooked into the other ports.

While there are other driver shields available for the arduino with
more features, the pen15 was kept simple so the function of every part
could be understood by someone with little to no prior electronics
knowledge. This allows it to be used in introductory
arduino/electronics workshops based around building a simple piece of
sex technology.


