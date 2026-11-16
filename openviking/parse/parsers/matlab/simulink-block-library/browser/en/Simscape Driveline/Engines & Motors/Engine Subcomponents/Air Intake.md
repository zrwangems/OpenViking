---
type: simulink-block
title: 'Air Intake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'airintake'
documentation_source_path: 'ref/airintake.html'
language: en
---

# Air Intake

## Ports

### Input

### **Thr** — Throttle command input, unitless physical signal

Physical signal input associated with the normalized throttle command,
where `0` represents a fully closed throttle, and
`1` represents a fully open throttle. The block
maps this input to a throttle-open angle between `0`
and `90` degrees.

### **EngSpd** — Rotational engine speed, rad/s physical signal

Physical signal input associated with the rotational speed, in rad/s.
### Output

### **Pim** — Intake manifold pressure input, kPa physical signal

Physical signal input associated with the intake manifold, in kPa.

## Parameters

### **Dry air specific gas constant** — Dry air specific gas constant `287.058` `J/(K*kg)` (default) | positive scalar

Specific gas constant of dry air.

### **Dry air specific heat ratio** — Dry air specific heat ratio `1.4` (default) | positive scalar

Specific heat ratio of dry air.

### **Ambient pressure** — Reference air pressure `101.325` `kPa` (default) | positive scalar

Pressure of the air entering the intake.

### **Ambient temperature** — Reference temperature `298.15` `K` (default) | positive scalar

Temperature of the air entering the intake.

### **Throttle rest angle** — Released throttle position `3` `deg` (default) | positive scalar

Radial distance from the resting throttle position to `0`
degrees.

### **Throttle plate diameter** — Throttle plate diameter `5` `cm` (default) | positive scalar

Diameter of the butterfly valve disc in the throttle body.

### **Throttle leakage area** — Throttle leakage area `1` `cm^2` (default) | nonnegative scalar

Cumulative area of throttle leakage.

### **Intake manifold volume** — Intake manifold volume `1000` `cm^3` (default) | positive scalar

Volumetric capacity of the intake manifold.

### **Engine displacement volume** — Engine displacement volume `1500` `cm^3` (default) | positive scalar

Combined displacement of all engine pistons.

### **Throttle response time constant** — Throttle response time constant `0.1` `s` (default) | positive scalar

Time constant associated with the response rate of the engine to the
throttle command.

## Libraries

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Combustion cylinder air supply intake

The Air Intake block represents an abstract air intake system
that computes lumped-parameter air flow dynamics. This block is suitable for internal
combustion engines. The block computes the intake manifold pressure from the throttle
and engine speed.

### Equations

The Air Intake block computes the intake manifold pressure as

ddtPim=RairTambVim(m˙thr−m˙cyl),

where

- *Rair* is the **Dry
  air specific gas constant** parameter.
- *Tamb* is the
  **Ambient temperature** parameter.
- *Vim* is the **Intake
  manifold volume** parameter.

The block calculates the combustion cylinder mass flow rate,
*ṁcyl*, as

m˙cyl=ωVdPim2RairTamb,

which is a time derivative formulation of the ideal gas law.
*ω* is the engine speed the block receives from port
**EngSpd**, and *Vd* is
the **Engine displacement volume** parameter.

The block calculates the throttle mass flow rate,
*ṁthr* as

m˙thr={SthrTambc1(Pamb−Pim)                            LaminarSthrTambPambc2[(PambPim)cb−(PambPim)ca]  SubsonicSthrTambc3Pamb                                        Choked

depending on the flow conditions. In this equation,
*Sthr* is the area of the throttle
opening, and *Pamb* is the ambient pressure.
The block defines the equation constants as

ca=κ+1κcb=2κc1=c2(Πlamcb−Πlamca)1−Πlamc2=2κRair(κ−1)c3=κRairΠcrca

where

- *κ* is the **Dry air specific heat
  ratio** parameter.
- *Πlam* is the laminar flow
  threshold constant.
- *Πcr* is the critical pressure
  ratio.

The block finds *Πcr* as

Πcr=(2κ+1)κκ−1.

**Throttle Open Area**

The block treats the throttle open area, *Sthr*,
as a third-order polynomial that functions with respect to the throttle angle,
*θ*. This method simplifies the block computation to
improve performance. The block computes the throttle open area as

Sthr(θ)=k0+k1θ+k2θ2+k3θ3,

where the block derives the coefficients,
*ki*, using these quantities:

- *Dplate* —
  **Throttle plate diameter** parameter
- *Arest* —
  **Throttle rest angle** parameter
- *Apeak* — 85°
- *Sleak* —
  **Throttle leakage area** parameter

The throttle open area uses these constraints:

Sthr(0)=Seng(0)Sthr(π2)=Seng(Apeak)ddθSthr(Arest)=ddθSeng(Arest)ddθthrSthr(Apeak)=0

where *Seng* is the
engineering formula for the throttle open area, such that

Seng(θ)=π(Dplate2)2(1−cos(θ)cos(Arest))+Sleak.

This figure shows a comparison of the polynomial result and
the engineering result.

Throttle open area with respect to throttle angle. The polynomial approximation has a different shape than the engineering equation, but they trend close to one another.
