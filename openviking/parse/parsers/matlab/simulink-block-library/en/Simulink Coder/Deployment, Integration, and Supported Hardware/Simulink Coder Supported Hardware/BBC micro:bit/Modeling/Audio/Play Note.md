---
type: simulink-block
title: 'Play Note'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Audio'
documentation_page: 'playnote'
documentation_source_path: 'microbit/ref/playnote.html'
language: en
---

# Play Note

## Ports

### Input

The block has one input port.

### **Port\_1(Frequency)** — Frequency of the musical note to be played scalar

The frequency (in Hz) corresponding to the
musical note to be played. The input frequency can
be derived from the output of a Note Generator block or from the output of a constant block or
a wave block.

**Data Types:** `double`

## Parameters

### **Pin** — Number of pin connected to speaker P1 (default)

The number of the pin on the BBC micro:bit that is
connected to the speaker intended to play the
musical note.

## Libraries

Simulink Coder Support Package for BBC micro:bit/Audio

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018a**

## Description

Play musical note on specified pin on BBC micro:bit

The Play Note block plays a musical note on a speaker connected
to the specified pin on a BBC micro:bit. The note played corresponds to the
input frequency.
