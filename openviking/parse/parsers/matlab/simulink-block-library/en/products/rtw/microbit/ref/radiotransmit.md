---
type: simulink-block
title: 'Radio Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Radio'
documentation_page: 'radiotransmit'
documentation_source_path: 'microbit/ref/radiotransmit.html'
language: en
---

# Radio Transmit

## Ports

### Input

### **Data** — Data to be transmitted vector

The port accepts data as an N-by-1 or 1-by-N array.

## Parameters

### **Channel number (1–100)** — Channel selected to transmit data `1` (default) | any integer from 1 to 100, inclusive

The channel number from which you want to transmit data.

**Note**

The transmitter and receiver must be set to the same channel
number.

## Libraries

Simulink Coder Support Package for BBC micro:bit/Radio

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Transmit data to micro:bit devices via radio

The Radio Transmit block transmits data to other micro:bit devices
through a wireless connection.
