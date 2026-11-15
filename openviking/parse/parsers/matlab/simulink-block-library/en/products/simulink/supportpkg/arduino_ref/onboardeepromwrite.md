---
type: simulink-block
title: 'On-board EEPROM Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'onboardeepromwrite'
documentation_source_path: 'supportpkg/arduino_ref/onboardeepromwrite.html'
language: en
---

# On-board EEPROM Write

## Ports

### Input

### **Data** — Data to Arduino EEPROM matrix

The block inputs a *N*-by-1 or 1-by-*N*
matrix of data that is has written to the Arduino EEPROM.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Write enable** — Enable write operation on Arduino EEPROM positive non–zero value

The block inputs a positive non–zero value that allows a writing operation on the
on–board Arduino EEPROM.

**Data Types:** `Boolean`

## Parameters

### **Start address** — EEPROM starting address `1` (default) | positive integer

Enter the starting memory address of the on–board Arduino EEPROM from where the write operation must begin.

**Note**

The total size of the input data type must not exceed the maximum number of
addressable on–board Arduino EEPROM memory locations from the starting address specified in this
parameter. For example, for the Arduino Uno board and `uint8` input data type, the starting
address of the EEPROM must not exceed 1021.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Write data to on-board Arduino EEPROM

Use the On-board EEPROM Write block to write nonvolatile data to the
on–board Arduino® electrically erasable programmable read–only memory (EEPROM). Each memory
position on the EEPROM can store one byte of data. The block compares the existing data on the
Arduino on–board EEPROM and writes only if the data has changed.

This table lists the memory size and the accessibility address range of on–board EEPROM of
these Arduino boards.

| Arduino Board | Size of On–Board EEPROM | Accessible Address Range |
| --- | --- | --- |
| Arduino Mega 2560 and Mega ADK | 4096 bytes | 0 to 4095 |
| Arduino Uno | 1024 bytes | 0 to 1023 |
| Arduino Leonardo | 1024 bytes | 0 to 1023 |
| Arduino Micro | 1024 bytes | 0 to 1023 |
| Arduino Nano 3.0 | 1024 bytes | 0 to 1023 |
