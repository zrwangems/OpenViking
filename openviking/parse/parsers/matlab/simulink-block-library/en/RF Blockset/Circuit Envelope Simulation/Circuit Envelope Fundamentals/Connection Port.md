---
type: simulink-block
title: 'Connection Port'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Circuit Envelope Fundamentals'
documentation_page: 'connectionport'
documentation_source_path: 'ref/connectionport.html'
language: en
---

# Connection Port

## Ports

Not documented in R2025b.

## Parameters

PMC Port mask

#### PMC\_Port: Physical Modelling Connection Port block for subsystems

### **Port number** — Connector port number `1` (default) | scalar

This field labels the subsystem connector port created by this block. Multiple
connector ports on the boundary of a single subsystem require different numbers as
labels.

### **Port location on parent subsystem** — Port location on the parent subsystem. Choices are: `left` (default) | `Right`

Use this parameter to choose on which side of the parent subsystem boundary the Port
is placed.

## Libraries

RF Blockset / Equivalent Baseband / Input RF Blockset / Circuit Envelope / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2021b: Connection Port block icon updated

Starting in R2021b, the Connection Port block icon has updated. When you
open a model created before R2021b containing a Connection Port block, the
software replaces the block icon with the R2021b version.

## Description

Connection port for RF subsystem

The Connection Port block, placed inside a subsystem composed of RF Blockset™ Equivalent Baseband blocks, creates an open round physical modeling connector
port open round physical modeling connector on the boundary of the subsystem. When it is connected to a connection
line, the port becomes solid Solid physical modeling connector.

You connect individual blocks and subsystems made of RF Blockset Equivalent Baseband blocks to one another with connection lines instead of
normal Simulink® signal lines. These blocks and subsystems are anchored at the open, round
physical modeling connector ports Round physical modeling connector ports. Subsystems constructed out of RF Blockset Equivalent Baseband blocks automatically have such open round physical modeling
connector ports. You can add additional connector ports by adding Connection Port blocks to
your subsystem.
