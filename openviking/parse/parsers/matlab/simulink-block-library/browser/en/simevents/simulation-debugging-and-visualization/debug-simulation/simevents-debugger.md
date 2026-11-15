---
type: simulink-block
title: 'SimEvents Debugger'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Simulation, Debugging, and Visualization / Debug Simulation'
documentation_page: 'simeventsdebugger'
documentation_source_path: 'ref/simeventsdebugger.html'
language: en
---

# SimEvents Debugger

## Ports

Not documented in R2025b.

## Parameters

### **Enable debugger** — Enable the debugger `on` (default) | `off`

Select this check box to enable the debugger for your model.

## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Debug SimEvents models

The SimEvents Debugger block enables the debugger for your SimEvents® model. Using this block, you can:

- Inspect entities and their attribute values in storage blocks
- Set breakpoints on blocks and events
- Watch entities

**Note**

The SimEvents debugger is a preliminary version.

To start debugging your model:

1. From the SimEvents Library, add the SimEvents Debugger block into your
   SimEvents model.
2. In the Simulink® Editor, click the **Step Forward** button.

   The debugger interface appears.

   SimEvents Debugger window containing an Explorer pane on the left with a search field. An Inspector section on the right side of the pane displays the data of the element selected on the left.

- Click the **Continue simulation** button (Green arrowhead pointing right within a sphere.) to begin the simulation in the debugger. When the
  simulation completes, the debugger interface closes.
- To explore their data and behavior, the model tree displays in the left pane. Select
  the elements in the tree.
- When done, on the Simulink editor, click the **Stop** button to stop the
  simulation.

### Inspect Entities

To inspect entities in the debugger:

- To step to the next time step and inspect entities, in the Simulink editor, click the **Step Forward** button again. This
  action skips over all events at `tnow`.
- To step to the next event and inspect entities, in the debugger, click Green arrow with a long vertical tail pointing right to a sheet of paper..
- To set a breakpoint:

  - At a particular time, use the Simulation Stepper to set breakpoints.
  - At an event on the event calendar, in the debugger, in the left pane, click an
    event calendar.
  - At every event, in the debugger, in the left pane, select the event calendar. In
    the Event Calendar Events pane, select the **Break before event
    execution** check box.
  - When an entity enters a block, in the debugger, select the block. At the bottom
    of the Inspector pane, select the **Break upon entry** check
    box.
  - When an entity leaves a block, in the debugger, select the block. At the bottom
    of the Inspector pane, select the **Break prior to entity exit**
    check box.
- To go to a breakpoint, in the debugger, click the **Continue**
  button (Green arrowhead pointing right within a sphere.).

  **Note**

  When you stop the debugger at a breakpoint, the Simulink editor and the MATLAB® Command Window appear unresponsive. However, you can inspect entities,
  set new breakpoints, and continue the simulation from the debugger window.
- To watch entities, in the left tree, click the block. In the Inspector pane, select
  the check box of the entity you want to watch.
