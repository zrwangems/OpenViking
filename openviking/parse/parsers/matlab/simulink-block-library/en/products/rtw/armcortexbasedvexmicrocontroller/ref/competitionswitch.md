---
type: simulink-block
title: 'Competition Switch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Gamepad'
documentation_page: 'competitionswitch'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/competitionswitch.html'
language: en
---

# Competition Switch

## Ports

### Input

### **Auto** — Signal used during simulation for enabling Autonomous mode `1` | `0`

Connect a source block to this port to simulate the position
of the Competition Switch in the VEX competition.

#### Dependencies

This port appears only when you select the **Add input ports for
simulation** parameter.

**Data Types:** `Boolean`

### **Driver** — Signal used during simulation for enabling Driver mode `1` | `0`

Connect a source block to this port to simulate the position of the Competition
Switch in the VEX competition.

#### Dependencies

This port appears only when you select the **Add input ports for
simulation** parameter.

**Data Types:** `Boolean`
### Output

### **Auto** — Outputs logical value for Autonomous mode based on switch `1` | `0`

The output is `1` if the position of the switch is Autonomous on
the VEXnet Competition Switch.

When the **Auto** output port is 1 and the
**Driver** output port is 0, the robot is in Autonomous
mode.

**Data Types:** `Boolean`

### **Driver** — Output port that provides logical value for Driver mode based on switch `1` | `0`

The output is `1` if the position of the switch is set at
`Driver` in the VEXnet Competition Switch.

When the Auto output port is 0 and the Driver output port is 1, the robot is in
Driver mode.

**Data Types:** `Boolean`

When both the Auto and Driver outputs are 0, the robot connected to the VEXnet
Competition Switch is disabled.

## Parameters

### **Add input ports for simulation** — Add two input ports to simulate input value `off` (default) | `on`

Select this check box to add two input ports – **Auto** and
**Driver** – to simulate the position of the VEXnet Competition
Switch.

### **Sample time** — Sample time for obtaining the value `0.02` (default) | positive real number

How often the Competition Switch block should read the position of
switch in VEXnet Competition Switch, specified in seconds. The default value is 0.02
seconds.

When the **Sample time** parameter is hidden and its value is
inherited.

#### Dependencies

This parameter is only available when **Add input
ports for simulation** is not selected.

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Read switch positions of VEXnet Competition Switch and provide logical values for Autonomous and Driver modes

The Competition Switch block reads the switch positions of the VEXnet Competition Switch
and provides the corresponding logical values (1 or 0) for the Autonomous mode and Driver
mode. This block can be used to switch between the logic required for Driver mode and
Autonomous mode, based on the switch position.
