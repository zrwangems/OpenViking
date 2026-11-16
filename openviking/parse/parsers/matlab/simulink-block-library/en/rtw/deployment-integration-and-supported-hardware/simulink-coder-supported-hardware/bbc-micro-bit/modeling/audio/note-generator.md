---
type: simulink-block
title: 'Note Generator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Audio'
documentation_page: 'notegenerator'
documentation_source_path: 'microbit/ref/notegenerator.html'
language: en
---

# Note Generator

## Ports

### Output

The block has one output port.

### **Port\_1(Frequency)** — Frequency generated corresponding to a musical note scalar

The frequency (in Hz) that is generated
corresponding to the specified musical
**Note** and
**Scale**.

**Data Types:** `double`

## Parameters

### **Scale** — Scale of musical note `Mid` (default) | `Low` | `High`

Specify the scale of the musical note. Scale can take
a value of `Low`,
`Mid`, or
`High`, placing the note
in one of three available octaves. Middle C, with a
frequency of 261.6 Hz, corresponds to a
**Note** value of C in the Mid
scale.

### **Note** — Letter name of note from the chromatic scale `C` (default) | `C#` | `D` | `D#` | `E` | `F` | `F#` | `G` | `G#` | `A` | `A#` | `B`

Specify one of the 12 notes of the chromatic scale.
The notes listed are in order from low to high in
pitch. Each pair of notes is one half step
apart.

## Libraries

Simulink Coder Support Package for BBC micro:bit/Audio

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Generate frequency corresponding to a musical note

The Note Generator block generates a frequency that corresponds
to the selected musical note and scale.
