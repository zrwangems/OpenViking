---
type: simulink-block
title: 'Continuously Variable Transmission'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain and Transmission / Transmission – Systems and Converters'
documentation_page: 'continuouslyvariabletransmission'
documentation_source_path: 'ref/continuouslyvariabletransmission.html'
language: en
---

# Continuously Variable Transmission

## Ports

### Inputs

### **Dir** — Direction request `scalar`

Direction request, *Dirreq*,
controlling the direction. The block filters the request to determine
the direction, forward or reverse. *Dir* equals `1` for
forward motion. *Dir* equals `-1` for
reverse.

Dir={1   when Dirreq≥0−1  when Dirreq<0

### **PllyRatioReq** — Pulley ratio request `scalar`

CVT pulley ratio request,
*ratiorequest*.

#### Dependencies

To create this port, for the **Control mode**
parameter, select `Ideal integrated
controller`.

### **PriDisp** — Primary pulley displacement `scalar`

Variator primary pulley displacement,
*xpri*, in m.

#### Dependencies

To create this port, for the **Control mode**
parameter, select `External
control`.

### **SecDisp** — Secondary pulley displacement `scalar`

Variator secondary pulley displacement,
*xsec*, in m.

#### Dependencies

To create this port, for the **Control mode**
parameter, select `External
control`.

### **EngTrq** — Input drive shaft torque `scalar`

External torque applied to the input drive shaft,
*Ti*, in N·m.

### **DiffTrq** — Output drive shaft torque `scalar`

External torque applied to the output drive shaft,
*To*, in N·m.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `EngTrq` | | | Input shaft torque | *Ti* | N·m |
| `DiffTrq` | | | Output shaft torque | *To* | N·m |
| `EngSpd` | | | Input shaft speed | *ωi* | rad/s |
| `DiffSpd` | | | Output shaft speed | *ωo* | rad/s |
| `PriRadius` | | | Primary pulley radius | *rpri* | m |
| `PriPhi` | | | Primary pulley wrap angle | *Φpri* | rad |
| `SecRadius` | | | Secondary pulley radius | *rsec* | m |
| `SecPhi` | | | Secondary pulley wrap angle | *Φsec* | rad |
| `BltLngthDelta` | | | Change in belt length | *ΔL* | m |
| `BltLngth` | | | Belt length | *L* | m |
| `BltLngthInit` | | | Initial belt length | *Lo* | m |
| `BltOnPriTrq` | | | Belt torque acting on the primary pulley | *TBoP\_pri* | N·m |
| `BltOnSecTrq` | | | Belt torque acting on the secondary pulley | *TBoP\_sec* | N·m |
| `BltVel` | | | Linear speed of the belt | *vb* | m/s |
| `PriAngVel` | | | Primary pulley speed | *ωpri* | rad/s |
| `SecAngVel` | | | Secondary pulley speed | *ωsec* | rad/s |
| `PriSlipDir` | | | Primary pulley slip direction indicator | *PriSlipDir* | N/A |
| `SecSlipDir` | | | Secondary pulley slip direction indicator | *SecSlipDir* | N/A |
| `TransSpdRatio` | | | Total no-slip gear ratio | *Nfinal* | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrEng` | Engine power | *Peng* | W |
| `PwrDiffrntl` | Differential power | *Pdiff* | W |
| `PwrNotTrnsfrd` | `PwrBltLoss` | Belt slip power loss | *Pbltloss* | W |
| `PwrGearInLoss` | Input planetary gear mechanical power loss | *Pgrinloss* | W |
| `PwrGearOutLoss` | Output gear reduction mechanical power loss | *Pgroutloss* | W |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | W |
| `PwrStored` | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | W |

### **EngSpd** — Input drive shaft speed `scalar`

Input drive shaft angular speed,
*ωi*, in rad/sec.

### **DiffSpd** — Output drive shaft speed `scalar`

Output drive shaft angular speed,
*ωo*, in rad/sec.

## Parameters

### **Control mode** — External or internal `Ideal integrated controller` (default) | `External control`

Specify the control method, either internal or external.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CtrlType` |
| **Values:** | `Ideal integrated controller` (default) | `External control` |
| **Data Types:** | `character vector` |

#### Dependencies

This table summarizes the port and input model
configurations.

| Control Mode | Creates Ports |
| --- | --- |
| `Ideal integrated controller` | `PllyRatioReq` |
| `External control` | `PriDisp`  `SecDisp` |

#### Kinematics

### **Maximum variator primary pulley radius, rp\_max** — Radius `.08` (default) | `scalar`

Maximum variator primary pulley radius,
*rpmax*, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rp_max` |
| **Values:** | `.08` (default) | `scalar` |
| **Data Types:** | `double` |

### **Maximum variator secondary pulley radius, rs\_max** — Radius `.07` (default) | `scalar`

Maximum variator secondary pulley radius,
*rsmax*, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rs_max` |
| **Values:** | `.07` (default) | `scalar` |
| **Data Types:** | `double` |

### **Minimum variator primary pulley radius, rp\_min** — Radius `.03` (default) | `scalar`

Minimum variator primary pulley radius,
*rpmin*, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rp_min` |
| **Values:** | `.03` (default) | `scalar` |
| **Data Types:** | `double` |

### **Minimum variator secondary pulley radius, rs\_min** — Radius `.03` (default) | `scalar`

Minimum variator secondary pulley radius,
*rsmin*, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rs_min` |
| **Values:** | `.03` (default) | `scalar` |
| **Data Types:** | `double` |

### **Gap distance between variator pulleys, rgap** — Specify crown wheel connection `.025` (default) | `scalar`

The gap between the secondary and primary pulleys,
*rgap*, in m. The figure shows the
pulley geometry.

Primary pulley and secondary pulley connected with belt. Primary pulley has radius rpri. Secondary pulley has radius rsec. Pulleys are in line and separated by distance rgap.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rgap` |
| **Values:** | `.025` (default) | `scalar` |
| **Data Types:** | `double` |

### **Variator wedge angle, thetawedge** — Specify crown wheel connection `11` (default) | `scalar`

Variator wedge angle, *Θwedge*, in deg.

Variator wedge angle, theta, showing ange between vertical line and projection of wedge.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `thetaWedge` |
| **Values:** | `11` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dynamics

### **Primary pulley inertia, J\_pri** — Inertia `0.1` (default) | `scalar`

Primary pulley inertia, *Jpri*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J_pri` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Secondary pulley inertia, J\_sec** — Inertia `0.1` (default) | `scalar`

Secondary pulley inertia, *Jsec*,
in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J_sec` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Primary pulley damping coefficient, b\_pri** — Damping `0.001` (default) | `scalar`

Primary pulley damping coefficient,
*bpri*, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b_pri` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Secondary pulley damping coefficient, b\_sec** — Damping `0.001` (default) | `scalar`

Secondary pulley damping coefficient,
*bsec*, in N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b_sec` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Belt damping coefficient, b\_b** — Damping `0.0025` (default) | `scalar`

Belt damping coefficient, *bb*, in
kg/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `b_b` |
| **Values:** | `0.0025` (default) | `scalar` |
| **Data Types:** | `double` |

### **Static friction coefficient, mu\_static** — Friction `0.3` (default) | `scalar`

Static friction coefficient between the belt and primary pulley,
*μstatic*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **Values:** | `0.3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, mu\_kin** — Friction `0.2` (default) | `scalar`

Kinetic friction coefficient between the belt and primary pulley,
*μkin*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_kin` |
| **Values:** | `0.2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Belt mass, m\_b** — Mass `3` (default) | `scalar`

Belt mass, *mb*, in kg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `m_b` |
| **Values:** | `3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Pulley clamp force, F\_ax** — Pulley clamp force `5000` (default) | `scalar`

Pulley clamp force, *Fax*, in
N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `F_ax` |
| **Values:** | `5000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Reverse and Output Ratio

### **Forward inertia, J\_fwd** — Inertia `0.1` (default) | `scalar`

Forward inertia, *Jfwd*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J_fwd` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Reverse inertia, J\_rev** — Inertia `0.1` (default) | `scalar`

Reverse inertia, *Jrev*, in
kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `J_rev` |
| **Values:** | `0.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Forward efficiency, eta\_fwd** — Efficiency `0.95` (default) | `scalar`

Forward efficiency, *ηfwd*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_fwd` |
| **Values:** | `0.95` (default) | `scalar` |
| **Data Types:** | `double` |

### **Reverse efficiency, eta\_rev** — Efficiency `0.95` (default) | `scalar`

Reverse efficiency, *ηrev*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_rev` |
| **Values:** | `0.95` (default) | `scalar` |
| **Data Types:** | `double` |

### **Reverse gear ratio, N\_rev** — Ratio `2` (default) | `scalar`

Reverse gear ratio, *Nrev*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_rev` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Shift time constant, tau\_s** — Constant `.01` (default) | `scalar`

Shift time constant, *τs*, in
s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `tau_s` |
| **Values:** | `.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Output gear ratio, N\_o** — Ratio `2` (default) | `scalar`

Output gear ratio, *No*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `N_o` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

### **Output gear efficiency, eta\_o** — Efficiency `0.98` (default) | `scalar`

Output gear efficiency, *ηo*,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `eta_o` |
| **Values:** | `0.98` (default) | `scalar` |
| **Data Types:** | `double` |

## Libraries

Powertrain Blockset / Transmission / Transmission Systems

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Push belt continuously variable transmission with independent radii control

The Continuously Variable Transmission block
implements a push belt continuously variable transmission (CVT) with
independent radii control. Use the block for control system design,
powertrain matching, and fuel economy studies. You can configure the
block for internal or external control:

- Internal — Input direction and pulley ratio
  requests
- External — Input direction and pulley displacement
  requests

The table summarizes the pulley kinematic, speed reduction,
and dynamic calculations made by the Continuously Variable
Transmission block.

| Calculation | Pulley Kinematics | Reverse and Final Speed Reduction | Dynamics |
| --- | --- | --- | --- |
| Final angular speed ratio | ✓ | ✓ | ✓ |
| Belt torque applied to the secondary and primary pulleys |  |  | ✓ |
| Torque applied to the secondary and primary pulleys |  | ✓ |  |
| Angular velocity of secondary and primary pulleys | ✓ | ✓ | ✓ |
| Belt and pulley geometry | ✓ |  |  |
| Belt linear speed |  |  | ✓ |
| Wrap angle on secondary and primary pulley | ✓ |  |  |
| Primary and secondary pulley radii | ✓ |  |  |

The figure shows the CVT variator with two configurations. In
the first configuration, which illustrates speed reduction, the variator
is set to decrease the primary pulley radius and increase the secondary
pulley radius. In the second configuration, which illustrates overdrive,
the variator is set to increase the primary pulley radius and decrease
the secondary pulley radius.

The figure shows the CVT variator with two configurations. In the first configuration, which illustrates speed reduction, the variator is set to decrease the primary pulley radius and increase the secondary pulley radius. In the second configuration, which illustrates overdrive, the variator is set to increase the primary pulley radius and decrease the secondary pulley radius.

### Pulley Kinematics

Using the physical dimensions of the system, the block calculates
the primary and secondary variator positions that meet the pulley
ratio request.

The figure and equations summarize the geometric dependencies.

Primary pulley and secondary pulley connected with belt. Primary pulley has radius rpri. Secondary pulley has radius rsec. Pulleys are in line and separated by distance rgap.

Cdist=rpmax+rgap+rsec\_maxL0=f(rpmax,rsmax,rpmin,rsmin,Cdist)ratiocommand=f(ratiorequest,ratiomax,ratiomin)rpri=f(r0,ratiocommand,Cdist)rsec=f(r0,ratiocommand,Cdist)xpri=f(r0,rpri,θwedge)xsec=f(r0,rsec,θwedge)

The equations use these variables.

|  |  |
| --- | --- |
| *ratiorequest* | Pulley gear ratio request |
| *ratiocommand* | Pulley gear ratio command, based on request and physical limitations |
| *rgap* | Gap distance between variator pulleys |
| *Cdist* | Distance between variator pulley centers |
| *rpmax* | Maximum variator primary pulley radius |
| *rsmax* | Maximum variator secondary pulley radius |
| *rpmin* | Minimum variator primary pulley radius |
| *rsmin* | Minimum variator secondary pulley radius |
| *ro* | Initial pulley radii with gear ratio of `1` |
| *Lo* | Initial belt length, resulting from variator specification |
| *xpri* | Variator primary pulley displacement, resulting from controller request |
| *xsec* | Variator secondary pulley displacement, resulting from controller request |
| *rpri* | Variator primary pulley radius, resulting from controller request |
| *rsec* | Variator secondary pulley radius, resulting from controller request |
| *Θwedge* | Variator wedge angle |
| *Φ* | Angle of belt to pulley contact point |
| *L* | Belt length, resulting from variator position |

### Reverse and Final Speed Reduction

The CVT input shaft connects to a planetary gear set that drives
the primary pulley. The shift direction determines the input gear
inertia, efficiency, and gear ratio. The shift direction is the filtered
commanded direction:

DirshiftDir(s)=1τss+1

For forward motion (Dirshift=1):

Ni=1ηi=ηfwdJi=Jfwd

For reverse motion
(Dirshift=−1):

Ni=−Nrevηi=ηrevJi=Jrev

The gear ratio and efficiency determine the input drive shaft
speed and torque applied to the primary pulley:

Tapp\_pri=ηiNiTi

The block reduces the secondary pulley speed and applied torque
using a fixed gear ratio.

Tapp\_sec=ToηoNoωo=ωsecNo

The final gear ratio, without slip, is given by:

Nfinal=ωiωo=NiNorsecrpri

The equations use these variables.

|  |  |
| --- | --- |
| *Ni* | Input planetary gear ratio |
| *Dir* | CVT direction command |
| *Dirshift* | Direction used to determine planetary inertia, efficiency, and ratio |
| *τs* | Direction shift time constant |
| *ηfwd*, *ηrev* | Forward and reverse gear efficiency, respectively |
| *Jfwd*, *Jrev* | Forward and reverse gear inertia, respectively |
| *Nrev* | Reverse gear ratio |
| *Tapp\_pri*, *Tapp\_sec* | Torque applied to primary and secondary pulleys, respectively |
| *Ti* | Input drive shaft torque |
| *ωi*, *ωo* | Input and output drive shaft speed, respectively |
| *ωpri*, *ωsec* | Primary and secondary pulley speed, respectively |
| *Nfinal* | Total no-slip gear ratio |

### Dynamics

The maximum torque that the CVT can transmit depends on the
friction between the pulleys and belt. According to *Prediction
of Friction Drive Limit of Metal V-Belt*, the torque friction
is defined as:

Tfric(rp,μ)=2μFaxrpcos(ϑwedge)

Without macro slip, the tangential acceleration of the pulley
is assumed to be equal to the belt acceleration. Once the torque reaches
the static friction limit, the belt begins to slip, and the pulley
and belt acceleration are independent. During slip, the torque transmitted
by the belt is a function of the kinetic friction factor. During the
transition from slip to non-slip conditions, the belt and tangential
pulley velocities are equal.

The block implements these equations for four different slip
conditions.

| Condition | Equations |
| --- | --- |
| Belt slips on both secondary and primary pulleys | (Jpri+Ji)ω˙pri=Tapp\_pri-TBoP\_pri-bpriωpriJsecω˙sec=Tapp\_sec-TBoP\_sec-bsecωsecmbv˙b=TBoP\_prirpri+TBoP\_secrsec-bbvbrpriωpri≠vbrsecωsec≠vb |
| Belt slips on only the primary pulley | (Jpri+Ji)ω˙pri=Tapp\_pri-TBoP\_pri-bpriωpri(mb+Jsecr2sec)v˙b=TBoP\_prirpri+TBoP\_secrsec-(bb+bsecr2sec)vbωsec=vbrsecrpriωpri≠vbTBoP\_pri=sgn(rpriωpri−vb)Tfric(rpri,μkin)|TBoP\_sec|<Tfric(rsec,μstatic) |
| Belt slips on only the secondary pulley | (mb+Jpri+Jir2pri)v˙b=Tapp\_prirpri+TBoP\_secrsec-(bb+bprir2pri)vbJsecω˙b=Tapp\_sec+TBoP\_sec-bsecωsecωpri=vbrprirsecωsec≠vbTBoP\_sec=sgn(rsecωsec−vb)Tfric(rsec,μkin)|TBoP\_pri|<Tfric(rpri,μstatic) |
| Belt does not slip | (mb+Jsecr2sec+Jpri+Jir2pri)v˙b=Tapp\_prirpri+Tapp\_secrsec-(bb+bsecr2sec+bprir2pri)vbωpri=vbrpriωsec=vbrsec|TBoP\_pri|<Tfric(rpri,μstatic)|TBoP\_sec|<Tfric(rsec,μstatic) |
| Slip direction | PriSlipDir={0rpriωpri=vb1rpriωpri>vb−1rpriωpri<vbSecSlipDir={0rsecωsec=vb1rsecωsec>vb−1rsecωsec<vb |

The equations use these variables.

|  |  |
| --- | --- |
| *TBoP\_pri*, *TBoP\_sec* | Belt torque acting on the primary and secondary pulleys, respectively |
| *Tapp\_pri*, *Tapp\_sec* | Torque applied to primary and secondary pulleys, respectively |
| *Jpri*, *Jsec* | Primary and secondary pulley rotational inertias, respectively |
| *bpri*, *bsec* | Primary and secondary pulley rotational viscous damping, respectively |
| *Fax* | Pulley clamp force |
| *μ* | Coefficient of friction |
| *μkin*, *μstatic* | Coefficient of kinetic and static friction |
| *vb*, *аb* | Linear speed and acceleration of the belt, respectively |
| *mb* | Total belt mass |
| *rpri*, *rsec* | Radii of the primary and secondary pulleys, respectively |
| *Φwrap* | Wrap angle of belt to pulley contact point |
| *Φwrap\_pri*, *Φwrap\_sec* | Primary and secondary pulley wrap angles, respectively |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrEng` | Engine power | *Peng* | ωiTi |
| `PwrDiffrntl` | Differential power | *Pdiff* | ωoTo |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrBltLoss` | Belt slip power loss | *Pbltloss* | (Jin+Jpri)ω˙priωpri+Jsecω˙secωsec+mbv˙bvb+bpriωpri2+bsecωsec2+bbvb2−Tapppriωpri−Tappsecωsec |
| `PwrGearInLoss` | Input planetary gear mechanical power loss | *Pgrinloss* | −|ωiTi−Τapp\_priωpri| |
| `PwrGearOutLoss` | Output gear reduction mechanical power loss | *Pgroutloss* | −|ωoTo−Τapp\_secωsec| |
| `PwrDampLoss` | Mechanical damping loss | *Pdamploss* | −bpriωpri2−bsecωsec2−bbvb2 |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredTrans` | Rate change in rotational kinetic energy | *Pstr* | (Jin+Jpri)ω˙priωpri+Jsecω˙secωsec+mbv˙bvb |

The equations use these variables.

|  |  |
| --- | --- |
| *Tapp\_pri*, *Tapp\_sec* | Torque applied to primary and secondary pulleys, respectively |
| *Ti*, *To* | Input and output drive shaft torque, respectively |
| *Jpri*, *Jsec* | Primary and secondary pulley rotational inertias, respectively |
| *bpri*, *bsec* | Primary and secondary pulley rotational viscous damping, respectively |
| *ωpri*, *ωsec* | Primary and secondary pulley speed, respectively |
| *ωi*, *ωo* | Input and output drive shaft speed, respectively |
| *vb*, *аb* | Linear speed and acceleration of the belt, respectively |
| *rpri*, *rsec* | Radii of the primary and secondary pulleys, respectively |
