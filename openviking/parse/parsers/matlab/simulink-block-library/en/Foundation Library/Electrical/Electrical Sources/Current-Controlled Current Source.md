---
type: simulink-block
title: 'Current-Controlled Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'currentcontrolledcurrentsource'
documentation_source_path: 'ref/currentcontrolledcurrentsource.html'
language: en
---

# Current-Controlled Current Source

## Ports
```yaml
ports: []
```

The block has four electrical conserving ports. Connections
+ and – on the left side of the block are the control ports.
The other two ports are the electrical terminals that provide the
output current. The arrows between each pair of ports indicate the
positive direction of the current flow.
## Parameters
```yaml
parameters: []
```

**Current gain K**
:   Ratio of the current between the two output terminals to the
    current passing between the two control terminals. The default value
    is `1`.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Linear current-controlled current source

The Current-Controlled Current Source block models
a linear current-controlled current source, described with the following
equation:

I2=K·I1

where

|  |  |
| --- | --- |
| *`I2`* | Output current |
| *`K`* | Current gain |
| *`I1`* | Current flowing from the + to the – control port |

To use the block, connect the + and – ports on the left
side of the block (the control ports) to the control current source.
The arrow between these ports indicates the positive direction of
the control current flow. The two ports on the right side of the block
(the output ports) generate the output current, with the arrow between
them indicating the positive direction of the output current flow.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
