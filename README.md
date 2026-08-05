# AI Lab Experiments

This repository contains Python implementations of various AI agent models as part of Semester 5 projects.

Each experiment is a standalone, dependency-free Python script that takes its environment from user input at the console and prints the agent's reasoning step by step. Together they show how an agent's decision-making grows in capability: from reacting to the present percept, to pursuing a goal, to weighing the value of the states it passes through.

## Experiments

### [Experiment 1: Simple Reflex Agent](Experiment-1/README.md)

**File:** `Experiment-1/VaccuumCleanerReflex.py`

A vacuum cleaner agent operating in a two-room world.
The script asks for the status of Room 'A' and Room 'B' (`0` for dirty, `1` for clean) and then acts on each room in turn using plain `if-else` condition-action rules.
Clean the room if it is dirty, otherwise leave it and move on — before shutting down.

The agent has no memory and no model of the world: its action depends only on the percept it currently holds, which is exactly what makes it a *simple reflex* agent.

### [Experiment 2: Goal-Based Agent](Experiment-2/README.md)

**File:** `Experiment-2/GoalBasedGrid.py`

A goal-based agent navigating a 2D grid.
The script asks for the grid dimensions, a starting cell and a goal cell, then moves the agent one step at a time.
First correcting the row (up/down), then the column (left/right) — printing each move until the goal is reached.

Unlike Experiment 1, the action chosen is not a direct response to a percept but a step justified by the distance still remaining to an explicit goal state.

### [Experiment 3: Utility-Based Agent](Experiment-3/README.md)

**File:** `Experiment-3/UtilityBasedAgent.py`
A utility-based agent in a richer grid environment. The script builds the grid from user input and populates it with obstacles (`X`), rewards (`R`) and penalties (`P`), then walks the agent from a start cell to a goal cell. When the preferred move is blocked by an obstacle, the agent sidesteps to another direction that still reduces the distance to the goal and reports "No path available" if every option is blocked. Rewards collected and penalties tackled are announced as they are encountered, visited cells are marked with `=`, and the grid is printed after every move.

Here reaching the goal is not the only consideration — the agent also cares about *how good* the path it takes is, which is the distinguishing trait of a utility-based agent.

## Grid Legend (Experiment 3)

| Symbol | Meaning                   |
|--------|---------------------------|
| `+`    | Free cell                 |
| `X`    | Obstacle                  |
| `R`    | Reward                    |
| `P`    | Penalty                   |
| `=`    | Cell visited by the agent |

## Running the Experiments

Any Python 3 installation will do; no external packages are required.

```bash
python Experiment-1/VaccuumCleanerReflex.py
python Experiment-2/GoalBasedGrid.py
python Experiment-3/UtilityBasedAgent.py
```

Rows and columns are zero-indexed, so a 5-by-5 grid has valid coordinates from `0` to `4`.
