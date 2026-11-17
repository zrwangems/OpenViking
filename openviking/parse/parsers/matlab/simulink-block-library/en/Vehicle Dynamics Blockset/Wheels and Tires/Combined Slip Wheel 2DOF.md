---
type: simulink-block
title: 'Combined Slip Wheel 2DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'combinedslipwheel2dof'
documentation_source_path: 'ref/combinedslipwheel2dof.html'
language: en
---

# Combined Slip Wheel 2DOF

## Ports
```yaml
ports:
- name: BrkPrs
  summary: Brake pressure scalar | *N*-by-1 vector
  direction: input
- name: AxlTrq
  summary: Axle torque scalar | *N*-by-1 vector
  direction: input
- name: Vx
  summary: Longitudinal velocity scalar | *N*-by-1 vector
  direction: input
- name: Vy
  summary: Lateral velocity scalar | *N*-by-1 vector
  direction: input
- name: Camber
  summary: Inclination angle scalar | *N*-by-1 vector
  direction: input
- name: YawRate
  summary: Tire angular velocity scalar | *N*-by-1 vector
  direction: input
- name: Prs
  summary: Tire inflation pressure scalar | *N*-by-1 vector
  direction: input
- name: Gnd
  summary: Ground displacement scalar | *N*-by-1 vector
  direction: input
- name: Fext
  summary: Axle force applied to tire scalar | *N*-by-1 vector
  direction: input
- name: RadialDeflct
  summary: Tire radial deflection scalar | *N*-by-1 vector
  direction: input
- name: ScaleFctrs
  summary: Scale factors 27-by-N array
  direction: input
- name: Info
  summary: Block data bus
  direction: output
- name: Omega
  summary: Wheel angular velocity scalar | *N*-by-1 vector
  direction: output
- name: Fx
  summary: Longitudinal axle force scalar | *N*-by-1 vector
  direction: output
- name: Fy
  summary: Lateral axle force scalar | *N*-by-1 vector
  direction: output
- name: Fz
  summary: Vertical axle force scalar | *N*-by-1 vector
  direction: output
- name: Mx
  summary: Overturning moment scalar | *N*-by-1 vector
  direction: output
- name: My
  summary: Rolling resistive moment scalar | *N*-by-1 vector
  direction: output
- name: Mz
  summary: Aligning moment scalar | *N*-by-1 vector
  direction: output
```

### Input

### **BrkPrs** — Brake pressure scalar | *N*-by-`1` vector

Brake pressure, in Pa.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

#### Dependencies

To enable this port, set the **Brake Type** parameter, to one of
these types:

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — Axle torque scalar | *N*-by-`1` vector

Axle torque, *Ta*, about wheel spin axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Vx** — Longitudinal velocity scalar | *N*-by-`1` vector

Axle longitudinal velocity, *Vx*, along
tire-fixed *x*-axis, in m/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Vy** — Lateral velocity scalar | *N*-by-`1` vector

Axle lateral velocity, *Vy*, along tire-fixed
*y*-axis, in m/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Camber** — Inclination angle scalar | *N*-by-`1` vector

Camber angle, *ɣ*, or inclination angle, *ε*, in
rad.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **YawRate** — Tire angular velocity scalar | *N*-by-`1` vector

Tire angular velocity, *r*, about the tire-fixed
*z*-axis (yaw rate), in rad/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Prs** — Tire inflation pressure scalar | *N*-by-`1` vector

Tire inflation pressure, *pi*, in Pa.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Gnd** — Ground displacement scalar | *N*-by-`1` vector

Ground displacement along tire-fixed *z*-axis, in m. Positive input
produces wheel lift.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fext** — Axle force applied to tire scalar | *N*-by-`1` vector

Axle force applied to tire, *Fext*, along
vehicle-fixed *z*-axis (positive input compresses the tire), in
N.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

#### Dependencies

To enable this parameter, set **Vertical Motion** to
`None` or `Magic
Formula`.

### **RadialDeflct** — Tire radial deflection scalar | *N*-by-`1` vector

Tire radial deflection, *RadialDeflct*, in m. This
value will be used in all internal dependent magic formula equations
that rely on deflection.

Vector is the number of wheels,
*N*, by `1`. If you provide a
scalar value, the block assumes that number of wheels is one.

#### Dependencies

To enable this port, set **Vertical Motion** to
`External Deflection`.

### **ScaleFctrs** — Scale factors `27`-by-`N` array

Magic Formula 6.2 scale factor array. Array dimensions are `27` by
the number of wheels, *N*.

The Magic Formula 6.2 equations use scale factors to account for static or simulation
run-time variations. Nominally, most are set to `1`.

| Array Element | Variable | Scale Factor |
| --- | --- | --- |
| `ScaleFctrs(1,1)` | `lam_Fzo` | Nominal load |
| `ScaleFctrs(2,1)` | `lam_mux` | Longitudinal peak friction coefficient |
| `ScaleFctrs(3,1)` | `lam_muy` | Lateral peak friction coefficient |
| `ScaleFctrs(4,1)` | `lam_muV` | Slip speed, *Vs*, decaying friction |
| `ScaleFctrs(5,1)` | `lam_Kxkappa` | Brake slip stiffness |
| `ScaleFctrs(6,1)` | `lam_Kyalpha` | Cornering stiffness |
| `ScaleFctrs(7,1)` | `lam_Cx` | Longitudinal shape factor |
| `ScaleFctrs(8,1)` | `lam_Cy` | Lateral shape factor |
| `ScaleFctrs(9,1)` | `lam_Ex` | Longitudinal curvature factor |
| `ScaleFctrs(10,1)` | `lam_Ey` | Lateral curvature factor |
| `ScaleFctrs(11,1)` | `lam_Hx` | Longitudinal horizontal shift |
| `ScaleFctrs(12,1)` | `lam_Hy` | Lateral horizontal shift |
| `ScaleFctrs(13,1)` | `lam_Vx` | Longitudinal vertical shift |
| `ScaleFctrs(14,1)` | `lam_Vy` | Lateral vertical shift |
| `ScaleFctrs(15,1)` | `lam_Kygamma` | Camber force stiffness |
| `ScaleFctrs(16,1)` | `lam_Kzgamma` | Camber torque stiffness |
| `ScaleFctrs(17,1)` | `lam_t` | Pneumatic trail (effecting aligning torque stiffness) |
| `ScaleFctrs(18,1)` | `lam_Mr` | Residual torque |
| `ScaleFctrs(19,1)` | `lam_xalpha` | Alpha influence on *Fx* (kappa) |
| `ScaleFctrs(20,1)` | `lam_ykappa` | Kappa influence on *Fy* (alpha) |
| `ScaleFctrs(21,1)` | `lam_Vykappa` | Induced ply steer *Fy* |
| `ScaleFctrs(22,1)` | `lam_s` | Moment arm of *Fx* |
| `ScaleFctrs(23,1)` | `lam_Cz` | Radial tire stiffness |
| `ScaleFctrs(24,1)` | `lam_Mx` | Overturning couple stiffness |
| `ScaleFctrs(25,1)` | `lam_VMx` | Overturning couple vertical shift |
| `ScaleFctrs(26,1)` | `lam_My` | Rolling resistance moment |
| `ScaleFctrs(27,1)` | `lam_Mphi` | Parking torque *Mz* |
### Output

### **Info** — Block data bus

Block data, returned as a bus signal containing these block
values.

| Signal | Description | Units |
| --- | --- | --- |
| `AxlTrq` | Axle torque about wheel-fixed *y*-axis | N·m |
| `Omega` | Wheel angular velocity about wheel-fixed *y*-axis | rad/s |
| `Fx` | Longitudinal vehicle force along tire-fixed *x*-axis | N |
| `Fy` | Lateral vehicle force along tire-fixed *y*-axis | N |
| `Fz` | Vertical vehicle force along tire-fixed *z*-axis | N |
| `Mx` | Overturning moment about tire-fixed *x*-axis | N·m |
| `My` | Rolling resistance torque about tire-fixed *y*-axis | N·m |
| `Mz` | Aligning moment about tire-fixed *z*-axis | N·m |
| `Vx` | Vehicle longitudinal velocity along tire-fixed *x*-axis | m/s |
| `Vy` | Vehicle lateral velocity along tire-fixed *y*-axis | m/s |
| `Re` | Loaded effective radius | m |
| `Kappa` | Longitudinal slip ratio | NA |
| `Alpha` | Side slip angle | rad |
| `a` | Contact patch half length | m |
| `b` | Contact patch half width | m |
| `RL` | Loaded radius | m |
| `RadialDeflct` | Tire radial deflection | m |
| `WhlTrq` | Wheel torque | N·m |
| `Gamma` | Camber angle | rad |
| `psidot` | Tire angular velocity about the tire-fixed *z*-axis (yaw rate) | rad/s |
| `BrkTrq` | Brake torque about vehicle-fixed *y*-axis | N·m |
| `BrkPrs` | Brake pressure | Pa |
| `z` | Axle local vertical displacement along tire-fixed *z*-axis | m |
| `zdot` | Axle vertical velocity along tire-fixed *z*-axis | m/s |
| `Gnd` | Ground displacement along tire-fixed *z*-axis (positive input produces wheel lift) | m |
| `GndFz` | Vertical sidewall force on ground along tire-fixed *z*-axis | N |
| `Prs` | Tire inflation pressure | Pa |

### **Omega** — Wheel angular velocity scalar | *N*-by-`1` vector

Wheel angular velocity, *ω*, about wheel-fixed *y*-axis, in rad/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fx** — Longitudinal axle force scalar | *N*-by-`1` vector

Longitudinal force acting on axle, *Fx*, along
tire-fixed *x*-axis, in N. Positive force acts to move the vehicle
forward.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fy** — Lateral axle force scalar | *N*-by-`1` vector

Lateral force acting on axle, *Fy*, along
tire-fixed *y*-axis, in N.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fz** — Vertical axle force scalar | *N*-by-`1` vector

Vertical force acting on axle, *Fz*, along
tire-fixed *z*-axis, in N.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Mx** — Overturning moment scalar | *N*-by-`1` vector

Longitudinal moment acting on axle, *Mx*,
about tire-fixed *x*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **My** — Rolling resistive moment scalar | *N*-by-`1` vector

Lateral moment acting on axle, *My*, about
tire-fixed *y*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Mz** — Aligning moment scalar | *N*-by-`1` vector

Vertical moment acting on axle, *Mz*, about
tire-fixed *z*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.
## Parameters
```yaml
parameters:
- name: Tire type
  summary: Select type External file | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger
    car 235/45R18 | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
  group: Tire Options
  block_parameter: tireType
  values: External file | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger car 235/45R18
    | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
- name: Tire file or object, tireParamSet
  summary: Tire file vdynPassCar.mat (default) | .tir | .txt
  group: Tire Options
  block_parameter: tireParamSet
  values: vdynPassCar.mat (default) | .tir | .txt
- name: Vertical Motion
  summary: Vertical motion model Magic Formula (default) | None | External deflection
  group: Tire Options
  block_parameter: vertType
  values: Magic Formula (default) | None | External deflection
- name: Ply steer
  summary: Include ply steer on (default) | off
  group: Tire Options
  block_parameter: plySteer
  values: on (default) | off
- name: Turn slip
  summary: Include turn slip on (default) | off
  group: Tire Options
  block_parameter: turnslip
  values: on (default) | off
- name: Brake type
  summary: Brake type None | Disc | Drum | Mapped
  group: Tire Options
  block_parameter: BrakeType
  values: None | Disc | Drum | Mapped
- name: Install Extended Tire Features
  summary: Option to install Extended Tire Features for Vehicle Dynamics Blockset™ support package button
  group: Plotting
- name: Plot steady state force, moment response
  summary: Option to plot steady-state force and moment tire responses button
  group: Plotting
- name: Static friction coefficient, mu_static
  summary: Static friction coefficient 0.3 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: mu_static
  values: 0.3 (default) | scalar | *N*-by-1 vector
- name: Kinetic friction coefficient, mu_kinetic
  summary: Kinetic friction 0.2 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: mu_kinetic
  values: 0.2 (default) | scalar | *N*-by-1 vector
- name: Disc brake actuator bore, disc_abore
  summary: Bore distance 0.05 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: disc_abore
  values: 0.05 (default) | scalar | *N*-by-1 vector
- name: Brake pad mean radius, Rm
  summary: Radius 0.177 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: Rm
  values: 0.177 (default) | scalar | *N*-by-1 vector
- name: Number of brake pads, num_pads
  summary: Number of brake pads 2 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: num_pads
  values: 2 (default) | scalar | *N*-by-1 vector
- name: Drum brake actuator bore, drum_abore
  summary: Bore distance 0.0508 (default) | scalar | *N*-by-1 vector
  group: Brake
  block_parameter: drum_abore
  values: 0.0508 (default) | scalar | *N*-by-1 vector
- name: Shoe pin to drum center distance, drum_a
  summary: Shoe pin to drum center distance 0.123 (default) | scalar
  group: Brake
  block_parameter: drum_a
  values: 0.123 (default) | scalar
- name: Shoe pin center to force application point distance, drum_c
  summary: Shoe pin center to force application point distance 0.212 (default) | scalar
  group: Brake
  block_parameter: drum_c
  values: 0.212 (default) | scalar
- name: Drum internal radius, drum_r
  summary: Drum internal radius 0.15 (default) | scalar
  group: Brake
  block_parameter: drum_r
  values: 0.15 (default) | scalar
- name: Shoe pin to pad start angle, drum_theta1
  summary: Shoe pin to pad start angle 0 (default) | scalar
  group: Brake
  block_parameter: drum_theta1
  values: 0 (default) | scalar
- name: Shoe pin to pad end angle, drum_theta2
  summary: Shoe pin to pad end angle 126 (default) | scalar
  group: Brake
  block_parameter: drum_theta2
  values: 126 (default) | scalar
- name: Brake actuator pressure breakpoints, brake_p_bpt
  summary: Brake actuator pressure breakpoints vector
  group: Brake
  block_parameter: brake_p_bpt
  values: vector
- name: Wheel speed breakpoints, brake_n_bpt
  summary: Wheel speed breakpoints vector
  group: Brake
  block_parameter: brake_n_bpt
  values: vector
- name: Brake torque map, f_brake_t
  summary: Lookup table for brake torque array
  group: Brake
  block_parameter: f_brake_t
  values: vector
- name: Nominal pressure, NOMPRES
  summary: Pressure scalar
  group: Simulation
  block_parameter: NOMPRES
  values: scalar
- name: Maximum pressure, PRESMAX
  summary: Maximum pressure scalar
  group: Simulation
  block_parameter: PRESMAX
  values: scalar
- name: Minimum pressure, PRESMIN
  summary: Minimum pressure scalar
  group: Simulation
  block_parameter: PRESMIN
  values: scalar
- name: Nominal normal force, FNOMIN
  summary: Force scalar
  group: Simulation
  block_parameter: FNOMIN
  values: scalar
- name: Maximum normal force, FZMAX
  summary: Force scalar
  group: Simulation
  block_parameter: FZMAX
  values: scalar
- name: Minimum normal force, FZMIN
  summary: Force scalar
  group: Simulation
  block_parameter: FZMIN
  values: scalar
- name: Velocity tolerance used to handle low velocity situations, VXLOW
  summary: Tolerance scalar
  group: Simulation
  block_parameter: VXLOW
  values: scalar
- name: Max allowable slip ratio (absolute), KPUMAX
  summary: Max allowable slip ratio scalar
  group: Simulation
  block_parameter: KPUMAX
  values: scalar
- name: Minimum allowable slip ratio (absolute), KPUMIN
  summary: Minimum allowable slip ratio scalar
  group: Simulation
  block_parameter: KPUMIN
  values: scalar
- name: Max allowable slip angle (absolute), ALPMAX
  summary: Max allowable slip angle scalar
  group: Simulation
  block_parameter: ALPMAX
  values: scalar
- name: Minimum allowable slip angle (absolute), ALPMIN
  summary: Minimum allowable slip angle scalar
  group: Simulation
  block_parameter: ALPMIN
  values: scalar
- name: Maximum allowable camber angle, CAMMAX
  summary: Maximum allowable camber angle scalar
  group: Simulation
  block_parameter: CAMMAX
  values: scalar
- name: Minimum allowable camber angle, CAMMIN
  summary: Minimum allowable camber angle scalar
  group: Simulation
  block_parameter: CAMMIN
  values: scalar
- name: Nominal longitudinal speed, LONGVL
  summary: Speed scalar
  group: Simulation
  block_parameter: LONGVL
  values: scalar
- name: Initial wheel rotational velocity, omegao
  summary: Initial wheel rotational velocity scalar | *N*-by-1 vector
  group: Simulation
  block_parameter: omegao
  values: scalar | *N*-by-1 vector
- name: Tire unloaded radius, UNLOADED_RADIUS
  summary: Radius scalar
  group: Dimension
  block_parameter: UNLOADED_RADIUS
  values: scalar
- name: Tire nominal section width, WIDTH
  summary: Tire nominal section width scalar
  group: Dimension
  block_parameter: WIDTH
  values: scalar
- name: Rim radius, RIM_RADIUS
  summary: Radius scalar
  group: Dimension
  block_parameter: RIM_RADIUS
  values: scalar
- name: Nominal aspect ratio, ASPECT_RATIO
  summary: Ratio scalar
  group: Dimension
  block_parameter: ASPECT_RATIO
  values: scalar
- name: Tire mass, MASS
  summary: Mass scalar | *N*-by-1 vector
  group: Inertial and Damping
  block_parameter: MASS
  values: scalar | *N*-by-1 vector
- name: Tire rotational inertia (rolling axis), IYY
  summary: Tire rotational inertia scalar | *N*-by-1 vector
  group: Inertial and Damping
  block_parameter: IYY
  values: scalar | *N*-by-1 vector
- name: Rotational damping, br
  summary: Rotational damping scalar | *N*-by-1 vector
  group: Inertial and Damping
  block_parameter: br
  values: scalar | *N*-by-1 vector
- name: Gravity, GRAVITY
  summary: Gravity scalar
  group: Inertial and Damping
  block_parameter: GRAVITY
  values: scalar
- name: Initial tire displacement, zo
  summary: Displacement scalar | *N*-by-1 vector
  group: Vertical
  block_parameter: zo
  values: scalar | *N*-by-1 vector
- name: Initial wheel vertical velocity (wheel fixed frame), zdoto
  summary: Velocity scalar | *N*-by-1 vector
  group: Vertical
  block_parameter: zdoto
  values: scalar | *N*-by-1 vector
- name: Effective rolling radius at low load stiffness, BREFF
  summary: Stiffness scalar
  group: Vertical
  block_parameter: BREFF
  values: scalar
- name: Effective rolling radius peak value, DREFF
  summary: Radius scalar
  group: Vertical
  block_parameter: DREFF
  values: scalar
- name: Effective rolling radius at high load stiffness, FREFF
  summary: Radius scalar
  group: Vertical
  block_parameter: FREFF
  values: scalar
- name: Unloaded to nominal rolling radius ratio, Q_RE0
  summary: Ratio scalar
  group: Vertical
  block_parameter: Q_RE0
  values: scalar
- name: Radius rotational speed dependence, Q_V1
  summary: Speed scalar
  group: Vertical
  block_parameter: Q_V1
  values: scalar
- name: Stiffness rotational speed dependence, Q_V2
  summary: Speed scalar
  group: Vertical
  block_parameter: Q_V2
  values: scalar
- name: Linear load change with deflection, Q_FZ1
  summary: Load change scalar
  group: Vertical
  block_parameter: Q_FZ1
  values: scalar
- name: Quadratic load change with deflection, Q_FZ2
  summary: Load change scalar
  group: Vertical
  block_parameter: Q_FZ2
  values: scalar
- name: Linear load change with deflection and quadratic camber, Q_FZ3
  summary: Load change scalar
  group: Vertical
  block_parameter: Q_FZ3
  values: scalar
- name: Load response to longitudinal force, Q_FCX
  summary: Force scalar
  group: Vertical
  block_parameter: Q_FCX
  values: scalar
- name: Load response to lateral force, Q_FCY
  summary: Force scalar
  group: Vertical
  block_parameter: Q_FCY
  values: scalar
- name: Vertical stiffness change due to lateral load dependency on lateral stiffness, Q_FCY2
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_FCY2
  values: scalar
- name: Stiffness response to pressure, PFZ1
  summary: Stiffness 0.7098 (default) | scalar
  group: Vertical
  block_parameter: PFZ1
  values: 0.7098 (default) | scalar
- name: Vertical tire stiffness, VERTICAL_STIFFNESS
  summary: Stiffness scalar
  group: Vertical
  block_parameter: VERTICAL_STIFFNESS
  values: scalar
- name: Vertical tire damping, VERTICAL_DAMPING
  summary: Damping scalar
  group: Vertical
  block_parameter: VERTICAL_DAMPING
  values: scalar
- name: Rim bottoming out offset, BOTTOM_OFFST
  summary: Offset scalar
  group: Vertical
  block_parameter: BOTTOM_OFFST
  values: scalar
- name: Bottoming out stiffness, BOTTOM_STIFF
  summary: Stiffness scalar
  group: Vertical
  block_parameter: BOTTOM_STIFF
  values: scalar
- name: Linear load dependent camber angle effect on vertical stiffness, Q_CAM1
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_CAM1
  values: scalar
- name: Quadratic load dependent camber angle effect on vertical stiffness, Q_CAM2
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_CAM2
  values: scalar
- name: Linear reduction of stiffness with load and camber angle, Q_CAM3
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_CAM3
  values: scalar
- name: Constant camber and slip angle effect on vertical stiffness, Q_FYS1
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_FYS1
  values: scalar
- name: Linear camber and slip angle effect on vertical stiffness, Q_FYS2
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_FYS2
  values: scalar
- name: Quadratic camber and slip angle effect on vertical stiffness, Q_FYS3
  summary: Stiffness scalar
  group: Vertical
  block_parameter: Q_FYS3
  values: scalar
- name: Longitudinal stiffness, LONGITUDINAL_STIFFNESS
  summary: Stiffness scalar
  group: Structural
  block_parameter: LONGITUDINAL_STIFFNESS
  values: scalar
- name: Lateral stiffness, LATERAL_STIFFNESS
  summary: Stiffness scalar
  group: Structural
  block_parameter: LATERAL_STIFFNESS
  values: scalar
- name: Linear vertical deflection influence on longitudinal stiffness, PCFX1
  summary: Deflection influence scalar
  group: Structural
  block_parameter: PCFX1
  values: scalar
- name: Quadratic vertical deflection influence on longitudinal stiffness, PCFX2
  summary: Deflection influence scalar
  group: Structural
  block_parameter: PCFX2
  values: scalar
- name: Pressure dependency on longitudinal stiffness, PCFX3
  summary: Pressure dependency scalar
  group: Structural
  block_parameter: PCFX3
  values: scalar
- name: Linear vertical deflection influence on lateral stiffness, PCFY1
  summary: Deflection influence scalar
  group: Structural
  block_parameter: PCFY1
  values: scalar
- name: Quadratic vertical deflection influence on lateral stiffness, PCFY2
  summary: Deflection influence scalar
  group: Structural
  block_parameter: PCFY2
  values: scalar
- name: Pressure dependency on longitudinal stiffness, PCFY3
  summary: Pressure dependency scalar
  group: Structural
  block_parameter: PCFY3
  values: scalar
- name: Contact length square root term, Q_RA1
  summary: Length term scalar
  group: Contact Patch
  block_parameter: Q_RA1
  values: scalar
- name: Contact length linear term, Q_RA2
  summary: Length term scalar
  group: Contact Patch
  block_parameter: Q_RA2
  values: scalar
- name: Contact width root term, Q_RB1
  summary: Width term scalar
  group: Contact Patch
  block_parameter: Q_RB1
  values: scalar
- name: Contact width linear term, Q_RB2
  summary: Width term scalar
  group: Contact Patch
  block_parameter: Q_RB2
  values: scalar
- name: Cfx shape factor, PCX1
  summary: Shape factor scalar
  group: Longitudinal
  block_parameter: PCX1
  values: scalar
- name: Longitudinal friction at nominal normal load, PDX1
  summary: Friction scalar
  group: Longitudinal
  block_parameter: PDX1
  values: scalar
- name: Frictional variation with load, PDX2
  summary: Friction variation scalar
  group: Longitudinal
  block_parameter: PDX2
  values: scalar
- name: Frictional variation with camber, PDX3
  summary: Friction variation scalar
  group: Longitudinal
  block_parameter: PDX3
  values: scalar
- name: Longitudinal curvature at nominal normal load, PEX1
  summary: Curvature scalar
  group: Longitudinal
  block_parameter: PEX1
  values: scalar
- name: Variation of curvature factor with load, PEX2
  summary: Curvature variation scalar
  group: Longitudinal
  block_parameter: PEX2
  values: scalar
- name: Variation of curvature factor with square of load, PEX3
  summary: Curvature variation scalar
  group: Longitudinal
  block_parameter: PEX3
  values: scalar
- name: Longitudinal curvature factor with slip, PEX4
  summary: Curvature scalar
  group: Longitudinal
  block_parameter: PEX4
  values: scalar
- name: Longitudinal slip stiffness at nominal normal load, PKX1
  summary: Stiffness scalar
  group: Longitudinal
  block_parameter: PKX1
  values: scalar
- name: Variation of slip stiffness with load, PKX2
  summary: Stiffness variation scalar
  group: Longitudinal
  block_parameter: PKX2
  values: scalar
- name: Slip stiffness exponent factor, PKX3
  summary: Slip stiffness scalar
  group: Longitudinal
  block_parameter: PKX3
  values: scalar
- name: Horizontal shift in slip ratio at nominal normal load, PHX1
  summary: Slip ratio shift scalar
  group: Longitudinal
  block_parameter: PHX1
  values: scalar
- name: Variation of horizontal slip ratio with load, PHX2
  summary: Slip variation scalar
  group: Longitudinal
  block_parameter: PHX2
  values: scalar
- name: Vertical shift in load at nominal normal load, PVX1
  summary: Load shift scalar
  group: Longitudinal
  block_parameter: PVX1
  values: scalar
- name: Variation of vertical shift with load, PVX2
  summary: Load variation scalar
  group: Longitudinal
  block_parameter: PVX2
  values: scalar
- name: Linear variation of longitudinal slip stiffness with tire pressure, PPX1
  summary: Stiffness variation scalar
  group: Longitudinal
  block_parameter: PPX1
  values: scalar
- name: Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2
  summary: Stiffness variation scalar
  group: Longitudinal
  block_parameter: PPX2
  values: scalar
- name: Linear variation of peak longitudinal friction with tire pressure, PPX3
  summary: Friction variation scalar
  group: Longitudinal
  block_parameter: PPX3
  values: scalar
- name: Quadratic variation of peak longitudinal friction with tire pressure, PPX4
  summary: Friction variation scalar
  group: Longitudinal
  block_parameter: PPX4
  values: scalar
- name: Combined slip Fx slope factor reduction, RBX1
  summary: Combined slip longitudinal force slope factor reduction scalar
  group: Longitudinal
  block_parameter: RBX1
  values: scalar
- name: Slip ratio Fx slope reduction variation, RBX2
  summary: Slip ratio longitudinal force slope reduction variation scalar
  group: Longitudinal
  block_parameter: RBX2
  values: scalar
- name: Camber influence on combined slip Fx stiffness, RBX3
  summary: Camber influence on combined slip longitudinal force stiffness scalar
  group: Longitudinal
  block_parameter: RBX3
  values: scalar
- name: Shape factor for combined slip Fx reduction, RCX1
  summary: Shape factor for combined slip longitudinal force reduction scalar
  group: Longitudinal
  block_parameter: RCX1
  values: scalar
- name: Combined Fx curvature factor, REX1
  summary: Combined longitudinal force curvature factor scalar
  group: Longitudinal
  block_parameter: REX1
  values: scalar
- name: Combined Fx curvature factor with load, REX2
  summary: Combined longitudinal force curvature factor scalar
  group: Longitudinal
  block_parameter: REX2
  values: scalar
- name: Combined slip Fx shift factor reduction, RHX1
  summary: Combined slip longitudinal force slip factor scalar
  group: Longitudinal
  block_parameter: RHX1
  values: scalar
- name: Vertical shift of overturning moment, QSX1
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX1
  values: scalar
- name: Overturning moment due to camber, QSX2
  summary: Overturning moment due to camber scalar
  group: Overturning
  block_parameter: QSX2
  values: scalar
- name: Overturning moment due to Fy, QSX3
  summary: Overturning moment due to lateral force scalar
  group: Overturning
  block_parameter: QSX3
  values: scalar
- name: Mx combined lateral force load and camber, QSX4
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX4
  values: scalar
- name: Mx load effect due to lateral force and camber, QSX5
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX5
  values: scalar
- name: Mx load effect due to B-factor, QSX6
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX6
  values: scalar
- name: Mx due to camber and load, QSX7
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX7
  values: scalar
- name: Mx due to lateral force and load, QSX8
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX8
  values: scalar
- name: Mx due to B-factor of lateral force and load, QSX9
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX9
  values: scalar
- name: Mx due to vertical force and camber, QSX10
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX10
  values: scalar
- name: Mx due to B-factor of vertical force and camber, QSX11
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX11
  values: scalar
- name: Mx due to squared camber, QSX12
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX12
  values: scalar
- name: Mx due to lateral force, QSX13
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX13
  values: scalar
- name: Mx due to lateral force with camber, QSX14
  summary: Overturning moment scalar
  group: Overturning
  block_parameter: QSX14
  values: scalar
- name: Mx due to inflation pressure, PPMX1
  summary: Overturning moment due to pressure scalar
  group: Overturning
  block_parameter: PPMX1
  values: scalar
- name: Cfy shape factor for lateral force, PCY1
  summary: Lateral force shape factor scalar
  group: Lateral
  block_parameter: PCY1
  values: scalar
- name: Lateral friction muy, PDY1
  summary: Lateral friction scalar
  group: Lateral
  block_parameter: PDY1
  values: scalar
- name: Lateral friction variation of muy with load, PDY2
  summary: Lateral friction variation scalar
  group: Lateral
  block_parameter: PDY2
  values: scalar
- name: Lateral friction variation of muy with squared camber, PDY3
  summary: Lateral friction variation scalar
  group: Lateral
  block_parameter: PDY3
  values: scalar
- name: Efy lateral curvature at nominal force FZNOM, PEY1
  summary: Lateral curvature at nominal force scalar
  group: Lateral
  block_parameter: PEY1
  values: scalar
- name: Efy curvature variation with load, PEY2
  summary: Lateral curvature variation scalar
  group: Lateral
  block_parameter: PEY2
  values: scalar
- name: Efy curvature constant camber dependency, PEY3
  summary: Lateral curvature constant scalar
  group: Lateral
  block_parameter: PEY3
  values: scalar
- name: Efy curvature variation with camber, PEY4
  summary: Lateral curvature variation scalar
  group: Lateral
  block_parameter: PEY4
  values: scalar
- name: Efy curvature variation with camber squared, PEY5
  summary: Lateral curvature variation scalar
  group: Lateral
  block_parameter: PEY5
  values: scalar
- name: Maximum KFy/FZNOM stiffness, PKY1
  summary: Maximum stiffness scalar
  group: Lateral
  block_parameter: PKY1
  values: scalar
- name: Load at maximum KFy/FZNOM stiffness, PKY2
  summary: Load scalar
  group: Lateral
  block_parameter: PKY2
  values: scalar
- name: KFy/FZNOM stiffness variation with camber, PKY3
  summary: Stiffness variation scalar
  group: Lateral
  block_parameter: PKY3
  values: scalar
- name: KFy curvature, PKY4
  summary: Lateral force stiffness curvature scalar
  group: Lateral
  block_parameter: PKY4
  values: scalar
- name: Variation of peak stiffness with squared camber, PKY5
  summary: Stiffness variation scalar
  group: Lateral
  block_parameter: PKY5
  values: scalar
- name: Fy camber stiffness factor, PKY6
  summary: Lateral force camber stiffness factor scalar
  group: Lateral
  block_parameter: PKY6
  values: scalar
- name: Camber stiffness vertical load dependency, PKY7
  summary: Stiffness scalar
  group: Lateral
  block_parameter: PKY7
  values: scalar
- name: SHY horizontal shift at FZNOM, PHY1
  summary: Horizontal shift at nominal force scalar
  group: Lateral
  block_parameter: PHY1
  values: scalar
- name: SHY variation with load, PHY2
  summary: Horizontal shift variation scalar
  group: Lateral
  block_parameter: PHY2
  values: scalar
- name: Svy/Fz vertical shift at FZNOM, PVY1
  summary: Vertical shift at nominal force scalar
  group: Lateral
  block_parameter: PVY1
  values: scalar
- name: Svy/Fz variation with load, PVY2
  summary: Vertical shift variation with load scalar
  group: Lateral
  block_parameter: PVY2
  values: scalar
- name: Svy/Fz variation with camber, PVY3
  summary: Vertical shift variation with camber scalar
  group: Lateral
  block_parameter: PVY3
  values: scalar
- name: Svy/Fz variation with load and camber, PVY4
  summary: Vertical shift variation with load and camber scalar
  group: Lateral
  block_parameter: PVY4
  values: scalar
- name: Cornering stiffness variation with inflation pressure, PPY1
  summary: Stiffness variation with pressure scalar
  group: Lateral
  block_parameter: PPY1
  values: scalar
- name: Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2
  summary: Stiffness variation with pressure scalar
  group: Lateral
  block_parameter: PPY2
  values: scalar
- name: Linear inflation pressure on peak lateral friction, PPY3
  summary: Pressure scalar
  group: Lateral
  block_parameter: PPY3
  values: scalar
- name: Quadratic inflation pressure on peak lateral friction, PPY4
  summary: Pressure scalar
  group: Lateral
  block_parameter: PPY4
  values: scalar
- name: Inflation pressure effect on camber stiffness, PPY5
  summary: Pressure scalar
  group: Lateral
  block_parameter: PPY5
  values: scalar
- name: Combined Fy reduction slope factor, RBY1
  summary: Combined lateral force reduction slope factor scalar
  group: Lateral
  block_parameter: RBY1
  values: scalar
- name: Fy slope reduction with slip angle, RBY2
  summary: Lateral force slope reduction with slip angle scalar
  group: Lateral
  block_parameter: RBY2
  values: scalar
- name: Fy shift reduction with slip angle, RBY3
  summary: Lateral force shift reduction with slip angle scalar
  group: Lateral
  block_parameter: RBY3
  values: scalar
- name: Fy combined stiffness variation from camber, RBY4
  summary: Lateral force combined stiffness variation from camber scalar
  group: Lateral
  block_parameter: RBY4
  values: scalar
- name: Fy combined reduction shape factor, RCY1
  summary: Lateral force combined reduction shape factor scalar
  group: Lateral
  block_parameter: RCY1
  values: scalar
- name: Fy combined curvature factor, REY1
  summary: Lateral force combined curvature factor scalar
  group: Lateral
  block_parameter: REY1
  values: scalar
- name: Fy combined curvature factor with load, REY2
  summary: Lateral force combined curvature factor with load scalar
  group: Lateral
  block_parameter: REY2
  values: scalar
- name: Fy combined reduction shift factor, RHY1
  summary: Lateral force combined reduction shift factor scalar
  group: Lateral
  block_parameter: RHY1
  values: scalar
- name: Fy combined reduction shift factor with load, RHY2
  summary: Lateral force combined reduction shift factor with load scalar
  group: Lateral
  block_parameter: RHY2
  values: scalar
- name: Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1
  summary: Slip ratio slide force at nominal force scalar
  group: Lateral
  block_parameter: RVY1
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with load, RVY2
  summary: Side force variation with load scalar
  group: Lateral
  block_parameter: RVY2
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with camber, RVY3
  summary: Side force variation with camber scalar
  group: Lateral
  block_parameter: RVY3
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with slip angle, RVY4
  summary: Side force variation with slip angle scalar
  group: Lateral
  block_parameter: RVY4
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with slip ratio, RVY5
  summary: Side force variation with slip ratio scalar
  group: Lateral
  block_parameter: RVY5
  values: scalar
- name: Side force Svyk/Muy\*Fz variation with slip ratio arctangent, RVY6
  summary: Side force variation with slip ratio arctangent scalar
  group: Lateral
  block_parameter: RVY6
  values: scalar
- name: Torque resistance coefficient, QSY1
  summary: Torque resistance scalar
  group: Rolling
  block_parameter: QSY1
  values: scalar
- name: Torque resistance due to Fx, QSY2
  summary: Torque resistance due to longitudinal force scalar
  group: Rolling
  block_parameter: QSY2
  values: scalar
- name: Torque resistance due to speed, QSY3
  summary: Torque resistance due to speed scalar
  group: Rolling
  block_parameter: QSY3
  values: scalar
- name: Torque resistance due to speed^4, QSY4
  summary: Torque resistance due to speed scalar
  group: Rolling
  block_parameter: QSY4
  values: scalar
- name: Torque resistance due to square of camber, QSY5
  summary: Torque resistance due to camber scalar
  group: Rolling
  block_parameter: QSY5
  values: scalar
- name: Torque resistance due to square of camber and load, QSY6
  summary: Torque resistance due to camber and load scalar
  group: Rolling
  block_parameter: QSY6
  values: scalar
- name: Torque resistance due to load, QSY7
  summary: Torque resistance due to load scalar
  group: Rolling
  block_parameter: QSY7
  values: scalar
- name: Torque resistance due to pressure, QSY8
  summary: Torque resistance due to pressure scalar
  group: Rolling
  block_parameter: QSY8
  values: scalar
- name: Trail slope factor for trail Bpt at FZNOM, QBZ1
  summary: Trail slope factor at nominal force scalar
  group: Aligning
  block_parameter: QBZ1
  values: scalar
- name: Bpt slope variation with load, QBZ2
  summary: Slope variation with load scalar
  group: Aligning
  block_parameter: QBZ2
  values: scalar
- name: Bpt slope variation with square of load, QBZ3
  summary: Slope variation with load 0 (default) | scalar
  group: Aligning
  block_parameter: QBZ3
  values: scalar
- name: Bpt slope variation with camber, QBZ4
  summary: Slope variation with camber scalar
  group: Aligning
  block_parameter: QBZ4
  values: scalar
- name: Bpt slope variation with absolute value of camber, QBZ5
  summary: Slope variation with camber scalar
  group: Aligning
  block_parameter: QBZ5
  values: scalar
- name: Bpt slope variation with square of camber, QBZ6
  summary: Slope variation with camber scalar
  group: Aligning
  block_parameter: QBZ6
  values: scalar
- name: Br of Mzr slope scaling factor, QBZ9
  summary: Slope scaling factor scalar
  group: Aligning
  block_parameter: QBZ9
  values: scalar
- name: Br of Mzr cornering stiffness factor, QBZ10
  summary: Cornering stiffness factor scalar
  group: Aligning
  block_parameter: QBZ10
  values: scalar
- name: Cpt pneumatic trail shape factor, QCZ1
  summary: Pneumatic trail shape factor scalar
  group: Aligning
  block_parameter: QCZ1
  values: scalar
- name: Dpt peak trail, QDZ1
  summary: Peak trail scalar
  group: Aligning
  block_parameter: QDZ1
  values: scalar
- name: Dpt peak trail variation with load, QDZ2
  summary: Peak trail variation with load scalar
  group: Aligning
  block_parameter: QDZ2
  values: scalar
- name: Dpt peak trail variation with camber, QDZ3
  summary: Peak trail variation with camber scalar
  group: Aligning
  block_parameter: QDZ3
  values: scalar
- name: Dpt peak trail variation with square of camber, QDZ4
  summary: Peak trail variation with camber scalar
  group: Aligning
  block_parameter: QDZ4
  values: scalar
- name: Dmr peak residual torque, QDZ6
  summary: Peak residual torque scalar
  group: Aligning
  block_parameter: QDZ6
  values: scalar
- name: Dmr peak residual torque variation with load, QDZ7
  summary: Peak residual torque variation with load scalar
  group: Aligning
  block_parameter: QDZ7
  values: scalar
- name: Dmr peak residual torque variation with camber, QDZ8
  summary: Peak residual torque variation with camber scalar
  group: Aligning
  block_parameter: QDZ8
  values: scalar
- name: Dmr peak residual torque variation with camber and load, QDZ9
  summary: Peak residual torque variation with camber and load scalar
  group: Aligning
  block_parameter: QDZ9
  values: scalar
- name: Dmr peak residual torque variation with square of camber, QDZ10
  summary: Peak residual torque variation with camber scalar
  group: Aligning
  block_parameter: QDZ10
  values: scalar
- name: Dmr peak residual torque variation with square of load, QDZ11
  summary: Peak residual torque variation with load scalar
  group: Aligning
  block_parameter: QDZ11
  values: scalar
- name: Ept trail curvature at FZNOM, QEZ1
  summary: Trail curvature at nominal force scalar
  group: Aligning
  block_parameter: QEZ1
  values: scalar
- name: Ept variation with load, QEZ2
  summary: Trail curvature variation with load scalar
  group: Aligning
  block_parameter: QEZ2
  values: scalar
- name: Ept variation with square of load, QEZ3
  summary: Trail curvature variation with load scalar
  group: Aligning
  block_parameter: QEZ3
  values: scalar
- name: Ept variation with sign of alpha-t, QEZ4
  summary: Trail curvature variation scalar
  group: Aligning
  block_parameter: QEZ4
  values: scalar
- name: Ept variation with sign of alpha-t and camber, QEZ5
  summary: Variation scalar
  group: Aligning
  block_parameter: QEZ5
  values: scalar
- name: Sht horizontal trail shift at FZNOM, QHZ1
  summary: Horizontal trail shift at nominal load scalar
  group: Aligning
  block_parameter: QHZ1
  values: scalar
- name: Sht variation with load, QHZ2
  summary: Horizontal trail shift variation with load scalar
  group: Aligning
  block_parameter: QHZ2
  values: scalar
- name: Sht variation with camber, QHZ3
  summary: Horizontal trail shift variation with camber scalar
  group: Aligning
  block_parameter: QHZ3
  values: scalar
- name: Sht variation with load and camber, QHZ4
  summary: Horizontal trail shift variation with load and camber scalar
  group: Aligning
  block_parameter: QHZ4
  values: scalar
- name: Inflation pressure influence on trail length, PPZ1
  summary: Pressure influence on trail length scalar
  group: Aligning
  block_parameter: PPZ1
  values: scalar
- name: Inflation pressure influence on residual aligning torque, PPZ2
  summary: Pressure influence on aligning torque scalar
  group: Aligning
  block_parameter: PPZ2
  values: scalar
- name: 'Nominal value of s/R0: effect of Fx on Mz, SSZ1'
  summary: Effect of longitudinal force on aligning torque scalar
  group: Aligning
  block_parameter: SSZ1
  values: scalar
- name: s/R0 variation with lateral to nominal force ratio, SSZ2
  summary: Variation with lateral to nominal force ratio scalar
  group: Aligning
  block_parameter: SSZ2
  values: scalar
- name: s/R0 variation with camber, SSZ3
  summary: Variation with camber scalar
  group: Aligning
  block_parameter: SSZ3
  values: scalar
- name: s/R0 variation with camber and load, SSZ4
  summary: Variation with camber and load scalar
  group: Aligning
  block_parameter: SSZ4
  values: scalar
- name: Fx peak reduction due to spin, PDXP1
  summary: Longitudinal force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDXP1
  values: scalar
- name: Fx peak reduction due to spin with varying load, PDXP2
  summary: Longitudinal force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDXP2
  values: scalar
- name: Fx peak reduction due to spin with slip ratio, PDXP3
  summary: Longitudinal force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDXP3
  values: scalar
- name: Cornering stiffness reduction due to spin, PKYP1
  summary: Stiffness reduction due to spin scalar
  group: Turnslip
  block_parameter: PKYP1
  values: scalar
- name: Fy peak reduction due to spin, PDYP1
  summary: Lateral force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDYP1
  values: scalar
- name: Fy peak reduction due to spin with varying load, PDYP2
  summary: Lateral force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDYP2
  values: scalar
- name: Fy peak reduction due to spin with slip angle, PDYP3
  summary: Lateral force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDYP3
  values: scalar
- name: Fy peak reduction due to square root of spin, PDYP4
  summary: Lateral force peak reduction due to spin scalar
  group: Turnslip
  block_parameter: PDYP4
  values: scalar
- name: Fy vs. slip angle response lateral shift limit, PHYP1
  summary: Lateral force versus slip angle response scalar
  group: Turnslip
  block_parameter: PHYP1
  values: scalar
- name: Fy vs. slip angle response max lateral shift limit, PHYP2
  summary: Lateral force versus slip angle response scalar
  group: Turnslip
  block_parameter: PHYP2
  values: scalar
- name: Fy vs. slip angle response max lateral shift limit with load, PHYP3
  summary: Lateral force versus slip angle response scalar
  group: Turnslip
  block_parameter: PHYP3
  values: scalar
- name: Fy vs. slip angle response lateral shift curvature factor, PHYP4
  summary: Lateral force versus slip angle response scalar
  group: Turnslip
  block_parameter: PHYP4
  values: scalar
- name: Camber stiffness reduction due to spin, PECP1
  summary: Camber stiffness reduction scalar
  group: Turnslip
  block_parameter: PECP1
  values: scalar
- name: Camber stiffness reduction due to spin with load, PECP2
  summary: Camber stiffness reduction scalar
  group: Turnslip
  block_parameter: PECP2
  values: scalar
- name: Turn slip pneumatic trail reduction factor, QDTP1
  summary: Turn slip pneumatic trail reduction factor scalar
  group: Turnslip
  block_parameter: QDTP1
  values: scalar
- name: Turn moment for constant turning and zero longitudinal speed, QCRP1
  summary: Turn moment for constant turning scalar
  group: Turnslip
  block_parameter: QCRP1
  values: scalar
- name: Turn slip moment increase with spin at 90deg slip angle, QCRP2
  summary: Turn slip moment scalar
  group: Turnslip
  block_parameter: QCRP2
  values: scalar
- name: Residual spin torque reduction from side slip, QBRP1
  summary: Residual spin torque reduction scalar
  group: Turnslip
  block_parameter: QBRP1
  values: scalar
- name: Turn slip moment peak magnitude, QDRP1
  summary: Turn slip moment peak magnitude scalar
  group: Turnslip
  block_parameter: QDRP1
  values: scalar
- name: Turn slip moment curvature, QDRP2
  summary: Turn slip moment curvature scalar
  group: Turnslip
  block_parameter: QDRP2
  values: scalar
```

### Tire Options

### **Tire type** — Select type `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

Use the **Tire type** parameter to select the
source of the tire data.

| Goal | Action |
| --- | --- |
| Import your own external file containing Magic Formula coefficients, and use them to drive the empirical equations modeling the tire1 and 2. The file you import can be a .mat, .tir, or .txt type, and must contain parameter names corresponding to those in the tire block. | Update the block parameters with fitting coefficients from a file:  1. Set **Tire type** to `External    file`. 2. On the **Wheel and Tire Parameters** > **External    tire source** pane, select **Select file**. 3. Select the tire coefficient file. 4. Select **Update mask values from file**. In the dialog box that    prompts you for confirmation, click **OK**. The block updates the    parameters. 5. Select **Apply**. |
| Select one of the Magic Formula built-in tire models to drive the empirical equations modeling the tire 1 and 2. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the tire that you    want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Select **Update block with applicable tire    values**. On the **Tire    Parameters** tab, the block updates the    applicable parameters, including **Tire nominal    section width**, **Rim    radius**, and **Tire mass**. 3. Select **Apply**. |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `tireType` |
| **Values:** | `External file` | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **Data Types:** | `character vector` |

### **Tire file or object, tireParamSet** — Tire file `vdynPassCar.mat` (default) | `.tir` | `.txt`

Tire file `.tir` or object containing empirical data
to model tire longitudinal and lateral behavior with the Magic Formula.
If you provide an `.txt` file, make sure the file
contains names that correspond to the block parameters.

Update the block parameters with
fitting coefficients from a file:

1. Set **Tire type** to
   `External file`.
2. On the **Wheel and Tire Parameters**
   > **External tire source** pane,
   select **Select file**.
3. Select the tire coefficient file.
4. Select **Update mask values from
   file**. In the dialog box that prompts you for
   confirmation, click **OK**. The block
   updates the parameters.
5. Select **Apply**.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `tireParamSet` |
| **Values:** | `vdynPassCar.mat` (default) | `.tir` | `.txt` |
| **Data Types:** | `character vector` |

### **Vertical Motion** — Vertical motion model `Magic Formula` (default) | `None` | `External deflection`

Type of vertical motion. By default, the block uses the Magic Formula
to calculate the vertical motion of the tire.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `vertType` |
| **Values:** | `Magic Formula` (default) | `None` | `External deflection` |
| **Data Types:** | `character vector` |

### **Ply steer** — Include ply steer `on` (default) | `off`

Select to include ply steer in the Magic Formula 6.2 equations.

By default, the blocks include ply steer and turn slip in the Magic Formula 6.2
equations. The equations are fit to flat-belt test data and predict a number of tire
effects, including ply steer and turn slip. Consider removing the effects if your:

- Test data does not include ply steer or turn slip data.
- Analysis does not require ply steer or turn slip effects.

If you clear **Ply steer**, the block internally sets these
parameters to 0:

- **Vertical shift of overturning moment, QSX1**
- **Combined slip Fx shift factor reduction, RHX1**
- **Efy curvature constant camber dependency, PEY3**
- **SHY horizontal shift at FZNOM, PHY1**
- **SHY variation with load, PHY2**
- **Svy/Fz vertical shift at FZNOM, PVY1**
- **Svy/Fz variation with load, PVY2**
- **Fy shift reduction with slip angle, RBY3**
- **Slip ratio side force Svyk/Muy\*Fz at FZNOM,
  RVY1**
- **Side force Svyk/Muy\*Fz variation with load,
  RVY2**
- **Bpt slope variation with camber, QBZ4**
- **Dpt peak trail variation with camber, QDZ3**
- **Dmr peak residual torque, QDZ6**
- **Dmr peak residual torque variation with load,
  QDZ7**
- **Ept variation with sign of alpha-t, QEZ4**
- **Sht horizontal trail shift at FZNOM, QHZ1**
- **Sht variation with load, QHZ2**
- **Nominal value of s/R0: effect of Fx on Mz,
  SSZ1**

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `plySteer` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

### **Turn slip** — Include turn slip `on` (default) | `off`

Select to include ply steer in Magic Formula 6.2 equations.

By default, the blocks include ply steer and turn slip in the Magic Formula 6.2
equations. The equations are fit to flat-belt test data and predict a number of tire
effects, including ply steer and turn slip. Consider removing the effects if your:

- Test data does not include ply steer or turn slip data.
- Analysis does not require ply steer or turn slip effects.

If you clear **Turn slip**, the block internally:

- Sets the Magic Formula turn slip equations to 1. Specifically, equations
  4.E77, 4.E79, 4.E81, 4.E83, 4.E84, 4.E92, 4.E102, 4.E101, and
  4.E1052.
- Uses Magic Formula terms that effect horizontal shift.
- Uses Magic Formula small turn slip values in
  4.E272.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `turnslip` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

### **Brake type** — Brake type `None` | `Disc` | `Drum` | `Mapped`

Use the **Brake Type** parameter to select the
brake.

| Action | Brake Type Setting |
| --- | --- |
| No braking | `None` |
| Implement brake that converts the brake cylinder pressure into a braking force | `Disc` |
| Implement simplex drum brake that converts the applied force and brake geometry into a net braking torque | `Drum` |
| Implement lookup table that is a function of the wheel speed and applied brake pressure | `Mapped` |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **Values:** | `None` | `Disc` | `Drum` | `Mapped` |
| **Data Types:** | `character vector` |

### Plotting

### **Install Extended Tire Features** — Option to install Extended Tire Features for Vehicle Dynamics Blockset™ support package button

Click **Install Extended Tire Features** to install the
Extended Tire Features for Vehicle Dynamics Blockset support package. With the support package, you can plot
steady-state force and moment tire responses from the Combined Slip Wheel 2DOF Block
Parameters dialog box.

### **Plot steady state force, moment response** — Option to plot steady-state force and moment tire responses button

Click **Plot steady state force, moment response** to
generate these plots:

- **Lateral force [N] vs Slip angle [rad]**
- **Self-aligning moment [Nm] vs Slip angle
  [rad]**
- **Longitudinal force [N] vs Longitudinal slip
  []**
- **Longitudinal force [N] vs Lateral force
  [N]**

#### Dependencies

To enable this parameter, click **Install Extended Tire
Features**.

### Brake

### **Static friction coefficient, mu\_static** — Static friction coefficient `0.3` (default) | scalar | *N*-by-`1` vector

Static friction coefficient, specified as a
scalar or *N*-by-`1` vector, dimensionless. If
you specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **Values:** | `0.3` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, mu\_kinetic** — Kinetic friction `0.2` (default) | scalar | *N*-by-`1` vector

Kinematic friction coefficient, specified as
a scalar or *N*-by-`1` vector, dimensionless.
If you specify a scalar, the block uses that value for all wheels. If you
specify a vector, you must specify vectors for the other brake
parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_kinetic` |
| **Values:** | `0.2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Disc

### **Disc brake actuator bore, disc\_abore** — Bore distance `0.05` (default) | scalar | *N*-by-`1` vector

Disc brake actuator bore, specified as a
scalar or *N*-by-`1` vector, in m. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `disc_abore` |
| **Values:** | `0.05` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Brake pad mean radius, Rm** — Radius `0.177` (default) | scalar | *N*-by-`1` vector

Brake pad mean radius, specified as a scalar
or *N*-by-`1` vector, in m. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you
must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rm` |
| **Values:** | `0.177` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Number of brake pads, num\_pads** — Number of brake pads `2` (default) | scalar | *N*-by-`1` vector

Number of brake pads, specified as a scalar
or *N*-by-`1` vector, dimensionless. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `num_pads` |
| **Values:** | `2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Drum

### **Drum brake actuator bore, drum\_abore** — Bore distance `0.0508` (default) | scalar | *N*-by-`1` vector

Drum brake actuator bore, specified as a
scalar or *N*-by-`1` vector, in m. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_abore` |
| **Values:** | `0.0508` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Shoe pin to drum center distance, drum\_a** — Shoe pin to drum center distance `0.123` (default) | scalar

Shoe pin to drum center distance, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_a` |
| **Values:** | `0.123` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin center to force application point distance, drum\_c** — Shoe pin center to force application point distance `0.212` (default) | scalar

Shoe pin center to force application point distance, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_c` |
| **Values:** | `0.212` (default) | scalar |
| **Data Types:** | `double` |

### **Drum internal radius, drum\_r** — Drum internal radius `0.15` (default) | scalar

Drum internal radius, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_r` |
| **Values:** | `0.15` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin to pad start angle, drum\_theta1** — Shoe pin to pad start angle `0` (default) | scalar

Shoe pin to pad start angle, in deg.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta1` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin to pad end angle, drum\_theta2** — Shoe pin to pad end angle `126` (default) | scalar

Shoe pin to pad end angle, in deg.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta2` |
| **Values:** | `126` (default) | scalar |
| **Data Types:** | `double` |

#### Mapped

### **Brake actuator pressure breakpoints, brake\_p\_bpt** — Brake actuator pressure breakpoints vector

Brake actuator pressure breakpoints, in bar.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_p_bpt` |
| **Values:** | vector |
| **Data Types:** | `double` |

### **Wheel speed breakpoints, brake\_n\_bpt** — Wheel speed breakpoints vector

Wheel speed breakpoints, in rpm.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_n_bpt` |
| **Values:** | vector |
| **Data Types:** | `double` |

### **Brake torque map, f\_brake\_t** — Lookup table for brake torque array

The lookup table for the brake
torque, fbrake(P,N), is a function of applied brake pressure and wheel speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in bar.
- *N* is wheel speed, in rpm.

Plot showing brake torque as a function of wheel speed and applied brake pressure

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_brake_t` |
| **Values:** | vector |
| **Data Types:** | `double` |

### Simulation

### **Nominal pressure, NOMPRES** — Pressure scalar

Nominal pressure, *NOMPRES*, in Pa.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NOMPRES` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Maximum pressure, PRESMAX** — Maximum pressure scalar

Maximum pressure, *PRESMAX*, in Pa.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PRESMAX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Minimum pressure, PRESMIN** — Minimum pressure scalar

Minimum pressure, *PRESMIN*, in Pa.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PRESMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal normal force, FNOMIN** — Force scalar

Nominal normal force, *FNOMIN*, in N.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FNOMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Maximum normal force, FZMAX** — Force scalar

Maximum normal force, *FZMAX*, in N.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FZMAX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Minimum normal force, FZMIN** — Force scalar

Minimum normal force, *FZMIN*, in N.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FZMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — Tolerance scalar

Velocity tolerance used to handle low velocity situations,
*VXLOW*, in m/s.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VXLOW` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — Max allowable slip ratio scalar

Max allowable slip ratio (absolute), *KPUMAX*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KPUMAX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — Minimum allowable slip ratio scalar

Minimum allowable slip ratio (absolute), *KPUMIN*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KPUMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — Max allowable slip angle scalar

Max allowable slip angle (absolute), *ALPMAX*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ALPMAX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — Minimum allowable slip angle scalar

Minimum allowable slip angle (absolute), *ALPMIN*, in
rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ALPMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Maximum allowable camber angle, CAMMAX** — Maximum allowable camber angle scalar

Maximum allowable camber angle *CAMMAX*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CAMMAX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Minimum allowable camber angle, CAMMIN** — Minimum allowable camber angle scalar

Minimum allowable camber angle, *CAMMIN*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CAMMIN` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal longitudinal speed, LONGVL** — Speed scalar

Nominal longitudinal speed, *LONGVL*, in m/s.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LONGVL` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Initial wheel rotational velocity, omegao** — Initial wheel rotational velocity scalar | *N*-by-`1` vector

Initial wheel rotational velocity, specified as a
scalar or *N*-by-`1` vector, in rad/s. If you specify
a scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### Dimension

### **Tire unloaded radius, UNLOADED\_RADIUS** — Radius scalar

Tire unloaded radius, *UNLOADED\_RADIUS*, in m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `UNLOADED_RADIUS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Tire nominal section width, WIDTH** — Tire nominal section width scalar

Tire nominal section width, *WIDTH*, in m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WIDTH` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Rim radius, RIM\_RADIUS** — Radius scalar

Rim radius, *RIM\_RADIUS*, in m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RIM_RADIUS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal aspect ratio, ASPECT\_RATIO** — Ratio scalar

Nominal aspect ratio, *ASPECT\_RATIO*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ASPECT_RATIO` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Inertial and Damping

### **Tire mass, MASS** — Mass scalar | *N*-by-`1` vector

Tire mass, specified as a scalar or
*N*-by-`1` vector, in kg. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you
must specify vectors for the other inertial parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Vertical Motion** to
`Magic Formula`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MASS` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — Tire rotational inertia scalar | *N*-by-`1` vector

Tire rotational inertia (rolling axis), specified as
a scalar or *N*-by-`1` vector, in
kg·m2. If you specify a scalar, the block uses that value
for all wheels. If you specify a vector, you must specify vectors for the other
rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IYY` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Rotational damping, br** — Rotational damping scalar | *N*-by-`1` vector

Rotational damping, specified as a scalar or
*N*-by-`1` vector, in N·m·s/rad. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Gravity, GRAVITY** — Gravity scalar

Gravity, *GRAVITY*, in m/s^2.

#### Dependencies

To enable this parameter, set **Vertical Motion** to
`Magic Formula`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `GRAVITY` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Vertical

### **Initial tire displacement, zo** — Displacement scalar | *N*-by-`1` vector

Initial tire displacement, specified as a
scalar or *N*-by-`1` vector, in m. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other vertical parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zo` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — Velocity scalar | *N*-by-`1` vector

Initial wheel vertical velocity, specified as
a scalar or *N*-by-`1` vector, in m/s. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other vertical parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zdoto` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Effective rolling radius at low load stiffness, BREFF** — Stiffness scalar

Effective rolling radius at low load stiffness, *BREFF*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BREFF` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Effective rolling radius peak value, DREFF** — Radius scalar

Effective rolling radius peak value, *DREFF*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DREFF` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Effective rolling radius at high load stiffness, FREFF** — Radius scalar

Effective rolling radius at high load stiffness, *FREFF*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FREFF` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Unloaded to nominal rolling radius ratio, Q\_RE0** — Ratio scalar

Unloaded to nominal rolling radius ratio, *Q\_RE0*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_RE0` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Radius rotational speed dependence, Q\_V1** — Speed scalar

Radius rotational speed dependence, *Q\_V1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_V1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Stiffness rotational speed dependence, Q\_V2** — Speed scalar

Stiffness rotational speed dependence, *Q\_V2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_V2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear load change with deflection, Q\_FZ1** — Load change `scalar`

Linear load change with deflection, *Q\_FZ1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic load change with deflection, Q\_FZ2** — Load change scalar

Quadratic load change with deflection, *Q\_FZ2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear load change with deflection and quadratic camber, Q\_FZ3** — Load change scalar

Linear load change with deflection and quadratic camber,
*Q\_FZ3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Load response to longitudinal force, Q\_FCX** — Force scalar

Load response to longitudinal force, *Q\_FCX*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FCX` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Load response to lateral force, Q\_FCY** — Force scalar

Load response to lateral force, *Q\_FCY*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FCY` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Vertical stiffness change due to lateral load dependency on lateral stiffness, Q\_FCY2** — Stiffness scalar

Vertical stiffness change due to lateral load dependency on lateral stiffness,
*Q\_FCY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FCY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Stiffness response to pressure, PFZ1** — Stiffness `0.7098` (default) | `scalar`

Stiffness response to pressure, *PFZ1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PFZ1` |
| **Values:** | `0.7098` (default) | `scalar` |
| **Data Types:** | `double` |

### **Vertical tire stiffness, VERTICAL\_STIFFNESS** — Stiffness scalar

Vertical tire stiffness, *VERTICAL\_STIFFNESS*, in N/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VERTICAL_STIFFNESS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Vertical tire damping, VERTICAL\_DAMPING** — Damping scalar

Vertical tire damping, *VERTICAL\_DAMPING*, in N·s/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VERTICAL_DAMPING` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Rim bottoming out offset, BOTTOM\_OFFST** — Offset scalar

Rim bottoming out offset, *BOTTOM\_OFFST*, in m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BOTTOM_OFFST` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bottoming out stiffness, BOTTOM\_STIFF** — Stiffness scalar

Bottoming out stiffness, *BOTTOM\_STIFF*, in N/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BOTTOM_STIFF` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear load dependent camber angle effect on vertical stiffness, Q\_CAM1** — Stiffness scalar

Linear load dependent camber angle effect on vertical stiffness,
*Q\_CAM1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_CAM1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic load dependent camber angle effect on vertical stiffness, Q\_CAM2** — Stiffness scalar

Quadratic load dependent camber angle effect on vertical stiffness,
*Q\_CAM2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_CAM2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear reduction of stiffness with load and camber angle, Q\_CAM3** — Stiffness scalar

Linear reduction of stiffness with load and camber angle,
*Q\_CAM3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_CAM3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Constant camber and slip angle effect on vertical stiffness, Q\_FYS1** — Stiffness scalar

Constant camber and slip angle effect on vertical stiffness,
*Q\_FYS1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FYS1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear camber and slip angle effect on vertical stiffness, Q\_FYS2** — Stiffness scalar

Linear camber and slip angle effect on vertical stiffness,
*Q\_FYS2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FYS2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic camber and slip angle effect on vertical stiffness, Q\_FYS3** — Stiffness scalar

Quadratic camber and slip angle effect on vertical stiffness,
*Q\_FYS3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_FYS3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Structural

### **Longitudinal stiffness, LONGITUDINAL\_STIFFNESS** — Stiffness scalar

Longitudinal stiffness, *LONGITUDINAL\_STIFFNESS*, in
N/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LONGITUDINAL_STIFFNESS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Lateral stiffness, LATERAL\_STIFFNESS** — Stiffness scalar

Longitudinal stiffness, *LATERAL\_STIFFNESS*, in N/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LATERAL_STIFFNESS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear vertical deflection influence on longitudinal stiffness, PCFX1** — Deflection influence scalar

Linear vertical deflection influence on longitudinal stiffness,
*PCFX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic vertical deflection influence on longitudinal stiffness, PCFX2** — Deflection influence scalar

Quadratic vertical deflection influence on longitudinal stiffness,
*PCFX2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Pressure dependency on longitudinal stiffness, PCFX3** — Pressure dependency scalar

Pressure dependency on longitudinal stiffness, *PCFX3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear vertical deflection influence on lateral stiffness, PCFY1** — Deflection influence scalar

Linear vertical deflection influence on lateral stiffness,
*PCFY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic vertical deflection influence on lateral stiffness, PCFY2** — Deflection influence scalar

Quadratic vertical deflection influence on lateral stiffness,
*PCFY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Pressure dependency on longitudinal stiffness, PCFY3** — Pressure dependency scalar

Pressure dependency on longitudinal stiffness, *PCFY3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCFY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Contact Patch

### **Contact length square root term, Q\_RA1** — Length term scalar

Contact length square root term, *Q\_RA1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_RA1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Contact length linear term, Q\_RA2** — Length term scalar

Contact length linear term, *Q\_RA2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_RA2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Contact width root term, Q\_RB1** — Width term scalar

Contact width root term, *Q\_RB1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_RB1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Contact width linear term, Q\_RB2** — Width term scalar

Contact width linear term, *Q\_RB2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Q_RB2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Longitudinal

### **Cfx shape factor, PCX1** — Shape factor scalar

Shape factor, *Cfx*,
*PCX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Longitudinal friction at nominal normal load, PDX1** — Friction scalar

Longitudinal friction at nominal normal load, *PDX1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Frictional variation with load, PDX2** — Friction variation scalar

Frictional variation with load, *PDX2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Frictional variation with camber, PDX3** — Friction variation scalar

Frictional variation with camber, *PDX3*, in 1/rad^2.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Longitudinal curvature at nominal normal load, PEX1** — Curvature scalar

Longitudinal curvature at nominal normal load, *PEX1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of curvature factor with load, PEX2** — Curvature variation scalar

Variation of curvature factor with load, *PEX2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of curvature factor with square of load, PEX3** — Curvature variation scalar

Variation of curvature factor with square of load, *PEX3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Longitudinal curvature factor with slip, PEX4** — Curvature scalar

Longitudinal curvature factor with slip, *PEX4*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Longitudinal slip stiffness at nominal normal load, PKX1** — Stiffness scalar

Longitudinal slip stiffness at nominal normal load, *PKX1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of slip stiffness with load, PKX2** — Stiffness variation scalar

Variation of slip stiffness with load, *PKX2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Slip stiffness exponent factor, PKX3** — Slip stiffness scalar

Slip stiffness exponent factor, *PKX3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Horizontal shift in slip ratio at nominal normal load, PHX1** — Slip ratio shift scalar

Horizontal shift in slip ratio at nominal normal load,
*PHX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of horizontal slip ratio with load, PHX2** — Slip variation scalar

Variation of horizontal slip ratio with load, *PHX2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Vertical shift in load at nominal normal load, PVX1** — Load shift scalar

Vertical shift in load at nominal normal load, *PVX1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of vertical shift with load, PVX2** — Load variation scalar

Variation of vertical shift with load, *PVX2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear variation of longitudinal slip stiffness with tire pressure, PPX1** — Stiffness variation scalar

Linear variation of longitudinal slip stiffness with tire pressure,
*PPX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2** — Stiffness variation scalar

Quadratic variation of longitudinal slip stiffness with tire pressure,
*PPX2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear variation of peak longitudinal friction with tire pressure, PPX3** — Friction variation scalar

Linear variation of peak longitudinal friction with tire pressure,
*PPX3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic variation of peak longitudinal friction with tire pressure, PPX4** — Friction variation scalar

Quadratic variation of peak longitudinal friction with tire pressure,
*PPX4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Combined slip Fx slope factor reduction, RBX1** — Combined slip longitudinal force slope factor reduction scalar

Combined slip longitudinal force,
*Fx*, slope factor reduction,
*RBX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Slip ratio Fx slope reduction variation, RBX2** — Slip ratio longitudinal force slope reduction variation scalar

Slip ratio longitudinal force, *Fx*,
slope reduction variation, *RBX2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber influence on combined slip Fx stiffness, RBX3** — Camber influence on combined slip longitudinal force stiffness scalar

Camber influence on combined slip longitudinal force,
*Fx*, stiffness,
*RBX3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Shape factor for combined slip Fx reduction, RCX1** — Shape factor for combined slip longitudinal force reduction scalar

Shape factor for combined slip longitudinal force,
*Fx*, reduction,
*RCX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RCX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Combined Fx curvature factor, REX1** — Combined longitudinal force curvature factor scalar

Combined longitudinal force, *Fx*,
curvature factor, *REX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `REX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Combined Fx curvature factor with load, REX2** — Combined longitudinal force curvature factor scalar

Combined longitudinal force, *Fx*,
curvature factor with load, *REX2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `REX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Combined slip Fx shift factor reduction, RHX1** — Combined slip longitudinal force slip factor scalar

Combined slip longitudinal force,
*Fx*, shift factor reduction,
*RHX1*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RHX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Overturning

### **Vertical shift of overturning moment, QSX1** — Overturning moment scalar

Vertical shift of overturning moment, *QSX1*,
dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Overturning moment due to camber, QSX2** — Overturning moment due to camber scalar

Overturning moment due to camber, *QSX2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Overturning moment due to Fy, QSX3** — Overturning moment due to lateral force scalar

Overturning moment due to lateral force, *QSX3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx combined lateral force load and camber, QSX4** — Overturning moment scalar

Overturning moment, *Mx*, combined
lateral force load and camber, *QSX4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx load effect due to lateral force and camber, QSX5** — Overturning moment scalar

Overturning moment, *Mx*, load effect
due to lateral force and camber, *QSX5*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx load effect due to B-factor, QSX6** — Overturning moment scalar

Overturning moment, *Mx*, load effect
due to B-factor, *QSX6*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to camber and load, QSX7** — Overturning moment scalar

Overturning moment, *Mx*, due to
camber and load, *QSX7*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX7` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force and load, QSX8** — Overturning moment scalar

Overturning moment, *Mx*, due to
lateral force and load, *QSX8*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX8` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to B-factor of lateral force and load, QSX9** — Overturning moment scalar

Overturning moment, *Mx*, due to
B-factor of lateral force and load, *QSX9*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX9` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to vertical force and camber, QSX10** — Overturning moment scalar

Overturning moment, *Mx*, due to
vertical force and camber, *QSX10*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX10` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to B-factor of vertical force and camber, QSX11** — Overturning moment scalar

Overturning moment, *Mx*, due to
B-factor of vertical force and camber, *QSX11*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX11` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to squared camber, QSX12** — Overturning moment scalar

Overturning moment, *Mx*, due to
squared camber, *QSX12*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX12` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force, QSX13** — Overturning moment scalar

Overturning moment, *Mx*, due to
lateral force, *QSX13*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX13` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to lateral force with camber, QSX14** — Overturning moment scalar

Overturning moment, *Mx*, due to
lateral force with camber, *QSX14*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSX14` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Mx due to inflation pressure, PPMX1** — Overturning moment due to pressure scalar

Overturning moment, *Mx*, due to
inflation pressure, *PPMX1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPMX1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Lateral

### **Cfy shape factor for lateral force, PCY1** — Lateral force shape factor scalar

Shape factor for lateral force, *Cfy*,
*PCY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Lateral friction muy, PDY1** — Lateral friction scalar

Lateral friction, *μy*,
*PDY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Lateral friction variation of muy with load, PDY2** — Lateral friction variation scalar

Variation of lateral friction, *μy*,
with load, *PDY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Lateral friction variation of muy with squared camber, PDY3** — Lateral friction variation scalar

Variation of lateral friction, *μy*,
with squared camber, *PDY3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Efy lateral curvature at nominal force FZNOM, PEY1** — Lateral curvature at nominal force scalar

Lateral curvature, *Efy*, at nominal
force, *FZNOM*, *PEY1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Efy curvature variation with load, PEY2** — Lateral curvature variation scalar

Lateral curvature, *Efy*, variation
with load, *PEY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Efy curvature constant camber dependency, PEY3** — Lateral curvature constant scalar

Lateral curvature, *Efy*, constant
camber dependency, *PEY3*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Efy curvature variation with camber, PEY4** — Lateral curvature variation scalar

Lateral curvature, *Efy*, variation
with camber, *PEY4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Efy curvature variation with camber squared, PEY5** — Lateral curvature variation scalar

Lateral curvature, *Efy*, variation
with camber squared, *PEY5*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEY5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Maximum KFy/FZNOM stiffness, PKY1** — Maximum stiffness scalar

Maximum lateral force stiffness,
*KFy*, to nominal force,
*FZNOM*, ratio,
*PKY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Load at maximum KFy/FZNOM stiffness, PKY2** — Load scalar

Load at maximum lateral force stiffness,
*KFy*, to nominal force,
*FZNOM*, ratio,
*PKY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **KFy/FZNOM stiffness variation with camber, PKY3** — Stiffness variation scalar

Lateral force stiffness, *KFy*, to
nominal force, *FZNOM*, stiffness
variation with camber, *PKY3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **KFy curvature, PKY4** — Lateral force stiffness curvature scalar

Lateral force stiffness, *KFy*
curvature, *PKY4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Variation of peak stiffness with squared camber, PKY5** — Stiffness variation scalar

Variation of peak stiffness with squared camber, *PKY5*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy camber stiffness factor, PKY6** — Lateral force camber stiffness factor scalar

Lateral force, *Fy*, camber stiffness
factor, *PKY6*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber stiffness vertical load dependency, PKY7** — Stiffness scalar

Camber stiffness vertical load dependency, *PKY7*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKY7` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **SHY horizontal shift at FZNOM, PHY1** — Horizontal shift at nominal force scalar

Horizontal shift, *SHY*, at nominal
force, *FZNOM*, *PHY1*,
dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **SHY variation with load, PHY2** — Horizontal shift variation scalar

Horizontal shift, *SHY*, variation
with load, *PHY2*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Svy/Fz vertical shift at FZNOM, PVY1** — Vertical shift at nominal force scalar

Vertical shift, *Svy*, at nominal
force, *FZNOM*, *PVY1*,
dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Svy/Fz variation with load, PVY2** — Vertical shift variation with load scalar

Vertical shift, *Svy*, variation with
load, *PVY2*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Svy/Fz variation with camber, PVY3** — Vertical shift variation with camber scalar

Vertical shift, *Svy*, variation with
camber, *PVY3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Svy/Fz variation with load and camber, PVY4** — Vertical shift variation with load and camber scalar

Vertical shift, *Svy*, variation with
load and camber, *PVY4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure, PPY1** — Stiffness variation with pressure scalar

Cornering stiffness variation with inflation pressure,
*PPY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Cornering stiffness variation with inflation pressure induced nominal load dependency, PPY2** — Stiffness variation with pressure scalar

Cornering stiffness variation with inflation pressure induced nominal load
dependency, *PPY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear inflation pressure on peak lateral friction, PPY3** — Pressure scalar

Linear inflation pressure on peak lateral friction, *PPY3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Quadratic inflation pressure on peak lateral friction, PPY4** — Pressure scalar

Quadratic inflation pressure on peak lateral friction,
*PPY4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Inflation pressure effect on camber stiffness, PPY5** — Pressure scalar

Inflation pressure effect on camber stiffness, *PPY5*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPY5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Combined Fy reduction slope factor, RBY1** — Combined lateral force reduction slope factor scalar

Combined lateral force, *Fy*,
reduction slope factor, *RBY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy slope reduction with slip angle, RBY2** — Lateral force slope reduction with slip angle scalar

Lateral force, *Fy*, slope reduction
with slip angle, *RBY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy shift reduction with slip angle, RBY3** — Lateral force shift reduction with slip angle scalar

Lateral force, *Fy*, shift reduction
with slip angle, *RBY3*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined stiffness variation from camber, RBY4** — Lateral force combined stiffness variation from camber scalar

Lateral force, *Fy*, combined
stiffness variation from camber, *RBY4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RBY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shape factor, RCY1** — Lateral force combined reduction shape factor scalar

Lateral force, *Fy*, combined
reduction shape factor, *RCY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RCY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined curvature factor, REY1** — Lateral force combined curvature factor scalar

Lateral force, *Fy*, combined
curvature factor, *REY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `REY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined curvature factor with load, REY2** — Lateral force combined curvature factor with load scalar

Lateral force, *Fy*, combined
curvature factor with load, *REY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `REY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shift factor, RHY1** — Lateral force combined reduction shift factor scalar

Lateral force, *Fy*, combined
reduction shift factor, *RHY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RHY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy combined reduction shift factor with load, RHY2** — Lateral force combined reduction shift factor with load scalar

Lateral force, *Fy*, combined
reduction shift factor with load, *RHY2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RHY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Slip ratio side force Svyk/Muy\*Fz at FZNOM, RVY1** — Slip ratio slide force at nominal force scalar

Slip ratio side force at nominal force,
*FZNOM*, *RVY1*,
dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with load, RVY2** — Side force variation with load scalar

Side force variation with load, *RVY2*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with camber, RVY3** — Side force variation with camber scalar

Side force variation with camber, *RVY3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with slip angle, RVY4** — Side force variation with slip angle scalar

Side force variation with slip angle, *RVY4*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with slip ratio, RVY5** — Side force variation with slip ratio scalar

Side force variation with slip ratio, *RVY5*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Side force Svyk/Muy\*Fz variation with slip ratio arctangent, RVY6** — Side force variation with slip ratio arctangent scalar

Side force variation with slip ratio arctangent, *RVY6*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RVY6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Rolling

### **Torque resistance coefficient, QSY1** — Torque resistance scalar

Torque resistance coefficient, *QSY1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to Fx, QSY2** — Torque resistance due to longitudinal force scalar

Torque resistance due to longitudinal force,
*Fx*, *QSY2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to speed, QSY3** — Torque resistance due to speed scalar

Torque resistance due to speed, *QSY3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to speed^4, QSY4** — Torque resistance due to speed scalar

Torque resistance due to speed^4, *QSY4*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to square of camber, QSY5** — Torque resistance due to camber scalar

Torque resistance due to square of camber, *QSY5*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to square of camber and load, QSY6** — Torque resistance due to camber and load scalar

Torque resistance due to square of camber and load, *QSY6*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to load, QSY7** — Torque resistance due to load scalar

Torque resistance due to load, *QSY7*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY7` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Torque resistance due to pressure, QSY8** — Torque resistance due to pressure scalar

Torque resistance due to pressure, *QSY8*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY8` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Aligning

### **Trail slope factor for trail Bpt at FZNOM, QBZ1** — Trail slope factor at nominal force scalar

Trail slope factor for trail *Bpt* at nominal force,
*FZNOM*,
*QBZ1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with load, QBZ2** — Slope variation with load scalar

Slope variation with load, *QBZ2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with square of load, QBZ3** — Slope variation with load `0` (default) | scalar

Slope variation with square of load, *QBZ3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with camber, QBZ4** — Slope variation with camber scalar

Slope variation with camber, *QBZ4*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with absolute value of camber, QBZ5** — Slope variation with camber scalar

Slope variation with absolute value of camber, *QBZ5*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Bpt slope variation with square of camber, QBZ6** — Slope variation with camber scalar

Slope variation with square of camber, *QBZ6*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Br of Mzr slope scaling factor, QBZ9** — Slope scaling factor scalar

Slope scaling factor, *QBZ9*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ9` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Br of Mzr cornering stiffness factor, QBZ10** — Cornering stiffness factor scalar

*Br* of *Mzr* cornering stiffness factor,
*QBZ10*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBZ10` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Cpt pneumatic trail shape factor, QCZ1** — Pneumatic trail shape factor scalar

Pneumatic trail shape factor, *Cpt*,
*QCZ1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QCZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dpt peak trail, QDZ1** — Peak trail scalar

Peak trail, *Dpt*,
*QDZ1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dpt peak trail variation with load, QDZ2** — Peak trail variation with load scalar

Peak trail, *Dpt*, variation with
load, *QDZ2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dpt peak trail variation with camber, QDZ3** — Peak trail variation with camber scalar

Peak trail, *Dpt*, variation with
camber, *QDZ3*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dpt peak trail variation with square of camber, QDZ4** — Peak trail variation with camber scalar

Peak trail, *Dpt*, variation with
square of camber, *QDZ4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque, QDZ6** — Peak residual torque scalar

Peak residual torque, *Dmr*,
*QDZ6*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ6` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque variation with load, QDZ7** — Peak residual torque variation with load scalar

Peak residual torque, *Dmr*, variation
with load, *QDZ7*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ7` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque variation with camber, QDZ8** — Peak residual torque variation with camber scalar

Peak residual torque, *Dmr*, variation
with camber, *QDZ8*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ8` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque variation with camber and load, QDZ9** — Peak residual torque variation with camber and load scalar

Peak residual torque, *Dmr*, variation
with camber and load, *QDZ9*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ9` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque variation with square of camber, QDZ10** — Peak residual torque variation with camber scalar

Peak residual torque, *Dmr*, variation
with square of camber, *QDZ10*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ10` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Dmr peak residual torque variation with square of load, QDZ11** — Peak residual torque variation with load scalar

Peak residual torque, *Dmr*, variation
with square of load, *QDZ11*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDZ11` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Ept trail curvature at FZNOM, QEZ1** — Trail curvature at nominal force scalar

Trail curvature, *Ept*, at nominal
force, *FZNOM*, *QEZ1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QEZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Ept variation with load, QEZ2** — Trail curvature variation with load scalar

Trail curvature, *Ept* variation with
load, *QEZ2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QEZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Ept variation with square of load, QEZ3** — Trail curvature variation with load scalar

Trail curvature, *Ept* variation with
square of load, *QEZ3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QEZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Ept variation with sign of alpha-t, QEZ4** — Trail curvature variation scalar

Trail curvature, *Ept* variation with
sign of alpha-t, *QEZ4*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QEZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Ept variation with sign of alpha-t and camber, QEZ5** — Variation scalar

Trail curvature, *Ept* variation with
sign of alpha-t and camber, *QEZ5*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QEZ5` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht horizontal trail shift at FZNOM, QHZ1** — Horizontal trail shift at nominal load scalar

Horizontal trail shift, *Sht*, at
nominal load, *FZNOM*,
*QHZ1*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QHZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht variation with load, QHZ2** — Horizontal trail shift variation with load scalar

Horizontal trail shift, *Sht*,
variation with load, *QHZ2*, dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QHZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht variation with camber, QHZ3** — Horizontal trail shift variation with camber scalar

Horizontal trail shift, *Sht*,
variation with camber, *QHZ3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QHZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Sht variation with load and camber, QHZ4** — Horizontal trail shift variation with load and camber scalar

Horizontal trail shift, *Sht*,
variation with load and camber, *QHZ4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QHZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Inflation pressure influence on trail length, PPZ1** — Pressure influence on trail length scalar

Inflation pressure influence on trail length, *PPZ1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Inflation pressure influence on residual aligning torque, PPZ2** — Pressure influence on aligning torque scalar

Inflation pressure influence on residual aligning torque,
*PPZ2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal value of s/R0: effect of Fx on Mz, SSZ1** — Effect of longitudinal force on aligning torque scalar

Nominal value of s/R0: effect of longitudinal force,
*Fx*, on aligning torque,
*Mz*, *SSZ1*,
dimensionless.

#### Dependencies

If you clear **Ply steer**, the block internally sets this
parameter to 0 in the Magic Formula equations.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SSZ1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with lateral to nominal force ratio, SSZ2** — Variation with lateral to nominal force ratio scalar

Variation with lateral to nominal force ratio, *SSZ2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SSZ2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with camber, SSZ3** — Variation with camber scalar

Variation with camber, *SSZ3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SSZ3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **s/R0 variation with camber and load, SSZ4** — Variation with camber and load scalar

Variation with camber and load, *SSZ4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SSZ4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Turnslip

### **Fx peak reduction due to spin, PDXP1** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin, *PDXP1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDXP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fx peak reduction due to spin with varying load, PDXP2** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin with varying load, *PDXP2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDXP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fx peak reduction due to spin with slip ratio, PDXP3** — Longitudinal force peak reduction due to spin scalar

Longitudinal force, *Fx*, peak
reduction due to spin with slip ratio, *PDXP3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDXP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Cornering stiffness reduction due to spin, PKYP1** — Stiffness reduction due to spin scalar

Cornering stiffness reduction due to spin, *PKYP1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin, PDYP1** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin, *PDYP1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin with varying load, PDYP2** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin with varying load, *PDYP2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDYP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to spin with slip angle, PDYP3** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to spin with slip angle, *PDYP3*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDYP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy peak reduction due to square root of spin, PDYP4** — Lateral force peak reduction due to spin scalar

Lateral force, *Fy*, peak reduction
due to square root of spin, *PDYP4*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDYP4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response lateral shift limit, PHYP1** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response lateral shift limit, *PHYP1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHYP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response max lateral shift limit, PHYP2** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response max lateral shift limit, *PHYP2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHYP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response max lateral shift limit with load, PHYP3** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response max lateral shift limit with load, *PHYP3*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHYP3` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Fy vs. slip angle response lateral shift curvature factor, PHYP4** — Lateral force versus slip angle response scalar

Lateral force, *Fy*, versus slip angle
response lateral shift curvature factor, *PHYP4*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHYP4` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber stiffness reduction due to spin, PECP1** — Camber stiffness reduction scalar

Camber stiffness reduction due to spin, *PECP1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PECP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Camber stiffness reduction due to spin with load, PECP2** — Camber stiffness reduction scalar

Camber stiffness reduction due to spin with load, *PECP2*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PECP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip pneumatic trail reduction factor, QDTP1** — Turn slip pneumatic trail reduction factor scalar

Turn slip pneumatic trail reduction factor, *QDTP1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDTP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn moment for constant turning and zero longitudinal speed, QCRP1** — Turn moment for constant turning scalar

Turn moment for constant turning and zero longitudinal speed,
*QCRP1*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QCRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment increase with spin at 90deg slip angle, QCRP2** — Turn slip moment scalar

Turn slip moment increase with spin at 90-degree slip angle,
*QCRP2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QCRP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Residual spin torque reduction from side slip, QBRP1** — Residual spin torque reduction scalar

Residual spin torque reduction from side slip, *QBRP1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QBRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment peak magnitude, QDRP1** — Turn slip moment peak magnitude scalar

Turn slip moment peak magnitude, *QDRP1*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDRP1` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Turn slip moment curvature, QDRP2** — Turn slip moment curvature scalar

Turn slip moment curvature, *QDRP2*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QDRP2` |
| **Values:** | scalar |
| **Data Types:** | `double` |
## Libraries

Vehicle Dynamics Blockset / Wheels and Tires

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: New **Tire type** option

Starting in R2024b, you can specify **Tire type** to use the new built-in
tire model, `Light passenger car 245/60R16`.

### R2024b: Renamed block parameters

Starting in R2024b, these parameters have been renamed.

| Old Name | New Name |
| --- | --- |
| **Wheel width** | **Tire nominal section width** |
| **Unloaded radius** | **Tire unloaded radius** |
| **Initial rotational velocity** | **Initial wheel rotational velocity** |
| **Wheel mass** | **Tire mass** |
| **Rotational inertia** | **Tire rotational inertia** |

### R2024b: New **Vertical Motion** option

Starting in R2024b, specifying **Vertical Motion** as `External Deflection` enables the **RadialDeflct** port. Use this port to define the sidewall deflection when interfacing with a tire in cases where forces are not provided.

### R2024b: New signals added to the **Info** port bus

Starting in R2024b, the **Info** port bus contains these new signals.

| Signal | Description |
| --- | --- |
| `RadialDeflct` | Tire radial deflection |
| `RL` | Loaded radius |
| `WhlTrq` | Wheel torque |

### R2024a: Plot steady-state force and moment responses

If you have the Extended Tire Features for Vehicle Dynamics Blockset support package installed, you can use the new **Plot
steady state force, moment response** button to generate plots.

### R2023a: New **Vertical Motion** Parameter

Starting from R2023a, the Combined Slip Wheel 2DOF block includes the **Vertical
Motion** parameter. By default, the Combined Slip Wheel 2DOF block uses the Magic
Formula to calculate the vertical motion of the tire.

### R2022b: Specify Brake and Tire Parameters for Each Wheel

Starting from R2022b, you can to use the Combined Slip Wheel 2DOF block to specify brake and
tire characteristics for each wheel on your vehicle. Specifically, the block allows
*N*-by-`1` vectors for these parameters:

- **Static friction coefficient, mu\_static**
- **Kinetic friction coefficient, mu\_kinetic**
- **Disc brake actuator bore, disc\_abore**
- **Brake pad mean radius, Rm**
- **Number of brake pads, num\_pads**
- **Drum brake actuator bore, disc\_abore**
- **Initial rotational velocity, omegao**
- **Rotational damping, br**
- **Wheel mass, MASS**
- **Rotational inertia (rolling axis), IYY**
- **Initial tire displacement, zo**
- **Initial wheel vertical velocity (wheel fixed frame),
  zdoto**

*N* is the number of wheels and must match the input signal dimensions.

### R2022b: New **Ply steer** and **Turn slip** Parameters

Starting from R2022b, the Combined Slip Wheel 2DOF block includes **Ply steer** and
**Turn slip** parameters. To remove ply steer and turn slip from the
Magic Formula implementation of these blocks, clear the **Ply steer** and
**Turn slip** parameters.

## Description

Combined slip 2DOF wheel with disc, drum, or mapped brake

Combined Slip Wheel 2DOF incorporates
two degrees of freedom (DOF's) of wheel motion, and 6 DOF's of tire forcing, in combined
longitudinal and lateral slip conditions.

- Wheel motion: Rotation about spin axis, and vertical displacement.
- Tire forces and moments: Fx, Fy, and Fz; Mx, My, and Mz.

It models the tire using the Magic Formula 6.2.[1] and [2] Set the Magic Formula 6.2 coefficients by either importing your own
tire model file, or selecting one of the built-in tire models.

Use this block in simulations like the following.

- Vehicle braking and acceleration, including rolling resistance.
- Vehicle ride motions, including effects of suspension modes.
- Maneuvers with combined lateral and longitudinal slip, such as lateral
  vehicle motion and yaw stability.

If you install the Extended Tire Features for Vehicle Dynamics Blockset support package, these additional capabilities are available:

- Plot generation — Click the **Plot steady state force, moment
  response** button to generate these plots:

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle
    [rad]**
  - **Longitudinal force [N] vs Longitudinal slip
    []**
  - **Longitudinal force [N] vs Lateral force
    [N]**
- Import tire parameters — Use the `tireModel.get` method to import tire parameter values defined in the
  Combined Slip Wheel 2DOF block to a `tireModel` object.
- Export tire parameters — Use the `set`
  method to export tire parameter values from a `tireModel` object to
  the Combined Slip Wheel 2DOF block.
- Tire model conversion — Use the `convert` method to convert a tire model of one of these types to a
  Magic Formula 6.2 tire model that you can import to the Combined Slip Wheel 2DOF block:

  - Magic Formula 5.2
  - Fiala
  - Dugoff

Use the **Tire type** parameter to select the
source of the tire data.

| Goal | Action |
| --- | --- |
| Import your own external file containing Magic Formula coefficients, and use them to drive the empirical equations modeling the tire1 and 2. The file you import can be a .mat, .tir, or .txt type, and must contain parameter names corresponding to those in the tire block. | Update the block parameters with fitting coefficients from a file:  1. Set **Tire type** to `External    file`. 2. On the **Wheel and Tire Parameters** > **External    tire source** pane, select **Select file**. 3. Select the tire coefficient file. 4. Select **Update mask values from file**. In the dialog box that    prompts you for confirmation, click **OK**. The block updates the    parameters. 5. Select **Apply**. |
| Select one of the Magic Formula built-in tire models to drive the empirical equations modeling the tire 1 and 2. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the tire that you    want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Select **Update block with applicable tire    values**. On the **Tire    Parameters** tab, the block updates the    applicable parameters, including **Tire nominal    section width**, **Rim    radius**, and **Tire mass**. 3. Select **Apply**. |

Use the **Brake Type** parameter to select the
brake.

| Action | Brake Type Setting |
| --- | --- |
| No braking | `None` |
| Implement brake that converts the brake cylinder pressure into a braking force | `Disc` |
| Implement simplex drum brake that converts the applied force and brake geometry into a net braking torque | `Drum` |
| Implement lookup table that is a function of the wheel speed and applied brake pressure | `Mapped` |

### Rotational Wheel Dynamics

The block calculates the inertial response of the wheel subject to:

- Axle losses
- Brake and drive torque
- Tire rolling resistance
- Ground contact through the tire-road interface

To implement the Magic Formula 6.2, the block uses these
equations from the cited references:

| Calculation | Equations |
| --- | --- |
| Longitudinal force | *Tire and Vehicle Dynamics*2 equations 4.E9 through 4.E57 |
| Lateral force - pure sideslip | *Tire and Vehicle Dynamics*2 equations 4.E19 through 4.E30 |
| Lateral force - combined slip | *Tire and Vehicle Dynamics*2 equations 4.E58 through 4.E67 |
| Vertical dynamics | *Tire and Vehicle Dynamics*2 equations 4.E68, 4.E1, 4.E2a, and 4.E2b |
| Overturning couple | *Tire and Vehicle Dynamics*2 equation 4.E69 |
| Rolling resistance | - *An improved Magic Formula/Swift tyre model that   can handle inflation pressure   changes*1 equation   6.1.2 - *Tire and Vehicle   Dynamics*2   equation 4.E70 |
| Aligning moment | *Tire and Vehicle Dynamics*2 equation 4.E31 through 4.E49 |
| Aligning torque - combined slip | *Tire and Vehicle Dynamics*2 equation 4.E71 through 4.E78  If you clear **Include turn slip**, the block sets some of these equations to 1. |

The input torque is the summation of the applied axle torque, braking torque, and
moment arising from the combined tire torque.

Ti=Ta−Tb+Td

For the moment arising from the combined tire torque, the block implements
tractive wheel forces and rolling resistance with first-order dynamics. The rolling
resistance has a time constant parameterized in terms of a relaxation length.

Td(s)=1Le|ω|Res+1(FxRe+My)

Braking torque is based on an idealized dry clutch friction model (if brakes are
selected). Depending on the lockup condition, the block implements these friction
and dynamic models:

| If | Lockup Condition | Friction Model | Dynamic Model |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | Unlocked | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | Locked | Tf=Ts | ω=0 |

The equations use these variables.

|  |  |
| --- | --- |
| *ω* | Wheel angular velocity |
| *a* | Velocity independent force component |
| *b* | Linear velocity force component |
| *c* | Quadratic velocity force component |
| *Le* | Tire relaxation length |
| *J* | Moment of inertia |
| *My* | Rolling resistance torque |
| *Ta* | Applied axle torque about wheel spin axis |
| *Tb* | Braking torque |
| *Td* | Combined tire torque |
| *Tf* | Frictional torque |
| *Ti* | Net input torque |
| *Tk* | Kinetic frictional torque |
| *To* | Net output torque |
| *Ts* | Static frictional torque |
| *Fc* | Applied clutch force |
| *Fx* | Longitudinal force developed by the tire road interface due to slip |
| *Reff* | Effective clutch radius |
| *Ro* | Annular disk outer radius |
| *Ri* | Annular disk inner radius |
| *Re* | Effective tire radius while under load and for a given pressure |
| *Vx* | Longitudinal axle velocity |
| *Fz* | Vehicle normal force |
| *ɑ* | Tire pressure exponent |
| *β* | Normal force exponent |
| *pi* | Tire pressure |
| *μs* | Coefficient of static friction |
| *μk* | Coefficient of kinetic friction |

### Tire and Wheel Coordinate Systems

To resolve the forces and moments, the block uses the Z-Up orientation of the tire and wheel coordinate systems.

- Tire coordinate system axes (*XT*, *YT*, *ZT*) are fixed in a reference frame attached to the tire. The origin is at the tire contact with the ground.
- Wheel coordinate system axes (*XW*, *YW*, *ZW*) are fixed in a reference frame attached to the wheel. The origin is at the wheel center.

**Z-Up Orientation**1

Z-Up tire and wheel coordinate systems showing wheel plane and road plane

### Brakes

**Disc**

If you specify the **Brake Type** parameter as
`Disc`, the block implements a disc brake. This figure
shows the side and front views of a disc brake.

Front and side view of disc brake, showing pad, disc, and caliper

A disc brake converts brake cylinder pressure from the brake cylinder into force. The disc brake applies the force at the brake pad mean radius.

The block uses these equations to calculate brake torque for the disc brake.

T={μPπBa2RmNpads4                when N≠0μstaticPπBa2RmNpads4         when N=0

Rm=Ro+Ri2

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *Npads* | Number of brake pads in disc brake assembly |
| *μstatic* | Disc pad-rotor coefficient of static friction |
| *μ* | Disc pad-rotor coefficient of kinetic friction |
| *Ba* | Brake actuator bore diameter |
| *Rm* | Mean radius of brake pad force application on brake rotor |
| *Ro* | Outer radius of brake pad |
| *Ri* | Inner radius of brake pad |

**Drum**

If you specify the **Brake Type** parameter as
`Drum`, the block implements a static (steady-state)
simplex drum brake. A simplex drum brake consists of a single two-sided hydraulic
actuator and two brake shoes. The brake shoes do not share a common hinge pin.

The simplex drum brake model uses the applied force and brake geometry to calculate a net torque for each brake shoe. The drum model assumes that the actuators and shoe geometry are symmetrical for both sides, allowing a single set of geometry and friction parameters to be used for both shoes.

The block implements equations that are derived from these equations in
*Fundamentals of Machine Elements*.

Trshoe=(πμcr(cosθ2−cosθ1)Ba22μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))PTlshoe=(πμcr(cosθ2−cosθ1)Ba2−2μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))P

T={Trshoe+Tlshoe                 when N≠0(Trshoe+Tlshoe)μstaticμ   when N=0

Side view of drum brake

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *μstatic* | Disc pad-rotor coefficient of static friction |
| *μ* | Disc pad-rotor coefficient of kinetic friction |
| *Trshoe* | Right shoe brake torque |
| *Tlshoe* | Left shoe brake torque |
| *a* | Distance from drum center to shoe hinge pin center |
| *c* | Distance from shoe hinge pin center to brake actuator connection on brake shoe |
| *r* | Drum internal radius |
| *Ba* | Brake actuator bore diameter |
| *Θ1* | Angle from shoe hinge pin center to start of brake pad material on shoe |
| *Θ2* | Angle from shoe hinge pin center to end of brake pad material on shoe |

**Mapped**

If you specify the **Brake Type** parameter as
`Mapped`, the block uses a lookup table to determine the
brake torque.

T={fbrake(P,N)                   when N≠0(μstaticμ)fbrake(P,N)    when N=0

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| fbrake(P,N) | Brake torque lookup table |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *μstatic* | Friction coefficient of drum pad-face interface under static conditions |
| *μ* | Friction coefficient of disc pad-rotor interface |

The lookup table for the brake torque, fbrake(P,N), is a function of applied brake pressure and wheel speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in bar.
- *N* is wheel speed, in rpm.

Plot of brake torque as a function of wheel speed and applied brake pressure
