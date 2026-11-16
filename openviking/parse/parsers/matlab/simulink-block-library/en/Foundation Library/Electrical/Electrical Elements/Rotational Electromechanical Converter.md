---
type: simulink-block
title: 'Rotational Electromechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'rotationalelectromechanicalconverter'
documentation_source_path: 'ref/rotationalelectromechanicalconverter.html'
language: en
---

# Rotational Electromechanical Converter

## Ports

The block has the following ports:

`+`
:   Electrical conserving port associated with the converter positive
    terminal.

`-`
:   Electrical conserving port associated with the converter negative
    terminal.

`C`
:   Mechanical rotational conserving port.

`R`
:   Mechanical rotational conserving port.

## Parameters

**Constant of proportionality K**
:   Constant of proportionality for electromechanical conversions.
    The default value is `0.1` V/(rad/s).

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Interface between electrical and mechanical rotational domains

The Rotational Electromechanical Converter block
provides an interface between the electrical and mechanical rotational
domains. It converts electrical energy into mechanical energy in the
form of rotational motion, and vice versa. The converter is described
with the following equations:

T=K·I

V=K·ω

where

|  |  |
| --- | --- |
| *`V`* | Voltage across the electrical ports of the converter |
| *`I`* | Current through the electrical ports of the converter |
| *`T`* | Torque |
| ω | Angular speed |
| *`K`* | Constant of proportionality |

The Rotational Electromechanical Converter block represents
a lossless electromechanical energy conversion, therefore the same
constant of proportionality is used in both equations.

Connections + and – are conserving electrical ports corresponding
to the positive and negative terminals of the converter, respectively.
Connections C and R are conserving mechanical rotational ports. If
the current flowing from the positive to the negative terminal is
positive, then the resulting torque is positive acting from port C
to port R. This direction can be altered by using a negative value
for K.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
