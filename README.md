# Pynter

**Pynter** is a graphical simulation written in Python that demonstrates the operation of basic algorithms from sequential game theory.

## Project Description
The simulation consists of a map of fields in space where spaceships move. By moving over a field, a spaceship captures it and colors it with its own color. The game ends when all fields are colored or a set number of rounds have passed. The goal is to have the most colored fields.

During their turn, spaceships can:
- stay in place,
- move exactly one field in any direction, or
- start moving in any direction until they reach a void or another spaceship.

I implemented the **MaxNAgent**, **MinimaxAgent**, and **MinimaxABAgent** algorithms, extending the base `Agent` class and designing the evaluation functions for multi-player and two-player sequential games. I also tested the agents on multiple maps with different round limits, timeouts, and maximum search depths to ensure optimal behavior.

