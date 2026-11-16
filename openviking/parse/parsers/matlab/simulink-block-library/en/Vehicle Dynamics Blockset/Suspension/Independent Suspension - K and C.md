---
type: simulink-block
title: 'Independent Suspension - K and C'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Suspension'
documentation_page: 'independentsuspensionkandc'
documentation_source_path: 'ref/independentsuspensionkandc.html'
language: en
---

# Independent Suspension - K and C

## Ports

### Input

### **WhlPz** — Wheel `z`-axis displacement array

Wheel displacement, *zw*, along wheel-fixed
*z*-axis, in m. Array dimensions are `1` by the
total number of wheels on the vehicle.

For example, for a two-axle vehicle with two wheels per axle, the
`WhlPz`:

- Signal array dimensions are `[1x4]`.

  WhlPz=zw=[zw1,1zw1,2zw2,1zw2,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `WhlPz(1,1)` | `1` | `1` |
  | Front right | `WhlPz(1,2)` | `1` | `2` |
  | Rear left | `WhlPz(1,3)` | `2` | `1` |
  | Rear right | `WhlPz(1,4)` | `2` | `2` |

### **WhlRe** — Wheel effective radius array

Effective wheel radius, *Rew*, in m. Array
dimensions are `1` by the total number of wheels on the vehicle.

For example, for a two-axle vehicle with two wheels per axle, the
`WhlRe`:

- Signal array dimensions are `[1x4]`.

  WhlRe=Rew=[Rew1,1Rew1,2Rew2,1Rew2,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `WhlRe(1,1)` | `1` | `1` |
  | Front right | `WhlRe(1,2)` | `1` | `2` |
  | Rear left | `WhlRe(1,3)` | `2` | `1` |
  | Rear right | `WhlRe(1,4)` | `2` | `2` |

### **WhlVz** — Wheel `z`-axis velocity array

Wheel velocity, *żw*, along wheel-fixed
*z*-axis, in m. Array dimensions are `1` by the
total number of wheels on the vehicle.

For example, for a two-axle vehicle with two wheels per axle, the
`WhlVz`:

- Signal array dimensions are `[1x4]`.

  WhlVz=z˙w=[z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `WhlVz(1,1)` | `1` | `1` |
  | Front right | `WhlVz(1,2)` | `1` | `2` |
  | Rear left | `WhlVz(1,3)` | `2` | `1` |
  | Rear right | `WhlVz(1,4)` | `2` | `2` |

### **WhlFx** — Longitudinal wheel force on vehicle array

Longitudinal wheel force applied to vehicle,
*Fwx*, along the inertial-fixed
*x*-axis. Array dimensions are `1` by the total
number of wheels on the vehicle.

For example, for a two-axle vehicle with two wheels per axle, the
`WhlFx`:

- Signal array dimensions are `[1x4]`.

  WhlFx=Fwx=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `WhlFx(1,1)` | `1` | `1` |
  | Front right | `WhlFx(1,2)` | `1` | `2` |
  | Rear left | `WhlFx(1,3)` | `2` | `1` |
  | Rear right | `WhlFx(1,4)` | `2` | `2` |

### **WhlFy** — Lateral wheel force on vehicle array

Lateral wheel force applied to vehicle,
*Fwy*, along the inertial-fixed
*y*-axis. Array dimensions are `1` by the total number
of wheels on the vehicle.

For example, for a two-axle vehicle with two wheels per axle, the
`WhlFy`:

- Signal array dimensions are `[1x4]`.

  WhlFy=Fwy=[Fwy1,1Fwy1,2Fwy2,1Fwy2,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `WhlFy(1,1)` | `1` | `1` |
  | Front right | `WhlFy(1,2)` | `1` | `2` |
  | Rear left | `WhlFy(1.3)` | `2` | `1` |
  | Rear right | `WhlFy(1,4)` | `2` | `2` |

### **WhlM** — Suspension moment on wheel array

Longitudinal, lateral, and vertical suspension
moments at axle `a`, wheel `t`, applied to the wheel at the
axle wheel carrier reference coordinate, in N·m. Input array dimensions are
`3` by the number of wheels on the vehicle.

- `WhlM(1,...)` — Suspension moment applied to the wheel about the
  inertial-fixed *x*-axis (longitudinal)
- `WhlM(2,...)` — Suspension moment applied to the wheel about the
  inertial-fixed *y*-axis (lateral)
- `WhlM(3,...)` — Suspension moment applied to the wheel about the
  inertial-fixed *z*-axis (vertical)

For example, for a two-axle vehicle with two
wheels per axle, the `WhlM`:

- Signal dimensions are
  `[3x4]`.
- Signal contains suspension moments applied
  to four wheels according to their axle and wheel locations.

  WhlM=Mw=[Mwx1,1Mwx1,2Mwx2,1Mwx2,2Mwy1,1Mwy1,2Mwy2,1Mwy2,2Mwz1,1Mwz1,2Mwz2,1Mwz2,2]

  | Wheel | Array Element | Axle | Wheel Number | Moment Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `WhlM(1,1)` | `1` | `1` | Inertial-fixed *x*-axis (longitudinal) |
  | Front right | `WhlM(1,2)` | `1` | `2` |
  | Rear left | `WhlM(1,3)` | `2` | `1` |
  | Rear right | `WhlM(1,4)` | `2` | `2` |
  | Front left | `WhlM(2,1)` | `1` | `1` | Inertial-fixed *y*-axis (lateral) |
  | Front right | `WhlM(2,2)` | `1` | `2` |
  | Rear left | `WhlM(2,3)` | `2` | `1` |
  | Rear right | `WhlM(2,4)` | `2` | `2` |
  | Front left | `WhlM(3,1)` | `1` | `1` | Inertial-fixed *z*-axis (vertical) |
  | Front right | `WhlM(3,2)` | `1` | `2` |
  | Rear left | `WhlM(3,3)` | `2` | `1` |
  | Rear right | `WhlM(3,4)` | `2` | `2` |

### **VehP** — Vehicle displacement array

Vehicle displacement from axle `a`, wheel `t` along
inertial-fixed coordinate system, in m. Input array dimensions are `3`
by the number of wheels on the vehicle.

- `VehP(1,...)` — Vehicle displacement from wheel,
  *xv*, along the
  inertial-fixed *x*-axis
- `VehP(2,...)` — Vehicle displacement from wheel,
  *yv*, along the
  inertial-fixed *y*-axis
- `VehP(3,...)` — Vehicle displacement from wheel,
  *zv*, along the
  inertial-fixed *z*-axis

For example, for a two-axle vehicle with two wheels per axle, the
`VehP`:

- Signal dimensions are `[3x4]`.
- Signal contains four displacements according to their axle and wheel locations.

  VehP=[xvyvzv]=[xv1,1xv1,2xv2,1xv2,2yv1,1yv1,2yv2,1yv2,2zv1,1zv1,2zv2,1zv2,2]

  | Wheel | Array Element | Axle | Wheel Number | Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `VehP(1,1)` | `1` | `1` | Inertial-fixed *x*-axis |
  | Front right | `VehP(1,2)` | `1` | `2` |
  | Rear left | `VehP(1,3)` | `2` | `1` |
  | Rear right | `VehP(1,4)` | `2` | `2` |
  | Front left | `VehP(2,1)` | `1` | `1` | Inertial-fixed *y*-axis |
  | Front right | `VehP(2,2)` | `1` | `2` |
  | Rear left | `VehP(2,3)` | `2` | `1` |
  | Rear right | `VehP(2,4)` | `2` | `2` |
  | Front left | `VehP(3,1)` | `1` | `1` | inertial-fixed *z*-axis |
  | Front right | `VehP(3,2)` | `1` | `2` |
  | Rear left | `VehP(3,3)` | `2` | `1` |
  | Rear right | `VehP(3,4)` | `2` | `2` |

### **VehV** — Vehicle velocity array

Vehicle velocity at axle `a`, wheel `t` along
inertial-fixed coordinate system, in m. Input array dimensions are `3`
by the number of wheels on the vehicle.

- `VehV(1,...)` — Vehicle velocity at wheel,
  *xv*, along the
  inertial-fixed *x*-axis
- `VehV(2,...)` — Vehicle velocity at wheel,
  *yv*, along the
  inertial-fixed *y*-axis
- `VehV(3,...)` — Vehicle velocity at wheel,
  *zv*, along the
  inertial-fixed *z*-axis

For example, for a two-axle vehicle with two wheels per axle, the
`VehV`:

- Signal dimensions are `[3x4]`.
- Signal contains `4` velocities according to their
  axle and wheel locations.

  VehV=[x˙vy˙vz˙v]=[x˙v1,1x˙v1,2x˙v2,1x˙v2,2y˙v1,1y˙v1,2y˙v2,1y˙v2,2z˙v1,1z˙v1,2z˙v2,1z˙v2,2]

  | Wheel | Array Element | Axle | Wheel Number | Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `VehV(1,1)` | `1` | `1` | Inertial-fixed *x*-axis |
  | Front right | `VehV(1,2)` | `1` | `2` |
  | Rear left | `VehV(1,3)` | `2` | `1` |
  | Rear right | `VehV(1,4)` | `2` | `2` |
  | Front left | `VehV(2,1)` | `1` | `1` | Inertial-fixed *y*-axis |
  | Front right | `VehV(2,2)` | `1` | `2` |
  | Rear left | `VehV(2,3)` | `2` | `1` |
  | Rear right | `VehV(2,4)` | `2` | `2` |
  | Front left | `VehV(3,1)` | `1` | `1` | Inertial-fixed *z*-axis |
  | Front right | `VehV(3,2)` | `1` | `2` |
  | Rear left | `VehV(3,3)` | `2` | `1` |
  | Rear right | `VehV(3,4)` | `2` | `2` |

### **StrgAng** — Steering angle, optional array

Optional steering angle for each wheel, *δ*.
Input array dimensions are `1` by
the number of steered wheels.

For example, for a two-axle vehicle with two wheels per axle, you can input steering angles for both wheels on the first axle.

- To enable the **StrgAng** port, set **Steered axle enable by
  axle, StrgEnByAxl** to `[1 0]`. The input signal array
  dimensions are `[1x2]`.
- The `StrgAng` signal contains two steering angles according to
  their axle and wheel locations.

  StrgAng=δsteer=[δsteer1,1δsteer1,2]

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `StrgAng(1,1)` | `1` | `1` |
  | Front right | `StrgAng(1,2)` | `1` | `2` |

#### Dependencies

To enable the port **StrgAng**, set an element of the **Steered axle
enable by axle, StrgEnByAxl** vector to `1`.

### **Phi** — Vehicle pitch angle `scalar`

Vehicle pitch angle about earth-fixed *Y*-axis, in rad.

### **TrckWdth** — Track width `array`

Distance between wheels on each axle. Input array dimensions are `1`-by-`2`.

| Array Element | Description |
| --- | --- |
| `TrckWdth(1,1)` | Distance between wheels on front axle |
| `TrckWdth(1,2)` | Distance between wheels on rear axle |
### Output

### **Info** — Bus signal bus

Bus signal containing block values. The signals are arrays that depend on the wheel
location.

For example, these are the indices for a two-axle, two-wheel vehicle. The total number
of wheels is four.

- 1D array signal (1-by-4)

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `(1,1)` | `1` | `1` |
  | Front right | `(1,2)` | `1` | `2` |
  | Rear left | `(1,3)` | `2` | `1` |
  | Rear right | `(1,4)` | `2` | `2` |
- 3D array signal (3-by-4)

  | Wheel | Array Element | Axle | Wheel Number |
  | --- | --- | --- | --- |
  | Front left | `(1,1)` | `1` | `1` |
  | Front right | `(1,2)` | `1` | `2` |
  | Rear left | `(1,3)` | `2` | `1` |
  | Rear right | `(1,4)` | `2` | `2` |
  | Front left | `(2,1)` | `1` | `1` |
  | Front right | `(2,2)` | `1` | `2` |
  | Rear left | `(2,3)` | `2` | `1` |
  | Rear right | `(2,4)` | `2` | `2` |
  | Front left | `(3,1)` | `1` | `1` |
  | Front right | `(3,2)` | `1` | `2` |
  | Rear left | `(3,3)` | `2` | `1` |
  | Rear right | `(3,4)` | `2` | `2` |

| Signal | Description | Array Signal | Variable | Units |
| --- | --- | --- | --- | --- |
| `Camber` | Wheel angles according to the axle and wheel location. | 1D | WhlAng[1,...]=ξ=[ξa,t] | rad |
| `Caster` | WhlAng[2,...]=η=[ηa,t] |
| `Toe` | WhlAng[3,...]=ζ=[ζa,t] |
| `Height` | Suspension height | 1D | *H* | m |
| `Power` | Suspension power dissipation | 1D | *Psusp* | W |
| `Energy` | Suspension absorbed energy | 1D | *Esusp* | J |
| `VehF` | Suspension forces applied to the vehicle | 3D | For a two-axle, two wheels per axle vehicle:  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2] | N |
| `VehM` | Suspension moments applied to vehicle | 3D | For a two-axle, two wheels per axle vehicle:  VehM=Mv=[Mvx1,1Mvx1,2Mvx2,1Mvx2,2Mvy1,1Mvy1,2Mvy2,1Mvy2,2Mvz1,1Mvz1,2Mvz2,1Mvz2,2] | N·m |
| `WhlF` | Suspension force applied to wheel | 3D | For a two-axle, two wheels per axle vehicle:  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2] | N |
| `WhlP` | Wheel displacement | 3D | For a two-axle, two wheels per axle vehicle:  WhlP=[xwywzw]=[xw1,1xw1,2xw2,1xw2,2yw1,1yw1,2yw2,1ywy2,2zwtr1,1zwtr1,2zwtr2,1zwtr2,2] | m |
| `WhlV` | Wheel velocity | 3D | For a two-axle, two wheels per axle vehicle:  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2] | m/s |
| `WhlAng` | Wheel camber, caster, toe angles | 3D | For a two-axle, two wheels per axle vehicle:  WhlAng=[ξηζ]=[ξ1,1ξ1,2ξ2,1ξ2,2η1,1η1,2η2,1η2,2ζ1,1ζ1,2ζ2,1ζ2,2] | rad |

### **VehF** — Suspension force on vehicle `array`

Longitudinal, lateral, and vertical
suspension force at axle `a`,
wheel `t`, applied to the vehicle
at the suspension connection point, in N. Array
dimensions are `3` by the number
of wheels on the vehicle.

- `VehF(1,...)` — Suspension
  force applied to vehicle along the inertial-fixed
  *x*-axis (longitudinal)
- `VehF(2,...)` — Suspension
  force applied to vehicle along the inertial-fixed
  *y*-axis (lateral)
- `VehF(3,...)` — Suspension
  force applied to vehicle along the inertial-fixed
  *z*-axis (vertical)

For example, for a two-axle vehicle with two
wheels per axle, the `VehF`:

- Signal dimensions are
  `[3x4]`.
- Signal contains suspension forces applied to
  the vehicle according to the axle and wheel locations.

  VehF=Fv=[Fvx1,1Fvx1,2Fvx2,1Fvx2,2Fvy1,1Fvy1,2Fvy2,1Fvy2,2Fvz1,1Fvz1,2Fvz2,1Fvz2,2]

  | Wheel | Array Element | Axle | Wheel Number | Force Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `VehF(1,1)` | `1` | `1` | Inertial-fixed *x*-axis (longitudinal) |
  | Front right | `VehF(1,2)` | `1` | `2` |
  | Rear left | `VehF(1,3)` | `2` | `1` |
  | Rear right | `VehF(1,4)` | `2` | `2` |
  | Front left | `VehF(2,1)` | `1` | `1` | Inertial-fixed *y*-axis (lateral) |
  | Front right | `VehF(2,2)` | `1` | `2` |
  | Rear left | `VehF(2,3)` | `2` | `1` |
  | Rear right | `VehF(2,4)` | `2` | `2` |
  | Front left | `VehF(3,1)` | `1` | `1` | Inertial-fixed *z*-axis (vertical) |
  | Front right | `VehF(3,2)` | `1` | `2` |
  | Rear left | `VehF(3,3)` | `2` | `1` |
  | Rear right | `VehF(3,4)` | `2` | `2` |

### **VehM** — Suspension moment on vehicle `array`

Longitudinal, lateral, and vertical
suspension moment at axle `a`,
wheel `t`, applied to the vehicle
at the suspension connection point, in N·m. Array
dimensions are `3` by the number
of wheels on the vehicle.

- `VehM(1,...)` — Suspension
  moment applied to the vehicle about the
  inertial-fixed *x*-axis
  (longitudinal)
- `VehM(2,...)` — Suspension
  moment applied to the vehicle about the
  inertial-fixed *y*-axis
  (lateral)
- `VehM(3,...)` — Suspension
  moment applied to the vehicle about the
  inertial-fixed *z*-axis
  (vertical)

For example, for a two-axle vehicle with two
wheels per axle, the `VehM`:

- Signal dimensions are
  `[3x4]`.
- Signal contains suspension moments applied
  to vehicle according to the axle and wheel locations.

  VehM=Mv=[Mvx1,1Mvx1,2Mvx2,1Mvx2,2Mvy1,1Mvy1,2Mvy2,1Mvy2,2Mvz1,1Mvz1,2Mvz2,1Mvz2,2]

  | Array Element | Axle | Wheel Number | Moment Axis |
  | --- | --- | --- | --- |
  | `VehM(1,1)` | `1` | `1` | Inertial-fixed *x*-axis (longitudinal) |
  | `VehM(1,2)` | `1` | `2` |
  | `VehM(1,3)` | `2` | `1` |
  | `VehM(1,4)` | `2` | `2` |
  | `VehM(2,1)` | `1` | `1` | Inertial-fixed *y*-axis (lateral) |
  | `VehM(2,2)` | `1` | `2` |
  | `VehM(2,3)` | `2` | `1` |
  | `VehM(2,4)` | `2` | `2` |
  | `VehM(3,1)` | `1` | `1` | Inertial-fixed *z*-axis (vertical) |
  | `VehM(3,2)` | `1` | `2` |
  | `VehM(3,3)` | `2` | `1` |
  | `VehM(3,4)` | `2` | `2` |

### **WhlF** — Suspension force on wheel `array`

Longitudinal, lateral, and vertical
suspension forces at axle `a`,
wheel `t`, applied to the wheel
at the axle wheel carrier reference coordinate, in
N. Array dimensions are `3` by
the number of wheels on the vehicle.

- `WhlF(1,...)` — Suspension
  force on wheel along the inertial-fixed
  *x*-axis (longitudinal)
- `WhlF(2,...)` — Suspension
  force on wheel along the inertial-fixed
  *y*-axis (lateral)
- `WhlF(3,...)` — Suspension
  force on wheel along the inertial-fixed
  *z*-axis (vertical)

For example, for a two-axle vehicle with two
wheels per axle, the `WhlF`:

- Signal dimensions are
  `[3x4]`.
- Signal contains wheel forces applied to the
  vehicle according to the axle and wheel locations.

  WhlF=Fw=[Fwx1,1Fwx1,2Fwx2,1Fwx2,2Fwy1,1Fwy1,2Fwy2,1Fwy2,2Fwz1,1Fwz1,2Fwz2,1Fwz2,2]

  | Wheel | Array Element | Axle | Wheel Number | Force Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `WhlF(1,1)` | `1` | `1` | Inertial-fixed *x*-axis (longitudinal) |
  | Front right | `WhlF(1,2)` | `1` | `2` |
  | Rear left | `WhlF(1,3)` | `2` | `1` |
  | Rear right | `WhlF(1,4)` | `2` | `2` |
  | Front left | `WhlF(2,1)` | `1` | `1` | Inertial-fixed *y*-axis (lateral) |
  | Front right | `WhlF(2,2)` | `1` | `2` |
  | Rear left | `WhlF(2,3)` | `2` | `1` |
  | Rear right | `WhlF(2,4)` | `2` | `2` |
  | Front left | `WhlF(3,1)` | `1` | `1` | Inertial-fixed *z*-axis (vertical) |
  | Front right | `WhlF(3,2)` | `1` | `2` |
  | Rear left | `WhlF(3,3)` | `2` | `1` |
  | Rear right | `WhlF(3,4)` | `2` | `2` |

### **WhlV** — Wheel velocity `array`

Longitudinal, lateral, and vertical wheel velocity at axle `a`, wheel
`t`, in m/s. Array dimensions are `3` by the number of
wheels on the vehicle.

- `WhlV(1,...)` — Wheel velocity along the inertial-fixed
  *x*-axis (longitudinal)
- `WhlV(2,...)` — Wheel velocity along the inertial-fixed
  *y*-axis (lateral)
- `WhlV(3,...)` — Wheel velocity along the inertial-fixed
  *z*-axis (vertical)

For example, for a two-axle vehicle with two wheels per axle, the `WhlV`:

- Signal dimensions are `[3x4]`.
- Signal contains wheel forces applied to the vehicle according to the axle and wheel locations.

  WhlV=[x˙wy˙wz˙w]=[x˙w1,1x˙w1,2x˙w2,1x˙w2,2y˙w1,1y˙w1,2y˙w2,1y˙w2,2z˙w1,1z˙w1,2z˙w2,1z˙w2,2]

  | Wheel | Array Element | Axle | Wheel Number | Force Axis |
  | --- | --- | --- | --- | --- |
  | Front left | `WhlV(1,1)` | `1` | `1` | Inertial-fixed *x*-axis (longitudinal) |
  | Front right | `WhlV(1,2)` | `1` | `2` |
  | Rear left | `WhlV(1,3)` | `2` | `1` |
  | Rear right | `WhlV(1,4)` | `2` | `2` |
  | Front left | `WhlV(2,1)` | `1` | `1` | Inertial-fixed *y*-axis (lateral) |
  | Front right | `WhlV(2,2)` | `1` | `2` |
  | Rear left | `WhlV(2,3)` | `2` | `1` |
  | Rear right | `WhlV(2,4)` | `2` | `2` |
  | Front left | `WhlV(3,1)` | `1` | `1` | Inertial-fixed *z*-axis (vertical) |
  | Front right | `WhlV(3,2)` | `1` | `2` |
  | Rear left | `WhlV(3,3)` | `2` | `1` |
  | Rear right | `WhlV(3,4)` | `2` | `2` |

### **WhlAng** — Wheel camber, caster, toe angles `array`

Camber, caster, and toe angles at axle `a`, wheel
`t`, in rad. Array dimensions are `3` by the
number of wheels on the vehicle.

- `WhlAng(1,...)` — Camber angle
- `WhlAng(2,...)` — Caster angle
- `WhlAng(3,...)` — Toe angle

For example, for a two-axle vehicle with two wheels per axle, the
`WhlAng`:

- Signal dimensions are `[3x4]`.
- Signal contains angles according to the axle and wheel locations.

  WhlAng=[ξηζ]=[ξ1,1ξ1,2ξ2,1ξ2,2η1,1η1,2η2,1η2,2ζ1,1ζ1,2ζ2,1ζ2,2]

  | Wheel | Array Element | Axle | Wheel Number | Angle |
  | --- | --- | --- | --- | --- |
  | Front left | `WhlAng(1,1)` | `1` | `1` | Camber |
  | Front right | `WhlAng(1,2)` | `1` | `2` |
  | Rear left | `WhlAng(1,3)` | `2` | `1` |
  | Rear right | `WhlAng(1,4)` | `2` | `2` |
  | Front left | `WhlAng(2,1)` | `1` | `1` | Caster |
  | Front right | `WhlAng(2,2)` | `1` | `2` |
  | Rear left | `WhlAng(2,3)` | `2` | `1` |
  | Rear right | `WhlAng(2,4)` | `2` | `2` |
  | Front left | `WhlAng(3,1)` | `1` | `1` | Toe |
  | Front right | `WhlF(3,2)` | `1` | `2` |
  | Rear left | `WhlF(3,3)` | `2` | `1` |
  | Rear right | `WhlF(3,4)` | `2` | `2` |

## Parameters

### **Steered axle enable by axle, StrgEnByAxl** — Boolean vector to enable axle steering `[1 0]` (default) | `vector`

Boolean vector that enables axle steering,
*Ensteer*, dimensionless. Vector is
`1` by the number of vehicle axles,
*Na*. For example:

- `[1 0]` — For a two-axle vehicle, enables axle 1 steering
  and disables axle 2 steering
- `[1 1]` — For a two-axle vehicle, enables axle 1 and axle
  2 steering

#### Dependencies

Setting any element of the **Steered axle enable by axle,
StrgEnByAxl** vector to 1 creates Input port
`StrgAng`.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgEnByAxl` |
| **Values:** | `[1 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Anti-sway axle enable by axle, AntiSwayEnByAxl** — Boolean vector to enable axle anti-sway `[0 0]` (default) | `vector`

Boolean vector that enables axle anti-sway for axle *a*,
dimensionless. For example, `[1 0]` enables axle 1 anti-sway and
disables axle 2 anti-sway. Vector is `1` by the number of vehicle
axles, *Na*.

If you enable an anti-sway bar on the axle, the anti-sway bar
stiffness is the difference between the anti-sway bar torque parameter, **Suspension
roll stiffness with anti-roll bar, RollStiffArb**, and the roll stiffness parameter
measured with no anti-sway bar present **Suspension roll stiffness without anti-roll
bar, RollStiffNoArb**.

If you do not enable an anti-sway bar, the stiffness is 0.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AntiSwayEnByAxl` |
| **Values:** | `[0 0]` (default) | `vector` |
| **Data Types:** | `double` |

### Suspension Parameters

### **Suspension type** — Type of suspension `Independent front and rear` (default) | `Independent front and twist beam rear`

Select type of suspension.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SuspType` |
| **Values:** | `Independent front and rear` (default) | `Independent front and twist beam rear` |
| **Data Types:** | `character vector` |

### **Drivetrain type** — Type of drivetrain `FWD` (default) | `RWD` | `AWD`

Select type of drivetrain.

- `AWD` – All-wheel drive
- `FWD` – Front-wheel drive
- `RWD` – Rear-wheel drive

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DrivetrainType` |
| **Values:** | `FWD` (default) | `RWD` | `AWD` |
| **Data Types:** | `character vector` |

#### Directions

### **+ Steer angle** — Positive steer angle `Right` (default) | `Left`

Direction of positive steer angle during kinematics and compliance test.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrPlusDirection` |
| **Values:** | `Right` (default) | `Left` |
| **Data Types:** | `character vector` |

### **+ Fx used in compliance tests** — Positive longitudinal force `Front` (default) | `Rear`

Direction of positive longitudinal force during kinematics and compliance
test.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `XPlusDirection` |
| **Values:** | `Front` (default) | `Rear` |
| **Data Types:** | `character vector` |

### **+ Fy used in compliance tests** — Positive lateral force `Right` (default) | `Left`

Direction of positive lateral force during kinematics and compliance test.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `YPlusDirection` |
| **Values:** | `Right` (default) | `Left` |
| **Data Types:** | `character vector` |

### **+ Suspension Jounce** — Positive suspension jounce `Up` (default) | `Down`

Direction of positive suspension jounce during kinematics and compliance
test.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ZPlusDirection` |
| **Values:** | `Up` (default) | `Down` |
| **Data Types:** | `character vector` |

### **+ WhlMz used in compliance tests** — Positive yaw moment `Counter-clockwise` (default) | `Clockwise`

Direction of positive yaw moment during kinematics and compliance test.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WhlMzDirection` |
| **Values:** | `Counter-clockwise` (default) | `Clockwise` |
| **Data Types:** | `character vector` |

#### Shock force

### **Shock type** — Type of shock force `Table-based` (default) | `Table-based individual` | `Constant`

Type of shock force.

If a table-based individual setting is chosen, table-based shock force is
implemented together with constant motion ratios. If a table-based setting is chosen
both shock force and motion ratios are calculated from lookup tables.

| Setting | Implementation |
| --- | --- |
| `Table-based` | Table-based shock force and motion ratios. |
| `Table-based individual` | Table-based shock force and constant motion ratios. |
| `Constant` | Constant shock force and motion ratios. |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShockType` |
| **Values:** | `Table-based` (default) | `Table-based individual` | `Constant` |
| **Data Types:** | `character vector` |

### **Shock force vs shock compression rate, ShckFrcVsCompRate** — Table `struct('FL',[-100. -5000;0 0;100. 5000],'FR',[-100. -5000;0 0;100. 5000],'RL',[-100. -5000;0 0;100. 5000],'RR',[-100. -5000;0 0;100. 5000])` (default)

Shock force versus shock compression rate, specified as a structure, in N/mm per
sec.

#### Dependencies

To create this parameter, set **Shock type** to
`Table-based` or `Table-based
individual`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShckFrcVsCompRate` |
| **Values:** | `struct('FL',[-100. -5000;0 0;100. 5000],'FR',[-100. -5000;0 0;100. 5000],'RL',[-100. -5000;0 0;100. 5000],'RR',[-100. -5000;0 0;100. 5000])` (default) |
| **Data Types:** | `struct` |

### **Motion ratios by axle, MotRatios** — Table `struct('FL',[-0.1 -0.1;0 0;0.1 0.1],'FR',[-0.1 -0.1;0 0;0.1 0.1],'RL',[-0.1 -0.1;0 0;0.1 0.1],'RR',[-0.1 -0.1;0 0;0.1 0.1])` (default)

Motion ratios by axle, specified as a structure.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MotRatios` |
| **Values:** | `struct('FL',[-0.1 -0.1;0 0;0.1 0.1],'FR',[-0.1 -0.1;0 0;0.1 0.1],'RL',[-0.1 -0.1;0 0;0.1 0.1],'RR',[-0.1 -0.1;0 0;0.1 0.1])` (default) |
| **Data Types:** | `struct` |

#### Bounce test

### **Bump steer, BumpSteer** — Table `struct('FL',[-0.1 1.1459;0 0;0.1 -1.1459],'FR',[-0.1 1.1459;0 0;0.1 -1.1459],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default)

Bump steer, specified as a structure, in deg/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BumpSteer` |
| **Values:** | `struct('FL',[-0.1 1.1459;0 0;0.1 -1.1459],'FR',[-0.1 1.1459;0 0;0.1 -1.1459],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default) |
| **Data Types:** | `struct` |

### **Bump camber, BumpCamber** — Table `struct('FL',[-0.1 1.7189;0 0;0.1 -1.7189],'FR',[-0.1 1.7189;0 0;0.1 -1.7189],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default)

Bump camber, specified as a structure, in deg/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BumpCamber` |
| **Values:** | `struct('FL',[-0.1 1.1459;0 0;0.1 -1.1459],'FR',[-0.1 1.1459;0 0;0.1 -1.1459],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default) |
| **Data Types:** | `struct` |

### **Bump caster, BumpCaster** — Table `struct('FL',[-0.1 1.1459;0 0;0.1 -1.1459],'FR',[-0.1 1.1459;0 0;0.1 -1.1459],'RL',[-0.1 -11.4592;0 0;0.1 11.4592],'RR',[-0.1 -11.4592;0 0;0.1 11.4592])` (default)

Bump caster, specified as a structure, in deg/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BumpCaster` |
| **Values:** | `struct('FL',[-0.1 1.1459;0 0;0.1 -1.1459],'FR',[-0.1 1.1459;0 0;0.1 -1.1459],'RL',[-0.1 -11.4592;0 0;0.1 11.4592],'RR',[-0.1 -11.4592;0 0;0.1 11.4592])` (default) |
| **Data Types:** | `struct` |

### **Lateral wheel center displacement, LatWhlCtrDisp** — Table `struct('FL',[-0.1 0.02;0 0;0.1 -0.02],'FR',[-0.1 0.02;0 0;0.1 -0.02],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default)

Lateral wheel center displacement, specified as a structure, in mm/mm.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LatWhlCtrDisp` |
| **Values:** | `struct('FL',[-0.1 0.02;0 0;0.1 -0.02],'FR',[-0.1 0.02;0 0;0.1 -0.02],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.;0 0;0.1 0.])` (default) |
| **Data Types:** | `struct` |

### **Longitudinal wheel center displacement, LngWhlCtrDisp** — Table `struct('FL',[-0.1 -0.002;0 0;0.1 0.002],'FR',[-0.1 -0.002;0 0;0.1 0.002],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.02;0 0;0.1 0.01])` (default)

Longitudinal wheel center displacement, specified as a structure, in mm/mm.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LngWhlCtrDisp` |
| **Values:** | `struct('FL',[-0.1 -0.002;0 0;0.1 0.002],'FR',[-0.1 -0.002;0 0;0.1 0.002],'RL',[-0.1 0.;0 0;0.1 0.],'RR',[-0.1 0.02;0 0;0.1 0.01])` (default) |
| **Data Types:** | `struct` |

### **Normal wheel rates, NrmlWhlRates** — Table `struct('FL',[-100. -5000;0 0;100. 5000],'FR',[-100. -5000;0 0;100. 5000],'RL',[-100. -5000;0 0;100. 5000],'RR',[-100. -5000;0 0;100. 5000])` (default) | vector

Normal wheel rates, specified as a structure, in N/mm.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NrmlWhlRates` |
| **Values:** | `struct('FL',[-100. -5000;0 0;100. 5000],'FR',[-100. -5000;0 0;100. 5000],'RL',[-100. -5000;0 0;100. 5000],'RR',[-100. -5000;0 0;100. 5000])` (default) | vector |
| **Data Types:** | `struct` |

### **Normal wheel force offsets, NrmlWhlFrcOff** — Force offset `[0 0 0 0]` (default)

Normal wheel force offsets, specified as a vector, in N.

#### Dependencies

To create this parameter, specify a **Normal wheel rates,
NrmlWhlRates** vector.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NrmlWhlFrcOff` |
| **Values:** | `[0 0 0 0]` (default) |
| **Data Types:** | `double` |

#### Roll test

### **Suspension roll stiffness with anti-roll bar, RollStiffArb** — Anti-sway bar enabled `[800 700]` (default) | `1`-by-`2` vector

Suspension roll stiffness with anti-roll bar, specified as a
`1`-by-`2` vector, in Nm/deg. The first
element is the front axle roll stiffness. The second element is the rear axle roll
stiffness.

If you enable an anti-sway bar on the axle, the anti-sway bar
stiffness is the difference between the anti-sway bar torque parameter, **Suspension
roll stiffness with anti-roll bar, RollStiffArb**, and the roll stiffness parameter
measured with no anti-sway bar present **Suspension roll stiffness without anti-roll
bar, RollStiffNoArb**.

If you do not enable an anti-sway bar, the stiffness is 0.

#### Dependencies

To enable this parameter, set **Suspension type** to
`Independent front and rear`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RollStiffArb` |
| **Values:** | `[800 700]` (default) | `1`-by-`2` vector |
| **Data Types:** | `double` |

**Data Types:** `double`

### **Suspension roll stiffness without anti-roll bar, RollStiffNoArb** — Anti-sway bar not enabled `[0 0]` (default) | `1`-by-`2` vector

Suspension roll stiffness without anti-roll bar, specified as a
`1`-by-`2` vector, in Nm/deg. The first
element is the front axle roll stiffness. The second element is the rear axle roll
stiffness.

If you enable an anti-sway bar on the axle, the anti-sway bar
stiffness is the difference between the anti-sway bar torque parameter, **Suspension
roll stiffness with anti-roll bar, RollStiffArb**, and the roll stiffness parameter
measured with no anti-sway bar present **Suspension roll stiffness without anti-roll
bar, RollStiffNoArb**.

If you do not enable an anti-sway bar, the stiffness is 0.

#### Dependencies

To enable this parameter, set **Suspension type** to
`Independent front and rear`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RollStiffNoArb` |
| **Values:** | `[0 0]` (default) | `1`-by-`2` vector |
| **Data Types:** | `double` |

**Data Types:** `double`

#### Steer test

### **Camber vs steer angle, CambVsSteerAng** — Table `struct('FL',[-10. -1.;0 0;10. 1.],'FR',[-10. 1.;0 0;10. -1.],'RL',[-10. -1.;0 0;10. 1.],'RR',[-10. 1.;0 0;10. -1.])` (default)

Camber vs steer angle, specified as a structure, in deg/deg.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CambVsSteerAng` |
| **Values:** | `struct('FL',[-10. -1.;0 0;10. 1.],'FR',[-10. 1.;0 0;10. -1.],'RL',[-10. -1.;0 0;10. 1.],'RR',[-10. 1.;0 0;10. -1.])` (default) |
| **Data Types:** | `struct` |

### **Caster vs steer angle, CastVsSteerAng** — Table `struct('FL',[-10. -1.;0 0;10. 1.],'FR',[-10. 1.;0 0;10. -1.],'RL',[-10. -1.;0 0;10. 1.],'RR',[-10. 1.;0 0;10. -1.])` (default)

Caster vs steer angle, specified as a structure, in deg/deg.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CastVsSteerAng` |
| **Values:** | `struct('FL',[-10. -1.;0 0;10. 1.],'FR',[-10. 1.;0 0;10. -1.],'RL',[-10. -1.;0 0;10. 1.],'RR',[-10. 1.;0 0;10. -1.])` (default) |
| **Data Types:** | `struct` |

#### Longitudinal compliance test

### **Longitudinal steer compliance, LngSteerCompl** — Table `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default)

Longitudinal steer compliance, specified as a structure, in deg/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LngSteerCompl` |
| **Values:** | `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default) |
| **Data Types:** | `struct` |

### **Longitudinal camber compliance, LngCambCompl** — Table `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default)

Longitudinal camber compliance, specified as a structure, in deg/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LngCambCompl` |
| **Values:** | `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default) |
| **Data Types:** | `struct` |

### **Longitudinal caster compliance, LngCastCompl** — Table `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default)

Longitudinal caster compliance, specified as a structure, in deg/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LngCastCompl` |
| **Values:** | `struct('NegFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]),'PosFx',struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.]))` (default) |
| **Data Types:** | `struct` |

### **Longitudinal wheel center compliance, LngWhlCtrCompl** — Table `struct('NegFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]),'PosFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]))` (default)

Longitudinal wheel center compliance, specified as a structure, in mm/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LngWhlCtrCompl` |
| **Values:** | `struct('NegFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]),'PosFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]))` (default) |
| **Data Types:** | `struct` |

### **Lateral wheel center compliance, LatWhlCtrComplLng** — Table `struct('NegFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]),'PosFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]))` (default)

Lateral wheel center compliance, specified as a structure, in mm/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LatWhlCtrComplLng` |
| **Values:** | `struct('NegFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]),'PosFx',struct('FL',[-2. -10.;0 0;2. 10.],'FR',[-2. 10.;0 0;2. -10.],'RL',[-2. -10.;0 0;2. 10.],'RR',[-2. 10.;0 0;2. -10.]))` (default) |
| **Data Types:** | `struct` |

#### Lateral compliance-opposed test

### **Lateral steer compliance, LatSteerCompl** — Table `struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.])` (default)

Lateral steer compliance, specified as a structure, in deg/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LatSteerCompl` |
| **Values:** | `struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.])` (default) |
| **Data Types:** | `struct` |

### **Lateral camber compliance, LatCambCompl** — Table `struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.])` (default)

Lateral camber compliance, specified as a structure, in deg/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LatCambCompl` |
| **Values:** | `struct('FL',[-2. -1.;0 0;2. 1.],'FR',[-2. 1.;0 0;2. -1.],'RL',[-2. -1.;0 0;2. 1.],'RR',[-2. 1.;0 0;2. -1.])` (default) |
| **Data Types:** | `struct` |

### **Lateral wheel center compliance from lateral sources, LatWhlCtrComplLat** — Table `struct('FL',[-2. -5.;0 0;2. 5.],'FR',[-2. 5.;0 0;2. -5.],'RL',[-2. -5.;0 0;2. 5.],'RR',[-2. 5.;0 0;2. -5.])` (default)

Lateral wheel center compliance from lateral sources, specified as a structure, in
mm/kN.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LatWhlCtrComplLat` |
| **Values:** | `struct('FL',[-2. -5.;0 0;2. 5.],'FR',[-2. 5.;0 0;2. -5.],'RL',[-2. -5.;0 0;2. 5.],'RR',[-2. 5.;0 0;2. -5.])` (default) |
| **Data Types:** | `struct` |

#### Aligning torque compliance-opposed test

### **Aligning torque steer compliance, AlgnTrqSteerCompl** — Table `struct('FL',[-0.2 -1.;0 0;0.2 1.],'FR',[-0.2 1.;0 0;0.2 -1.],'RL',[-0.2 -1.;0 0;0.2 1.],'RR',[-0.2 1.;0 0;0.2 -1.])` (default)

Aligning torque steer compliance, specified as a structure, in deg/kNm.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AlgnTrqSteerCompl` |
| **Values:** | `struct('FL',[-0.2 -1.;0 0;0.2 1.],'FR',[-0.2 1.;0 0;0.2 -1.],'RL',[-0.2 -1.;0 0;0.2 1.],'RR',[-0.2 1.;0 0;0.2 -1.])` (default) |
| **Data Types:** | `struct` |

### **Aligning torque camber compliance, AlgnTrqCambCompl** — Table `struct('FL',[-0.2 -1.;0 0;0.2 1.],'FR',[-0.2 1.;0 0;0.2 -1.],'RL',[-0.2 -1.;0 0;0.2 1.],'RR',[-0.2 1.;0 0;0.2 -1.])` (default)

Aligning torque camber compliance, specified as a structure, in deg/kNm.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AlgnTrqCambCompl` |
| **Values:** | `struct('FL',[-0.2 -1.;0 0;0.2 1.],'FR',[-0.2 1.;0 0;0.2 -1.],'RL',[-0.2 -1.;0 0;0.2 1.],'RR',[-0.2 1.;0 0;0.2 -1.])` (default) |
| **Data Types:** | `struct` |

#### Static alignment settings

### **Toe, StatToe** — Wheel toe angle `[0 0 0 0]` (default) | `1`-by-`4` vector

Static toe angle for each wheel, specified as a
`1`-by-`4` vector, in deg.

| Wheel | Array Element | Axle | Wheel Location |
| --- | --- | --- | --- |
| Front left | `(1,1)` | `1` | `1` |
| Front right | `(1,2)` | `1` | `2` |
| Rear left | `(1,3)` | `2` | `1` |
| Rear left | `(1,4)` | `2` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StatToe` |
| **Values:** | `[0 0 0 0]` (default) | `1`-by-`4` vector |
| **Data Types:** | `double` |

### **Camber, StatCamber** — Wheel camber angle `[0 0 0 0]` (default) | `1`-by-`4` vector

Static camber angle for each wheel, specified as a
`1`-by-`4` vector, in deg.

| Wheel | Array Element | Axle |
| --- | --- | --- |
| Front left | `(1,1)` | `1` |
| Front right | `(1,2)` | `1` |
| Rear left | `(1,3)` | `2` |
| Rear left | `(1,4)` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StatCamber` |
| **Values:** | `[0 0 0 0]` (default) | `1`-by-`4` vector |
| **Data Types:** | `double` |

### **Caster, StatCaster** — Wheel caster angle `[0 0 0 0]` (default) | `1`-by-`4` vector

Static caster angle for each wheel, specified as a
`1`-by-`4` vector, in deg.

| Wheel | Array Element | Axle |
| --- | --- | --- |
| Front left | `(1,1)` | `1` |
| Front right | `(1,2)` | `1` |
| Rear left | `(1,3)` | `2` |
| Rear left | `(1,4)` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StatCaster` |
| **Values:** | `[0 0 0 0]` (default) | `1`-by-`4` vector |
| **Data Types:** | `double` |

#### Wheels

### **Static loaded radius of wheels, StatLdWhlR** — Wheel radius `[0.3 0.3 0.3 0.3]` (default) | `1`-by-`4` vector

Static loaded radius of wheels, specified as a
`1`-by-`4` vector, in m.

| Wheel | Array Element | Axle |
| --- | --- | --- |
| Front left | `(1,1)` | `1` |
| Front right | `(1,2)` | `1` |
| Rear left | `(1,3)` | `2` |
| Rear left | `(1,4)` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StatLdWhlR` |
| **Values:** | `[0.3 0.3 0.3 0.3]` (default) | `1`-by-`4` vector |
| **Data Types:** | `double` |

## Libraries

Vehicle Dynamics Blockset / Suspension

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2022b: Parameter name change from `NumTracksByAxl` to `NumWhlsByAxl`

The **Number of tracks by axle, NumTracksByAxl** parameter is renamed
to **Number of wheels by axle, NumWhlsByAxl**.

The block uses the number of wheels per axle to index the
input and output block signals.

### R2022b: New **Suspension type** and **Drivetrain type** Parameters

Starting from R2022b, the Independent Suspension - K and C block includes **Suspension
type** and **Drivetrain type** parameters that allow
you specify a suspension and drivetrain. Previously, the block was configured for
front wheel drive with independent front and rear suspensions.

## Description

Independent kinematics and compliance test suspension

In the Vehicle Dynamics Blockset™ library, there are two types of suspension blocks that implement the
kinematics and compliance (K and C) test suspension characteristics measured from
simulated or actual laboratory suspension tests.

| Block | **Suspension type** Setting | Implementation |
| --- | --- | --- |
| Twist-Beam Suspension - K and C  Twist-Beam Suspension - K and C | `Independent front and twist-beam rear` | Kinematics and compliance effects of:  - Independent suspension on a front axle with two   wheels - Twist-beam suspension on a rear axle with two   wheels    For more information, see Twist-Beam Suspension - K and C. |
| Independent Suspension - K and C  Independent Suspension - K and C | `Independent front and rear` | Kinematics and compliance effects of four independent suspensions on a vehicle with two axles and two wheels per axle. |

### K and C Effects on Suspension

To determine the overall suspension forces and geometric effects on the vehicle and
wheels, the block adds the individual effects from kinematic (bounce, roll, steering) and
compliance (longitudinal and lateral forces, aligning moments) inputs. Specifically, the
block multiplies the suspension geometry states by either gradient or table values to
determine the K and C effects on wheel orientation and suspension forces.

Wheel orientation:

- Camber, caster, and steer angles
- Lateral wheel center displacement
- Longitudinal wheel center displacement

Vertical suspension forces:

- Anti-sway bar
- Shock force
- Wheel rate
- Contact patch swing arm (CPSA) force
- Longitudinal side view swing arm (SVSA) anti-effects

**Camber, Caster, and Steer Angles**

The block uses these parameters to account for the K and C effects on the camber,
caster, and steer angles.

- **Bounce test**– Independent suspension
- **Roll test**– Independent suspension
- **Steer test**
- **Longitudinal compliance test**
- **Lateral compliance-opposed test**
- **Aligning torque compliance-opposed test**

Use the **Static alignment settings** parameters to set the initial
state of the suspension.

**Lateral Wheel Center Displacement**

The block uses these parameters to account for the K and C effects the lateral wheel
center displacement.

- **Bounce test**
- **Longitudinal compliance test**
- **Lateral compliance-opposed test**

**Longitudinal Wheel Center Displacement**

The block uses these parameters to account for the K and C effects on the longitudinal
wheel center displacement.

- **Bounce test**
- **Longitudinal compliance test**

**Shock Force**

The block uses the **Shock force** parameters to calculate the shock
force effect on the vertical suspension force. You can specify table-based or constant
parameter values.

**Wheel Rate**

The block uses the **Bounce test** parameters to calculate the wheel
rate effect on the vertical suspension force.

**Contact Patch Swing Arm**

The block uses these equations to calculate the effect of the contact patch swing arm
(CPSA) forces on vertical suspension force.

tan(θCPSA)=f(Zw)FzCPSA=Fytan(θCPSA)

The block also uses the **Static loaded radius of
wheels** parameter in the CPSA force calculation.

The equations use these variables.

|  |  |
| --- | --- |
| *ϴCPSA* | Contact patch swing arm angle |
| *Fy* | Lateral suspension force |
| *FzCPSA* | CPSA effect on vertical suspension force |
| *zw* | Wheel displacement |

**Longitudinal Side View Swing Arm Anti-Effects**

The block uses these equations to calculate the effect of the side view swing arm
(SVSA) forces on vertical suspension force during acceleration and braking.

tan(θSVSA)=f(Zw)FzSVSA=Fxtan(θSVSA)

Use the **Drivetrain type** parameter to ensure that
the block applies the acceleration anti-effects to the correct wheels.

The equations use these variables.

|  |  |
| --- | --- |
| *ϴSVSA* | Contact patch swing arm angle |
| *Fx* | Longitudinal wheel force |
| *FzSVSA* | SVSA effect on vertical suspension force |
| *zw* | Wheel displacement |

### Anti-Sway Bar

Optionally, use the **Anti-sway axle enable by axle,
AntiSwayEnByAxl** parameter to implement anti-sway bar reaction forces
by axle.

If you enable an anti-sway bar on the axle, the
anti-sway bar stiffness is the difference between the anti-sway bar torque
parameter, **Suspension roll stiffness with anti-roll bar,
RollStiffArb**, and the roll stiffness parameter measured with no
anti-sway bar present **Suspension roll stiffness without anti-roll bar,
RollStiffNoArb**.

If you do not enable an anti-sway bar, the roll stiffness is 0.
