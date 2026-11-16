---
type: simulink-block
title: 'Diagnostic Service Component'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Classic Platform / Basic Software'
documentation_page: 'diagnosticservicecomponent'
documentation_source_path: 'ref/diagnosticservicecomponent.html'
language: en
---

# Diagnostic Service Component

## Ports

Not documented in R2025b.

## Parameters

### **ID (RTE tab)** — ID that identifies service event, operation cycle, or function with inhibition condition 1 (default) | scalar

Each row in the RTE tab table represents a call into Dem or FiM services
from a Basic Software caller block. Check the ID mappings for events,
operation cycles, and functions with inhibition conditions. For events,
calls that act on the same event use the same event ID. For an example of
mapping Dem client ports to shared event IDs, see Simulate AUTOSAR Basic Software Services and Run-Time Environment.

### **Increment step size** — Fixed-step value to increment event ID counter when PREFAIL events arrive 1 (default) | scalar (1 to 32767)

Specify a fixed-step value that the Dem event ID counter increments by
when PREFAIL events arrive.

### **Decrement step size** — Fixed-step value to decrement the event ID counter when PREPASS events arrive 1 (default) | scalar (1 to 32767)

Specify a fixed-step value that the Dem event ID counter decrements by
when PREPASS events arrive.

### **Failed threshold** — Dem event ID counter threshold that represents a failed status 2 (default) | scalar (1 to 32767)

Specify a Dem event ID counter threshold value to represent failed status.
Events that reach this threshold are considered to have failed.

### **Passed threshold** — Dem event ID counter threshold that represents passed status -1 (default) | scalar (-32768 to -1)

Specify a Dem event ID counter threshold value to represent passed status.
Events that reach this threshold are considered to have passed.

### **ID (FiM tab)** — Inhibition condition ID 1 (default) | scalar

In the FiM tab table, each row grouped under an FID represents an
inhibition condition with an ID, one or more component client ports
associated with the ID, and a mask. For each inhibition condition, you can
modify the ID value. For examples of inhibition condition configuration, see
Configure and Simulate AUTOSAR Function Inhibition Service Calls.

### **Mask** — Inhibition condition mask LAST\_FAILED | NOT\_TESTED | TESTED | TESTED\_AND\_FAILED

In the FiM tab table, each row grouped under an FID represents an
inhibition condition with an ID, one or more component client ports
associated with the ID, and a mask. For each inhibition condition, you can
modify the mask value. For examples of inhibition condition configuration,
see Configure and Simulate AUTOSAR Function Inhibition Service Calls.

## Libraries

AUTOSAR Blockset / Classic Platform / Basic Software / Diagnostic Event Manager (Dem)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Configure AUTOSAR Diagnostic Services and Runtime Environment (RTE) for emulation

The Diagnostic Service Component block provides reference implementations of
Diagnostic Event Manager (Dem) and Function Inhibition Manager (FiM) services supported
by AUTOSAR Basic Software (BSW) caller blocks. When coupled with Dem and FiM caller
blocks, the reference implementations enable you to configure and run system-level or
composition-level simulations of AUTOSAR Dem and FiM service calls.

The block has prepopulated parameters, including RTE service ID parameters, Dem
**Counter-Based Debouncing** parameters, and FiM inhibition
condition parameters. Examine the parameter settings and, if necessary, make
modifications based on how you are using the Dem or FiM service operations.

The RTE tab lists component client ports and their mapping to Dem or FiM service IDs
for events, operation cycles, or functions with inhibition conditions. Each row in the
table represents a call into Dem or FiM services from a Basic Software caller block, for
which you can modify an ID value.

The Dem tab **Counter-Based Debouncing** parameters control the
counter-based debounce algorithm provided by the Dem service reference implementations.
During multiple simulations, you can adjust event step size and threshold parameters and
observe the effects.

Use the counter-based debouncing parameters to determine when a monitored event has
passed or failed. For each event ID, the software maintains a counter. When PREFAIL
events arrive, the event ID counter increments by the **Increment step
size** (default 1). When PREPASS events arrive, the event ID counter
decrements by the **Decrement step size** (default 1). To determine the
event ID counter thresholds at which an event fails or passes, use block parameters
**Failed threshold** (default 2) and **Passed
threshold** (default -1).

In the Dem reference implementations, the step size and threshold parameters apply
globally to event IDs, not to individual IDs.

The FIM tab lists function identifiers (FIDs) and their associated inhibition
conditions and client ports. The tab provides graphical controls for adding or removing
inhibition conditions for a selected FID. For each inhibition condition, select ID and
mask values.
