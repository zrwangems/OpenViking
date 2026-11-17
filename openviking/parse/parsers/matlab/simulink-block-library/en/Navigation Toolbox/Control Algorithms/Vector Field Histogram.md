---
type: simulink-block
title: 'Vector Field Histogram'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Control Algorithms'
documentation_page: 'vectorfieldhistogram'
documentation_source_path: 'ref/vectorfieldhistogram.html'
language: en
---

# Vector Field Histogram

## Ports
```yaml
ports:
- name: Ranges
  summary: Range values from scan data vector of scalars
  direction: input
- name: Angles
  summary: Angle values from scan data vector of scalars
  direction: input
- name: TargetDir
  summary: Target direction for vehicle scalar
  direction: input
- name: SteerDir
  summary: Steering direction for vehicle scalar
  direction: output
```

### Input

### **Ranges** — Range values from scan data vector of scalars

Range values from scan data, specified as a vector of scalars
in meters. These range values are distances from a sensor at specified
angles. The vector must be the same length as the corresponding **Angles** vector.

### **Angles** — Angle values from scan data vector of scalars

Angle values from scan data, specified as a vector of scalars
in radians. These angle values are the specific angles of the specified
ranges. The vector must be the same length as the corresponding **Ranges** vector.

### **TargetDir** — Target direction for vehicle scalar

Target direction for the vehicle, specified as a scalar in radians.
The forward direction of the vehicle is considered zero radians, with
positive angles measured counterclockwise. You can use the
**TargetDir** output from the Pure Pursuit block when
generating controls from a set of waypoints.
### Output

### **SteerDir** — Steering direction for vehicle scalar

Steering direction for the vehicle, specified as a scalar in radians.
This obstacle-free direction is calculated based on the VFH+ algorithm.
The forward direction of the vehicle is considered zero radians, with
positive angles measured counterclockwise.
## Parameters
```yaml
parameters:
- name: Number of angular sectors
  summary: Number of bins used to create the histograms 180 (default) | scalar
  group: ''
- name: Range distance limits (m)
  summary: Limits for range readings [0.05 2] (default) | two-element vector of scalars
  group: ''
- name: Histogram thresholds
  summary: Thresholds for computing binary histogram [3 10] (default) | two-element vector of scalars
  group: ''
- name: vehicle radius (m)
  summary: Radius of the vehicle 0.1 (default) | scalar
  group: ''
- name: Safety distance (m)
  summary: Safety distance around the vehicle 0.1 (default) | scalar
  group: ''
- name: Minimum turning radius (m)
  summary: Minimum turning radius at current speed 0.1 (default) | scalar
  group: ''
- name: Simulate using
  summary: Specify type of simulation to run Code generation (default) | Interpreted execution
  group: ''
- name: Target direction weight
  summary: Cost function weight for target direction 5 (default) | scalar
  group: ''
- name: Current direction weight
  summary: Cost function weight for current direction 2 (default) | scalar
  group: ''
- name: Previous direction weight
  summary: Cost function weight for previous direction 2 (default) | scalar
  group: ''
```

#### Main

### **Number of angular sectors** — Number of bins used to create the histograms `180` (default) | scalar

Number of bins used to create the histograms, specified as a scalar. This
parameter is nontunable. You can set this parameter only when the object is
initialized.

### **Range distance limits (m)** — Limits for range readings `[0.05 2]` (default) | two-element vector of scalars

Limits for range readings in meters, specified as a two-element vector of
scalars. The range readings input are only considered if they fall within
the distance limits. Use the lower distance limit to ignore false positives
from poor sensor performance at lower ranges. Use the upper limit to ignore
obstacles that are too far away from the vehicle.

### **Histogram thresholds** — Thresholds for computing binary histogram `[3 10]` (default) | two-element vector of scalars

Thresholds for computing binary histogram, specified as a two-element
vector of scalars. The algorithm uses these thresholds to compute the binary
histogram from the polar obstacle density. Polar obstacle density values
higher than the upper threshold are represented as occupied space (1) in the
binary histogram. Values smaller than the lower threshold are represented as
free space (0). Values that fall between the limits are set to the values of
a previous computed binary histogram if one exists from previous iterations.
If a previous histogram does not exist, the value is set as free space
(0).

### **vehicle radius (m)** — Radius of the vehicle `0.1` (default) | scalar

Radius of the vehicle, specified as a scalar in meters. This dimension
defines the smallest circle that can circumscribe your vehicle. The vehicle
radius is used to account for vehicle size when computing the obstacle-free
direction.

### **Safety distance (m)** — Safety distance around the vehicle `0.1` (default) | scalar

Safety distance left around the vehicle position in addiction to
**vehicle radius**, specified as a scalar in meters.
The vehicle radius and safety distance are used to compute the obstacle-free
direction.

### **Minimum turning radius (m)** — Minimum turning radius at current speed `0.1` (default) | scalar

Minimum turning radius for the vehicle moving at its current speed,
specified as a scalar in meters.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Code generation` — Simulate model
  using generated C code. The first time you run a simulation,
  Simulink® generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.
- `Interpreted execution` — Simulate
  model using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.

**Tunable:** No

#### Cost Function Weights

### **Target direction weight** — Cost function weight for target direction `5` (default) | scalar

Cost function weight for moving toward the target direction, specified as
a scalar. To follow a target direction, set this weight to be higher than
the sum of **Current direction weight** and
**Previous direction weight**. To ignore the target
direction cost, set this weight to `0`.

### **Current direction weight** — Cost function weight for current direction `2` (default) | scalar

Cost function weight for moving the vehicle in the current heading
direction, specified as a scalar. Higher values of this weight produce
efficient paths. To ignore the current direction cost, set this weight to
`0`.

### **Previous direction weight** — Cost function weight for previous direction `2` (default) | scalar

Cost function weight for moving in the previously selected steering
direction, specified as a scalar. Higher values of this weight produce
smoother paths. To ignore the previous direction cost, set this weight to
`0`.
## Libraries

Navigation Toolbox / Control Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Avoid obstacles using vector field histogram

The Vector Field Histogram (VFH) block enables your vehicle to avoid obstacles
based on range sensor data. Given a range sensor reading in terms of ranges and angles,
and a target direction to drive toward, the VFH controller computes an obstacle-free
steering direction.

For more information on the algorithm details, see Vector Field Histogram under Algorithms.
