# UKROC 2027 Rocketry Project

This repository contains early calculations and simulations for our planned
entry in the 2027 UK Youth Rocketry Challenge (UKROC). The competition asks
teams to design, build, and launch a model rocket carrying a fragile payload,
with goals for altitude and total flight duration.

## What we have made

| File | Purpose |
| --- | --- |
| `rocket sim 1.py` | Simulates a small rocket's vertical flight with constant thrust during a set burn time, then estimates the thrust needed to reach a target apogee. Plots velocity and altitude. |
| `rocket sim calculus 1.py` | Calculates a simple idealized vertical-flight estimate, including initial speed, acceleration, time, and height. |
| `rocket sim 3.py` | Prototype descent/braking simulation with changing mass, gravity, drag, and thrust. |
| `rocket sim2 (landing).py` | Prototype powered-descent simulation with changing mass and plots of velocity and altitude. |
| `ksp rocket suicide burn.py` | Estimates a powered landing burn using fixed vehicle and engine parameters; originally framed as a Kerbal Space Program calculation. |
| `hohmann transfer calculator.py` | Interactive orbital-transfer calculator for Earth, the Sun, Kerbin, or Mars. This is a spaceflight calculation, not a UKROC flight simulator. |
| `haack series matplot lib.py` | Draws a Haack-series nose-cone profile from its length, diameter, and shape parameter. |
| `UKROC-2027-Sponsorship-Letter-Template-2.docx` | Draft template for seeking support for the team's UKROC entry. |

## Running the Python scripts

The scripts use Python 3 and NumPy; scripts that plot also use Matplotlib.
Install the libraries with:

```bash
python -m pip install numpy matplotlib
```

Run a script from the repository directory, for example:

```bash
python "rocket sim 1.py"
```

The orbital-transfer calculator asks for a central body and orbit values.
Several other scripts use parameters written directly in the source code, so
edit those values before trying a different scenario.

## UKROC rules and engineering status

The calculations in this repository are prototypes and physics exercises, not
validated UKROC design tools. They use simplified models and example values;
their outputs must not be treated as evidence that a rocket meets competition
requirements or as construction or launch instructions.

Before using any calculation to make a competition design decision, compare the
design and simulation assumptions with the latest official UKROC rules and
safety guidance. Record the applicable rule, the design evidence, and any
organizer clarification separately. This README summarizes the work currently
in the repository; it does not reproduce or interpret the full rulebook.

## Next steps

- Read the current UKROC rules and team handbook, and turn relevant requirements
  into a verified design checklist.
- Agree on the competition rocket's measured inputs and document their sources.
- Update and test the flight model against those inputs before relying on its
  results.
- Keep design, safety, and launch decisions under appropriate adult and
  competition-organizer supervision.
