---
type: simulink-block
title: 'CVT Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain and Transmission / Transmission – Controllers'
documentation_page: 'cvtcontroller'
documentation_source_path: 'ref/cvtcontroller.html'
language: en
---

# CVT Controller

## Ports

### Inputs

### **DirReq** — Direction request `scalar`

Direction request, *Dirreq*,
controlling the direction, either forward or reverse. *Dir* equals `1` for
forward motion. *Dir* equals `-1` for
reverse.

Dir={1   when Dirreq≥0−1  when Dirreq<0

### **PllyRatioReq** — Pulley ratio request `scalar`

CVT pulley ratio request,
*ratiorequest*.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | Description | Variable | Units |
| --- | --- | --- | --- | --- |
| `Radius` | `PriRadius` | Variator primary pulley radius, resulting from controller request | *rpri* | m |
| `SecRadius` | Variator secondary pulley radius, resulting from controller request | *rsec* | m |
| `InitPllyRadius` | Initial pulley radii with gear ratio of 1 | *ro* | m |
| `RatioAdj` | | Pulley gear ratio command, based on request and physical limitations | *ratiocommand* | N/A |
| `RatioMax` | | Maximum pulley ratio | *ratiomax* | N/A |
| `RatioMin` | | Minimum pulley ratio | *ratiomin* | N/A |
| `PriDispCmd` | | Variator primary pulley displacement, resulting from controller request | *xpri* | m |
| `SecDispCmd` | | Variator secondary pulley displacement, resulting from controller request | *xsec* | m |

### **Dir** — Direction request `scalar`

Direction request, *Dirreq*,
controlling the direction, either forward or reverse. *Dir* equals `1` for
forward motion. *Dir* equals `-1` for
reverse.

Dir={1   when Dirreq≥0−1  when Dirreq<0

### **PriDispCmd** — Primary pulley displacement `scalar`

Variator primary pulley displacement,
*xpri*, in m.

### **SecDispCmd** — Secondary pulley displacement `scalar`

Variator secondary pulley displacement,
*xsec*, in m.

## Parameters

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

## Libraries

Powertrain Blockset / Transmission / Transmission Controllers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Continuously variable transmission controller

The CVT Controller block implements a push belt
continuously variable transmission (CVT) controller. The block uses
standard pulley and geometric equations to calculate the kinematic
setpoints for the CVT variator. You can use the block to control a
CVT.

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
