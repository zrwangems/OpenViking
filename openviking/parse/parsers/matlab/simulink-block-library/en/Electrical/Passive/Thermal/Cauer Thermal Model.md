---
type: simulink-block
title: 'Cauer Thermal Model'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'cauerthermalmodel'
documentation_source_path: 'ref/cauerthermalmodel.html'
language: en
---

# Cauer Thermal Model

## Ports

### Conserving

### **A** — First surface of the semiconductor individual layer thermal

Thermal conserving port associated with the first surface of the
individual layer of the semiconductor.

### **B** — Second surface of the semiconductor last layer thermal

Thermal conserving port associated with the second surface of the last
layer of the semiconductor.

## Parameters

### **Parameterize Cauer model using Foster coefficient data** — Parameterize Cauer model using Foster coefficient data `Off` (default) | `On`

Whether to parameterize the Cauer model by using coefficient data from a
Foster model.

### **Thermal resistance data** — Thermal resistances `1e-3 * [2.6468, 3.8701, 1.2007, .8824]` `K/W` (default)

Vector of thermal resistances.

#### Dependencies

To enable this parameter, clear the **Parameterize Cauer model
using Foster coefficient data** parameter.

### **Thermal time constant data** — Thermal time constants `[.0086, .054, .3624, 1.651]` `s` (default)

Vector of thermal time constants.

#### Dependencies

To enable this parameter, clear the **Parameterize Cauer model
using Foster coefficient data** parameter.

### **Thermal resistance data (Foster)** — Thermal resistances parameterized from Foster data `[.0016, .0043, .0013, .0014]` `K/W` (default)

Vector of thermal resistances parameterized by using data from a Foster
model.

#### Dependencies

To enable this parameter, select the **Parameterize Cauer
model using Foster coefficient data** parameter.

### **Thermal time constant data (Foster)** — Thermal time constants parameterized from Foster data `[.0068, .064, .32, 2]` `s` (default)

Vector of thermal time constants parameterized by using data from a Foster
model.

#### Dependencies

To enable this parameter, select the **Parameterize Cauer
model using Foster coefficient data** parameter.

## Libraries

Simscape / Electrical / Passive / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2022b: Removal of **R** port and **Show absolute reference port** parameter

The Cauer Thermal Model block no longer supports the external
**R** port. The reference temperature is set to
`0` Kelvin. In your models, delete the blocks previously
connected to the **R** port of the Cauer Thermal Model
block.

## Description

Heat transfer through multiple layers of a semiconductor module

The Cauer Thermal Model block represents heat transfer
through multiple layers of a semiconductor module. A Cauer Thermal
Model contains multiple Cauer Thermal Model Element components. The
figure shows an equivalent circuit for a Cauer Thermal Model
Element.

The multiple layers of a Cauer thermal model include chip, solders, substrate, and
base. Other terms that describe a Cauer thermal model are:

- Continued fraction circuit
- T model
- Ladder network

This figure shows an equivalent circuit for a Cauer Thermal Model.

The temperature at **R** is equal to the absolute zero
temperature.

### Equations

The defining equations for each Cauer thermal model element are

Cthermal=τRthermal,

QAB=TABRthermal,

and

QAR=CthermaldTARdt,

where:

- *Cthermal* is the thermal
  capacity.
- *τ* is the thermal time constant.
- *Rthermal* is the thermal
  resistance.
- *QAB* is the heat flow through
  the material.
- *TAB* is the temperature
  difference between the material layers.
- *QAR* is the heat flow through
  the thermal capacity.
- *TAR* is the temperature drop
  across the thermal capacity.

### Parameterize Cauer Model from Foster Coefficients

The datasheets of semiconductor devices often use Foster coefficients to specify
the thermal model. However, Cauer thermal models are more useful as you can extend
them with additional thermal components such as heatsinks and radiation or
convection elements.

To parameterize the Cauer Thermal Model block from Foster thermal model data,
select the **Parameterize Cauer model using Foster coefficient
data** parameter.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

To specify the initial temperatures of each thermal capacity, set the value of the
**Vector of thermal mass temperatures** variable. The length of
this vector must be equal to the number of Cauer thermal model elements. It
corresponds to the temperature drop across each thermal capacity in the model.
