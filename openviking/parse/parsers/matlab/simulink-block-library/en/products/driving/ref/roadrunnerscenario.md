---
type: simulink-block
title: 'RoadRunner Scenario'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / RoadRunner Scenario Simulation / Simulate RoadRunner Scenarios with MATLAB and Simulink'
documentation_page: 'roadrunnerscenario'
documentation_source_path: 'ref/roadrunnerscenario.html'
language: en
---

# RoadRunner Scenario

## Ports

Not documented in R2025b.

## Parameters

### Actions

### **Action name** — Name of user-defined action string

Name of user-defined action to map to a bus object.

To add an action name, click the **Add** button below the
**User-defined actions** input table and double-click on a cell in
the **Action name** column to type a new table entry.

### **Bus object name** — Name of bus object string

Name of bus object that corresponds to a user-defined action.

To add a bus object name corresponding to a user-defined action, double-click on a
cell in the **Bus object name** column at the same level of the
user-defined action, and type a new table entry.

All added bus object names must have a corresponding bus object. Bus objects
represent a user-defined action. You must define a bus object in MATLAB® in such a way that it contains the same parameter names, data types and
values as the user-defined action that it represents in RoadRunner Scenario. The RoadRunner Scenario Reader and RoadRunner
Scenario Writer blocks rely on a bus object loaded to the MATLAB workspace to recognize the structure of incoming user-defined
actions.

For more information about creating a bus object for a user-defined action, see
Author RoadRunner Actor Behavior Using User-Defined Actions or Events in Simulink.

### Events

### **Event name** — Name of user-defined event string

Name of user-defined event to map to a bus object.

To add an event name, click the **Add** button below the
**User-defined events** input table and double-click on a cell in
the **Event name** column to type a new table entry.

### **Bus object name** — Name of bus object string

Name of bus object that corresponds to a user-defined event.

To add a bus object name corresponding to a user-defined event, double-click on a
cell in the **Bus object name** column at the same level of the
user-defined event, and type a new table entry.

All added bus object names must have a corresponding bus object. Bus objects
represent a user-defined event. You must define a bus object in MATLAB in such a way that it contains the same parameter names, data types and
values as the user-defined event that it represents in RoadRunner Scenario. The RoadRunner Scenario Reader and RoadRunner
Scenario Writer blocks rely on a bus object loaded to the MATLAB workspace to recognize the structure of incoming user-defined
events.

For more information about creating a bus object for a user-defined event, see
Author RoadRunner Actor Behavior Using User-Defined Actions or Events in Simulink.

### Configuration

### **Maximum Points on Path** — Maximum number of points on path `500` (default) | positive scalar

Maximum number of points on the path of a vehicle actor to be read by a
path-following action.

You can set the value of this parameter to any positive scalar between 1 and
264. There is a tradeoff between the maximum number of
points and the simulation performance of the actor behavior model.

This parameter is applicable only if a Simulink actor behavior model contains a RoadRunner Scenario
Reader block that reads the Path
Following action of an actor by setting **Topic Category**
to `Action` and **Action Type** to
`Path Following`. The RoadRunner Scenario
Reader block stops reading points on a path after its number reaches the
maximum value.

**Data Types:** `uint64`

## Libraries

Automated Driving Toolbox / RoadRunner Scenario

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

### R2025a: Specify maximum number of points on path of actor

You can specify the maximum number of points on the path of a vehicle actor to be read
by a path-following action.

To configure the maximum number of points, in the **Maximum Points on
Path** field, on the **Configuration** tab, specify the required
value.

## Description

Define interface for Simulink actor model

The RoadRunner Scenario block defines the interface of a Simulink® actor model. The Block Parameters dialog box contains these tabs under which
inputs are grouped together.

- Actions
- Events
- Configuration

The RoadRunner Scenario block must be present at the root level
of the model, otherwise model compilation results in an error.
