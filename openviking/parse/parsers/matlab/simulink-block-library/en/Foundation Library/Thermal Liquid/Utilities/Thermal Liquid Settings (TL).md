---
type: simulink-block
title: 'Thermal Liquid Settings (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Utilities'
documentation_page: 'thermalliquidsettingstl'
documentation_source_path: 'ref/thermalliquidsettingstl.html'
language: en
---

# Thermal Liquid Settings (TL)

## Ports
```yaml
ports:
- name: A
  summary: Thermal liquid network connector thermal liquid
  direction: conserving
```

### Conserving

### **A** — Thermal liquid network connector thermal liquid

Port identifying the thermal liquid network to which the specified
fluid properties apply.
## Parameters
```yaml
parameters:
- name: Table dimensions
  summary: Dimensions of the fluid property tables 2D tables based on temperature and pressure (T,p) (default) | 1D vectors
    based on temperature (T)
  group: ''
- name: Temperature vector
  summary: 'Reference temperatures at which to specify the fluid properties [273.1600 : 10 : 373.16]'' K (default) | *M*-element
    column vector with units of temperature'
  group: ''
- name: Pressure vector
  summary: 'Reference pressures at which to specify the fluid properties [0.01, 0.1, 5 : 5 : 50] MPa (default) | *N*-element
    row vector with units of pressure'
  group: ''
- name: Atmospheric pressure
  summary: Absolute pressure of the thermal liquid network environment 0.101325 MPa (default) | scalar with units of pressure
  group: ''
- name: Valid pressure-temperature region parameterization
  summary: Specification method for the pressure-temperature validity region Specified minimum and maximum values (default)
    | Validity matrix
  group: ''
- name: Minimum valid temperature
  summary: Lowest temperature allowed in a model 273.16 K (default) | scalar with units of temperature
  group: ''
- name: Maximum valid temperature
  summary: Highest temperature allowed in a model 373.16 K (default) | scalar with units of temperature
  group: ''
- name: Minimum valid pressure
  summary: Lowest pressure allowed in a model 0.01 MPa (default) | scalar with units of pressure
  group: ''
- name: Maximum valid pressure
  summary: Highest pressure allowed in a model 50 MPa (default) | scalar with units of pressure
  group: ''
- name: Pressure-temperature validity matrix
  summary: Matrix of allowed and disallowed pressure-temperature conditions 11-by-12 matrix of zeros and ones (default) |
    unitless *M*-by-*N* matrix
  group: ''
- name: Pressure and temperature outside valid range
  summary: Whether to notify when pressure or temperature are outside valid range Error (default) | Warning | None
  group: ''
- name: Density parameterization
  summary: Specification method for the fluid density Density, bulk modulus and thermal expansion tables - rho(T,p), beta(T,p),
    alpha(T,p) (default) | Density table - rho(T,p) | Reference density | Density vector - rho(T)
  group: ''
- name: Density table, rho(T,p)
  summary: Matrix of fluid densities at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix
    with units of mass/volume
  group: ''
- name: Density vector, rho(T)
  summary: Vector of fluid densities at the specified temperatures 11-element column vector (default) | *M*-element vector
    with units of mass/volume
  group: ''
- name: Isothermal bulk modulus table, beta(T,p)
  summary: Matrix of isothermal bulk moduli at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N*
    matrix with units of pressure
  group: ''
- name: Isobaric thermal expansion coefficient table, alpha(T,p)
  summary: Matrix of isobaric thermal expansion coefficients at the specified temperatures and pressures 11-by-12 matrix (default)
    | *M*-by-*N* matrix with units of 1/temperature
  group: ''
- name: Reference density
  summary: Density at a known operating condition 998.21 kg/m^3 (default) | scalar with units of mass/volume
  group: ''
- name: Reference temperature
  summary: Temperature at a known operating condition 293.16 K (default) | scalar with units of temperature
  group: ''
- name: Reference pressure
  summary: Pressure at a known operating condition 0.101325 MPa (default) | scalar with units of pressure
  group: ''
- name: Constant isothermal bulk modulus
  summary: Isothermal bulk modulus at a known operating condition 2.1791 GPa (default) | scalar with units of pressure
  group: ''
- name: Constant isobaric thermal expansion coefficient
  summary: Isobaric thermal expansion coefficient at a known operating condition 2.0691e-4 1/K (default) | scalar with units
    of 1/temperature
  group: ''
- name: Internal energy parameterization
  summary: Specification method for the fluid internal energy Specific internal energy and specific heat tables - u(T,p),
    cp(T,p) (default) | Specific internal energy table - u(T,p) | Specific heat table - cp(T,p)
  group: ''
- name: Specific internal energy table, u(T,p)
  summary: Matrix of internal energies at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N*
    matrix with units of energy/mass
  group: ''
- name: Specific internal energy vector, u(T)
  summary: Vector of internal energies at the specified temperatures 11-element vector (default) | *M*-element vector with
    units of energy/mass
  group: ''
- name: Specific heat at constant pressure table, cp(T,p)
  summary: Matrix of specific heats at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix
    with units of energy/(mass\*temperature)
  group: ''
- name: Specific heat at constant pressure vector, u(T)
  summary: Vector of specific heats at the specified temperatures 11-element vector (default) | *M*-element vector with units
    of energy/(mass\*temperature)
  group: ''
- name: Kinematic viscosity table, nu(T,p)
  summary: Matrix of kinematic viscosities at the specified temperatures and pressures 11-element vector (default) | *M*-element
    vector with units of area/time
  group: ''
- name: Thermal conductivity table, K(T,p)
  summary: Matrix of thermal conductivities at the specified temperatures and pressures 11-element vector (default) | *M*-element
    vector with units of power/(length\*temperature)
  group: ''
- name: Kinematic viscosity vector, nu(T)
  summary: Vector of kinematic viscosities at the specified temperatures 11-by-12 matrix (default) | *M*-by-*N* matrix with
    units of area/time
  group: ''
- name: Thermal conductivity vector, K(T)
  summary: Vector of thermal conductivities at the specified temperatures 11-by-12 matrix (default) | *M*-by-*N* matrix with
    units of power/(length\*temperature)
  group: ''
```

#### Temperature and Pressure

### **Table dimensions** — Dimensions of the fluid property tables `2D tables based on temperature and pressure (T,p)` (default) | `1D vectors based on temperature (T)`

Dimensions of the fluid property tables. This parameter determines whether
the fluid properties are variable or constant with pressure. Select
`1D vectors based on temperature (T)` to ignore
the pressure dependences of the fluid properties.

### **Temperature vector** — Reference temperatures at which to specify the fluid properties `[273.1600 : 10 : 373.16]' K` (default) | *M*-element column vector with units of temperature

Vector of temperatures at which to specify the values of the fluid
properties. Each temperature corresponds to a row of a fluid property
table.

### **Pressure vector** — Reference pressures at which to specify the fluid properties `[0.01, 0.1, 5 : 5 : 50] MPa` (default) | *N*-element row vector with units of pressure

Vector of pressures at which to specify the values of the fluid
properties. Each pressure corresponds to a column of a fluid property
table.

#### Dependencies

This parameter is active only when the **Table
dimensions** parameter is set to `2D vectors
based on temperature and pressure (T,p)`.

### **Atmospheric pressure** — Absolute pressure of the thermal liquid network environment `0.101325 MPa` (default) | scalar with units of pressure

Absolute pressure of the outside environment of the attached thermal
liquid network. The default value corresponds to the earth's standard
atmospheric pressure.

### **Valid pressure-temperature region parameterization** — Specification method for the pressure-temperature validity region `Specified minimum and maximum values` (default) | `Validity matrix`

Specification method for the pressure-temperature validity region. You can
specify the limits of a square pressure-temperature region or a matrix of
validity values for an arbitrarily shaped pressure-temperature region.

#### Dependencies

This parameter is active only when the **Table
dimensions** parameter is set to `2D vectors
based on temperature and pressure (T,p)`.

### **Minimum valid temperature** — Lowest temperature allowed in a model `273.16 K` (default) | scalar with units of temperature

Lowest temperature that the attached thermal liquid network is allowed to
reach during simulation.

### **Maximum valid temperature** — Highest temperature allowed in a model `373.16 K` (default) | scalar with units of temperature

Highest temperature that the attached thermal liquid network is allowed to
reach during simulation.

### **Minimum valid pressure** — Lowest pressure allowed in a model `0.01 MPa` (default) | scalar with units of pressure

Lowest pressure that the attached thermal liquid network is allowed to
reach during simulation.

### **Maximum valid pressure** — Highest pressure allowed in a model `50 MPa` (default) | scalar with units of pressure

Highest pressure that the attached thermal liquid network is allowed to
reach during simulation.

### **Pressure-temperature validity matrix** — Matrix of allowed and disallowed pressure-temperature conditions 11-by-12 matrix of zeros and ones (default) | unitless *M*-by-*N* matrix

Matrix of validity values for the various temperature-pressure data
points. A value of `1` denotes a valid point and a value of
`0` denotes an invalid point.

#### Dependencies

This parameter is active only when the **Valid
pressure-temperature region parameterization** parameter is
set to `Validity matrix`.

### **Pressure and temperature outside valid range** — Whether to notify when pressure or temperature are outside valid range `Error` (default) | `Warning` | `None`

Select what happens if the fluid pressure or temperature go beyond the
valid range during simulation:

- `None` ― The block does not return an
  error if the properties go out of range.
- `Warning` ― The block issues a warning,
  but continues the simulation.
- `Error` ― The block returns an error and
  stops the simulation.

#### Density

### **Density parameterization** — Specification method for the fluid density `Density, bulk modulus and thermal expansion tables - rho(T,p), beta(T,p), alpha(T,p)` (default) | `Density table - rho(T,p)` | `Reference density` | `Density vector - rho(T)`

Specification method for the density of the thermal liquid. The density
can be a function of temperature and pressure or as a function of
temperature alone.

### **Density table, rho(T,p)** — Matrix of fluid densities at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of mass/volume

Tabulated density data specified at the temperatures and pressures
provided in the **Temperature and Pressure** section. Each
row corresponds to a different temperature and each column corresponds to a
different pressure.

### **Density vector, rho(T)** — Vector of fluid densities at the specified temperatures 11-element column vector (default) | *M*-element vector with units of mass/volume

Tabulated density data specified at the temperatures provided in the
**Temperature and Pressure** section. Each element
corresponds to a different temperature. The dependence of density on
pressure is ignored.

### **Isothermal bulk modulus table, beta(T,p)** — Matrix of isothermal bulk moduli at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of pressure

Tabulated data for the isothermal bulk modulus at the temperatures and
pressures provided in the **Temperature and Pressure**
section. Each row corresponds to a different temperature and each column
corresponds to a different pressure.

### **Isobaric thermal expansion coefficient table, alpha(T,p)** — Matrix of isobaric thermal expansion coefficients at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of 1/temperature

Tabulated data for the isobaric thermal expansion coefficient at the
temperatures and pressures provided in the **Temperature and
Pressure** section. Each row corresponds to a different
temperature and each column corresponds to a different pressure.

### **Reference density** — Density at a known operating condition `998.21 kg/m^3` (default) | scalar with units of mass/volume

Density of the thermal liquid at a known operating point. The block uses
this data to arrive at an analytical expression for density as a function
pressure and temperature.

### **Reference temperature** — Temperature at a known operating condition `293.16 K` (default) | scalar with units of temperature

Temperature of the thermal liquid at a known operating point. The block
uses this data to arrive at an analytical expression for density as a
function pressure and temperature.

### **Reference pressure** — Pressure at a known operating condition `0.101325 MPa` (default) | scalar with units of pressure

Pressure of the thermal liquid at a known operating point. The block uses
this data to arrive at an analytical expression for density as a function
pressure and temperature.

### **Constant isothermal bulk modulus** — Isothermal bulk modulus at a known operating condition `2.1791 GPa` (default) | scalar with units of pressure

Isothermal bulk modulus of the thermal liquid at a known operating point.
The block uses this data to arrive at an analytical expression for density
as a function pressure and temperature.

### **Constant isobaric thermal expansion coefficient** — Isobaric thermal expansion coefficient at a known operating condition `2.0691e-4 1/K` (default) | scalar with units of 1/temperature

Isobaric thermal expansion coefficient of the thermal liquid at a known
operating point. The block uses this data to arrive at an analytical
expression for density as a function pressure and temperature.

#### Internal Energy

### **Internal energy parameterization** — Specification method for the fluid internal energy `Specific internal energy and specific heat tables - u(T,p), cp(T,p)` (default) | `Specific internal energy table - u(T,p)` | `Specific heat table - cp(T,p)`

Specification method for the internal energy of the thermal liquid. The
internal energy can be a function of temperature and pressure or as a
function of temperature alone. It can also be calculated from specific heat
data that you specify in the place of internal energy.

### **Specific internal energy table, u(T,p)** — Matrix of internal energies at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of energy/mass

Tabulated data for the specific internal energy at the temperatures and
pressures provided in the **Temperature and Pressure**
section. Each row corresponds to a different temperature and each column
corresponds to a different pressure.

### **Specific internal energy vector, u(T)** — Vector of internal energies at the specified temperatures 11-element vector (default) | *M*-element vector with units of energy/mass

Tabulated data for the specific internal energy at the temperatures
provided in the **Temperature and Pressure** section. Each
element corresponds to a different temperature. The dependence of the
specific internal energy on pressure is ignored.

### **Specific heat at constant pressure table, cp(T,p)** — Matrix of specific heats at the specified temperatures and pressures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of energy/(mass\*temperature)

Tabulated data for the specific heat at the temperatures and pressures
provided in the **Temperature and Pressure** section. Each
row corresponds to a different temperature and each column corresponds to a
different pressure.

### **Specific heat at constant pressure vector, u(T)** — Vector of specific heats at the specified temperatures 11-element vector (default) | *M*-element vector with units of energy/(mass\*temperature)

Tabulated data for the specific heat at the temperatures provided in the
**Temperature and Pressure** section. Each row
corresponds to a different temperature. The dependence of the specific heat
on pressure is ignored.

#### Viscosity and Conductivity

### **Kinematic viscosity table, nu(T,p)** — Matrix of kinematic viscosities at the specified temperatures and pressures 11-element vector (default) | *M*-element vector with units of area/time

Tabulated data for the kinematic viscosity at the temperatures and
pressures provided in the **Temperature and Pressure** tab.
Each row corresponds to a different temperature and each column corresponds
to a different pressure.

### **Thermal conductivity table, K(T,p)** — Matrix of thermal conductivities at the specified temperatures and pressures 11-element vector (default) | *M*-element vector with units of power/(length\*temperature)

Tabulated data for the thermal conductivity at the temperatures and
pressures provided in the **Temperature and Pressure**
section. Each row corresponds to a different temperature and each column
corresponds to a different pressure.

### **Kinematic viscosity vector, nu(T)** — Vector of kinematic viscosities at the specified temperatures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of area/time

Tabulated data for the kinematic viscosity at the temperatures provided in
the **Temperature and Pressure** section. Each row
corresponds to a different temperature. The dependence of the kinematic
viscosity on pressure is ignored.

### **Thermal conductivity vector, K(T)** — Vector of thermal conductivities at the specified temperatures 11-by-12 matrix (default) | *M*-by-*N* matrix with units of power/(length\*temperature)

Tabulated data for the thermal conductivity at the temperatures provided
in the **Temperature and Pressure** section. Each row
corresponds to a different temperature. The dependence of the thermal
conductivity on pressure is ignored.
## Libraries

Simscape / Foundation Library / Thermal Liquid / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2025a: Default parameter values adjusted to match the domain

In R2025a, the default parameter values have been adjusted to match the
corresponding values in the domain file:

- **Maximum valid temperature** changed from
  `363.16 K` to `373.16 K`.
- **Minimum valid pressure** changed from `0.05
  MPa` to `0.01 MPa`.

### R2023a: Control block behavior when fluid properties go out of range during simulation

Previously, if fluid properties went beyond the valid range during simulation, the
block would return an error. You can now use the new **Pressure and
temperature outside valid range** parameter to control the block
behavior if fluid properties go out of range during simulation.

## Description

Physical properties of a thermal liquid

The Thermal Liquid Settings (TL) block provides the physical properties
of a fluid to a thermal liquid network. The properties are global: they apply not to one
component but to all those that comprise the network. Every thermal liquid network in a
model must connect to exactly one instance of this block. Among the properties specified
in this block are:

- Thermodynamic properties — Density, specific internal energy, and specific
  heat
- Derivative properties — Bulk modulus and thermal expansion
  coefficient
- Transport properties — Kinematic viscosity and thermal conductivity

Each fluid property is specified in tabulated form against both temperature and
pressure or against temperature alone. Use the option to ignore pressure-induced changes
if those changes are known to be negligible, if pressure is expected to be nearly
constant, or if fluid property data is accessible in terms of temperature only.

### Data Visualization

The block provides the option to plot the specified fluid properties over their
temperature and pressure domains. To create the plots, right-click the block and
select **Foundation Library** > **Plot Fluid Properties**. Use the drop-down list located at the top of the plot to select the
fluid property to visualize. Click the **Reload** button to
regenerate a plot following a block parameter update.

Use the plots to visualize the dependences of the fluid properties on pressure and
temperature—for example, to more easily catch anomalies in the specified data. Most
fluid properties are shown as variable over pressure only if they are specified as
functions of pressure. Exceptions include density, which derives a pressure
dependence from the bulk modulus and thermal expansion coefficient, and any
properties calculated from density, such as specific heat.

**Thermal Liquid Properties Plot**

### Parameterizations

The block provides several parameterizations for the independent state variables,
density, and specific internal energy. The parameterization that you select for each
determines the data that you must obtain and the state variables with respect to
which you must specify it. The setting of the **Table dimensions**
parameter affects which parameters you see in other tabs.

**Pressure and Temperature**

Pressure and temperature are the *across* variables of the
thermal liquid domain. As such, they are the natural choice of independent state
variables against which to specify all other fluid properties. The block
provides two parameterizations based on these state variables. They are
available through the **Table dimensions** parameter:

- `2D tables based on temperature and
  pressure` — Provide tabulated data against both
  temperature and pressure. The region of valid temperatures and
  pressures is specified in terms of minimum and maximum values
  (**I** in the figure) or in terms
  of a validity matrix (**II**).

  **Validity Region Types**
- `1D vectors based on temperature` —
  Provide tabulated data against temperature and ignore any
  dependences on pressure. The region of valid temperatures and
  pressures is specified in terms of minimum and maximum values only.
  The bulk modulus provides a pressure dependence to density and to
  any fluid properties calculated from density.

**Density and Derivatives**

The block provides three types of parameterizations for density and for the
two derivative parameters that the density calculation often depends on—the
isothermal bulk modulus and the isobaric thermal expansion coefficient. Options include:

- `Density, bulk modulus, and thermal expansion
  coefficient tables` — Provide tabulated data for
  density, the bulk modulus, and the thermal expansion coefficient.
  The data must be specified against both temperature and pressure.
  The **Table dimensions** parameter must be set to
  `2D tables based on temperature and
  pressure`.
- `Density table/vector` — Provide
  tabulated data for density against temperature (and, in the 2D case,
  pressure). The block computes the isothermal bulk modulus and
  isobaric thermal expansion coefficient from the tabulated data using
  the finite-difference method. The isothermal bulk modulus
  *β* is defined as:

  1β=1ρ(∂ρ∂p)T,

  where *ρ* is density, *T* is
  temperature, and *p* is pressure. The isobaric
  thermal expansion coefficient *α* is defined
  as:

  α=−1ρ(∂ρ∂T)p.
- `Reference Density` — Provide the
  density, bulk modulus, and thermal expansion coefficient at a known
  temperature (and, in the 2D case, pressure). The block uses an
  analytical expression to calculate the density at other temperatures
  and pressures. The calculation is based on the expression:

  ln(ρρR)=−α(T−TR)+p−pRβ,

  where the subscript R denotes a reference quantity (specified in
  the block dialog box).

**Specific Internal Energy**

As in the case of density, the block provides three types of parameterization
for the specific internal energy and for a related quantity from which it can be
computed—the specific heat. Options include:

- `Specific internal energy and specific heat
  tables` — Provide tabulated data for the specific
  internal energy and the specific heat coefficient. The data must be
  specified against both temperature and pressure. The **Table
  dimensions** parameter must be set to `2D
  tables based on temperature and pressure`.
- `Specific internal energy table/vector` —
  Provide tabulated data for the specific internal energy against
  temperature (and, in the 2D case, pressure). The block computes the
  specific heat coefficient from the specific internal energy data.
  The calculation is based on the expression:

  cp(T,p)=(∂u∂T)p+pαρ,

  where *c*p is the specific
  heat coefficient, and *u* is the specific internal
  energy.
- `Specific heat coefficient table/vector`
  — Provide tabulated data for the specific heat coefficient against
  temperature (and, in the 2D case, pressure). The block computes the
  specific internal energy from the specific heat coefficient data.
  The calculation is based on the expression:

  u(T,p)=∫TRT(cp(T,p)−pα(T,p)ρ(T,p))dT+uR,

  where the subscript R denotes a reference quantity. The value of
  *u*R is set to zero, a
  suitable choice because it is the difference in specific internal
  energy, rather than its value, that is relevant for simulation. The
  value of *u* can differ from that provided in other
  sources, such as the REFPROP fluids database.

### Specific Heat at Constant Volume

Specific heat at constant volume, *c*v,
must be greater than zero. The block derives this quantity from the other fluid
properties:

cv=cp−Tα2βρ.

If you get a warning that specific heat at constant volume must be greater than
zero, this equation can help you understand how to avoid negative
*c*v values by adjusting the fluid
properties that you provide to the block.

You can also use data visualization plots. Right-click the block, select **Foundation Library** > **Plot Fluid Properties**, and then, from the drop-down list at the top of the plot, select
**Specific Heat at Constant Volume (kJ/(K\*kg))**. If
*c*v is negative only in a small
pressure and temperature region of the plot and you are not simulating the model in
that region, you can cut out these pressure and temperature ranges from the fluid
property tables.
