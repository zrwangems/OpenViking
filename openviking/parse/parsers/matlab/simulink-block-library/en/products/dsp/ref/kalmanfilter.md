---
type: simulink-block
title: 'Kalman Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Adaptive Filters'
documentation_page: 'kalmanfilter'
documentation_source_path: 'ref/kalmanfilter.html'
language: en
---

# Kalman Filter

## Ports

Not documented in R2025b.

## Parameters

**Number of filters**
:   Specify the number of filters to use to predict or estimate the current
    value.

**Enable filters**
:   Specify which filters are enabled or disabled at each time step. If you
    select `Always`, the filters are always enabled. If you
    choose `Specify via input port <Enable>`, the Enable
    port appears on the block.

**Reset the estimated state and estimated error covariance when filters are disabled**
:   If you select this check box, the estimated and predicted states as well
    as the estimated error covariance that correspond to the disabled filters
    are reset to their initial values. This parameter is visible if, for the
    **Enable filters** parameter, you select
    `Specify via input port <Enable>`.

**Initial condition for estimated state**
:   Enter the initial condition for the estimated state.

**Initial condition for estimated error covariance**
:   Enter the initial condition for the estimated error covariance.

**State transition matrix**
:   Enter the state transition matrix.

**Process noise covariance**
:   Enter the process noise covariance.

**Measurement matrix source**
:   Specify how to enter the measurement matrix values. If you select
    `Specify via dialog`, the **Measurement
    matrix** parameter appears in the dialog box. If you select
    `Input port <H>`, the H port appears on the
    block.

**Measurement matrix**
:   Enter the measurement matrix values. This parameter is visible if you
    select `Specify via dialog` for the **Measurement
    matrix source** parameter.

**Measurement noise covariance**
:   Enter the measurement noise covariance.

**Output estimated measurement <Z\_est>**
:   Select this check box if you want the block to output the estimated
    measurement.

**Output estimated state <X\_est>**
:   Select this check box if you want the block to output the estimated
    state.

**Output MSE of estimated state <MSE\_est>**
:   Select this check box if you want the block to output the mean-squared
    error of the estimated state.

**Output predicted measurement <Z\_prd>**
:   Select this check box if you want the block to output the predicted
    measurement.

**Output predicted state <X\_prd>**
:   Select this check box if you want the block to output the predicted
    state.

**Output MSE of predicted state <MSE\_prb>**
:   Select this check box if you want the block to output the mean-squared
    error of the predicted state.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Predict or estimate states of dynamic systems

Use the Kalman Filter block to predict or estimate the state of a dynamic system from
a series of incomplete and/or noisy measurements. Suppose you have a noisy linear system
that is defined by the following equations:

xk=Axk−1+wk−1zk=Hxk+vk

This block can use the previously estimated state, x^k−1, to predict the current state at time *k*, xk−, as shown by the following equation:

xk−=Ax^k−1Pk−=AP^k−1AT+Q

The block can also use the current measurement, zk, and the predicted state, xk−, to estimate the current state value at time *k*, x^k, so that it is a more accurate approximation:

Kk=Pk−HT(HPk−HT+R)−1x^k=xk−+Kk(zk−Hxk−)P^k=(I−KkH)Pk−

The variables in the previous equations are defined in the following table.

| Variable | Definition | Default Value or Initial Condition |
| --- | --- | --- |
| *x* | State | N/A |
| x^ | Estimated state | `zeros([6, 1])` |
| x− | Predicted state | N/A |
| *A* | State transition matrix | [101000010100001000000100000010000001] |
| *w* | Process noise | N/A |
| *z* | Measurement | N/A |
| *H* | Measurement matrix | [100000010000000010000001] |
| *v* | Measurement noise | N/A |
| P^ | Estimated error covariance | `10*eye(6)` |
| *P-* | Predicted error covariance | N/A |
| *Q* | Process noise covariance | `0.05*eye(6)` |
| *K* | Kalman gain | N/A |
| *R* | Measurement noise covariance | `eye(4)` |
| *I* | Identity matrix | N/A |

In the previous equations, *z* is a vector of measurement values.
Most of the time, the block processes Z, an M-by-N matrix, where M is the number of
measurement values and N is the number of filters.

Use the **Number of filters** parameter to specify the number of
filters to use to predict or estimate the current value.

Use the **Enable filters** parameter to specify which filters are
enabled or disabled at each time step. If you select `Always`, the
filters are always enabled. If you choose `Specify via input port
<Enable>`, the Enable port appears on the block. The input to this
port must be a row vector of 1s and 0s whose length is equal to the number of filters.
For example, if there are 3 filters and the input to the Enable port is [1 0 1], only
the first and third filter are enabled at this time step. If you select the
**Reset the estimated state and estimated error covariance when filters are
disabled** check box, the estimated and predicted states as well as the
estimated error covariance that correspond to the disabled filters are reset to their
initial values.

**Note**

All filters have the same state transition matrix, measurement matrix, initial
conditions, and noise covariance, but their state, measurement, enable, and MSE
signals are unique. Within the state, measurement, enable, and MSE signals, each
column corresponds to a filter.

Use the **Measurement matrix source** parameter to specify how to
enter the measurement matrix values. If you select `Specify via
dialog`, the **Measurement matrix** parameter appears in the
dialog box. If you select `Input port <H>`, the H port appears on
the block. Use this port to specify your measurement matrix.
