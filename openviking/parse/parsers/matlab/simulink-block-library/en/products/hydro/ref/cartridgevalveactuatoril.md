---
type: simulink-block
title: 'Cartridge Valve Actuator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Valve Actuators and Forces'
documentation_page: 'cartridgevalveactuatoril'
documentation_source_path: 'ref/cartridgevalveactuatoril.html'
language: en
---

# Cartridge Valve Actuator (IL)

## Ports

### Conserving

### **A** — Pressure port isothermal liquid

Pressure port associated with the valve inlet.

### **B** — Pressure port isothermal liquid

Pressure port associated with the valve outlet.

### **X** — Pressure port isothermal liquid

Pressure port at poppet end.

### **Y** — Pressure port isothermal liquid

Pilot pressure port. To enable this port, set **Number of
pressure ports** to `4`.
### Output

### **S** — Poppet position, m physical signal

Poppet position in m, specified as a physical signal.

## Parameters

### **Number of pressure ports** — Number of pilot pressure ports `3` (default) | `4`

Number of pilot pressure ports. Port **X** measures the
pressure at the end of the poppet. Setting this parameter to
`4` enables the additional pilot-side port
**Y**.

### **Port A poppet area** — Cross-sectional area of port A `1e-4 m^2` (default) | positive scalar

Cross-sectional area of port **A**.

### **Port A poppet to port X pilot area ratio** — Ratio of inlet to pilot port area `0.5` (default) | positive scalar

Ratio of the inlet port, **A**, to the pilot pressure
port, **X**. This value is used to calculate the force at
port **X**.

### **Port Y pilot area** — Cross-sectional area of port Y `1.5e-4 m^2` (default) | positive scalar

Cross-sectional area of port **Y**.

#### Dependencies

To enable this parameter, set **Number of pressure
ports** to `4`.

### **Spring preload force** — Initial spring force `25 N` (default) | positive scalar

Spring force in the valve due to spring preloading. This parameter is a
threshold value which, when added to the pilot pressures at ports
**X** and **Y**, counterbalances the
valve opening due to the pressures at ports **A** and
**B**.

### **Spring stiffness** — Stiffness constant `15e3 N/m` (default) | positive scalar

Spring stiffness constant.

### **Poppet stroke** — Maximum poppet extension `5e-3 m` (default) | positive scalar

Maximum poppet extension.

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | positive scalar in the range [0,1]

Continuous smoothing factor that introduces a layer of gradual change to the piston position
when it is near full extension or full retraction. Set this value to a
nonzero value less than one to increase the stability of your simulation in
these regimes.

### **Connected valve opening orientation** — Direction of poppet displacement `Positive displacement opens valve` (default) | `Negative displacement opens valve`

Direction of the poppet displacement that opens a connected valve. Setting
this parameter to `Positive displacement opens
valve` indicates poppet extension. Setting the parameter to
`Negative displacement opens valve` indicates
poppet retraction.

### **Actuator dynamics** — Whether to account for transients during actuation `Off` (default) | `On`

Whether to account for transient effects in the spool position due to
actuation. Setting **Actuator dynamics** to
`On` approximates actuator motion by introducing a
first-order lag in the spool position. The **Actuator time
constant** also impacts the modeled dynamics.

### **Actuator time constant** — Piston displacement time constant `0.1 s` (default) | positive scalar

Constant that captures the time required for the piston to reach
steady-state when moving from one position to another. This parameter
impacts the modeled actuator dynamics.

#### Dependencies

To enable this parameter, set **Actuator dynamics**
to `On`.

## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Actuator that maintains equilibrium between valve and pilot pressures in an isothermal liquid system

The Cartridge Valve Actuator (IL) block models an actuator that maintains equilibrium
between the valve and pilot-line pressures. The valve between ports
**A** and **B** remains closed until the pilot
spring **Spring preload force** is surpassed, at which point the piston
begins to move. The piston position is output as a physical signal at port
**S**. A schematic of a 4-port cartridge valve actuator is shown
below.

### Actuator Force Balance

The actuator piston moves to adjust the pressure in the actuator chamber, which
maintains equilibrium between the actuator port pressures and pilot line pressures:

pAAA+pBAB=Fpreload+Fpilot,

where:

- *p*A and
  *p*B are the pressures at
  ports **A** and **B**.
- *A*X is calculated from the
  **Port A to port X area ratio**.
- *A*B is the port
  **B** area, AX−AA, when the **Number of pressure
  ports** is set to `3`. When the
  **Number of pressure ports** is set to
  `4`,
  *A*B is AX−AA+AY.
- *F*preload is the initial
  spring force in the system.
- *F*pilot is pXAX if **Number of pressure ports** is
  set to `3` and pXAX+pYAY if **Number of pressure ports** is
  set to `4`.

### Piston Position

The steady piston displacement is calculated as:

xsteady=Fεk=FA+FB−Fpilot−Fpreloadkε,

where *ε* is the **Opening
orientation**, which assigns movement in a positive direction
(extension) or negative direction (retraction). The dynamic change in piston
displacement is:

x˙dyn=xsteady−xdynτ,

where *τ* is the **Actuator time
constant**. When x˙dyn=xdynτ. is less than the **Spring preload force**,
*x*steady = 0.

If x˙dyn=xdynτ. is greater than the sum of the preload force and
*kx*stroke,
*x*steady =
*x*stroke.

### Opening Dynamics

If opening dynamics are modeled, a lag is introduced to the flow response to the
modeled control pressure. *p*control becomes
the dynamic control pressure, *p*dyn;
otherwise, *p*control is the steady-state
pressure. The instantaneous change in dynamic control pressure is calculated based
on the **Opening time constant**, *τ*:

p˙dyn=pcontrol−pdynτ.

By default, **Opening dynamics** is set to
`Off`.

### Numerically-Smoothed Force

When the actuator is close to full extension or full retraction, you can maintain
numerical robustness in your simulation by adjusting the block **Smoothing
factor**. A smoothing function is applied to all calculated forces,
but primarily influences the simulation at the extremes of the piston motion.

The normalized force is

F^=FA+FB−FPreload−FPilotkxstroke.

where:

- *FA* is the force at port
  **A**.
- *FB* is the force at port
  **B**.
- *FPreload* is the
  **Spring preload force**.
- *FPilot* is the force at port
  **X**.

If the **Smoothing factor** parameter is nonzero, the block smoothly
saturates the normalized force between `0` and
`1`.

For more information, see Numerical Smoothing.

### Assumptions and Limitations

Internal fluid volumes are not modeled in this block. There is no mass flow rate
through ports **A**, **B**,
**X**, and **Y**.
