---
type: simulink-block
title: 'RST Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'rstcontroller'
documentation_source_path: 'ref/rstcontroller.html'
language: en
---

# RST Controller

## Ports

### Input

### **r** — Plant reference scalar

Plant system reference signal.

**Data Types:** `single` | `double`

### **y** — Plant output scalar

Plant system output signal.

**Data Types:** `single` | `double`
### Output

### **u** — Controller output scalar

Control system output signal.

**Data Types:** `single` | `double`

## Parameters

### **Controller parameterization** — Parameterization method `Controller polynomials` (default) | `Generate polynomials`

Method for parameterizing the controller. If you know the discrete-time
*R*, *S*, and *T*
polynomial values, select `Controller polynomials`.
Otherwise, select `Generate polynomials`.

#### Dependencies

Selecting a parameterization method enables other parameters.

### **R polynomial** — *R* polynomial values `1` (default) | positive, scalar or vector

Vector of the *R* polynomials for the RST control.

#### Dependencies

Selecting `Controller polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **S polynomial** — *S* polynomial values `1` (default) | positive, scalar or vector

Vector of the *S* polynomials for the RST control.

#### Dependencies

Selecting `Controller polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **T polynomial** — *T* polynomial values `1` (default) | positive, scalar or vector

Vector of the *T* polynomials for the RST control.

#### Dependencies

Selecting `Controller polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **Model discrete transfer function numerator** — Transfer function numerator `1` (default) | scalar or vector

Numerator of the system discretized transfer function. To determine the
discrete transfer function, if you have a license for Control System Toolbox™, use the `c2d` function.

#### Dependencies

Selecting `Generate polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **Model discrete transfer function denominator** — Transfer function denominator `[1 0.5]` (default) | vector

Denominator of the system discretized transfer function. To determine the
discrete transfer function, if you have a license for Control System Toolbox, use the `c2d` function.

#### Dependencies

Selecting `Generate polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **Control horizon (samples)** — Number of control-horizon samples `5` (default) | positive integer

Number of samples in the control horizon.

#### Dependencies

Selecting `Generate polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **Control weighting factor** — Weighting factor `0.5` (default) | positive number

Weighting factor for the RST controller.

#### Dependencies

Selecting `Generate polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **System dead time (samples)** — Number of dead-time samples `2` (default) | `0` or a positive integer

Number of samples of the dead time.

#### Dependencies

Selecting `Generate polynomials` for the
**Controller parameterization** parameter enables
this parameter.

### **Sample time (-1 for inherited)** — Sampling interval `-1` (default) | default value or a positive number

Time interval between samples. If the block is
inside a triggered subsystem, inherit the sample time by setting this
parameter to `-1`. If this block is in a continuous
variable-step model, specify the sample time explicitly. For more
information, see What Is Sample Time? and
Specify Sample Time.

## Libraries

Simscape / Electrical / Control / General Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Predictive control using a polynomial representation

The RST Controller block implements a generalized predictive controller
using a reference signal tracking polynomial representation. The diagram shows the
equivalent circuit for the control algorithm.

### Equations

A controlled auto-regressive integrated moving average (CARIMA) model describes
the plant:

A(z−1)y(k)=z−dB(z−1)u(k−1)+e(k)C(z−1)D(z−1)

A(z−1)=1+a1z−1+⋯+anAz−nA

B(z−1)=b0+b1z−1+⋯+bnBz−nB

C(z−1)=1

D(z−1)=1−z−1,

where:

- *d* is the system dead-time.
- *y(k)* is the plant output.
- *u(k)* is the controller output.
- *e(k)* is white noise with a zero-mean value.
- *A(z-1)* and
  *B(z-1)* are the
  system polynomials.
- *nA* and
  *nB* are the polynomials
  degrees.
- *C(z-1)* and
  *D(z-1)* are the
  disturbance polynomials for obtaining the steady-state error.

The prediction model is given as

y^(k+j|k)=Gj−d(z−1)D(z−1)z−d−1u(k+j)+Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k)

and

j=hi,hp¯

where:

- *hi* is the minimum prediction.
- *hp* is the prediction horizon.

The future control sequence, computed at time *k*, is

u(k+j−1|k),

where

j=1,hc¯

and *hc* is the control horizon.

The predicted values of the output is

y^(k+j|k).

To determine the system polynomials, Fj−d(z−1), Gj−d(z−1), and Hj−d(z−1), the block uses two Diophantine equations. The first Diophantine
equation is

C(z−1)A(z−1)D(z−1)=Ej−d(z−1)+z−j+dFj−d(z−1)A(z−1)D(z−1),

where:

Ej−d(z−1)=1+1+e1z−1+⋯+enEz−nE

Fj−d(z−1)=f0+f1z−1+⋯+fnFz−nF

nE=j−d−1

nF=max(nA+nD−1,nC−j+d)

The second Diophantine equation is

Ej−d(z−1)B(z−1)=C(z−1)Gj−d(z−1)+z−j+dHj−d(z−1),

where:

Gj−d(z−1)=g0+g1z−1+⋯+gnGz−nG

Hj−d(z−1)=h0+h1z−1+⋯+hnHz−nH

nG=j−d−1

nH=max(nC,nB+d)−1

The resulting prediction model is

y^(k+j|k)=Gj−d(z−1)D(z−1)z−d−1u(k+j)+y^0(k+j|k),

where

y^0(k+j|k)=Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k)

represents the free response of the system.

Using the matrix notation, the prediction model can be written as

y^=Gud+y^0,

where:

y^=[y^(k+hi|k),y^(k+hi+1|k),⋯,y^(k+hp|k)]T

G=[ghi−d−1⋯g00⋯0ghi−d⋯g1g0⋯0⋯⋯⋯⋯⋯⋯ghc−1⋯⋯⋯⋯g0ghp−d−1⋯⋯⋯⋯ghp−hc−1]

ud=[D(z−1)u(k),⋯,D(z−1)u(k+hc−1)]T

y^0=[y^0(k+hi|k),y^0(k+hi+1|k),⋯,y^0(k+hp|k)]T

To minimize tracking error and controller output, the block uses a cost function.
To trade off between the minimization of the tracking error and the minimization of
the controller output, the block uses a weighting factor, λ, such that

J=(Gud+y^0−w)T(Gud+y^0−w)+λudTud

for

D(z−1)u(k+i)=0

and

i∈[hc,hp−d−1],

where *w* is the reference trajectory vector. Minimizing the cost
function, yields the equation for the optimal control sequence:

ud\*=(GTG+λIhc)GT[w−y^0].

As *γj* and j=hi,hp¯ are elements in the first row of the matrix (GTG+λIhc)−1GT, applying the receding horizon principle yields the control
algorithm equation as

D(z−1)u(k)=∑j=hihpγj[w(k+j|k)−y^0(k+j|k)].

Substitution using y^0(k+j|k)=Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k) yields this form of the control algorithm equation:

C(z−1)D(z−1)u(k)=−∑j=hihpγjHj−d(z−1)D(z−1)u(k−1)−∑j=hihpγjFj−d(z−1)y(k)+∑j=hihpγjC(z−1)w(k+j).

The polynomial form of the control algorithm follows as

R(z−1)u(k)+S(z−1)y(k)=T(z−1)w(k+hp),

where:

R(z−1)=(C(z−1)+∑j=hihpγjz−1Hj−d(z−1)) D(z−1),

S(z−1)=∑j=hihpγjFj−d(z−1),

and

T(z−1)=C(z−1)∑j=hihpγjz−hp+j.

### Limitations

To obtain the *R*, *S*, and *T*
polynomials, use the discrete-time instead of the continuous-time transfer
function.
