---
type: simulink-block
title: 'Within Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'withinimplies'
documentation_source_path: 'ref/withinimplies.html'
language: en
---

# Within Implies

## Ports

Not documented in R2025b.

## Parameters

### **External reset** — specify whether the block can be reset off (default) | on

Specify whether the block observation of `Obs` can be
reset by an external Boolean reset signal.

## Libraries

Simulink Design Verifier / Temporal Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

## Description

Verify response occurs within desired duration

The Within Implies block captures the within implication by observing whether the
`Obs` input is `true` for at least one step within
each `true` duration of the first input `In`. Whenever
`Obs` is not detected within a particular input true duration, the
output becomes `false` for one time step in the step that follows the
input `true` duration.

*True duration* of a signal is defined as consecutive time steps
during which a signal is true
