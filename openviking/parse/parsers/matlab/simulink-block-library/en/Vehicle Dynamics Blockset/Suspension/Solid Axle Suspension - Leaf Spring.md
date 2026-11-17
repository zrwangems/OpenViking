---
type: simulink-block
title: 'Solid Axle Suspension - Leaf Spring'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Suspension'
documentation_page: 'solidaxlesuspensionleafspring'
documentation_source_path: 'ref/solidaxlesuspensionleafspring.html'
language: en
---

# Solid Axle Suspension - Leaf Spring

## Ports
```yaml
ports:
- name: WhlPz
  summary: Wheel z-axis displacement array
  direction: input
- name: WhlRe
  summary: Wheel effective radius array
  direction: input
- name: WhlVz
  summary: Wheel z-axis velocity array
  direction: input
- name: WhlFx
  summary: Longitudinal wheel force on vehicle array
  direction: input
- name: WhlFy
  summary: Lateral wheel force on vehicle array
  direction: input
- name: WhlM
  summary: Suspension moment on wheel array
  direction: input
- name: VehP
  summary: Vehicle displacement array
  direction: input
- name: VehV
  summary: Vehicle velocity array
  direction: input
- name: StrgAng
  summary: Steering angle, optional array
  direction: input
- name: Info
  summary: Bus signal bus
  direction: output
- name: VehF
  summary: Suspension force on vehicle array
  direction: output
- name: VehM
  summary: Suspension moment on vehicle array
  direction: output
- name: WhlF
  summary: Suspension force on wheel array
  direction: output
- name: WhlV
  summary: Wheel velocity array
  direction: output
- name: WhlAng
  summary: Wheel camber, caster, toe angles array
  direction: output
```

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
### Output

### **Info** — Bus signal bus

Bus signal containing block values. The signals are arrays that depend on the wheel
location.

For example, these are the indices for a two-axle, two-wheel vehicle. The total number
of wheels is four.

- 1D array signal (1-by-4)

  | Array Element | Axle | Wheel Number |
  | --- | --- | --- |
  | `(1,1)` | `1` | `1` |
  | `(1,2)` | `1` | `2` |
  | `(1,3)` | `2` | `1` |
  | `(1,4)` | `2` | `2` |
- 3D array signal (3-by-4)

  | Array Element | Axle | Wheel Number |
  | --- | --- | --- |
  | `(1,1)` | `1` | `1` |
  | `(1,2)` | `1` | `2` |
  | `(1,3)` | `2` | `1` |
  | `(1,4)` | `2` | `2` |
  | `(2,1)` | `1` | `1` |
  | `(2,2)` | `1` | `2` |
  | `(2,3)` | `2` | `1` |
  | `(2,4)` | `2` | `2` |
  | `(3,1)` | `1` | `1` |
  | `(3,2)` | `1` | `2` |
  | `(3,3)` | `2` | `1` |
  | `(3,4)` | `2` | `2` |

| Signal | Description | Array Signal | Variable | Units |
| --- | --- | --- | --- | --- |
| `Camber` | Wheel angles according to the axle. | 1D | WhlAng[1,...]=ξ=[ξa,t] | rad |
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
```yaml
parameters:
- name: Number of axles, NumAxl
  summary: Number of axles 2 (default) | scalar
  group: Axles
  block_parameter: NumAxl
  values: 2 (default) | scalar
- name: Number of wheels by axle, NumWhlsByAxl
  summary: Number of wheels per axle [2 2] (default) | vector
  group: Axles
  block_parameter: NumWhlsByAxl
  values: '[2 2] (default) | vector'
- name: Steered axle enable by axle, StrgEnByAxl
  summary: Boolean vector to enable axle steering [1 0] (default) | vector
  group: Axles
  block_parameter: StrgEnByAxl
  values: '[1 0] (default) | vector'
- name: Axle and wheels lumped principal moments of inertia about longitudinal axis, AxlIxx
  summary: Inertia 200 (default) | vector
  group: Axles
  block_parameter: AxlIxx
  values: 200 (default) | vector
- name: Axle and wheels lumped mass, AxlM
  summary: Mass 300 (default) | vector
  group: Axles
  block_parameter: AxlM
  values: 300 (default) | vector
- name: Track hardpoint coordinates relative to axle center, TrackCoords
  summary: Point [0 0 0 0;-1 1 -1 1;0 0 0 0] (default) | array
  group: Axles
  block_parameter: TrackCoords
  values: '[0 0 0 0;-1 1 -1 1;0 0 0 0] (default) | array'
- name: Suspension hardpoint coordinates relative to axle center, SuspCoords
  summary: Point [0 0 0 0;-1 1 -1 1;0 0 0 0] (default) | array
  group: Axles
  block_parameter: SuspCoords
  values: '[0 0 0 0;-1 1 -1 1;0 0 0 0] (default) | array'
- name: Wheel and axle interface compliance constant, KzWhlAxl
  summary: Spring rate 6437000 (default) | scalar
  group: Axles
  block_parameter: KzWhlAxl
  values: 6437000 (default) | scalar
- name: Wheel and axle interface compliance preload, F0zWhlAxl
  summary: Spring rate 9810 (default) | scalar
  group: Axles
  block_parameter: F0zWhlAxl
  values: 9810 (default) | scalar
- name: Wheel and axle interface damping constant, CzWhlAxl
  summary: Damping 10000 (default) | scalar
  group: Axles
  block_parameter: CzWhlAxl
  values: 10000 (default) | scalar
- name: Suspension spring constant, Kz
  summary: Suspension spring constant 64370 (default) | scalar | vector
  group: Suspension
  block_parameter: Kz
  values: 64370 (default) | scalar | vector
- name: Suspension spring preload, F0z
  summary: Suspension spring preload 9810 (default) | scalar | vector
  group: Suspension
  block_parameter: F0z
  values: 9810 (default) | scalar | vector
- name: Suspension shock damping constant, Cz
  summary: Suspension shock damping constant 10000 (default) | scalar | vector
  group: Suspension
  block_parameter: Cz
  values: 10000 (default) | scalar | vector
- name: Suspension maximum height, Hmax
  summary: Height 0.5 (default) | scalar | vector
  group: Suspension
  block_parameter: Hmax
  values: 0.5 (default) | scalar | vector
- name: Toe angle at steering center, Toe
  summary: Toe angle 0.0349 (default) | scalar
  group: Suspension
  block_parameter: Toe
  values: 0.0349 (default) | scalar
- name: Roll steer vs suspension height slope, RollStrgSlp
  summary: Steer angle suspension slope -0.2269 (default) | scalar | vector
  group: Suspension
  block_parameter: RollStrgSlp
  values: -0.2269 (default) | scalar | vector
- name: Toe angle vs steering angle slope, ToeStrgSlp
  summary: Toe angle steering slope 0.01 (default) | scalar | vector
  group: Suspension
  block_parameter: ToeStrgSlp
  values: 0.01 (default) | scalar | vector
- name: Caster angle at steering center, Caster
  summary: Caster angle at steering center 0.0698 (default) | scalar
  group: Suspension
  block_parameter: Caster
  values: 0.0698 (default) | scalar
- name: Caster angle vs suspension height slope, CasterHslp
  summary: Caster angle versus suspension height slope -0.2269 (default) | scalar | vector
  group: Suspension
  block_parameter: CasterHslp
  values: -0.2269 (default) | scalar | vector
- name: Caster angle vs steering angle slope, CasterStrgSlp
  summary: Caster angle versus steering angle slope 0.01 (default) | scalar | vector
  group: Suspension
  block_parameter: CasterStrgSlp
  values: 0.01 (default) | scalar | vector
- name: Camber angle at steering center, Camber
  summary: Camber angle at steering center 0.0698 (default) | scalar
  group: Suspension
  block_parameter: Camber
  values: 0.0698 (default) | scalar
- name: Camber angle vs suspension height slope, CamberHslp
  summary: Camber angle versus suspension height slope -0.2269 (default) | scalar | vector
  group: Suspension
  block_parameter: CamberHslp
  values: -0.2269 (default) | scalar | vector
- name: Camber angle vs steering angle slope, CamberStrgSlp
  summary: Camber angle versus steering angle slope 0.01 (default) | scalar | vector
  group: Suspension
  block_parameter: CamberStrgSlp
  values: 0.01 (default) | scalar | vector
- name: Suspension height vs steering angle slope, StrgHgtSlp
  summary: Suspension height versus steering angle slope 0.1432 (default) | scalar | vector
  group: Suspension
  block_parameter: StrgHgtSlp
  values: 0.1432 (default) | scalar | vector
```

### Axles

### **Number of axles, NumAxl** — Number of axles `2` (default) | `scalar`

Number of axles, *Na*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumAxl` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Number of wheels by axle, NumWhlsByAxl** — Number of wheels per axle `[2 2]` (default) | `vector`

Number of wheels per axle, *Nta*,
dimensionless. Vector is `1` by the number of vehicle axles,
*Na*. For example,
`[1,2]` represents one wheel on axle one and two wheels on axle
two.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NumWhlsByAxl` |
| **Values:** | `[2 2]` (default) | `vector` |
| **Data Types:** | `double` |

### **Steered axle enable by axle, StrgEnByAxl** — Boolean vector to enable axle steering `[1 0]` (default) | `vector`

Boolean vector that enables axle steering,
*Ensteer*, dimensionless. Vector is
`1` by the number of vehicle axles,
*Na*. For example:

- `[1 0]`—For a two-axle vehicle, enables axle one
  steering and disables axle two steering
- `[1 1]`—For a two-axle vehicle, enables axle one and
  axle two steering

#### Dependencies

Setting an element of the **Steered axle enable by axle,
StrgEnByAxl** vector to 1:

- Creates input port `StrgAng`.
- Creates these parameters

  - **Toe angle vs steering angle slope,
    ToeStrgSlp**
  - **Caster angle vs steering angle slope,
    CasterStrgSlp**
  - **Camber angle vs steering angle slope,
    CamberStrgSlp**
  - **Suspension height vs steering angle slope,
    StrgHgtSlp**

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

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgEnByAxl` |
| **Values:** | `[1 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Axle and wheels lumped principal moments of inertia about longitudinal axis, AxlIxx** — Inertia `200` (default) | `vector`

Axle and wheels lumped principal moments of inertia about longitudinal axis,
*AxlIxx*, in kg\*m^2.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AxlIxx` |
| **Values:** | `200` (default) | `vector` |
| **Data Types:** | `double` |

### **Axle and wheels lumped mass, AxlM** — Mass `300` (default) | `vector`

Axle and wheels lumped mass, *AxlM*, in kg.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AxlM` |
| **Values:** | `300` (default) | `vector` |
| **Data Types:** | `double` |

### **Track hardpoint coordinates relative to axle center, TrackCoords** — Point `[0 0 0 0;-1 1 -1 1;0 0 0 0]` (default) | `array`

Track hardpoint coordinates, *Tct*, along
the solid axle *x*, *y*, and
*z*-axes, in m.

For example, for a two-axle vehicle with two wheels per axle, the
`TrackCoords` array:

- Dimensions are `[3x4]`.
- Contains four track hardpoint coordinates according to their axle and
  wheel locations.

  Tct=[xw1,1xw1,2xw2,1xw2,2yw1,1yw1,2yw2,1yw2,2zw1,1zw1,2zw2,1zw2,2]

  | Array Element | Axle | Wheel Number | Axis |
  | --- | --- | --- | --- |
  | `TrackCoords(1,1)` | `1` | `1` | Solid axle *x*-axis |
  | `TrackCoords(1,2)` | `1` | `2` |
  | `TrackCoords(1,3)` | `2` | `1` |
  | `TrackCoords(1,4)` | `2` | `2` |
  | `TrackCoords(2,1)` | `1` | `1` | Solid axle *y*-axis |
  | `TrackCoords(2,2)` | `1` | `2` |
  | `TrackCoords(2,3)` | `2` | `1` |
  | `TrackCoords(2,4)` | `2` | `2` |
  | `TrackCoords(3,1)` | `1` | `1` | Solid axle *z*-axis |
  | `TrackCoords(3,2)` | `1` | `2` |
  | `TrackCoords(3,3)` | `2` | `1` |
  | `TrackCoords(3,4)` | `2` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrackCoords` |
| **Values:** | `[0 0 0 0;-1 1 -1 1;0 0 0 0]` (default) | `array` |
| **Data Types:** | `double` |

### **Suspension hardpoint coordinates relative to axle center, SuspCoords** — Point `[0 0 0 0;-1 1 -1 1;0 0 0 0]` (default) | `array`

Suspension hardpoint coordinates, *Sct*,
along the solid axle *x*-, *y*-, and
*z*-axes, in m.

For example, for a two-axle vehicle with two wheels per axle, the
`SuspCoords` array:

- Dimensions are `[3x4]`.
- Contains four track hardpoint coordinates according to their axle and
  track locations.

  Sct=[xs1,1xs1,2xs2,1xs2,2ys1,1ys1,2ys2,1ys2,2zs1,1zs1,2zs2,1zs2,2]

  | Array Element | Axle | Track | Axis |
  | --- | --- | --- | --- |
  | `SuspCoords(1,1)` | `1` | `1` | Solid axle *x*-axis |
  | `SuspCoords(1,2)` | `1` | `2` |
  | `SuspCoords(1,3)` | `2` | `1` |
  | `SuspCoords(1,4)` | `2` | `2` |
  | `SuspCoords(2,1)` | `1` | `1` | Solid axle *y*-axis |
  | `SuspCoords(2,2)` | `1` | `2` |
  | `SuspCoords(2,3)` | `2` | `1` |
  | `SuspCoords(2,4)` | `2` | `2` |
  | `SuspCoords(3,1)` | `1` | `1` | Solid axle *z*-axis |
  | `SuspCoords(3,2)` | `1` | `2` |
  | `SuspCoords(3,3)` | `2` | `1` |
  | `SuspCoords(3,4)` | `2` | `2` |

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SuspCoords` |
| **Values:** | `[0 0 0 0;-1 1 -1 1;0 0 0 0]` (default) | `array` |
| **Data Types:** | `double` |

### **Wheel and axle interface compliance constant, KzWhlAxl** — Spring rate `6437000` (default) | `scalar`

Wheel and axle interface compliance constant,
*kwaz*, in N/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KzWhlAxl` |
| **Values:** | `6437000` (default) | `scalar` |
| **Data Types:** | `double` |

### **Wheel and axle interface compliance preload, F0zWhlAxl** — Spring rate `9810` (default) | `scalar`

Wheel and axle interface compliance preload,
*Fwaz0*, in N.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `F0zWhlAxl` |
| **Values:** | `9810` (default) | `scalar` |
| **Data Types:** | `double` |

### **Wheel and axle interface damping constant, CzWhlAxl** — Damping `10000` (default) | `scalar`

Wheel and axle interface damping constant,
*cwaz*, in m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CzWhlAxl` |
| **Values:** | `10000` (default) | `scalar` |
| **Data Types:** | `double` |

### Suspension

#### Compliance and Damping - Passive

### **Suspension spring constant, Kz** — Suspension spring constant `64370` (default) | `scalar` | `vector`

Linear vertical spring constant for independent suspension wheels on axle a,
*kza*, in
N/m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kz` |
| **Values:** | `64370` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Suspension spring preload, F0z** — Suspension spring preload `9810` (default) | `scalar` | `vector`

Vertical preload spring force applied to the wheels on the axle at wheel carrier
reference coordinates,
*Fz0a*, in N.
Positive preload forces:

- Cause the vehicle to lift.
- Point along the negative inertial-fixed
  *z*-axis.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `F0z` |
| **Values:** | `9810` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Suspension shock damping constant, Cz** — Suspension shock damping constant `10000` (default) | `scalar` | `vector`

Linear vertical damping constant for independent suspension wheels on axle a,
*cza*, in
Ns/m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Dependencies

To create this parameter, clear **Enable active
damping**.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cz` |
| **Values:** | `10000` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Suspension maximum height, Hmax** — Height `0.5` (default) | `scalar` | `vector`

Maximum suspension extension or minimum suspension compression height,
*Hmax*, for axle
`a` before the suspension reaches a hardstop, in m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Hmax` |
| **Values:** | `0.5` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

#### Geometry

### **Toe angle at steering center, Toe** — Toe angle `0.0349` (default) | `scalar`

Nominal suspension toe angle at zero steering angle,
*ζ0a*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Toe` |
| **Values:** | `0.0349` (default) | `scalar` |
| **Data Types:** | `double` |

### **Roll steer vs suspension height slope, RollStrgSlp** — Steer angle suspension slope `-0.2269` (default) | `scalar` | `vector`

Roll steer angle versus suspension height,
*mhtoea*,
in rad/m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RollStrgSlp` |
| **Values:** | `-0.2269` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Toe angle vs steering angle slope, ToeStrgSlp** — Toe angle steering slope `0.01` (default) | `scalar` | `vector`

Toe angle versus steering angle slope,
*mtoesteera*,
dimensionless.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Dependencies

To enable the port **StrgAng**, set an element of the **Steered axle
enable by axle, StrgEnByAxl** vector to `1`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ToeStrgSlp` |
| **Values:** | `0.01` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Caster angle at steering center, Caster** — Caster angle at steering center `0.0698` (default) | `scalar`

Nominal suspension caster angle at zero steering angle,
*η0a*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Caster` |
| **Values:** | `0.0698` (default) | `scalar` |
| **Data Types:** | `double` |

### **Caster angle vs suspension height slope, CasterHslp** — Caster angle versus suspension height slope `-0.2269` (default) | `scalar` | `vector`

Caster angle versus suspension height,
*mhcastera*,
in rad/m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CasterHslp` |
| **Values:** | `-0.2269` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Caster angle vs steering angle slope, CasterStrgSlp** — Caster angle versus steering angle slope `0.01` (default) | `scalar` | `vector`

Caster angle versus steering angle slope,
*mcastersteera*,
dimensionless.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Dependencies

To enable the port **StrgAng**, set an element of the **Steered axle
enable by axle, StrgEnByAxl** vector to `1`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CasterStrgSlp` |
| **Values:** | `0.01` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Camber angle at steering center, Camber** — Camber angle at steering center `0.0698` (default) | `scalar`

Nominal suspension camber angle at zero steering angle,
*ξ0a*, in rad.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Camber` |
| **Values:** | `0.0698` (default) | `scalar` |
| **Data Types:** | `double` |

### **Camber angle vs suspension height slope, CamberHslp** — Camber angle versus suspension height slope `-0.2269` (default) | `scalar` | `vector`

Camber angle versus suspension height,
*mhcambera*,
in rad/m.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CamberHslp` |
| **Values:** | `-0.2269` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Camber angle vs steering angle slope, CamberStrgSlp** — Camber angle versus steering angle slope `0.01` (default) | `scalar` | `vector`

Camber angle versus steering angle slope,
*mcambersteera*,
dimensionless.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Dependencies

To enable the port **StrgAng**, set an element of the **Steered axle
enable by axle, StrgEnByAxl** vector to `1`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CamberStrgSlp` |
| **Values:** | `0.01` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |

### **Suspension height vs steering angle slope, StrgHgtSlp** — Suspension height versus steering angle slope `0.1432` (default) | `scalar` | `vector`

Steering angle to vertical force slope applied at suspension wheel carrier
reference point,
*mhsteera*, in
m/rad.

Vector is `1` by the number of vehicle axles,
*Na*. If you provide a scalar value, the block
uses that value for all axles.

#### Dependencies

To enable the port **StrgAng**, set an element of the **Steered axle
enable by axle, StrgEnByAxl** vector to `1`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgHgtSlp` |
| **Values:** | `0.1432` (default) | `scalar` | `vector` |
| **Data Types:** | `double` |
## Libraries

Vehicle Dynamics Blockset / Suspension

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2022b: Parameter name change from `NumTracksByAxl` to `NumWhlsByAxl`

The **Number of tracks by axle, NumTracksByAxl** parameter is renamed
to **Number of wheels by axle, NumWhlsByAxl**.

The block uses the number of wheels per axle to index the
input and output block signals.

## Description

Solid axle suspension with leaf spring

The Solid Axle Suspension - Leaf Spring block implements a solid axle
suspension with a leaf spring for multiple axles with multiple wheels per axle.

The block models the suspension compliance, damping, and
geometric effects as functions of the wheel positions and velocities, with axle-specific
compliance and damping parameters. Using the wheel position and velocity, the block calculates
the vertical wheel position and suspension forces on the vehicle and wheel. The block uses the
*Z*-down coordinate system (defined in SAE J670) and a solid axle
coordinate system. The solid axle coordinate system is aligned with the
*Z*-down vehicle coordinate system, with the *x*-axis in the
direction of forward vehicle motion.

Illustration of a solid axle

This table describes the settings you can specify for each suspension
element.

| Suspension Element | Setting |
| --- | --- |
| Axle | - Multiple wheels - Suspension parameters |
| Wheel | - Steering angles |

The block contains energy-storing spring elements and energy-dissipating damper
elements. The block also stores energy via the axle roll angular acceleration and axle center of
mass vertical and lateral acceleration.

This table summarizes the block parameter settings for a
vehicle with:

- Two axles
- Two wheels per axle
- Steering angle input for both wheels on the front axle

| Parameter | Setting |
| --- | --- |
| **Number of axles, NumAxl** | `2` |
| **Number of wheels by axle, NumWhlsByAxl** | `[2 2]` |
| **Steered axle enable by axle, StrgEnByAxl** | `[1 0]` |

The block uses the wheel number, *t*, to index
the input and output signals. This table summarizes the wheel, axle, and corresponding wheel
number for a vehicle with:

- Two axles
- Two wheels per axle

| Wheel | Axle | Wheel Number |
| --- | --- | --- |
| Front left | Front | `1` |
| Front right | Front | `2` |
| Rear left | Rear | `1` |
| Rear right | Rear | `2` |

### Suspension Compliance and Damping

The block uses a linear spring and damper to model the vertical dynamic effects of the
suspension system on the vehicle and wheel. Specifically, the block:

| Uses | To Calculate |
| --- | --- |
| - Longitudinal and lateral displacement and velocity of the   vehicle. - Longitudinal and lateral displacement and velocity of the   wheel. - Vertical wheel forces applied to the vehicle. | - Suspension forces applied to the axle center. - Vertical displacements and velocities of the vehicle and   wheel. - Longitudinal, lateral and vertical suspension forces and   moments applied to the vehicle. - Longitudinal, lateral and vertical suspension forces and   moments applied to the wheel. |

To calculate the dynamics of the axle, the block implements these equations. The block
neglects the effects of:

- Lateral and longitudinal translational velocity.
- Angular velocity about the vertical and lateral axes.

[x¨ay¨az¨a]=1Ma[FxaFyaFza]+[x˙ay˙az˙a]×[pqr]=1Ma[00Fza]+[00z˙a]×[p00]+[00g]=[0pz˙aFzaMa+g][p˙q˙r˙]=[[MxMyMz]−[pqr]×[Ixx000Iyy000Izz][pqr]][Ixx000Iyy000Izz]−1=[[Mx00]−[pq0]×[Ixx000Iyy000Izz][p00]][Ixx000Iyy000Izz]−1=[MxIxx00]

The net vertical force on the axle center of mass is the sum of the wheel and suspension
forces acting on the axle.

Fza=∑t=1Nta(Fwza,t+Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t))

The net moment about the roll axis of the solid axle suspension accounts for the
hardpoint coordinates of the suspension and wheels.

Mx=∑t=1Nta(Fwza,tywt+(Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t))yst+Mwxa,tIxxIxx+Maywt)

Block parameters provide the track and suspension hardpoints coordinates.

Tct=[xw1xw2…yw1yw2…zw1zw2…]Sct=[xs1xs2…ys1ys2…zs1zs2…]

The block uses Euler angles to transform the track and suspension displacements,
velocities, and accelerations to the vehicle coordinate system.

To calculate the suspension forces applied to the vehicle, the block implements this equation.

Fvza,t=−(Fz0a+kza(zva,t−zsa,t+mhsteera|δsteera,t|)+cza(z˙va,t−z˙sa,t)+Fzhstopa,t)

The suspension forces and moments applied to the vehicle are equal to the suspension
forces and moments applied to the wheel.

Fvxa,t=Fwxa,tFvya,t=Fwya,tFvza,t=−Fwza,tMvxa,t=Mwxa,t+Fwya,t(Rewya,t+Ha,t)Mvya,t=Mwya,t+Fwxa,t(Rewxa,t+Ha,t)Mvza,t=Mwza,t

To calculate the vertical force applied to the suspension at the wheel location, the block
implements a stiff spring-damper, shown here.

Illustration of a spring damper on a solid axle.

The block uses this equation.

Fwza,t=−Fwaz0−kwaz(zwa,t−zsa,t)−cwaz(z˙wa,t−z˙sa,t)

The equations use these variables.

|  |  |
| --- | --- |
| *Fwza,t*, *Mwza,t* | Suspension force and moment applied to the wheel on axle `a`, wheel `t` along wheel-fixed *z*-axis |
| *Fwxa,t*, *Mwxa,t* | Suspension force and moment applied to the wheel on axle `a`, wheel `t` along wheel-fixed *x*-axis |
| *Fwya,t*, *Mwya,t* | Suspension force and moment applied to the wheel on axle `a`, wheel `t` along wheel-fixed *y*-axis |
| *Fvza,t*, *Mvza,t* | Suspension force and moment applied to the vehicle on axle `a`, wheel `t` along wheel-fixed *z*-axis |
| *Fvxa,t*, *Mvxa,t* | Suspension force and moment applied to the vehicle on axle `a`, wheel `t` along wheel-fixed *x*-axis |
| *Fvya,t*, *Mvya,t* | Suspension force and moment applied to the vehicle on axle `a`, wheel `t` along wheel-fixed *y*-axis |
| *Fz0a* | Vertical suspension spring preload force applied to the wheels on axle `a` |
| *kza* | Vertical spring constant applied to wheels on axle `a` |
| *kwaz* | Wheel and axle interface compliance constant |
| *mhsteera* | Steering angle to vertical force slope applied at wheel carrier for wheels on axle `a` |
| *δsteera,t* | Steering angle input for axle `a`, wheel `t` |
| *cza* | Vertical damping constant applied to wheels on axle `a` |
| *cwaz* | Wheel and axle interface damping constant |
| *Rewa,t* | Effective wheel radius for axle `a`, wheel `t` |
| *Fzhstopa,t* | Vertical hardstop force at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *Fzaswya,t* | Vertical anti-sway force at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *Fwaz0* | Wheel and axle interface compliance constant |
| *zva,t*, *żva,t* | Vehicle displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *zwa,t*, *żwa,t* | Wheel displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *xva,t*, *ẋva,t* | Vehicle displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *xwa,t*, *ẋwa,t* | Wheel displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *yva,t*, *ẏva,t* | Vehicle displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *y*-axis |
| *ywa,t*, *ẏwa,t* | Wheel displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *y*-axis |
| *Ha,t* | Suspension height at axle `a`, wheel `t` |
| *Rewa,t* | Effective wheel radius at axle `a`, wheel `t` |

### Hardstop Forces

The hardstop feedback force, *Fzhstopa,t*, that the block applies depends on whether the suspension is compressing or extending. The block applies the force:

- In compression, when the suspension is compressed more than the maximum
  distance specified by the **Suspension maximum height, Hmax**
  parameter
- In extension, when the suspension extension is greater than maximum extension
  specified by the **Suspension maximum height, Hmax**
  parameter

To calculate the force, the block uses a stiffness based on a hyperbolic tangent and exponential scaling.

### Camber, Caster, and Toe Angles

To calculate the camber, caster, and toe angles, block uses linear functions of the suspension
height and steering angle.

ξa,t=ξ0a+mhcambera(zwa,t−zva,t−mhsteera|δsteera,t|)+mcambersteera|δsteera,t|ηa,t=η0a+mhcastera(zwa,t−zva,t−mhsteera|δsteera,t|)+mcastersteera|δsteera,t|ζa,t=ζ0a+mhtoea(zwa,t−zva,t−mhsteera|δsteera,t|)+mtoesteera|δsteera,t|

The equations use these variables.

|  |  |
| --- | --- |
| *ξa,t* | Camber angle of wheel on axle `a`, wheel `t` |
| *ηa,t* | Caster angle of wheel on axle `a`, wheel `t` |
| *ζa,t* | Toe angle of wheel on axle `a`, wheel `t` |
| *ξ0a*, *η0a*, *ζ0a* | Nominal suspension axle a camber, caster, and toe angles, respectively, at zero steering angle |
| *mhcambera*, *mhcastera*, *mhtoea* | Camber, caster, and toe angles, respectively, versus suspension height slope for axle `a` |
| *mcambersteera*, *mcastersteera*, *mtoesteera* | Camber, caster, and toe angles, respectively, versus steering angle slope for axle `a` |
| *mhsteera* | Steering angle versus vertical force slope for axle `a` |
| *δsteera,t* | Steering angle input for axle `a`, wheel `t` |
| *zva,t* | Vehicle displacement at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *zwa,t* | Wheel displacement at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |

### Steering Angles

Optionally, use the **Steered axle enable by axle, StrgEnByAxl** parameter to
input steering angles for the wheels. To calculate the steering angles for the wheels, the block
offsets the input steering angles with a linear function of the suspension height.

δwhlsteera,t=δsteera,t+mhtoea(zwa,t−zva,t−mhsteera|δsteera,t|)+mtoesteera|δsteera,t|

The equation uses these variables.

|  |  |
| --- | --- |
| *mtoesteera* | Axle `a` toe angle versus steering angle slope |
| *mhsteera* | Axle `a` steering angle versus vertical force slope |
| *mhtoea* | Axle `a` toe angle versus suspension height slope |
| *δwhlsteera,t* | Wheel steering angle for axle `a`, wheel `t` |
| *δsteera,t* | Steering angle input for axle `a`, wheel `t` |
| *zva,t* | Vehicle displacement at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *zwa,t* | Wheel displacement at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |

### Power and Energy

The block calculates these suspension characteristics for each axle,
`a`, wheel,
`t`.

| Calculation | Equation |
| --- | --- |
| Dissipated power, *Psuspa,t* | Psuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| Absorbed energy, *Esuspa,t* | Esuspa,t=Fwzlookupa(z˙va,t−z˙wa,t,z˙va,t−z˙wa,t,δsteera,t) |
| Suspension height, *Ha,t* | Ha,t=−(zva,t−zwa,t+Fz0akza+mhsteera|δsteera,t|) |
| Distance from wheel carrier center to tire/road interface | zwtra,t=Rewa,t+Ha,t |

The equations use these variables.

|  |  |
| --- | --- |
| *mhsteera* | Steering angle to vertical force slope applied at wheel carrier for wheels on axle `a` |
| *δsteera,t* | Steering angle input for axle `a`, wheel `t` |
| *Rewa,t* | Axle `a`, wheel `t` effective wheel radius from wheel carrier center to tire/road interface |
| *Fz0a* | Vertical suspension spring preload force applied to the wheels on axle `a` |
| *zwtra,t* | Distance from wheel carrier center to tire/road interface, along the inertial-fixed *z*-axis |
| *zva,t*, *żva,t* | Vehicle displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
| *zwa,t*, *żwa,t* | Wheel displacement and velocity at axle `a`, wheel `t`, along the inertial-fixed *z*-axis |
