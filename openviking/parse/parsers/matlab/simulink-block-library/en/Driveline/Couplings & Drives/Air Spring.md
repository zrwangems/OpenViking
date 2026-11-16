---
type: simulink-block
title: 'Air Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'airspring'
documentation_source_path: 'ref/airspring.html'
language: en
---

# Air Spring

## Ports

### Conserving

### **C** — Follower port mechanical translational

Mechanical translational conserving port associated with the follower
of the air spring. Positive physical signals travel from
**R** to **C**.

### **R** — Base port mechanical translational

Mechanical translational conserving port associated with the base end
of the air spring. Positive physical signals travels from
**R** to **C**.

## Parameters

### Spring

### **Parameterization** — Effective force parameterization `Load as a function of height` (default) | `Stiffness as a function of height`

Option to parameterize by height or load. Obtain data for your air
spring from manufacturer-supplied specifications or experimental
results.

### **Height vector** — Height breakpoints that correspond to load or stiffness data `[5, 7, 11, 14, 17, 20]` `cm` (default) | nonnegative vector

Vector of spring heights. These values correspond to either the load
or stiffness values, depending on the way you choose to parameterize the
spring. You must specify a vector that has at least three
elements.

### **Load vector** — Load for a given height breakpoint `[3000, 2000, 1500, 1200, 800, 100]` `N` (default) | positive vector

Vector of spring loads. This vector must be the same length as the
**Height vector** parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Load as a
function of height`.

### **Stiffness vector** — Stiffness for a given height breakpoint `[600, 300, 100, 80, 40, 5]` `N/cm` (default) | positive vector

Vector of spring stiffness values. This vector must be the same length
as the **Height vector** parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Stiffness
as a function of height`.

### **Damping vector** — Spring damping for given height breakpoint `[100, 60, 30, 15, 10, 10]` `s*N/cm` (default) | nonnegative vector

Vector of spring damping values. This vector must be the same length
as the **Height vector** parameter.

### **Interpolation method** — Method of interpolation between breakpoint values `Smooth` (default) | `Linear`

Lookup table breakpoint interpolation. The block uses the
`tablelookup` function to model nonlinearity by
using array data to map input values to output values:

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to
  produce a continuous curve with continuous first-order
  derivatives.

For more information, see `tablelookup`.

### **Extrapolation method** — Method of handling input values that fall outside range of breakpoint data set `Linear` (default) | `Nearest` | `Error`

Lookup table breakpoint extrapolation. This method determines the
output value when the input value is outside the range specified in the
argument list. The block uses the `tablelookup`
function to model nonlinearity by using array data to map input values
to output values:

- `Linear` — Select this option to
  produce a curve with continuous first-order derivatives in
  the extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Select this option to
  produce an extrapolation that does not go above the highest
  point in the data or below the lowest point in the
  data.
- `Error` — Select this option to
  avoid extrapolating when you want your data to be within the
  table range. If the input signal is outside the range of the
  table, the simulation stops and generates an error.

For more information, see `tablelookup`.

### Hard Stops

### **Hard stop at full extension** — Simulate hard stop at maximum spring height `off` (default) | `on`

Option to enable a hard stop when the air spring is fully extended. The hard stop occurs
as the spring reaches the value of the **Maximum
height** parameter. For more information, see Translational Hard Stop.

### **Maximum height** — Location of full-extension hard stop `25` `cm` (default) | positive scalar

Maximum spring height. This parameter determines the location of the
full-extension hard stop.

#### Dependencies

To enable this parameter, select **Hard stop at full
extension**.

### **Stiffness at full extension** — Full-extension hard stop stiffness `1e8` `N/cm` (default) | positive scalar

Stiffness to apply as the spring reaches full extension.

#### Dependencies

To enable this parameter, select **Hard stop at full
extension**.

### **Damping at full extension** — Full-extension hard stop damping `1e8` `s*N/cm` (default) | positive scalar

Damping to apply as the spring reaches full extension.

#### Dependencies

To enable this parameter, select **Hard stop at full
extension**.

### **Hard stop at full compression** — Simulate hard stop at minimum spring height `off` (default) | `on`

Option to enable a hard stop when the air spring is fully extended. The hard stop occurs
as the spring reaches the value of the **Minimum
height** parameter. For more information, see Translational Hard Stop.

### **Minimum height** — Location of full-compression hard stop `5` `cm` (default) | positive scalar

Minimum spring height. This parameter determines the location of the
full-compression hard stop.

#### Dependencies

To enable this parameter, select **Hard stop at full
compression**.

### **Stiffness at full compression** — Full-compression hard stop stiffness `1e8` `N/cm` (default) | positive scalar

Stiffness to apply as the spring reaches full compression.

#### Dependencies

To enable this parameter, select **Hard stop at full
compression**.

### **Damping at full compression** — Full-compression hard stop damping `1e8` `s*N/cm` (default) | positive scalar

Damping to apply as the spring reaches full compression.

#### Dependencies

To enable this parameter, select **Hard stop at full
compression**.

### **Hard stop model** — Hard stop transition behavior `Stiffness and damping applied smoothly through transition region, damped rebound` (default) | ...

Stiffness and rebound options for the hard stop model. The block uses a composite
implementation of the Translational Hard
Stop block. You can choose from the following options:

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

#### Dependencies

To enable this parameter, select **Hard stop at full extension** or
**Hard stop at full compression**.

### **Transition region** — Region of partial hard stop effects `0.1` `mm` (default) | positive scalar

Distance from full compression or full extension where the effects of
stiffness and damping are partially applied. When you set **Hard
stop model** to `Stiffness and damping applied
smoothly through transition region, damped rebound`,
the block will smoothly transition the onset of stiffness and damping as
the spring approaches full extension or full compression.

#### Dependencies

To enable this parameter, select **Hard stop at full extension** or
**Hard stop at full compression**, and set
**Hard stop model** to `Stiffness
and damping applied smoothly through transition region, damped
rebound`.

### **Coefficient of restitution** — Ratio of final-to-initial relative speed between slider and stop after collision `0.7` (default) | unitless value between 0 and 1

Ratio of the final to the initial relative speed between the slider
and the stop after the slider bounces.

#### Dependencies

To enable this parameter, select **Hard stop at full extension** or
**Hard stop at full compression**, and set
**Hard stop model** to `Based on
coefficient of restitution`.

### **Static contact speed threshold** — Threshold relative speed between slider and stop before collision `0.001` `m/s` (default) | nonnegative scalar

Threshold relative speed between the slider and the stop before
collision. When the slider hits the case with speed less than the value
of this parameter, they stay in contact. Otherwise, the slider bounces.
To avoid modeling static contact between the slider and the case, set
this parameter to `0`.

#### Dependencies

To enable this parameter, select **Hard stop at full extension** or
**Hard stop at full compression**, and set
**Hard stop model** to `Based on
coefficient of restitution`.

### **Static contact release force threshold** — Threshold force needed to transition from contact mode to free mode `0.001` `N` (default)

Minimum force needed to release the slider from a static contact
mode.

#### Dependencies

To enable this parameter, select **Hard stop at full extension** or
**Hard stop at full compression**, and set
**Hard stop model** to `Based on
coefficient of restitution`.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

### R2025a: Enumeration Updates

The **Hard stop at full extension** and **Hard stop at
full compression** parameters now use check boxes. These parameters
used drop downs in previous releases.

### R2023a: Composite Hard Stop Updates

Due to updates in the Translational Hard Stop block, the **Hard stop
model** parameter now features the `Coefficient of
restitution` option.

## Description

Sealed translational air spring

The Air Spring block represents a generic sealed
translational pneumatic spring that isolates equipment from shocks and vibrations. The
compressibility of gas gives air springs desirable isolation performance. Air springs
are common in automotive and industrial applications where low spring rate and low
natural frequency are beneficial. Air springs can help you to:

- Reduce wear and tear on the sprung mass.
- Reduce the wear and tear that the unsprung mass deals to
  infrastructure.
- Lighten suspension systems to allow for greater total mass.
- Filter out specific unwanted frequencies.

Air springs consist of bellows that confine a column of compressed air or other gas. The air
bears the force of the load, and the bellows hold the air. Sealed air springs maintain a
constant mass of air, so the increasing load lowers the volume of air and the resulting
spring rate. The reverse is also true. The natural frequency of a sealed air spring
system also depends on this relationship. Due to the large amount of variability in air
spring requirements and performance, manufacturers commonly provide pressure
characteristic tables for each model.

Based on the data that you possess, you can set **Parameterization** to
`Load as a function of height` or `Stiffness as
a function of height`. The Air Spring
block uses the information that you enter to create a lookup table. The lookup table
allows the block to simulate the nonlinear force response of an arbitrary air spring.
This is the effective force to achieve a given height, which is equivalent to the
**Load vector** parameter or the element-wise product of the
**Stiffness vector** parameter and the **Height
vector** parameter. For more information about using lookup tables in
Simscape™, see `tablelookup`.

The block takes the relative translational motion between port **R** and
port **C** to evaluate the air spring height and velocity and uses this
information to find the appropriate lookup table entry. The block computes the nonlinear
effective force response *ΣF(x(t),t)*, such that:

∑F(x(t),t)=−c(x(t))x˙(t)−k(x(t))x(t)+Fexternal,

where

- *x(t)* is the height of the spring relative to the
  undisturbed position.
- *ẋ(t)* is the velocity of the spring.
- *-c(x(t))ẋ(t)* is the viscous damping force. The
  damping coefficient *c* varies with spring height.
- *-k(x(t))x(t)* is the stiffness force. The spring
  coefficient *k* varies with spring height.
- *Fexternal* is the force
  transmitted through the ports.

You can choose whether to implement hard stops in your model on the **Hard
Stops** tab. When you set **Hard stop at full extension**
or **Hard stop at full compression** to `On`,
you can specify a boundary height, the stiffness and damping at that height, and the
length of the transition region. The hard stops are equivalent to the Translational Hard Stop block.

### Variables

Use the **Variables** tab to set the priority and initial target
values for the block variables before simulating. For more information, see Set Priority and Initial Target for Block Variables.

The sign of the **Force** variable is negative when the load is
positive.
