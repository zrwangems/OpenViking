---
type: simulink-block
title: 'Combined Slip Wheel STI'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'combinedslipwheelsti'
documentation_source_path: 'ref/combinedslipwheelsti.html'
language: en
---

# Combined Slip Wheel STI

## Ports
```yaml
ports:
- name: Xe
  summary: Wheel position in inertial reference frame N-by-3 vector
  direction: input
- name: DCM
  summary: Direction cosine matrix 3-by-3 vector
  direction: input
- name: Ang
  summary: Rotation angle of the rim 3-by-3 vector
  direction: input
- name: Ve
  summary: Wheel velocity in inertial reference frame N-by-3 vector
  direction: input
- name: Omega
  summary: Rotational velocity N-by-3 vector
  direction: input
- name: OmegaWc
  summary: Rim rotational velocity scalar
  direction: input
- name: Road
  summary: Wheel position, rotation matrix, velocity 1-by-18 vector
  direction: input
- name: ScaleFctrs
  summary: Scale factors 27-by-N array
  direction: input
- name: Prs
  summary: Tire inflation pressure scalar | N-by-1 vector
  direction: input
- name: Info
  summary: Block data bus
  direction: output
- name: Fwc
  summary: Force at wheel center 1-by-3 vector
  direction: output
- name: Mwc
  summary: Moment at wheel center 1-by-3 vector
  direction: output
```

### Input

### **Xe** — Wheel position in inertial reference frame `N`-by-`3` vector

Wheel position along inertial-fixed *X*-,
*Y*-, *Z*-axes, respectively,
in m.

Vector is the number of wheels,
*N*, by `3`.

### **DCM** — Direction cosine matrix `3`-by-`3` vector

Transformation matrix from the wheel coordinate system to the
Earth-fixed inertial coordinate system.

### **Ang** — Rotation angle of the rim `3`-by-`3` vector

Rotation angle of rim with respect to the wheel center, in rad.

### **Ve** — Wheel velocity in inertial reference frame `N`-by-`3` vector

Wheel velocity along inertial-fixed *X*-,
*Y*-, and *Z*-axes,
respectively, in m/s.

Vector is the number of wheels,
*N*, by `3`.

### **Omega** — Rotational velocity `N`-by-`3` vector

Wheel rotational velocity along inertial-fixed
*X*-, *Y*-, and
*Z*-axes, respectively, in rad/s.

Vector is the number of wheels,
*N*, by `3`.

### **OmegaWc** — Rim rotational velocity `scalar`

Rim rotational velocity, *ω*, about wheel spin axis,
in rad/s.

### **Road** — Wheel position, rotation matrix, velocity `1`-by-`18` vector

Vector containing wheel position, rotation, and velocity with respect
to the Earth-fixed inertial coordinate system.

| Vector Element | Description |
| --- | --- |
| `Road(1,1)`  `Road(1,2)`  `Road(1,3)` | Wheel position along inertial-fixed *X*-, *Y*-, and *Z*-axes, respectively, in m. |
| `Road(1,4)`  `Road(1,5)`  `Road(1,6)`  `Road(1,7)`  `Road(1,8)`  `Road(1,9)`  `Road(1,10)`  `Road(1,11)`  `Road(1,12)` | Transformation matrix from the wheel coordinate system to the Earth-fixed inertial coordinate system. |
| `Road(1,13)`  `Road(1,14)`  `Road(1,15)` | Wheel velocity along inertial-fixed *X*-, *Y*-, and *Z*-axes, respectively, in m/s. |
| `Road(1,16)`  `Road(1,17)`  `Road(1,18)` | Wheel angular velocity along inertial-fixed *X*-, *Y*-, and *Z*-axes, respectively, in rad/s. |

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

### **Prs** — Tire inflation pressure `scalar` | `N`-by-`1` vector

Tire inflation pressure, *pi*,
in Pa.

Vector is the number of wheels,
*N*, by `1`. If you provide a
scalar value, the block assumes that number of wheels is one.

#### Dependencies

To create this port, select **Input tire
pressure**.
### Output

### **Info** — Block data bus

Block data, returned as a bus signal containing these block
values.

| Signal | | Description | Units |
| --- | --- | --- | --- |
| `CPI_info` | `Omega` | Wheel angular velocity about wheel-fixed *y*-axis | rad/s |
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
| `Gamma` | Camber angle | rad |
| `psidot` | Tire angular velocity about the tire-fixed *z*-axis (yaw rate) | rad/s |
| `RadialDeflct` | Tire radial deflection | m |
| `FNormal` | Vertical sidewall force on ground along tire-fixed *z*-axis | N |
| `Prs` | Tire inflation pressure | Pa |
| `DCM` | | Transformation matrix from the wheel coordinate system to the Earth-fixed inertial coordinate system | NA |
| `Xe` | | Wheel position along inertial-fixed *X*-, *Y*-, *Z*-axes, respectively | m |
| `Ang` | | Rotation angle of the rim with respect to the wheel center | rad |
| `Omega` | | Tire rotational velocity, *ω*, about wheel spin axis | rad/s |
| `Ve` | | Wheel velocity along inertial-fixed *X*-, *Y*-, *Z*-axes, respectively | m/s |
| `OmegaWc` | | Rim rotational velocity, *ω*, about wheel spin axis | rad/s |
| `Road` | | Vector containing wheel position, rotation, and velocity with respect to the Earth-fixed inertial coordinate system | NA |

### **Fwc** — Force at wheel center `1`-by-`3` vector

Force applied at wheel center by tire along wheel-fixed
*x*-, *y*-,
*z*-axes, respectively, in N.

### **Mwc** — Moment at wheel center `1`-by-`3` vector

Moment applied at wheel center by tire about wheel-fixed
*x*-, *y*-,
*z*-axes, respectively, in N·m.
## Parameters
```yaml
parameters:
- name: Tire type
  summary: Select type External file | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger
    car 235/45R18 | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
  group: Tire Options
  block_parameter: tireType
  values: External file (default) | Light passenger car 205/60R15 | Light passenger car 245/60R16 | Mid-size passenger car
    235/45R18 | Performance car 225/40R19 | SUV 265/50R20 | Light truck 275/65R18 | Commercial truck 295/75R22.5
- name: Tire file or object, tireParamSet
  summary: Tire file .mat | .tir | .txt
  group: Tire Options
  block_parameter: tireParamSet
  values: vdynPassCar.mat (default) | .tir | .txt
- name: Tire side
  summary: Select tire side Right (default) | Left | Symmetric
  group: Tire Options
  block_parameter: TireSide
  values: Right (default) | Left | Symmetric
- name: Tire pressure
  summary: Select tire side scalar
  group: Tire Options
  block_parameter: TirePrs
  values: scalar
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
- name: Install Extended Tire Features
  summary: Option to install Extended Tire Features for Vehicle Dynamics Blockset™ support package button
  group: Plotting
- name: Plot steady state force, moment response
  summary: Option to plot steady-state force and moment tire responses button
  group: Plotting
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
- name: Default tyre side, tyreside
  summary: Side 'Right' (default) | char
  group: Simulation
  block_parameter: tyreside
  values: '''Right'' (default) | char'
- name: Initial wheel rotational velocity, omegao
  summary: Velocity scalar
  group: Simulation
  block_parameter: omegao
  values: scalar
- name: Tire unloaded radius, UNLOADED_RADIUS
  summary: Radius scalar
  group: Dimension
  block_parameter: UNLOADED_RADIUS
  values: scalar
- name: Tire nominal section width, WIDTH
  summary: Width scalar
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
  summary: Mass scalar
  group: Inertial and Damping
  block_parameter: MASS
  values: scalar
- name: Tire rotational inertia (rolling axis), IYY
  summary: Inertia scalar
  group: Inertial and Damping
  block_parameter: IYY
  values: scalar
- name: Rotational damping, br
  summary: Damping scalar
  group: Inertial and Damping
  block_parameter: br
  values: scalar
- name: Gravity, GRAVITY
  summary: Gravity scalar
  group: Inertial and Damping
  block_parameter: GRAVITY
  values: scalar
- name: Initial tire displacement, zo
  summary: Displacement scalar
  group: Vertical
  block_parameter: zo
  values: scalar
- name: Initial wheel vertical velocity (wheel fixed frame), zdoto
  summary: Velocity scalar
  group: Vertical
  block_parameter: zdoto
  values: scalar
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
  summary: Stiffness scalar
  group: Vertical
  block_parameter: PFZ1
  values: scalar
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

Use the **Tire type** parameter to select the source of the tire data.

| Goal | Action |
| --- | --- |
| Implement the Magic Formula 6.2 using empirical equations1, 2. The equations use fitting coefficients that correspond to the block parameters. | Update the block parameters with fitting coefficients from a file:  1. Set **Tire type** to `External file`. 2. On the **External tire    source** pane, Click **Select    file**. 3. Select the tire coefficient file. 4. Click **Update mask values from    file**. In the dialog box that prompts    you for confirmation, click    **OK**. The block updates the    parameters. 5. Click **Apply**. |
| Select one of the Magic Formula 6.2 built-in tire models to drive the empirical equations modeling the tire 1 and 2. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the    tire that you want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Click **Update block with    applicable tire values**. On the    **Tire Parameters** tab, the    block updates the applicable parameters, including    **Tire nominal section width**,    **Rim radius**, and    **Tire mass**. 3. Click **Apply**. |

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
| **Values:** | `External file` (default) | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **Data Types:** | `character vector` |

### **Tire file or object, tireParamSet** — Tire file `.mat` | `.tir` | `.txt`

Tire file `.tir` or object containing empirical data
to model tire longitudinal and lateral behavior with the Magic Formula
6.2. If you provide an `.txt` file, make sure the file
contains names that correspond to the block parameters.

Update the block parameters with
fitting coefficients from a file:

1. Set **Tire type** to
   `External file`.
2. On the **External tire source** pane,
   click **Select file**.
3. Select the tire coefficient file.
4. Click **Update mask values from file**.
   In the dialog box that prompts you for confirmation, click
   **OK**. The block updates the
   parameters.
5. Click **Apply**.

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

### **Tire side** — Select tire side `Right` (default) | `Left` | `Symmetric`

Specify the tire side.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `TireSide` |
| **Values:** | `Right` (default) | `Left` | `Symmetric` |
| **Data Types:** | `character vector` |

### **Tire pressure** — Select tire side scalar

Tire inflation pressure, *p*, in Pa.

#### Dependencies

To enable this parameter, clear **Input tire
pressure**.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `TirePrs` |
| **Values:** | scalar |
| **Data Types:** | `double` |

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

### Plotting

### **Install Extended Tire Features** — Option to install Extended Tire Features for Vehicle Dynamics Blockset™ support package button

Click **Install Extended Tire Features** to install the
Extended Tire Features for Vehicle Dynamics Blockset support package. With the support package, you can plot
steady-state force and moment tire responses from the Combined Slip Wheel STI Block
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

Velocity tolerance used to handle low-velocity situations,
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

### **Default tyre side, tyreside** — Side `'Right'` (default) | char

Default tyre side, *tyreside*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tyreside` |
| **Values:** | `'Right'` (default) | char |
| **Data Types:** | `character vector` |

### **Initial wheel rotational velocity, omegao** — Velocity scalar

Initial rotational velocity, specified as a
scalar, in rad/s.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Dimension

### **Tire unloaded radius, UNLOADED\_RADIUS** — Radius scalar

Tire unloaded radius, *UNLOADED\_RADIUS*, in m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `UNLOADED_RADIUS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Tire nominal section width, WIDTH** — Width scalar

Tire nominal section width, *WIDTH*, in m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `WIDTH` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Rim radius, RIM\_RADIUS** — Radius scalar

Rim radius, *RIM\_RADIUS*, in m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `RIM_RADIUS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Nominal aspect ratio, ASPECT\_RATIO** — Ratio scalar

Nominal aspect ratio, *ASPECT\_RATIO*,
dimensionless.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `ASPECT_RATIO` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Inertial and Damping

### **Tire mass, MASS** — Mass scalar

Tire mass, specified as a scalar, in
kg.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `MASS` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — Inertia scalar

Tire rotational inertia (rolling
axis), specified as a scalar, in
kg·m2.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `IYY` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Rotational damping, br** — Damping scalar

Rotational damping, specified as a
scalar, in N·m·s/rad.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Gravity, GRAVITY** — Gravity scalar

Gravity, *GRAVITY*, in m/s^2.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `GRAVITY` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### Vertical

### **Initial tire displacement, zo** — Displacement scalar

Initial tire displacement, *zo*, in m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zo` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — Velocity scalar

Initial wheel vertical velocity (wheel fixed frame), *zdoto*,
in m/s.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zdoto` |
| **Values:** | scalar |
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

### **Linear load change with deflection, Q\_FZ1** — Load change scalar

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

### **Stiffness response to pressure, PFZ1** — Stiffness scalar

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
| **Values:** | scalar |
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

**Introduced in R2021b**

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

### R2024b: New signal added to the **Info** port bus

Starting from R2024b, the **Info** port bus contains this new signal.

| Signal | Description |
| --- | --- |
| `RadialDeflct` | Tire radial deflection |

### R2024a: Plot steady-state force and moment responses

If you have the Extended Tire Features for Vehicle Dynamics Blockset support package installed, you can use the new **Plot
steady state force, moment response** button to generate plots.

### R2022b: New **Ply steer** and **Turn slip** Parameters

Starting from R2022b, the Combined Slip Wheel STI block includes **Ply steer** and
**Turn slip** parameters. To remove ply steer and turn slip from the
Magic Formula implementation of these blocks, clear the **Ply steer** and
**Turn slip** parameters.

## Description

Combined slip wheel compliant with STI Tydex standard

The Combined Slip Wheel STI block implements the longitudinal and
lateral behavior of a wheel characterized by the Magic Formula[1][2] 6.2 that complies with the standard tire interface (STI) Tyre Data
Exchange Format (TYDEX)[3] standard. You can import your own tire model or use a built-in tire
model. Use the block in driveline and vehicle simulations where low-frequency tire road
interactions are required to determine vehicle acceleration and wheel-rolling
resistance. The block is suitable for applications that require combined lateral slip,
for example, in lateral motion and yaw stability studies.

Based on the wheel rotational velocity, longitudinal and lateral velocity, wheel
camber angle, and inflation pressure, the block determines the vertical motion, forces,
and moments in all six degrees of freedom (DOF). Use the vertical DOF to study
tire-suspension resonances from road profiles or chassis motion.

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
  Combined Slip Wheel STI block to a `tireModel` object.
- Export tire parameters — Use the `set`
  method to export tire parameter values from a `tireModel` object to
  the Combined Slip Wheel STI block.
- Tire model conversion — Use the `convert` method to convert a tire model of one of these types to a
  Magic Formula 6.2 tire model that you can import to the Combined Slip Wheel STI block:

  - Magic Formula 5.2
  - Fiala
  - Dugoff

Use the **Tire type** parameter to select the source of the tire data.

| Goal | Action |
| --- | --- |
| Implement the Magic Formula 6.2 using empirical equations1, 2. The equations use fitting coefficients that correspond to the block parameters. | Update the block parameters with fitting coefficients from a file:  1. Set **Tire type** to `External file`. 2. On the **External tire    source** pane, Click **Select    file**. 3. Select the tire coefficient file. 4. Click **Update mask values from    file**. In the dialog box that prompts    you for confirmation, click    **OK**. The block updates the    parameters. 5. Click **Apply**. |
| Select one of the Magic Formula 6.2 built-in tire models to drive the empirical equations modeling the tire 1 and 2. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the    tire that you want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Click **Update block with    applicable tire values**. On the    **Tire Parameters** tab, the    block updates the applicable parameters, including    **Tire nominal section width**,    **Rim radius**, and    **Tire mass**. 3. Click **Apply**. |

### Rotational Wheel Dynamics

The block calculates the inertial response of the wheel subject to:

- Axle losses
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

### STI Wheel Coordinate System

The block uses wheel coordinate system axes
(*XW*,
*YW*,
*ZW*) that are fixed in a
reference frame attached to the wheel. The origin is at the wheel center.

The STI wheel coordinate system is shown in blue.

**Note**

The STI wheel coordinate system (blue) is equivalent to the TYDEX
centre-axis coordinate system.

1

Z-Up tire and wheel coordinate systems showing wheel plane and road plane

| Axis | Description |
| --- | --- |
| *XW* | *XW* and *YW* are parallel to the wheel plane:  - *XW*   is parallel to the local road plane. - *YW* is   parallel to the wheel-spin axis. |
| *YW* |
| *ZW* | *ZW* points upward. |
