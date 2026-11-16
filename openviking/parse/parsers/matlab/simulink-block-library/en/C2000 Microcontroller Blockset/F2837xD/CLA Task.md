---
type: simulink-block
title: 'C28x CLA Task'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c28xclatask'
documentation_source_path: 'ref/c28xclatask.html'
language: en
---

# C28x CLA Task

## Ports

### Output

### **Port\_1** — Function-call signal to a function-call subsystem or function-call model scalar

The output triggers the CLA task that executes a downstream function-call
subsystem on the CLA core.

## Parameters

### **CLA task number** — CLA task number executed on CLA core `1` (default) | integer in [1, 8]

The CLA task number that you want to execute on the CLA core.

### **CLA task trigger source** — Source of CLA task trigger `Software` (default) | peripheral interrupt

The software or peripheral interrupt source that triggers the CLA task to
execute on the CLA core.

### **Wait until completion of task** — Block C28x execution until CLA task is completed `off` (default) | on

Select the parameter **Wait until completion of task**, for
the software source to trigger the CLA task.

Enabling this will halt the C28x execution until all the pending CLA tasks are
completed.

#### Dependencies

To enable this parameter, set the **CLA task trigger
source** parameter as `software`.

### **Sample time** — Frequency at which function-call subsystem is triggered `0.2` (default) | `-1` | scalar

Set the frequency at which the function-call subsystem is triggered by the
**CLA task trigger source**. To execute this block
asynchronously, set this parameter to `-1`.

#### Dependencies

To enable this parameter, select the `Software`
option in the **CLA task trigger source**.

## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Create CLA task that executes downstream function-call subsystem on CLA core

The CLA Task block creates a (Control Law Accelerator) CLA task that
executes a downstream function-call subsystem on the CLA core. CLA is a coprocessor that
allows parallel processing. Utilizing the CLA for time-critical tasks frees up the main CPU
to perform other system and communication functions concurrently.

You can specify the interrupt source to trigger the CLA task. You can create up to eight
CLA tasks to execute on the CLA core.

For information about how to configure a CLA block to execute a downstream function-call
subsystem, see Overview of CLA Configuration for C2000 Processors Using Subsystem.

**Note**

Not all TI C2000 hardware board variants support CLA. For instance, within the TI
Piccolo F2805x processor family, only the F28055 and F28053 processors support CLA,
while the F28054, F28052, F28051, and F28050 processors do not.
