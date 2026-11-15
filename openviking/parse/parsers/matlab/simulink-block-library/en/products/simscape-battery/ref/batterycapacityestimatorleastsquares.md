---
type: simulink-block
title: 'Battery Capacity Estimator (Least Squares)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Estimators\u200b / Health Estimation'
documentation_page: 'batterycapacityestimatorleastsquares'
documentation_source_path: 'ref/batterycapacityestimatorleastsquares.html'
language: en
---

# Battery Capacity Estimator (Least Squares)

## Ports

### Input

### **Current** — Battery current, A scalar | vector

Battery current, in amperes, specified as a scalar for a single cell or a vector
for multiple cells. To specify this input as a vector of cell currents, select the
**Specify Current input as cell current(s)** parameter. If you
select this parameter, the size of this input port must be equal to the size of the
other input ports.

### **CellSOC** — Cell state of charge, unitless scalar | vector

State of charge of one or multiple cells, specified as a scalar or vector of
entries in the range [0, 1]. The size of this input port must be equal to the size of
the **InitialCellAH** input port.

### **InitialCellAH** — Initial cell capacity, A\*Hr scalar | vector

Initial cell capacity of the battery, in ampere-hours, specified as a scalar for a
single cell or a vector for multiple cells. The size of this input port must be equal
to the size of the **CellSOC** input port.
### Output

### **CellAH** — Estimated cell capacity, A\*Hr scalar | vector

Estimated cell capacity of the battery, in ampere-hours, returned as a scalar or a
vector. The size of this output port is equal to the size of the
**InitialCellAH** input port.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Specify Current input as cell current(s)** — Option to specify current input port as vector `off` (default) | `on`

Option to specify the value of the **Current** input port as a vector
of cell currents. If you select this parameter, the value at the
**Current** input port can be a scalar or a vector of size equal to
the size of the block inputs.

### **Least square algorithm** — Least-square algorithm `Ordinary least squares` (default) | `Recursive total least squares` | `Approximate total least squares`

Least-square algorithm that the block uses to estimate the battery cell
capacity.

### **SOC change detection threshold** — Threshold to detect change in SOC `0.03` (default) | scalar in the range (0,1)

Threshold to detect a change in the SOC. Typical values are 0.05 or 0.03, which
represent a 5% or 3% change.

### **Forgetting factor, gamma** — Forgetting factor `0.9` (default) | scalar in the range (0,1]

Forgetting factor.

### **Variance of SOC, VarianceX** — Variance of SOC `2e-4` (default) | positive scalar

Variance of the battery SOC.

#### Dependencies

To enable this parameter, set **Least squares algorithm** to
`Approximate total least squares`.

### **Variance of current measurement, VarianceY** — Variance of current measurement `5e-7` (default) | positive scalar

Variance of the current measurement.

### **Scaling factor k in VarianceX=k^2\*VarianceY** — Scaling factor *k* `10` (default) | positive scalar

Scaling factor *k*.

#### Dependencies

To enable this parameter, set **Least squares algorithm** to
`Recursive total least squares` or `Approximate
total least squares`.

### **Sample time (-1 for inherited)** — Block sample time `1` (default) | `0` | `-1` | positive integer

Time between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

For inherited discrete-time operation, specify this parameter as
`-1`. For discrete-time operation, specify this parameter as a
positive integer. For continuous-time operation, specify this parameter as
`0`.

If this block is in a masked subsystem or a variant subsystem that supports
switching between continuous and discrete operations, promote the sample time parameter.
Promoting the sample time parameter ensures correct switching between the continuous and
discrete implementations of the block. For more information, see Promote Block Parameters on a Mask.

### **Algorithm data type** — Option to choose data type for block algorithm `Inherit: auto` (default) | `double` | `single` | `<data type expression>`

*Since R2025a*

Option to choose the data type for the block algorithm, specified as one of these values:

- `Inherit: auto` — You can simulate the block in
  both `single` and `double`
  precision. You must explicitly provide the inputs and parameters as either
  `single` or
  `double`.
- `double` — The block algorithm casts all inputs
  and parameters to `double` data type.
- `single` — The block algorithm casts all inputs
  and parameters to `single` data type.
- `<data type expression>` — The block
  algorithm casts all inputs and parameters to the data type object you
  specify.

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant and Control Data Types of Signals.

## Libraries

Simscape / Battery / BMS / Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Switch between single-precision and double-precision floating-point simulation using **Algorithm data type** parameter

You can now easily switch between single-precision and double-precision floating-point simulation of the block algorithm by using the **Algorithm data type** parameter.

## Description

Battery capacity estimator using least-squares algorithms

The Battery Capacity Estimator (Least Squares) block calculates the cell
capacity of a battery by using least-squares algorithms.

For discrete-time simulation, set the **Sample time** parameter to a
positive value. To inherit the sample time, set **Sample time** to
`-1`. For continuous-time simulation, set **Sample time**
to `0`.

This diagram shows the structure of the block:

### Equations

The least-squares estimation finds the line of best fit for a set of data points by
minimizing the sum of the squared residuals. The squared residuals are the difference
between the observed responses and the predicted responses of the model. This line of best
fit predicts the dependent variable.

This equation defines the battery state of charge (SOC) at time
*t*n2,

SOC(tn2)=SOC(tn1)+1Q∫tn1tn2i(τ)dτ,

where:

- *SOC*(*t*n1) is the SOC
  at time *t*n1, with
  *n*={1,…,N}.
- *Q* is the capacity in ampere-hours.
- *i* is the battery cell current in amperes.
- ∫tn1tn2i(τ)dτ denotes the integrated battery cell current over the time interval
  *t*n2 -
  *t*n1. Time
  *t*n1 and
  *t*n2 must be in hours for the units to be
  consistent.

Define xn=SOC(tn2)−SOC(tn1) and yn=∫tn1tn2i(τ)dτ, and rewrite the SOC equation:

yn=Qxn.

The block uses this linear equation to determine an estimate of the cell capacity using
the least squares estimation,

(yn−Δyn)=Q^(xn−Δxn),

where:

- *Δx*n is the error associated with the SOC
  estimation.
- *Δy*n is the error associated with the
  current sensor.
- Q^ is an estimate of the true cell capacity under noisy
  measurements.

**Ordinary Least Squares**

The weighted ordinary least squares (OLS) method estimates the cell capacity by
minimizing the weighted squared errors, *Δy*n, of
the merit function

xWLS2=∑n=1N(yn−Yn)2σyn2=∑n=1N(yn−Q^xn)2σyn2,

where
*σ*2yn denotes the
variance of the current measurement and *Y*n is a
point on the line Yn=Q^xn that corresponds to the measurement data point
{*x*n,*y*n}.
The block assumes that *y*n has noise and
*x*n has no noise.

To solve the weighted OLS problem, the block differentiates the merit function with
respect to Q^ and solves for Q^ by setting the partial derivative to zero [1]:

∂xWLS2∂Q^=−2∑n=1Nxn(yn−Q^xn)σyn2=0Q^∑n=1Nxn2σyn2=∑n=1Nxnynσyn2Q^=∑n=1Nxnynσyn2∑n=1Nxn2σyn2

This method can be computed recursively and is easily adapted to allow
fading of past measurements.

If you define the forgetting factor as 0≪γ≤1, then the block obtains the estimated capacity from the equation

Q^=k2,nk1,n,

where:

k1,n=γk1,n−1+xn2σyn2k2,n=γk2,n−1+xnynσyn2

**Total Least Squares**

The weighted total least squares (TLS) method estimates the cell capacity by
minimizing the sum of both weighted square errors,
*Δx*n and
*Δy*n, of the merit function [1],[2],

χWLTS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2,

where
*σ*2yn denotes the
variance of the current measurement,
*σ*2xn denotes the
variance of the error on the SOC estimates, and
*X*n and
*Y*n are points on the line Yn=Q^Xn that corresponds to the noisy measured data point
{*x*n,*y*n}.

To enforce Yn=Q^Xn, the block augments the merit function with Lagrange multipliers
*λi*:

χWLTS,a2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2−λi(Yn−Q^Xn).

The block sets the partial derivatives of χWLTS,a2 with respect to *λi*,
*Y*n, and
*X*n to zero:

∂χWLTS,a2∂λi=−(Yn−Q^Xn)=0→Yn=Q^Xn∂χWLTS,a2∂Yn=−2(yn−Yn)σyn2−λi=0→λi=−2(yn−Yn)σyn2∂χWLTS,a2∂Xn=−2(xn−Xn)σxn2+λiQ^=0→Xn=xnσyn2+Q^ynσxn2σyn2+Q^2σxn2

Then the block rewrites the merit function as [1]:

χWLTS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2σxn2=∑n=1N(yn−Q^xn)2σyn2+Q^2σxn2.

Finally, the block sets the partial derivative of χWLTS2 with respect to Q^ to zero:

∂χWLTS2∂Q^=∑n=1N2(Q^xn−yn)(Q^ynσxn2+xnσyn2)(Q^2σxn2+σyn2)2=0.

In this equation:

- There is no closed-form solution in the general case. To find a closed-form
  solution, perform a Newton-Raphson search for Q^.
- There is no recursive update in the general case.
- The solution is impractical for implementation in an embedded system.

**Recursive Approximation of Total Least Squares (RTLS)**

The block substitutes σxn=kσyn in the equation of χWLTS2:

χRTLS2=∑n=1N(yn−Yn)2σyn2+(xn−Xn)2kσyn2=∑n=1N(yn−Q^xn)2(Q^2k2+1)σyn2.

The partial derivative of the WTLS merit function reduces to:

∂χRTLS2∂Q^=2∑n=1N(Q^xn−yn)(Q^k2yn+xn)(Q^2k2+1)2σyn2=0Q^2∑n=1Nk2xnynσyn2︸a+∑n=1Nk2xn2−k2yn2σyn2︸b+∑n=1N−xnynσyn2︸c=0Q^=−b±b2−4ac2a

The block incorporates fading memory by using this equation

Q^=−k1,n+k2k3,n+(k1,n−k2k3,n)2+4k2k2,n22k2k2,n,

where:

k1,n=γk1,n−1+xn2σyn2k2,n=γk2,n−1+xnynσyn2k3,n=γk3,n−1+yn2σyn2

**Approximate Total Least Squares (ATLS)**

The ATLS method is recursive and allows
*σ*2yn and
*σ*2xn to be
non-proportional.

This figure shows the definitions the block uses to derive the approximate weighted
total least squares:

The block defines *Δx*n and
*Δy*n as the *x*-distance and
*y*-distance between the data point *n* and the line,
respectively. The slope of the line is Q^=ΔynΔxn for all *n*. The angle of the line is θ=tan−1Q^.

This equation defines the shortest distance between the line and a given data point:

Rn=Δyncosθ=Δyn1+Q^2.

If δxi=Risinθ and δyi=Ricosθ, the block defines the *x* and *y*
components of the perpendicular distance between the data point *n* and
the fitting line. Then the block can define the AWTLS merit function using this equation:

χAWTLS2=∑n=1Nδxn2σxn2+δyn2σyn2=∑n=1N(yn−Q^xn)2(Q^2+1)2(Q^2σxn2+1σyn2).

This equation defines the Jacobian of the AWTLS merit function:

∂χAWTLS2∂Q^=2(Q^2+1)3∑n=1NQ^4xnynσxn2+Q^3(2xn2σxn2−xn2σyn2−yn2σxn2)+Q^2(3xnynσyn2−3xnynσxn2)+Q^(xn2−2yn2σyn2+yn2σxn2)+−xnynσyn2.

The roots of the quartic equation are the candidate solutions for Q^. The block rewrites the quartic equations as

c5,nQ^4+(2c4,n−c1,n−c6,n)Q^3+(3c2,n−3c5,n)Q^2+(c1,n−2c3,n+c6,n)Q^−c2,n=0,

where:

c1,n=γc1,n−1+xn2k2σyn2c2,n=γc2,n−1+kxnynk2σyn2c3,n=γc3,n−1+yn2σyn2c4,n=γc4,n−1+xn2σxn2c5,n=γc5,n−1+kxnynσxn2c6,n=γc6,n−1+k2yn2σxn2

The ATLS merit function does not equal the weighted TLS merit function when σxn=kσyn.

When σxn=kσyn, the block uses this equation to estimate the true cell capacity:

Q^corrected=Q^k.

### Implementation

This figure shows how the block estimates the battery capacity using the different
least-squares algorithms:

During the Data Acquisition phase, the block runs in a loop until the
algorithm finds a valid data point. The block follows these steps:

1. The block receives an SOC estimate at time
   *t*n1 using an SOC estimator.
2. The block receives a second SOC estimate at time
   *t*n2.
3. While SOC(tn1)−SOC(tn2)<SOCmin\_change, the block:

   - Keeps receiving SOC estimates.
   - Integrates cell current, yn=∫tn1tn2i(τ)dτ.
   - Overwrites time *t*n2 with a new
     timestamp.
   - If the battery is charging, the block discards the measurement and goes back
     to step 1.

### Assumptions and Limitations

- The block assumes the random errors *Δx*n
  and *Δy*n follow a zero-mean normal
  distribution.
- The block assumes that the weights
  *σ*2xn and
  *σ*2yn are
  known.
- In the RTLS algorithm, the scaling factor *k* must proportionally
  relate the weights
  *σ*2xn and
  *σ*2yn such that σxn=kσyn
