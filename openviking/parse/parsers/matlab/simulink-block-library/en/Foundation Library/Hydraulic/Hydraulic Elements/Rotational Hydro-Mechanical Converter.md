---
type: simulink-block
title: 'Rotational Hydro-Mechanical Converter'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'rotationalhydromechanicalconverter'
documentation_source_path: 'ref/rotationalhydromechanicalconverter.html'
language: en
---

# Rotational Hydro-Mechanical Converter

## Ports
```yaml
ports: []
```

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the converter inlet.

`S`
:   Mechanical rotational conserving port associated with the shaft of the converter.

`C`
:   Mechanical rotational conserving port associated with the case of the converter.

`P`
:   Physical signal input port that passes the position information from a Simscape™
    Multibody™ joint. Connect this port to the position sensing port
    **q** of the joint. For more information, see Connecting Simscape Networks to Simscape Multibody Joints. To enable this
    port, set the **Interface rotation** parameter to `Provide
    input signal from Multibody joint`.
## Parameters
```yaml
parameters: []
```

**Displacement**
:   Effective converter displacement. The default value is `1.2e-4`
    m^3/rad.

**Converter orientation**
:   Specifies converter orientation with respect to the globally assigned positive
    direction. The converter can be installed in two different ways, depending upon whether
    it generates torque in the positive or in the negative direction when pressure is
    applied at its inlet:

    - `Pressure at A causes positive displacement of R relative to
      C` — Increase in the fluid pressure results in a positive
      rotation of port **R** relative to port **C**.
      This is the default.
    - `Pressure at A causes negative displacement of R relative to
      C` — Increase in the fluid pressure results in a negative
      rotation of port **R** relative to port
      **C**.

**Compressibility**
:   Specifies whether fluid density is taken as constant or varying with pressure. The
    default value is `Off`, in which case the block models an ideal
    transducer. If you select `On`, the block dialog box displays
    additional parameters that let you model dynamic variations of the fluid density without
    adding any extra blocks.

**Shaft rotation**
:   Select method to determine rotation of port **R** relative to port
    **C**:

    - `Calculate from velocity of port R relative to port C`
      — Calculate rotation from relative port velocities, based on the block
      equations. This is the default method.
    - `Provide input signal from Multibody joint` —
      Enable the input physical signal port **q** to pass the rotation
      information from a Multibody joint. Use this method only when you connect the
      converter to a Multibody joint by using a Rotational Multibody
      Interface block. For more information, see How to Pass Position Information.

    This parameter is enabled when **Compressibility** is
    `On`.

**Initial shaft angle**
:   Initial offset of the piston from the cylinder cap. This parameter is enabled when
    **Compressibility** is `On` and
    **Shaft rotation** is `Calculate from velocity of port R
    relative to port C`. The default value is `0`.

**Dead volume**
:   Volume of fluid in the chamber at zero piston position. This parameter is enabled
    when **Compressibility** is `On`. The default
    value is `1e-4` m^3.

**Specific heat ratio**
:   Gas-specific heat ratio. This parameter is enabled when
    **Compressibility** is `On`. The default
    value is `1.4`.

**Initial pressure**
:   Initial pressure in the chamber. This parameter specifies the initial condition for
    use in computing the block's initial state at the beginning of a simulation run. It is
    enabled when **Compressibility** is `On`. The
    default value is `0`.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Interface between hydraulic and mechanical rotational domains

The Rotational Hydro-Mechanical Converter block models an ideal transducer
that converts hydraulic energy into mechanical energy, in the form of rotational motion of the
converter shaft, and vice versa. Physically, the converter represents the main component of a
single-acting rotary vane actuator. The compressibility option makes the converter account for
dynamic variations of the fluid density.

Using this block as a basic element, you can build a large variety of rotary actuators by
adding application-specific effects, such as leakage, friction, hard stops, and so on.

The converter is simulated according to the following equations:

q=d(ρρl0V)dt=d(ρρl0)dtV+ρρl0⋅ε⋅(ωS−ωC)⋅D

T=ε⋅p⋅D

ρ={(α1−α)ρg0+ρl0(α1−α)(p0p+p0)1γ+e−pβlif compressibility is onρl0if compressibility is off

where

|  |  |
| --- | --- |
| *q* | Flow rate to the converter chamber |
| *D* | Converter displacement, or fluid volume needed to rotate the shaft per angle unit |
| ωS | Converter shaft angular velocity |
| ωC | Converter case angular velocity |
| *T* | Torque on the shaft |
| *p* | Gauge pressure of fluid in the converter chamber |
| *V* | Piston volume |
| *α* | Relative amount of trapped air |
| *ρ*l0 | Fluid density at atmospheric conditions |
| *ρ*g0 | Gas density at atmospheric conditions |
| *p*0 | Atmospheric pressure |
| *γ* | Specific heat ratio |
| *β*l | Bulk modulus at atmospheric conditions and no gas |
| *ε* | Mechanical orientation of the converter (`1` if increase in fluid pressure causes positive rotation of R relative to C, `-1` if increase in fluid pressure causes negative rotation of R relative to C) |

The piston volume is computed according to

V=Vdead+D⋅(θ0+θ)dθdt=ε⋅(ωS−ωC)

where

|  |  |
| --- | --- |
| *V*dead | Chamber dead volume |
| *θ*0 | Shaft initial angle |
| *θ* | Shaft rotation from initial position |

Port A is a hydraulic conserving port associated with the converter inlet. Ports S and C
are mechanical rotational conserving ports associated with the shaft and the case of the
converter, respectively. Pressure at port A generates torque in the direction specified by the
**Converter orientation** parameter.

The block dialog box does not have a **Source code** link. To view the
underlying component source, open the following files in the MATLAB® editor:

- For incompressible converter implementation — `rotational_converter_incompressible.ssc`
- For compressible converter implementation — `rotational_converter_compressible.ssc`
