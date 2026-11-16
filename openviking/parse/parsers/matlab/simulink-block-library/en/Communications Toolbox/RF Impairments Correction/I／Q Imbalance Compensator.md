---
type: simulink-block
title: 'I/Q Imbalance Compensator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'iqimbalancecompensator'
documentation_source_path: 'ref/iqimbalancecompensator.html'
language: en
---

# I/Q Imbalance Compensator

## Ports

Not documented in R2025b.

## Parameters

**Source of compensator coefficient**
:   Specify the source of the compensator coefficients as `Estimated
    from input signal` or `Input port`.
    If set to `Estimated from input signal`,
    the compensator calculates the coefficients from the input signal.
    If set to `Input port`, all other properties
    are disabled and you must provide the coefficients through the input
    port. The default value is `Estimated from input signal`.

**Initial compensator coefficient**
:   Specify the initial coefficient used by the internal algorithm
    to compensate for the I/Q imbalance. The default value is `0+0j`.

**Source of adaptation step size**
:   Specify the source of the adaptation step size as `Property` or `Input
    port`. If set to `Property`,
    specify the step size in the **Adaptation step size** field.
    If set to `Input port`, you must specify
    the step size through an input port. The default value is `Property`.

**Adaptation step size**
:   Specify the step size of the adaptation algorithm as a real
    scalar. This parameter is available only when **Source of
    adaptation step size** is set to `Property`.
    The default value is `0.00001`.

**Coefficient adaptation input port**
:   Select this check box to create an input port that permits a
    signal to control the adaptation process. If the check box is selected
    and if the input signal is `true`, the estimated
    compensation coefficients are updated. If the adaptation port is not
    enabled or if the input signal is `false`, the compensation
    coefficients do not change. By default, the check box is not selected.

**Estimated coefficient output port**
:   Select this check box to provide the estimated compensation
    coefficients to an output port. By default, the check box is not selected.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Compensate for imbalance between in-phase and quadrature components

The I/Q Imbalance Compensator mitigates the effects
of an amplitude and phase imbalance between the in-phase and quadrature
components of a modulated signal. The supported modulation schemes
include OFDM, M-PSK, and M-QAM, where M > 2.

This block accepts up to three input ports, of which one is
the input signal. When you set the **Source of compensator
coefficient** parameter to `Estimated from input
signal`, two additional input ports are enabled. The
first is enabled when you set the **Source of adaptation step
size** parameter to `Input port` and
the second is enabled when you check the **Coefficient adaptation
input port** box. The two options are independent. Additionally,
you can check the **Estimated coefficient output port** box
to create an optional output port from which the estimated compensator
coefficients are made available.

When you set the **Source of compensator coefficient** parameter
to `Input port`, only one possible configuration
is possible (input signal port, coefficient input port, and output
signal port).
