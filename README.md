# Cellular Automaton Image Generator

This Python script generates a series of animated GIFs using cellular automata. The generated animations represent various states of the automaton with different configurations and visual styles.

## Description

The script uses cellular automaton rules to simulate the evolution of a grid of cells over a specified number of time steps. Each frame of the animation represents a different state of the grid, creating visually intriguing patterns and structures.

## Features

- **Customization**: You can specify the number of images you want to generate, allowing you to create a series of animations.

- **Random Configurations**: The script randomly selects parameters such as rule numbers, grid sizes, initialization conditions, and impulse positions to create diverse animations.

- **Colorful Animations**: It offers a wide range of color schemes to make your animations visually appealing.

- **Data Logging**: The script logs information about each animation, including the rule number, color scheme, initialization condition, and position, into a `REC.txt` file.

## Dependencies

The script relies on the following Python libraries:

- `numpy`: For numerical operations and array handling.
- `selenium`: For web automation (not used).
- `matplotlib`: For generating animations and visualizations.

## Usage

1. Clone or download the repository to your local machine.

2. Install the required libraries by running:

   ```shell
   pip install numpy matplotlib

3. Run the script and specify the number of images you want to generate when prompted.

4. The script will create a series of animated GIFs in the "Collection_1" folder, each with a unique configuration and visual style.

## Configuration

The script allows you to configure various parameters, including:

1. rule_number: The rule number for the cellular automaton.
2. size: The width of the automaton grid.
3. steps: The number of time steps to simulate.
4. init_cond: The initialization condition ('random' or 'impulse').
5. impulse_pos: The position of the impulse ('left', 'right', or 'center').


