---
type: simulink-block
title: 'Ignition Trigger'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'ignitiontrigger'
documentation_source_path: 'ref/ignitiontrigger.html'
language: en
---

# Ignition Trigger

## Ports

### Inputs

### **Cam** — Crank position, deg physical signal

Physical signal input associated with the crank position in 720 degree
cycles.

### **Sw** — Ignitor switch input signal, binary physical signal

Physical signal input associated with the ignitor switch input signal,
where `0` turns off the ignitor and
`1` turns on the ignitor.

### **SA** — Spark angle input, deg physical signal

Physical signal input associated with the spark angle before top dead center, in
degrees.
### Outputs

### **Trig** — Asynchronous trigger report, binary physical signal

Physical signal output associated with the asynchronous spark trigger
events that the block generates, where `0` turns off
the trigger and `1` turns on the trigger.

## Parameters

### **Number of cylinders** — Total cylinder count `Single Cylinder` (default) | `Two Cylinders` | `Three Cylinders` | `Four Cylinders`

Number of spark ignition cylinders.

## Libraries

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Trigger system for spark-ignited combustion engine

The Ignition Trigger block represents an abstract ignition
trigger system for internal combustion engine models. This block takes the spark angle
as input at port **SA** and generates an asynchronous event trigger
output at port **Trig** when the crank position crosses the spark
angle. The block ignores the dynamics of the ignition system.

Connect a Crankshaft block to the **Cam**
port.
