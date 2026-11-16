---
type: simulink-block
title: 'Competition Switch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'competitionswitch'
documentation_source_path: 'vexv5/ref/competitionswitch.html'
language: en
---

# Competition Switch

## Ports

### Output

### **Auto** — Output port that provides logical value for Autonomous mode based on the position of the switch `1` or `0`

The output is 1 if the position of the switches are set at
`Enabled` and `Autonomous` in the VEXnet
Competetion Switch.

When the Auto output port is 1 and the Driver output port is 0, the robot is in
Autonomous mode.

**Data Types:** `Boolean`

### **Driver** — Output port that provides logical value for Driver Controlled mode based on the position of the switch `1` or `0`

The output is 1 if the position of the switches are set at
`Enabled` and `Driver` in the VEXnet Competition
Switch.

When the Auto output port is 0 and the Driver output port is 1, the robot is in
Driver mode.

**Data Types:** `Boolean`

### **Pre-Auto** — Output port that provides logical value for Pre-autonomous mode based on the position of the switch `1` or `0`

The output is 1 if the position of the switch is set at
`Disabled` in the VEXnet Competition
Switch.

**Data Types:** `Boolean`

The following table lists the modes and the three outputs based on the switch
position.

| Enable/Disable Switch | Autonomous/Driver Switch | Mode | Pre-Auto | Auto | Driver |
| --- | --- | --- | --- | --- | --- |
| Disable | Autonomous | Pre-Autonomous | 1 | 0 | 0 |
| Enable | Autonomous | Autonomous | 0 | 1 | 0 |
| Enable | Driver | Driver Controlled | 0 | 0 | 1 |
| Disable | Driver | Disabled | 0 | 0 | 0 |

## Parameters

### **Sample time** — Sample time for obtaining the value `0.02` (default) | seconds

Specify how often the Competition Switch block should read the
position of switches in VEXnet Competition Switch. The default value is 0.02
seconds.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Read the switch positions of VEXnet Competition Switch or field controller

The Competition Switch block is used to read the switch positions of the VEXnet
Competition Switch, and provide the corresponding logical values (1 or 0) as outputs. This
block can be used to enable the required logic for the Pre-Autonomous, Autonomous and Driver
Controlled modes, based on the switch position.
