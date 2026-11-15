---
type: simulink-block
title: 'Joystick'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: 'joystick'
documentation_source_path: 'supportpkg/raspberrypi_ref/joystick.html'
language: en
---

# Joystick

## Ports

### Output

### **Port\_1** — Output port to return value of the Joystick button scalar

This is the output port that returns the value of the button
pressed on Joystick.

**Data Types:** `uint8`

## Parameters

### **View Position information** — View the position of the Joystick button position

Click this button to know the position of the button pressed.
The picture shows the positions of the Joystick button and the position
of the other sensors on the SenseHAT board.

### **Sample time** — Frequency at which data is read from pressure sensor 0.1 (default) | scalar

Specify how often this block reads the data from the pressure
sensor.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Read the state of five-position Joystick

Read the state of five-position Joystick. The block outputs
a value between 0-5 based on the Joystick button pressed. The Joystick
button positions are shown.

The positions on the Joystick that correspond to the five values
of the block output are:

0- when you have not pressed a button

1- when you press the center button

2- when you press the left button

3- when you press the top button

4- when you press the right button

5- when you press the bottom button.
