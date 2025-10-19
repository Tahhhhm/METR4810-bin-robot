# METR4810 Miniaturized Garbage/Recycling Bin

A mechatronics engineering project for METR4810 focused on automation, machine vision, and smart waste management.

## 🚀 Features

- 🗑️ Pick up and deposit garbage/recycling contents
- 🧠 Automatic detection of bins
- 🤖 Automated motion and pathfinding
- 🚧 Obstacle avoidance
- 👁️ Machine vision

## 📋 Procedure

1. Navigate (near entire) track to find delivery zones and bins
2. Use A* search algorithm to compute the shortest path to each bin
3. Travel to the closest bin and record the lid colour
4. Extract contents from the bin
5. Move to the deposit zone
6. If bin lid was **red**, deposit to **landfill** pile, else deposit to **recycling** pile
7. Repeat until all bins are cleared — collection is complete

## 🧰 Requirements

### 🔧 Hardware

- Raspberry Pi Zero 2 W  
- *(Add other components as applicable)*

### 💻 Software

#### General

- `Blinka`
- `CircuitPython`

#### Machine Vision

- `ultralytics` (YOLO models)

#### Motor Control

- `gpiozero`
- `time`

#### Servo Control

- `piicodev`

#### I2C Multiplexing

- `adafruit-circuitpython-tca9548a`

#### Required CircuitPython Libraries

- `blinka`

## 👨‍💻 Contributors

- **Tom Ng**
- **Brandon Pang**
- **Amaana Hussein**
- **Karan Vijay Shankar**
