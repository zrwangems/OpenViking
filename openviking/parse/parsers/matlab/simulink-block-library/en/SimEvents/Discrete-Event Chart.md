---
type: simulink-block
title: 'Discrete-Event Chart'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'discreteeventchart'
documentation_source_path: 'ref/discreteeventchart.html'
language: en
---

# Discrete-Event Chart

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

SimEvents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016a**

## Description

Discrete event chart

The Discrete-Event Chart block is similar to a Stateflow® chart but is used for discrete events. The block requires a Stateflow license.

The distinguishing characteristic of the Discrete-Event Chart block is
that it executes in an event-based rather than time-based fashion. The
Discrete-Event Chart block provides these advantages for
discrete-event modeling:

- Precise timing — The time resolution for occurrence of events can be
  arbitrarily precise and is not limited by the sample time of the
  model.
- Trigger on arrival — A Discrete-Event Chart block executes
  immediately on message arrival. It does not wait for the next sample time
  hit.
- Variable execution order — A Discrete-Event Chart block
  does not have a fixed sorted execution order. The order of execution depends
  on the run-time conditions of the model.
- Multiple executions per time step — A Discrete-Event Chart
  block can execute zero or multiple times in a single time step.

The Discrete Event Chart can be used in a similar fashion to the
Stateflow
Chart (Stateflow).

To access the chart properties, right-click the chart and select
**Properties**. For more information about the block properties,
see Create Custom Queuing Systems Using Discrete-Event Stateflow Charts.

For information about SimEvents® common design patterns with Discrete-Event Chart block, see
SimEvents Common Design Patterns.
