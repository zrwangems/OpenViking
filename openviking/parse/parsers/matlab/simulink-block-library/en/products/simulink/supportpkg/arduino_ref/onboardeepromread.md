---
type: simulink-block
title: 'On-board EEPROM Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'onboardeepromread'
documentation_source_path: 'supportpkg/arduino_ref/onboardeepromread.html'
language: en
---

# On-board EEPROM Read

## Ports

### Output

### **Data** — Data from Arduino EEPROM matrix

The block outputs a *N*-by-1 or 1-by-*N*
matrix of data that is has read from the Arduino EEPROM.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Start address** — EEPROM starting address `1` (default) | positive integer

Enter the starting memory address of the on–board Arduino EEPROM from where the read operation must begin.

**Note**

The total size of the retrieved data type must not exceed the maximum number of
addressable on–board Arduino EEPROM memory locations from the starting address specified in this
parameter. For example, for the Arduino Uno board and `uint8` input data type, the starting
address of the EEPROM must not exceed 1021.

### **Data type** — Data type of data to read from EEPROM `uint8` (default) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

Select the data type of the data to read from the on–board Arduino EEPROM.

### **Data size (N)** — Size of data to read from EEPROM `1` (default) | positive integer

Specify the size of the data to read from the on–board Arduino EEPROM based on the data type specified in the **Data
type** parameter.

### **Sample time** — Frequency at which block reads data `0.1` (default) | scalar

Specify how often the block reads data from the on–board Arduino EEPROM.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Read data from on-board Arduino EEPROM

Use the On-board EEPROM Read block to read nonvolatile data from the
on–board Arduino® electrically erasable programmable read–only memory (EEPROM). The block reads
and outputs one byte of data at a time from the on–board Arduino EEPROM.

This table lists the memory size and the accessibility address range of on–board EEPROM of
these Arduino boards.

| Arduino Board | Size of On–Board EEPROM | Accessible Address Range |
| --- | --- | --- |
| Arduino Mega 2560 and Mega ADK | 4096 bytes | 0 to 4095 |
| Arduino Uno | 1024 bytes | 0 to 1023 |
| Arduino Leonardo | 1024 bytes | 0 to 1023 |
| Arduino Micro | 1024 bytes | 0 to 1023 |
| Arduino Nano 3.0 | 1024 bytes | 0 to 1023 |
