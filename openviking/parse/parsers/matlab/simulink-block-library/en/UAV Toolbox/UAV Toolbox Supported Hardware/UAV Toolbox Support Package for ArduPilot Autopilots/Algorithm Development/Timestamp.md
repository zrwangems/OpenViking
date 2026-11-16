---
type: simulink-block
title: 'Timestamp'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'timestamp'
documentation_source_path: 'ardupilot/ref/timestamp.html'
language: en
---

# Timestamp

## Ports

### Output

### **Timestamp** — Absolute timestamp vector

Absolute timestamp in microseconds from the ArduPilot board.

**Data Types:** `uint64`

## Parameters

### **Sample time** — Interval at which the block reads values `-1` (default)

The time interval at which the block reads values from the ArduPilot
Autopilots.

## Libraries

UAV Toolbox Support Package for ArduPilot Autopilots / Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025b**

## Description

Reads absolute timestamp

The Timestamp block reads the absolute timestamp in microseconds from the ArduPilot
board into the Simulink® model. This timestamp information is absolute, ensuring it never wraps or
goes backwards.
