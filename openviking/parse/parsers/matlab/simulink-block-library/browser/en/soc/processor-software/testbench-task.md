---
type: simulink-block
title: 'Testbench Task'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Software'
documentation_page: 'testbenchtask'
documentation_source_path: 'ref/testbenchtask.html'
language: en
---

# Testbench Task

## Ports

### Input

### **Timer Task Function Call** — Function-call input port from a timer-driven task scalar

This port accepts a function-call event signal from a timer-driven task event port
of the Task Manager
block.

## Parameters

Not documented in R2025b.

## Libraries

SoC Blockset / Processor Testbench

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Embedded Coder™ does not generate code for this block.

## Version History

**Introduced in R2019b**

## Description

An external timer-driven task load on your SoC processor application

The Testbench Task block simulates a timer-driven task load external to
your software application. Using Testbench Task blocks, you can simulate the
impact of your software application in the presence of other processes that compete for
execution time of the processor.

**Note**

As part of a processor testbench, the Testbench Task block must be placed
in the top-level of your SoC model.
