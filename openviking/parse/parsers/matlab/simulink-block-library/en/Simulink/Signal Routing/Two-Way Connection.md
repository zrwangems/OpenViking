---
type: simulink-block
title: 'Two-Way Connection'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'twowayconnection'
documentation_source_path: '../autoblks/../simulink/ref_extras/twowayconnection.html'
language: en
---

# Two-Way Connection

## Ports
```yaml
ports: []
```

The block has a Simulink input port, a Simulink output port, and a two-way connector port.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

## Description

Two-way connector port for subsystem

The Two-Way Connection block has a two-way connector port, which
transports Simulink® signals both ways. Consider using the block to:

- Reduce number of port connections.
- Represent Simulink block inputs and feedback as a single physical
  connection.

To implement, connect the two-way connector port to another two-way connector port.

The connection transports the signals.

- `Signal1` – First Two-Way Connection block
  input port to second Two-Way Connection block output
  port
- `Signal2` – Second Two-Way Connection
  block input port to first Two-Way Connection block output
  port

The Two-Way Connection block supports invariant model architecture for
top-down or bottom-up design. It lets you build subsystems as Simulink models, based on signals, and then connect them as if they are physical
systems. Place the Two-Way Connection blocks inside the subsystem and
connect them to the Connection Port (Simscape) blocks. Then the ports
on the subsystem boundary appear as two-way connector ports .

**Note**

The Powertrain Blockset™ and Vehicle Dynamics Blockset™ blocks may include a **Port Configuration** parameter
option allowing you to specify `Two-way connection` or
`Simulink` connections. Although the connections look
different, the blocks function the same with either configuration.
