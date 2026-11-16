---
type: simulink-block
title: 'J1939 Network Configuration'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'J1939 Communication'
documentation_page: 'j1939networkconfiguration'
documentation_source_path: 'ug/j1939networkconfiguration.html'
language: en
---

# J1939 Network Configuration

## Ports

Not documented in R2025b.

## Parameters

### **Configuration name** — Define a name for this J1939 network configuration `ConfigX` (default) | character vector

The default value is `ConfigX`, where the number
`X` increases from 1 based on the number of existing
blocks.

### **Database File** — Specify the J1939 database file name relative to the current folder not set (default) | character vector

An example file name, enter `J1939.dbc` if the file is in the
current folder; otherwise enter the full path with the file name, such as
`C:\work\J1939.dbc`.

The database file defines the J1939 parameter groups and nodes. This file must
be in the DBC file format defined by Vector Informatik GmbH.

### **Enable address claiming** — Enable standard address claim procedure on (default) | off

When selected (checked on), this parameter allows J1939 Node Configuration
blocks to use a standard address claim procedure to dynamically assign addresses
of nodes on the bus.

## Libraries

Simulink Real-Time / J1939 Communication Vehicle Network Toolbox / J1939 Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015b**

## Description

Define J1939 network configuration name and database file

The J1939 Network Configuration block is where you define a configuration name and
specify the associated user-supplied J1939 database. You can include more than one block
per model, each corresponding to a unique configuration on the CAN bus.

To use this block, you must have a license for both Vehicle Network Toolbox™ and Simulink® software.

The J1939 communication blocks support the use of Simulink accelerator and rapid accelerator modes. You can speed up the execution of
Simulink models by using these modes. For more information on these modes, see Acceleration (Simulink).

The J1939 communication blocks also support code generation that have limited deployment
capabilities. Code generation requires a C++ compiler that is compatible with the code
generation target. For the current list of supported compilers, see Supported and Compatible Compilers.
