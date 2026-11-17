---
type: simulink-block
title: 'N-Channel IGBT'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'nchanneligbt'
documentation_source_path: 'ref/nchanneligbt.html'
language: en
---

# N-Channel IGBT

## Ports
```yaml
ports:
- name: C
  summary: Collector terminal electrical
  direction: conserving
- name: G
  summary: Gate terminal electrical
  direction: conserving
- name: E
  summary: Emitter terminal electrical
  direction: conserving
- name: H
  summary: Thermal port thermal
  direction: conserving
```

### Conserving

### **C** — Collector terminal electrical

Electrical conserving port associated with the PNP emitter
terminal.

### **G** — Gate terminal electrical

Electrical conserving port associated with the IGBT gate
terminal.

### **E** — Emitter terminal electrical

Electrical conserving port associated with the PNP collector
terminal.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set **Modeling option** to
`Full I-V and capacitance characteristics | Show
thermal port` or `Simplified I-V
characteristics and event-based timing | Show thermal
port`.
## Parameters
```yaml
parameters:
- name: Modeling Option
  summary: IGBT representation Full I-V and capacitance characteristics | No thermal port (default) | Full I-V and capacitance
    characteristics | Show thermal port | Simplified I-V characteristics and event-based timing | No thermal port | Simplified
    I-V characteristics and event-based timing | Show thermal port
  group: ''
- name: I-V characteristics defined by
  summary: IGBT representation Fundamental nonlinear equations (default) | Lookup table (2D, temperature independent) | Lookup
    table (3D, temperature dependent)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Zero gate voltage collector current, Ices
  summary: Zero gate voltage collector current 2 mA (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Voltage at which Ices is defined
  summary: Voltage at which Ices is defined 600 V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Gate-emitter threshold voltage, Vge(th)
  summary: Gate-emitter threshold voltage 6 V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Collector-emitter saturation voltage, Vce(sat)
  summary: Collector-emitter saturation voltage 2.6 V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Collector current at which Vce(sat) is defined
  summary: Collector current at which Vce(sat) is defined 400 A (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Gate-emitter voltage at which Vce(sat) is defined
  summary: Gate-emitter voltage at which Vce(sat) is defined 10 V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Measurement temperature
  summary: Measurement temperature 25 degC (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Vector of gate-emitter voltages, Vge
  summary: Vector of gate-emitter voltages [-1 0 0.5 1 1.5 2 2.5 3 3.5 4] V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Vector of collector-emitter voltages, Vce
  summary: Vector of collector-emitter voltages [-2 6 7 8 10 12 15 20] V (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Tabulated collector currents, Ic(Vge,Vce)
  summary: Tabulated collector currents temperature independent [-1.015e-05, 1.35e-08, .00047135, .0005092, .0005105, .00051175,
    .00051299, .00051423, .00051548, .00051672; -9.9869e-06, 1.35e-08, .00047135, .0005092, .0005105, .00051175, .00051299,
    .00051423, .00051548, .00051672; -9.955e-06, 1.35e-08, .0065225, 3.3324, 48.154, 93.661, 105.52, 105.72, 105.93, 106.14;
    -9.955e-06, 1.35e-08, .0065235, 3.5783, 70.264, 166.33, 252.4, 317.67, 353.38, 357.39; -9.955e-06, 1.35e-08, .006524,
    3.7206, 89.171, 228.09, 371.63, 511.02, 642.69, 764.04; -9.9549e-06, 1.35e-08, .0065242, 3.7716, 97.793, 256.21, 424.27,
    592.92, 759.2, 921.52; -9.9549e-06, 1.35e-08, .0065243, 3.8067, 104.52, 278.11, 464.6, 654.37, 844.57, 1033.9; -9.9549e-06,
    1.35e-08, .0065244, 3.8324, 109.92, 295.67, 496.54, 702.28, 909.96, 1118.3] A (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Vector of temperatures, T
  summary: Vector of temperatures [25 125] degC (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Tabulated collector currents, Ic(Vge,Vce,T)
  summary: Tabulated collector currents temperature dependent zeros(8, 10, 2) A (default)
  group: Main (Full I-V and Capacitance Characteristics)
- name: Parameterization
  summary: Junction capacitance parameterization Specify fixed input, reverse transfer, and output capacitance (default) |
    Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance | Specify tabulated input, reverse transfer,
    and output capacitance | Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Input capacitance, Cies
  summary: Input capacitance 26.4 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Input capacitance, Cies (Vce)
  summary: Input capacitance with tabulated input [80 40 32 28 27.5 27 26.5 26.5 26.5] nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Reverse transfer capacitance, Cres
  summary: Reverse transfer capacitance 2.7 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Reverse transfer capacitance, Cres (Vce)
  summary: Reverse transfer capacitance with tabulated input [55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7] nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Output capacitance, Coes
  summary: Output capacitance 0 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Output capacitance, Coes (Vce)
  summary: Output capacitance with tabulated input [60 20 12 8 6 4.8 4 3.5 3.1] nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Gate-emitter capacitance
  summary: Gate-emitter capacitance 23.7 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Gate-emitter capacitance, Cge(Vge,Vce)
  summary: Gate-emitter capacitance with tabulated values [25 31 26.5 24.9 25 24.9 24.6 24.7 24.8] nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Gate-collector capacitance
  summary: Gate-collector capacitance 2.7 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Gate-collector capacitance, Cgc(Vge,Vce)
  summary: Gate-collector capacitance with tabulated values [55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7] nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Corresponding gate-emitter voltages for tabulated gate capacitance, Vge
  summary: Corresponding collector-emitter voltages 0 V (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Collector-emitter capacitance
  summary: Collector-emitter capacitance 0 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Collector-emitter capacitance, Cce(Vce)
  summary: Collector-emitter capacitance with tabulated values [5 11 6.5 4.9 3.5 2.7 2.1 1.7 1.4] nF (default) | nF
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Corresponding collector-emitter voltages
  summary: Corresponding collector-emitter voltages [0 1 2 5 10 15 20 25 30] V (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Charge-voltage linearity
  summary: Charge-voltage linearity Gate-collector capacitance is constant (default) | Gate-collector charge function is nonlinear
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Gate-collector oxide capacitance
  summary: Gate-collector oxide capacitance 20 nF (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Collector-gate voltage below which oxide capacitance becomes active
  summary: Collector-gate voltage below which oxide capacitance becomes active -5 V (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Total forward transit time
  summary: Total forward transit time 0 us (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Turn-off tail current transit time
  summary: Total forward transit time 0 us (default)
  group: Junction Capacitance (Full I-V and Capacitance Characteristics)
- name: Collector lead resistance
  summary: Collector lead resistance of transistor 0 Ohm (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Emitter lead resistance
  summary: Emitter lead resistance of transistor 0 Ohm (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Gate lead resistance
  summary: Gate lead resistance of transistor 0 Ohm (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Collector lead inductance
  summary: Collector lead inductance of transistor 0 nH (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Emitter lead inductance
  summary: Emitter lead inductance of transistor 0 nH (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Gate lead inductance
  summary: Gate lead inductance of transistor 0 nH (default) | nonnegative scalar
  group: Packaging (Full I-V and Capacitance Characteristics)
- name: Emission coefficient, N
  summary: Emission coefficient 1 (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Forward Early voltage, VAF
  summary: Forward Early voltage 200 V (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Collector resistance, RC
  summary: Collector resistance 0.001 Ohm (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Emitter resistance, RE
  summary: Emitter resistance 0.001Ohm (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Internal gate resistance, RG
  summary: Internal gate resistance 0.001Ohm (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Forward current transfer ratio, BF
  summary: Forward current transfer ratio 50 (default)
  group: Advanced (Full I-V and Capacitance Characteristics)
- name: Parameterization
  summary: Temperature dependence parameterization None — Simulate at parameter measurement temperature (default) | Specify
    Ices and Vce(sat) at second measurement temperature | Specify Vce(sat) at second measurement temperature plus the energy
    gap, EG
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Energy gap, EG
  summary: Energy gap 1.11 eV (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Zero gate voltage collector current, Ices, at second measurement temperature
  summary: Zero gate voltage collector current, Ices, at second measurement temperature 100 mA (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Collector-emitter saturation voltage, Vce(sat), at second measurement temperature
  summary: Collector-emitter saturation voltage, Vce(sat), at second measurement temperature 3 V (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Second measurement temperature
  summary: Second measurement temperature 125 degC (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Saturation current temperature exponent, XTI
  summary: Saturation current temperature exponent 3 (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Mobility temperature exponent, BEX
  summary: Mobility temperature exponent -1.5 (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Internal gate resistance temperature coefficient
  summary: Internal gate resistance temperature coefficient 0 1/K (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Device simulation temperature
  summary: Device simulation temperature 25 degC (default)
  group: Temperature Dependence (Full I-V and Capacitance Characteristics)
- name: Vector of collector currents, Ic
  summary: Vector of collector currents [0, 10, 50, 100, 200, 400, 600] A (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Vector of temperatures, Tj
  summary: Vector of temperatures [298.15, 398.15] K (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Corresponding on-state collector-emitter voltages
  summary: Corresponding on-state collector-emitter voltages [0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7] V (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Collector-emitter on-state voltages, Vce=fcn(Tj,Ic)
  summary: Collector-emitter on-state voltages [0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1.0, 1.15, 1.35, 1.7, 2.35, 3.0] V
    (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Miller resistance
  summary: Miller resistance 0.1 Ohm (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Off-state conductance
  summary: Off-state conductance 1e-5 Ohm (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Gate-emitter threshold voltage, Vge(th)
  summary: Threshold voltage 6 V (default)
  group: Main (Simplified I-V Characteristics and Event-Based Timing)
- name: Vector of temperatures for switching losses, Tj
  summary: Switching losses temperatures [298.15, 398.15] K (default)
  group: Switching Losses (Simplified I-V Characteristics and Event-Based Timing)
- name: Vector of collector currents for switching losses, Ic
  summary: Switching losses collector currents [0, 10, 50, 100, 200, 400, 600] A (default)
  group: Switching Losses (Simplified I-V Characteristics and Event-Based Timing)
- name: Turn-on switching losses, Eon=fcn(Tj,Ic)
  summary: Turn-on switching losses [0, 0.2, 1, 2, 4, 8, 15; 0, 0.3, 1.3, 2.5, 5, 11, 18]*1e-3 J (default)
  group: Switching Losses (Simplified I-V Characteristics and Event-Based Timing)
- name: Turn-off switching losses, Eoff=fcn(Tj,Ic)
  summary: Turn-off switching losses [0, 0.3, 1.5, 3, 6, 15, 25; 0, 0.7, 3.3, 6.5, 13, 25, 35]*1e-3 J (default)
  group: Switching Losses (Simplified I-V Characteristics and Event-Based Timing)
- name: Turn-on delay
  summary: Turn-on delay 0.07 us (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
- name: Current rise time
  summary: Current rise time 0.7 us (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
- name: Turn-off delay
  summary: Turn-off delay 0.2 us (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
- name: Current fall time
  summary: Current fall time 0.5 us (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
- name: Off-state voltage for rise and fall times
  summary: Off-state voltage for rise and fall times 300 V (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
- name: Off-state voltage for rise and fall times
  summary: Off-state voltage for rise and fall times 300 V (default)
  group: Dynamics (Simplified I-V Characteristics and Event-Based Timing)
```

### **Modeling Option** — IGBT representation `Full I-V and capacitance characteristics | No thermal port` (default) | `Full I-V and capacitance characteristics | Show thermal port` | `Simplified I-V characteristics and event-based timing | No thermal port` | `Simplified I-V characteristics and event-based timing | Show thermal port`

Select the IGBT representation:

- `Full I-V and capacitance characteristics | No
  thermal port` — Detailed model that does
  not simulate the effects of generated heat and device
  temperature. This is the default.
- `Full I-V and capacitance characteristics | Show
  thermal port` — Detailed model with
  exposed thermal port.
- `Simplified I-V characteristics and event-based
  timing | No thermal port` — Simplified
  event-based model, which also does not simulate the effects of
  generated heat and device temperature.
- `Simplified I-V characteristics and event-based
  timing | Show thermal port` — Simplified
  event-based model with exposed thermal port.

### Main (Full I-V and Capacitance Characteristics)

This configuration of the **Main** setting corresponds to the
detailed block modeling option, which is the default. If you are using the
simplified, event-based modeling option of the block, see Main (Simplified I-V Characteristics and Event-Based Timing).

### **I-V characteristics defined by** — IGBT representation `Fundamental nonlinear equations` (default) | `Lookup table (2D, temperature independent)` | `Lookup table (3D, temperature dependent)`

Select the IGBT representation:

- `Fundamental nonlinear equations`
  — Use an equivalent circuit based on a PNP bipolar
  transistor and N-channel MOSFET. This is the default.
- `Lookup table (2D, temperature
  independent)` — Use 2-D table lookup
  for collector current as a function of gate-emitter voltage
  and collector-emitter voltage.
- `Lookup table (3D, temperature
  dependent)` — Use 3-D table lookup
  for collector current as a function of gate-emitter voltage,
  collector-emitter voltage, and temperature.

### **Zero gate voltage collector current, Ices** — Zero gate voltage collector current `2` `mA` (default)

Collector current that flows when the gate-emitter voltage is set to
zero, and a large collector-emitter voltage is applied, that is, the
device is in the off-state. The value of the large collector-emitter
voltage is defined by the parameter **Voltage at which Ices is
defined**.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Voltage at which Ices is defined** — Voltage at which Ices is defined `600` `V` (default)

Voltage used when measuring the **Zero gate voltage collector
current, Ices**.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Gate-emitter threshold voltage, Vge(th)** — Gate-emitter threshold voltage `6` `V` (default)

Threshold voltage used in the MOSFET equations.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Collector-emitter saturation voltage, Vce(sat)** — Collector-emitter saturation voltage `2.6` `V` (default)

Collector-emitter voltage for a typical on-state as specified by the
manufacturer.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Collector current at which Vce(sat) is defined** — Collector current at which Vce(sat) is defined `400` `A` (default)

Collector-emitter current when the gate-emitter voltage is
*V*ge(sat) and
collector-emitter voltage is
*V*ce(sat).

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Gate-emitter voltage at which Vce(sat) is defined** — Gate-emitter voltage at which Vce(sat) is defined `10` `V` (default)

Gate voltage used when measuring
*V*ce(sat) and
*I*ce(sat).

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Measurement temperature** — Measurement temperature `25` `degC` (default)

Temperature for which the parameters are quoted
(*T*m1).

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Fundamental nonlinear
equations`.

### **Vector of gate-emitter voltages, Vge** — Vector of gate-emitter voltages `[-1 0 0.5 1 1.5 2 2.5 3 3.5 4]` `V` (default)

Vector of gate-emitter voltages, to be used for table lookup. The
vector values must be strictly increasing. The values can be
nonuniformly spaced.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to either `Lookup table (2D,
temperature independent)` or `Lookup
table (3D, temperature dependent)`.

### **Vector of collector-emitter voltages, Vce** — Vector of collector-emitter voltages `[-2 6 7 8 10 12 15 20]` `V` (default)

Vector of collector-emitter voltages, to be used for table lookup. The
vector values must be strictly increasing. The values can be
nonuniformly spaced.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to either `Lookup table (2D,
temperature independent)` or `Lookup
table (3D, temperature dependent)`.

### **Tabulated collector currents, Ic(Vge,Vce)** — Tabulated collector currents temperature independent `[-1.015e-05, 1.35e-08, .00047135, .0005092, .0005105, .00051175, .00051299, .00051423, .00051548, .00051672; -9.9869e-06, 1.35e-08, .00047135, .0005092, .0005105, .00051175, .00051299, .00051423, .00051548, .00051672; -9.955e-06, 1.35e-08, .0065225, 3.3324, 48.154, 93.661, 105.52, 105.72, 105.93, 106.14; -9.955e-06, 1.35e-08, .0065235, 3.5783, 70.264, 166.33, 252.4, 317.67, 353.38, 357.39; -9.955e-06, 1.35e-08, .006524, 3.7206, 89.171, 228.09, 371.63, 511.02, 642.69, 764.04; -9.9549e-06, 1.35e-08, .0065242, 3.7716, 97.793, 256.21, 424.27, 592.92, 759.2, 921.52; -9.9549e-06, 1.35e-08, .0065243, 3.8067, 104.52, 278.11, 464.6, 654.37, 844.57, 1033.9; -9.9549e-06, 1.35e-08, .0065244, 3.8324, 109.92, 295.67, 496.54, 702.28, 909.96, 1118.3]` `A` (default)

Tabulated values for collector current as a function of gate-emitter
voltage and collector-emitter voltage, to be used for 2-D table lookup.
Each value in the matrix specifies the collector current for a specific
combination of gate-emitter voltage and collector-emitter voltage. The
matrix size must match the dimensions defined by the gate-emitter
voltage and collector-emitter voltage vectors. The default values, in A,
are:

```
[-1.015e-5 1.35e-8 4.7135e-4 5.092e-4 5.105e-4 5.1175e-4 5.1299e-4 5.1423e-4 5.1548e-4 5.1672e-4;
 -9.9869e-6 1.35e-8 4.7135e-4 5.092e-4 5.105e-4 5.1175e-4 5.1299e-4 5.1423e-4 5.1548e-4 5.1672e-4;
 -9.955e-6 1.35e-8 0.0065225 3.3324 48.154 93.661 105.52 105.72 105.93 106.14;
 -9.955e-6 1.35e-8 0.0065235 3.5783 70.264 166.33 252.4 317.67 353.38 357.39;
 -9.955e-6 1.35e-8 0.006524 3.7206 89.171 228.09 371.63 511.02 642.69 764.04;
 -9.9549e-6 1.35e-8 0.0065242 3.7716 97.793 256.21 424.27 592.92 759.2 921.52;
 -9.9549e-6 1.35e-8 0.0065243 3.8067 104.52 278.11 464.6 654.37 844.57 1.0339e+3;
 -9.9549e-6 1.35e-8 0.0065244 3.8324 109.92 295.67 496.54 702.28 909.96 1.1183e+3]
```

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Lookup table (2D,
temperature independent)`.

### **Vector of temperatures, T** — Vector of temperatures `[25 125]` `degC` (default)

Vector of temperatures, to be used for table lookup. The vector values
must be strictly increasing. The values can be nonuniformly
spaced.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Lookup table (3D,
temperature dependent)`.

### **Tabulated collector currents, Ic(Vge,Vce,T)** — Tabulated collector currents temperature dependent `zeros(8, 10, 2)` `A` (default)

Tabulated values for collector current as a function of gate-emitter
voltage, collector-emitter voltage, and temperature, to be used for 3-D
table lookup. Each value in the matrix specifies the collector current
for a specific combination of gate-emitter voltage and collector-emitter
voltage at a specific temperature. The matrix size must match the
dimensions defined by the gate-emitter voltage, collector-emitter
voltage, and temperature vectors.

#### Dependencies

To enable this parameter, set **I-V characteristics
defined by** to `Lookup table (3D,
temperature dependent)`.

### Junction Capacitance (Full I-V and Capacitance Characteristics)

### **Parameterization** — Junction capacitance parameterization `Specify fixed input, reverse transfer, and output capacitance` (default) | `Specify fixed gate-emitter, gate-collector, and collector-emitter capacitance` | `Specify tabulated input, reverse transfer, and output capacitance` | `Specify tabulated gate-emitter, gate-collector, and collector-emitter capacitance`

Select one of the following methods for block parameterization:

- `Specify fixed input, reverse transfer, and
  output capacitance` — Provide fixed
  parameter values from datasheet and let the block convert
  the input, output, and reverse transfer capacitance values
  to junction capacitance values, as described in Charge Model. This is
  the default method.
- `Specify fixed gate-emitter, gate-collector,
  and collector-emitter capacitance` —
  Provide fixed values for junction capacitance parameters
  directly.
- `Specify tabulated input, reverse transfer,
  and output capacitance` — Provide
  tabulated capacitance and collector-emitter voltage values
  based on datasheet plots. The block converts the input,
  output, and reverse transfer capacitance values to junction
  capacitance values, as described in Charge Model.
- `Specify tabulated gate-emitter,
  gate-collector, and collector-emitter
  capacitance` — Provide tabulated
  values for junction capacitances and collector-emitter
  voltage.

### **Input capacitance, Cies** — Input capacitance `26.4` `nF` (default)

Gate-emitter capacitance with the collector shorted to the
emitter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed input, reverse transfer, and output
capacitance`.

### **Input capacitance, Cies (Vce)** — Input capacitance with tabulated input `[80 40 32 28 27.5 27 26.5 26.5 26.5]` `nF` (default)

Gate-emitter capacitance with the collector shorted to the emitter,
tabulated with the collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated input, reverse transfer, and output
capacitance`.

### **Reverse transfer capacitance, Cres** — Reverse transfer capacitance `2.7` `nF` (default)

Collector-gate capacitance with the emitter connected to
ground.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed input, reverse transfer, and output
capacitance`.

### **Reverse transfer capacitance, Cres (Vce)** — Reverse transfer capacitance with tabulated input `[55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7]` `nF` (default)

Collector-gate capacitance with the emitter connected to ground,
tabuled with the collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated input, reverse transfer, and output
capacitance`.

### **Output capacitance, Coes** — Output capacitance `0` `nF` (default)

Collector-emitter capacitance with the gate and emitter
shorted.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed input, reverse transfer, and output
capacitance`.

### **Output capacitance, Coes (Vce)** — Output capacitance with tabulated input `[60 20 12 8 6 4.8 4 3.5 3.1]` `nF` (default)

Collector-emitter capacitance with the gate and emitter shorted,
tabulated with collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated input, reverse transfer, and output
capacitance`.

### **Gate-emitter capacitance** — Gate-emitter capacitance `23.7` `nF` (default)

Capacitance placed between the gate and the emitter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Gate-emitter capacitance, Cge(Vge,Vce)** — Gate-emitter capacitance with tabulated values `[25 31 26.5 24.9 25 24.9 24.6 24.7 24.8]` `nF` (default)

Capacitance placed between the gate and the emitter, tabulated with
gate-emitter voltage and collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Gate-collector capacitance** — Gate-collector capacitance `2.7` `nF` (default)

Capacitance placed between the gate and the collector.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Gate-collector capacitance, Cgc(Vge,Vce)** — Gate-collector capacitance with tabulated values `[55 9 5.5 3.1 2.5 2.1 1.9 1.8 1.7]` `nF` (default)

Capacitance placed between the gate and the collector, tabulated with
the gate-emitter voltage and the collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Corresponding gate-emitter voltages for tabulated gate capacitance, Vge** — Corresponding collector-emitter voltages `0` `V` (default)

Gate-emitter voltages corresponding to the tabulated gate capacitance
values.

If this value is a scalar, then **Gate-emitter capacitance,
Cge(Vge,Vce)** and **Gate-collector capacitance,
Cgc(Vge,Vce)** are vectors of scalars. If this value is a
vector, then **Gate-emitter capacitance, Cge(Vge,Vce)**
and **Gate-collector capacitance, Cgc(Vge,Vce)** are
matrices of scalars.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Collector-emitter capacitance** — Collector-emitter capacitance `0` `nF` (default)

Capacitance placed between the collector and the emitter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
fixed gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Collector-emitter capacitance, Cce(Vce)** — Collector-emitter capacitance with tabulated values `[5 11 6.5 4.9 3.5 2.7 2.1 1.7 1.4]` `nF` (default) | `nF`

Capacitance placed between the collector and the emitter, tabulated
with the collector-emitter voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Corresponding collector-emitter voltages** — Corresponding collector-emitter voltages `[0 1 2 5 10 15 20 25 30]` `V` (default)

Collector-emitter voltages corresponding to the tabulated capacitance
values.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
tabulated input, reverse transfer, and output
capacitance` or `Specify tabulated
gate-emitter, gate-collector, and collector-emitter
capacitance`.

### **Charge-voltage linearity** — Charge-voltage linearity `Gate-collector capacitance is constant` (default) | `Gate-collector charge function is nonlinear`

Whether the gate-drain capacitance is fixed or nonlinear:

- `Gate-collector capacitance is
  constant` — The capacitance value is
  constant and defined according to the selected
  parameterization option, either directly or derived from a
  datasheet. This is the default method.
- `Gate-collector charge function is
  nonlinear` — The gate-collector
  charge relationship is defined according to the
  piecewise-nonlinear function described in Charge Model. Two
  additional parameters appear to let you define the
  gate-collector charge function.

#### Dependencies

To enable this parameter, set
**Parameterization** to his
`Specify fixed input, reverse transfer and output
capacitance` or `Specify fixed
gate-emitter, gate-collector and output
capacitance`.

### **Gate-collector oxide capacitance** — Gate-collector oxide capacitance `20` `nF` (default)

Gate-collector capacitance when the device is on and the
collector-gate voltage is small.

#### Dependencies

To enable this parameter, set **Charge-voltage
linearity** to `Gate-collector charge
function is nonlinear`.

### **Collector-gate voltage below which oxide capacitance becomes active** — Collector-gate voltage below which oxide capacitance becomes active `-5` `V` (default)

Collector-gate voltage at which the collector-gate capacitance
switches between off-state
(*C*GC) and on-state
(*C*ox) capacitance
values.

#### Dependencies

To enable this parameter, set **Charge-voltage
linearity** to `Gate-collector charge
function is nonlinear`.

### **Total forward transit time** — Total forward transit time `0` `us` (default)

Forward transit time for the PNP transistor used as part of the
underlying IGBT model. It affects how quickly charge is removed from the
channel when the IGBT is turned off.

#### Dependencies

To enable this parameter, in the **Main**
settings, set **I-V characteristics defined by** to
`Fundamental nonlinear
equations`.

### **Turn-off tail current transit time** — Total forward transit time `0` `us` (default)

Turn-off transit time for the tail current.

#### Dependencies

To enable this parameter, in the **Main**
settings, set **I-V characteristics defined by** to
`Lookup table (2D, temperature
independent)` or `Lookup table (3D,
temperature dependent)`.

### Packaging (Full I-V and Capacitance Characteristics)

### **Collector lead resistance** — Collector lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Collector lead resistance of the transistor, that is, the series lead
resistance associated with the collector contact. Use this parameter to
model parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### **Emitter lead resistance** — Emitter lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Emitter lead resistance of the transistor, that is, the series lead
resistance associated with the emitter contact. Use this parameter to
model parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### **Gate lead resistance** — Gate lead resistance of transistor `0` `Ohm` (default) | nonnegative scalar

*Since R2024b*

Gate lead resistance of the transistor, that is, the series lead
resistance associated with the gate contact. Use this parameter to model
parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### **Collector lead inductance** — Collector lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Collector lead inductance of the transistor, that is, the series lead
inductance associated with the collector contact. Use this parameter to
model parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### **Emitter lead inductance** — Emitter lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Emitter lead inductance of the transistor, that is, the series lead
inductance associated with the emitter contact. Use this parameter to
model parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### **Gate lead inductance** — Gate lead inductance of transistor `0` `nH` (default) | nonnegative scalar

*Since R2024b*

Gate lead inductance of the transistor, that is, the series lead
inductance associated with the gate contact. Use this parameter to model
parasitic effects in the transistor.

#### Dependencies

To enable this parameter, set **Modeling option**
to `Full I-V and capacitance characteristics | No
thermal port` or `Full I-V and
capacitance characteristics | Show thermal
port`.

### Advanced (Full I-V and Capacitance Characteristics)

The lookup table representation combines all the equivalent circuit components
into one lookup table, and therefore this setting is empty. If you use the
equivalent circuit representation, this setting has the following parameters.

### **Emission coefficient, N** — Emission coefficient `1` (default)

Emission coefficient or ideality factor of the bipolar
transistor.

### **Forward Early voltage, VAF** — Forward Early voltage `200` `V` (default)

Forward Early voltage for the PNP transistor used in the IGBT model.
For more information, see the PNP Bipolar Transistor block
reference page.

### **Collector resistance, RC** — Collector resistance `0.001` `Ohm` (default)

Resistance at the collector.

### **Emitter resistance, RE** — Emitter resistance `0.001``Ohm` (default)

Resistance at the emitter.

### **Internal gate resistance, RG** — Internal gate resistance `0.001``Ohm` (default)

Resistance of the internal gate resistor at the measurement
temperature. This is not the value of the external circuit series gate
resistance, which you should model externally to the IGBT.

### **Forward current transfer ratio, BF** — Forward current transfer ratio `50` (default)

Ideal maximum forward current gain for the PNP transistor used in the
IGBT model. See the PNP Bipolar
Transistor block reference page for more
information.

### Temperature Dependence (Full I-V and Capacitance Characteristics)

For the 2-D lookup table representation, the electrical equations do not depend on
temperature and therefore this setting is empty. For the 3-D lookup table
representation with exposed thermal port, this setting is also empty because the 3-D
matrix on the **Main** setting captures the temperature
dependence. If the block thermal port is not exposed for the 3-D lookup table
representation, then this setting contains only the **Device
simulation temperature** parameter. If you use the equivalent circuit
representation, this setting has the following parameters.

### **Parameterization** — Temperature dependence parameterization `None — Simulate at parameter measurement temperature` (default) | `Specify Ices and Vce(sat) at second measurement temperature` | `Specify Vce(sat) at second measurement temperature plus the energy gap, EG`

Select one of the following methods for temperature dependence parameterization:

- `None — Simulate at parameter
  measurement temperature` —
  Temperature dependence is not modeled, and none of the other
  parameters on this setting are visible. This is the default
  method.
- `Specify Ices and Vce(sat) at second
  measurement temperature` — Model
  temperature-dependent effects by providing values for the
  zero gate voltage collector current,
  *Ices*, and collector-emitter voltage,
  *V*ce(sat), at
  the second measurement temperature.
- `Specify Vce(sat) at second measurement
  temperature plus the energy gap, EG`
  — Use this option when the datasheet does not provide
  information on the zero gate voltage collector current,
  *Ices*, at a higher measurement
  temperature.

### **Energy gap, EG** — Energy gap `1.11` `eV` (default)

Energy gap value.

#### Dependencies

To enable this parameter, in the **Temperature
Dependence** setting, set
**Parameterization** to `Specify
Vce(sat) at second measurement temperature plus the energy gap,
EG`.

### **Zero gate voltage collector current, Ices, at second measurement temperature** — Zero gate voltage collector current, Ices, at second measurement temperature `100` `mA` (default)

Zero gate collector current value at the second measurement
temperature.

#### Dependencies

To enable this parameter, in the **Temperature
Dependence** setting, set
**Parameterization** to `Specify
Ices and Vce(sat) at second measurement
temperature`.

### **Collector-emitter saturation voltage, Vce(sat), at second measurement temperature** — Collector-emitter saturation voltage, Vce(sat), at second measurement temperature `3` `V` (default)

Collector-emitter saturation voltage value at the second measurement
temperature, and when the collector current and gate-emitter voltage are
as defined by the corresponding parameters on the
**Main** setting.

### **Second measurement temperature** — Second measurement temperature `125` `degC` (default)

Second temperature *T*m2 at
which **Zero gate voltage collector current, Ices, at second
measurement temperature** and **Collector-emitter
saturation voltage, Vce(sat), at second measurement
temperature** are measured.

### **Saturation current temperature exponent, XTI** — Saturation current temperature exponent `3` (default)

Saturation current exponent value for your device type. If you have
graphical data for the value of *Ices* as a function of
temperature, you can use it to fine-tune the value of
*XTI*.

### **Mobility temperature exponent, BEX** — Mobility temperature exponent `-1.5` (default)

Mobility temperature coefficient value. You can use the default value
for most devices. If you have graphical data for
*Vce(sat)* at different
temperatures, you can use it to fine-tune the value of
*BEX*.

### **Internal gate resistance temperature coefficient** — Internal gate resistance temperature coefficient `0` `1/K` (default)

Represents the fractional rate of change (*α*) of
internal gate resistance (RG) with temperature. Thus the gate resistance
is *R* =
*R*meas(1 +
*α*
(*T*s –
Tm1 )), where *R*meas
is the **Internal gate resistance, RG** parameter
value.

### **Device simulation temperature** — Device simulation temperature `25` `degC` (default)

Temperature *T*s at which the
device is simulated.

### Main (Simplified I-V Characteristics and Event-Based Timing)

This configuration of the **Main** setting
corresponds to the simplified, event-based block modeling option. If you are using
the detailed modeling option of the block, see Main (Full I-V and Capacitance Characteristics).

### **Vector of collector currents, Ic** — Vector of collector currents `[0, 10, 50, 100, 200, 400, 600]` `A` (default)

Collector currents for which the on-state collector-emitter voltages
are defined. The first element must be zero.

To model multiple N-Channel IGBT blocks in parallel, use a single
N-Channel IGBT block and multiply the value of the this parameter by the
number of IGBT devices that you wanted to model in parallel.

### **Vector of temperatures, Tj** — Vector of temperatures `[298.15, 398.15]` `K` (default)

Temperature values at which the collector-emitter and turn-on/turn-off
losses are quoted.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### **Corresponding on-state collector-emitter voltages** — Corresponding on-state collector-emitter voltages `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7]` `V` (default)

Collector-emitter voltages corresponding to the vector of collector
currents. The first element must be zero.

#### Dependencies

To enable this parameter, set **Modeling
option** to `Simplified I-V characteristics
and event-based timing | No thermal port`.

### **Collector-emitter on-state voltages, Vce=fcn(Tj,Ic)** — Collector-emitter on-state voltages `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1.0, 1.15, 1.35, 1.7, 2.35, 3.0]` `V` (default)

Collector-emitter voltages when in the on state, defined as a function
of both temperature and current.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### **Miller resistance** — Miller resistance `0.1` `Ohm` (default)

When the device turns on, it has a constant-value Miller resistance in
series with the demanded voltage ramp. This resistance represents the
partial conductance path through the device during turn on, and can be
used to match the voltage spike observed when reconnecting a
current-carrying inductor and corresponding freewheeling diode. A
typical value is 10 to 50 times the effective on-state
resistance.

### **Off-state conductance** — Off-state conductance `1e-5` `Ohm` (default)

Conductance when the device is in the off state.

### **Gate-emitter threshold voltage, Vge(th)** — Threshold voltage `6` `V` (default)

Gate-emitter voltage must be greater than this value for the device to
turn on.

### Switching Losses (Simplified I-V Characteristics and Event-Based Timing)

### **Vector of temperatures for switching losses, Tj** — Switching losses temperatures `[298.15, 398.15]` `K` (default)

Temperatures at which switching losses are tabulated.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### **Vector of collector currents for switching losses, Ic** — Switching losses collector currents `[0, 10, 50, 100, 200, 400, 600]` `A` (default)

Collector currents at which switching losses are tabulated.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### **Turn-on switching losses, Eon=fcn(Tj,Ic)** — Turn-on switching losses `[0, 0.2, 1, 2, 4, 8, 15; 0, 0.3, 1.3, 2.5, 5, 11, 18]*1e-3` `J` (default)

Energy loss when turning the device on, defined as a function of
temperature and final on-state current.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### **Turn-off switching losses, Eoff=fcn(Tj,Ic)** — Turn-off switching losses `[0, 0.3, 1.5, 3, 6, 15, 25; 0, 0.7, 3.3, 6.5, 13, 25, 35]*1e-3` `J` (default)

Energy loss when turning the device off, defined as a function of
temperature and final on-state current.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.

### Dynamics (Simplified I-V Characteristics and Event-Based Timing)

### **Turn-on delay** — Turn-on delay `0.07` `us` (default)

Time before which the device starts to ramp on.

### **Current rise time** — Current rise time `0.7` `us` (default)

Time taken for the current to ramp up when driving a resistive
load.

### **Turn-off delay** — Turn-off delay `0.2` `us` (default)

Time before which the device starts to ramp off.

### **Current fall time** — Current fall time `0.5` `us` (default)

Time taken for the current to ramp down when driving a resistive
load.

### **Off-state voltage for rise and fall times** — Off-state voltage for rise and fall times `300` `V` (default)

Off-state collector-emitter voltage used when specifying the rise and
fall times. The default value is `300` V.

#### Dependencies

To enable this parameter, set **Modeling
option** to `Simplified I-V characteristics
and event-based timing | No thermal port`.

### **Off-state voltage for rise and fall times** — Off-state voltage for rise and fall times `300` `V` (default)

Off-state collector-emitter voltage used when specifying the rise
times, fall times, and the losses data.

#### Dependencies

To enable this parameter, expose the thermal port by setting
**Modeling option** to `Simplified
I-V characteristics and event-based timing | Show thermal
port`.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

### R2024b: Model the parasitic lead resistances and inductances in each transistor terminal

You can now model parasitic effects in each terminal of the N-Channel IGBT block by
specifying lead resistances and inductances using these parameters:

- **Collector lead resistance**
- **Emitter lead resistance**
- **Gate lead resistance**
- **Collector lead inductance**
- **Emitter lead inductance**
- **Gate lead inductance**

## Description

N-Channel insulated gate bipolar transistor

The N-Channel IGBT block models an Insulated Gate
Bipolar Transistor (IGBT). The block provides two main modeling options, by setting the
**Modeling option** parameter to either:

- **Full I-V and capacitance characteristics**
  — This modeling option is a detailed component model suitable for
  simulating detailed switching characteristics and predicting component
  losses. This modeling option, in turn, provides two ways of modeling an
  IGBT:

  - As an equivalent circuit based on a PNP bipolar transistor and
    N-channel MOSFET. For more information on using this model, see
    Representation by Equivalent Circuit, Fine-Tuning the Current-Voltage Characteristics, and
    Modeling Temperature Dependence.
  - By a 2-D lookup table approximation to the I-V (current-voltage)
    curve. For details, see Representation by 2-D Lookup Table.
  - By a 3-D lookup table approximation to the I-V (current-voltage)
    curve that includes temperature data. For details, see Representation by 3-D Lookup Table.

  The gate capacitance in the detailed model is represented as a fixed
  gate-emitter capacitance *CGE* and
  either a fixed or a nonlinear gate-collector capacitance
  *C*GC. For details, see Charge Model.
- **Simplified I-V characteristics and event-based
  timing** — This modeling option models the IGBT more
  simply by using just the on-state I-V data as a function of the
  collector-emitter voltage. In the off state (gate-emitter voltage less than
  **Threshold voltage, Vth**), the IGBT is modeled by a
  constant **Off-state conductance**. This simplified model
  is suitable when approximate dynamic characteristics are sufficient, and
  simulation speed is of paramount importance. For details, see Event-Based IGBT Modeling Option.

Together with the thermal port modeling options (see Thermal Port), the block therefore provides you with four choices. To
select the desired modeling option, set the **Modeling option**
parameter to either:

- `Full I-V and capacitance characteristics | No thermal
  port` — Detailed model that does not simulate the
  effects of generated heat and device temperature. This is the default.
- `Full I-V and capacitance characteristics | Show thermal
  port` — Detailed model with exposed thermal port.
- `Simplified I-V characteristics and event-based timing | No
  thermal port` — Simplified event-based model, which also
  does not simulate the effects of generated heat and device temperature.
- `Simplified I-V characteristics and event-based timing | Show
  thermal port` — Simplified event-based model with
  exposed thermal port.

### Representation by Equivalent Circuit

The equivalent circuit of the detailed block modeling option consists of a PNP
Bipolar Transistor block driven by an N-Channel MOSFET block, as shown in the
following figure:

The MOSFET source is connected to the bipolar transistor collector, and the MOSFET
drain is connected to the bipolar transistor base. The MOSFET uses the
threshold-based equations shown in the N-Channel MOSFET block reference page. The bipolar transistor uses the
equations shown in the PNP Bipolar Transistor block reference
page, but with the addition of an emission coefficient parameter
*N* that scales *kT/q*.

The N-Channel IGBT block uses the on and off characteristics you
specify in the block dialog box to estimate the parameter values for the underlying
N-Channel MOSFET and PNP bipolar transistor.

The block uses the off characteristics to calculate the base-emitter voltage,
*Vbe*, and the saturation current,
*IS*.

When the transistor is off, the gate-emitter voltage is zero and the IGBT
base-collector voltage is large, so the PNP base and collector current equations
simplify to:

Ib=0=−Is[1βF(e−qVbe/(NkT)−1)−1βR]Ic=−Is[e−qVbe/(NkT)(1+VbcVAF)+1βR]

where *N* is the **Emission coefficient, N**
parameter value, *VAF* is the forward Early
voltage, and *Ic* and
*Ib* are defined as positive flowing
into the collector and base, respectively. See the PNP Bipolar Transistor reference page for definitions of the remaining
variables. The first equation can be solved for
*Vbe*.

The base current is zero in the off-condition, and hence
*Ic* =
–*Ices*, where
*Ices* is the Zero gate voltage
collector current. The base-collector voltage,
*Vbc*, is given by
*Vbc* =
*Vces* +
*Vces*, where
*Vces* is the voltage at which
*Ices* is measured. Hence we can
rewrite the second equation as follows:

Ices=Is[e−qVbe/(NkT)(1+Vces+VbeVAF)+1βR]

The block sets *βR* and
*βF* to typical values of 1 and 50,
so these two equations can be used to solve for
*Vbe* and
*IS*:

Vbe=−NkTqlog(1+βFβR)Is=Ice−qVbe/(NkT)+1βR

**Note**

The block does not require an exact value for
*βF* because it can adjust the
MOSFET gain *K* to ensure the overall device gain is
correct.

The block parameters **Collector-emitter saturation voltage,
Vce(sat)** and **Collector current at which Vce(sat) is
defined** are used to determine
*Vbe(sat)* by solving the following
equation:

Ice(sat)=Is[e−qVbe(sat)/(NkT)(1+Vce(sat)+Vbe(sat)VAF)+1βR]

Given this value, the block calculates the MOSFET gain, *K*,
using the following equation:

Itf=TFdIcdtIds=Ib−Itf=K[(VGE(sat)−Vth)Vds−Vds22]

where *Vth* is the **Gate-emitter
threshold voltage, Vge(th)** parameter value,
*VGE(sat)* is the
**Gate-emitter voltage at which Vce(sat) is defined** parameter
value, and *TF* is the **Total forward transit
time** parameter value.

*Vds* is related to the transistor
voltages as *Vds* =
*Vce* –
*Vbe*. The block substitutes this
relationship for *Vds*, sets the
base-emitter voltage and base current to their saturated values, and rearranges the
MOSFET equation to give

K=Ib(sat)[(VGE(sat)−Vth)(Vbe(sat)+Vce(sat))−(Vbe(sat)+Vce(sat))22]

where *Vce(sat)* is the
**Collector-emitter saturation voltage, Vce(sat)** parameter
value.

These calculations ensure the zero gate voltage collector current and
collector-emitter saturation voltage are exactly met at these two specified
conditions. However, the current-voltage plots are very sensitive to the emission
coefficient *N* and the precise value of
*Vth*. If the manufacturer datasheet
gives current-voltage plots for different
*VGE* values, then the
*N* and *Vth* can be
tuned by hand to improve the match.

### Representation by 2-D Lookup Table

For the lookup table representation of the detailed block modeling option, you
provide tabulated values for collector current as a function of gate-emitter voltage
and collector-emitter voltage. The main advantage of using this option is simulation
speed. It also lets you parameterize the device from either measured data or from
data obtained from another simulation environment. To generate your own data from
the equivalent circuit representation, you can use a test harness, such as shown in
the IGBT Characteristics example.

The lookup table representation combines all of the equivalent circuit components
(PNP transistor, N-channel MOSFET, collector resistor and emitter resistor) into one
equivalent lookup table.

**Note**

To ensure that the signs of the collector-emitter current and
collector-emitter voltage are consistent:

- If the collector-emitter voltage is equal to `0`,
  the value of the **Tabulated collector currents,
  Ic(Vge,Vce)** parameter must be equal to
  `0`.
- The tabulated power, which is the product of the
  **Tabulated collector currents, Ic(Vge,Vce)**
  parameter and the collector-emitter voltage, must be greater than or
  equal to `0`.
- The tabulated conductance, which is the gradient of the
  **Tabulated collector currents, Ic(Vge,Vce)**
  parameter with respect to the collector-emitter voltage
  *Vce*, must be
  greater than or equal to `0`.
- The first gradient of the **Tabulated collector currents,
  Ic(Vge,Vce)** parameter, with respect to gate-emitter
  voltage *Vge*, must be equal
  to `0`.

### Representation by 3-D Lookup Table

For the temperature-dependent lookup table representation of the detailed block
modeling option, you provide tabulated values for collector current as a function of
gate-emitter voltage, collector-emitter voltage, and temperature.

The lookup table representation combines all of the equivalent circuit components
(PNP transistor, N-channel MOSFET, collector resistor and emitter resistor) into one
equivalent lookup table.

If the block thermal port is not exposed, then the **Device simulation
temperature** parameter on the **Temperature
Dependence** setting lets you specify the simulation
temperature.

**Note**

To ensure that the signs of the collector-emitter current and
collector-emitter voltage are consistent:

- If the collector-emitter voltage is equal to `0`,
  the value of the **Tabulated collector currents,
  Ic(Vge,Vce,T)** parameter must be equal to
  `0`.
- The tabulated power, which is the product of the
  **Tabulated collector currents, Ic(Vge,Vce,T)**
  parameter and the collector-emitter voltage, must be greater than or
  equal to `0`.
- The tabulated conductance, which is the gradient of the
  **Tabulated collector currents, Ic(Vge,Vce,T)**
  parameter with respect to the collector-emitter voltage
  *Vce*, must be
  greater than or equal to `0`.
- The first gradient of the **Tabulated collector currents,
  Ic(Vge,Vce,T)** parameter, with respect to gate-emitter
  voltage *Vge*, must be equal
  to `0`.

### Charge Model

The detailed modeling option of the block models capacitances either by fixed
capacitance values, or by tabulated values as a function of the collector-emitter
voltage. In either case, you can either directly specify the gate-emitter and
gate-collector capacitance values, or let the block derive them from the input and
reverse transfer capacitance values. Therefore, the
**Parameterization** options for charge model on the
**Junction Capacitance** setting are:

- `Specify fixed input, reverse transfer and output
  capacitance` — Provide fixed parameter values from
  datasheet and let the block convert the input and reverse transfer
  capacitance values to capacitance values, as described below. This is the
  default method.
- `Specify fixed gate-emitter, gate-collector and
  collector-emitter capacitance` — Provide fixed
  values for capacitance parameters directly.
- `Specify tabulated input, reverse transfer and output
  capacitance` — Provide tabulated capacitance and
  collector-emitter voltage values based on datasheet plots. The block
  converts the input and reverse transfer capacitance values to capacitance
  values, as described below.
- `Specify tabulated gate-emitter, gate-collector and
  collector-emitter capacitance` — Provide tabulated
  values for capacitances and collector-emitter voltage.

Use one of the tabulated capacitance options (`Specify tabulated
input, reverse transfer and output capacitance` or
`Specify tabulated gate-emitter, gate-collector and
collector-emitter capacitance`) when the datasheet provides a plot
of capacitances as a function of collector-emitter voltage. Using tabulated
capacitance values will give more accurate dynamic characteristics, and avoids the
need to iteratively tune parameters to fit the dynamics.

If you use the `Specify fixed gate-emitter, gate-collector and
collector-emitter capacitance` or `Specify tabulated
gate-emitter, gate-collector and collector-emitter capacitance`
option, the **Junction Capacitance** setting lets you specify the
**Gate-emitter capacitance**, **Gate-collector
capacitance**, and **Collector-emitter capacitance**
parameter values (fixed or tabulated) directly. Otherwise, the block derives them
from the **Input capacitance, Cies**, **Reverse transfer
capacitance, Cres**, and **Output capacitance, Coes**
parameter values. These two parameterization methods are related as follows:

- *CGC* =
  *Cres*
- *CGE* = *Cies* –
  *Cres*
- *C*CE = *Coes* –
  *Cres*

The two fixed capacitance options (`Specify fixed input, reverse
transfer and output capacitance` or `Specify fixed
gate-emitter, gate-collector and collector-emitter capacitance`)
let you model gate capacitance as a fixed gate-emitter capacitance
*C*GE and either a fixed or a nonlinear
gate-collector capacitance *C*GC. If you
select the `Gate-collector charge function is nonlinear`
option for the **Charge-voltage linearity** parameter, then the
gate-collector charge relationship is defined by the piecewise-linear function shown
in the following figure.

With this nonlinear capacitance, the gate-emitter and collector-emitter voltage
profiles take the form shown in the next figure, where the collector-emitter voltage
fall has two regions (labeled 2 and 3) and the gate-emitter voltage has two
time-constants (before and after the threshold voltage
*V*th):

You can determine the capacitor values for *Cies*,
*Cres*, and *C*ox as
follows, assuming that the IGBT gate is driven through an external resistance
*R*G:

1. Set *Cies* to get correct time-constant for
   *V*GE in Region 1. The time
   constant is defined by the product of *Cies* and
   *R*G. Alternatively, you can use
   a datasheet value for *Cies*.
2. Set *Cres* so as to achieve the correct
   *VCE* gradient in Region 2.
   The gradient is given by (*VGE* –
   *Vth*)/(*Cres*
   · *R*G).
3. Set *VCox* to the voltage at which
   the *VCE* gradient changes minus the
   threshold voltage *V*th.
4. Set *Cox* to get correct Miller
   length and time constant in Region 4.

Because the underlying model is a simplification of an actual charge distribution,
some iteration of these four steps may be required to get a best overall fit to
measured data.

The collector current tail when the IGBT is turned off is determined by the
**Total forward transit time** parameter if you set the
**I-V characteristics defined by** parameter to
`Fundamental nonlinear equation`.

If you set the **I-V characteristics defined by** parameter to
`Lookup table (2D, temperature independent)` or
`Lookup table (3D, temperature dependent)`, then the
collector current tail when the IGBT is turned off is determined by the
**Turn-off tail current transit time** parameter:

ic=ioff+(ion−ioff)exp(−t−toffTT)

Where *ioff* is the IGBT
turn-off current, *ion* is the IGBT turn-on
current, *toff* is the turn-off time, and
*TT* is the value of the **Turn-off tail current
transit time** parameter.

**Note**

Because this block implementation includes a charge model, you must model the
impedance of the circuit driving the gate to obtain representative turn-on and
turn-off dynamics. Therefore, if you are simplifying the gate drive circuit by
representing it as a controlled voltage source, you must include a suitable
series resistor between the voltage source and the gate.

### Fine-Tuning the Current-Voltage Characteristics

For the equivalent circuit representation of the detailed model, use the
parameters on the **Advanced** setting to fine-tune the
current-voltage characteristics of the modeled device. To use these additional
parameters effectively, you will need a manufacturer datasheet that provides plots
of the collector current versus collector-emitter voltage for different values of
gate-emitter voltage. The parameters on the **Advanced** setting
have the following effects:

- The **Emission coefficient, N** parameter controls the
  shape of the current-voltage curves around the origin.
- The **Collector resistance, RC** and **Emitter
  resistance, RE** parameters affect the slope of the
  current-voltage curve at higher currents, and when fully turned on by a high
  gate-emitter voltage.
- The **Forward Early voltage, VAF** parameter affects the
  shape of the current-voltage curves for gate-emitter voltages around the
  **Gate-emitter threshold voltage, Vge(th)**.

### Modeling Temperature Dependence

For the 2-D lookup table representation, the electrical equations do not depend on
temperature. However, you can model temperature dependence by either using the 3-D
lookup table representation, or by using the equivalent circuit representation of
the detailed model.

For the equivalent circuit representation, temperature dependence is modeled by
the temperature dependence of the constituent components. See the N-Channel MOSFET and PNP Bipolar Transistor block reference pages for further information on
the defining equations.

Some datasheets do not provide information on the zero gate voltage collector
current, *Ices*, at a higher measurement temperature. In this case,
you can alternatively specify the energy gap, *EG*, for the device,
using a typical value for the semiconductor type. For silicon, the energy gap is
usually `1.11` eV.

### Event-Based IGBT Modeling Option

This implementation has much simpler equations than that with full I-V and
capacitance characteristics. Use the event-based modeling option when the focus of
the analysis is to understand overall circuit behavior rather than to verify the
precise IGBT timing or losses characteristics.

The device is always in one of the following four states:

- Off
- Turning on
- On
- Turning off

In the off state, the relationship between collector current
(*i*c) and collector-emitter voltage
(*vce*) is

|  |  |
| --- | --- |
| *ic* = *Goff**vce* | **(1)** |

In the on state, the relationship between collector current
(*ic*) and collector-emitter voltage
(*vce*) is

|  |  |
| --- | --- |
| *vce* = tablelookup(*ic*) | **(2)** |

When turning on, the collector-emitter voltage is ramped down to zero over the
rise time, the device moving into the on state when the voltage falls below the
tabulated on-state value. Similarly when turning off, the collector-emitter voltage
is ramped up over the (current) fall time to the specified blocking voltage value.

The following figure shows the resulting voltage and current profiles when driving
a resistive load.

### Thermal Port

The block has an optional thermal port, hidden by default. To expose the thermal
port, set the **Modeling option** parameter to:

- `Full I-V and capacitance characteristics | Show thermal
  port` — Detailed model. This action displays the thermal
  port **H** on the block icon, and exposes the
  **Thermal Port** parameters.
- `Simplified I-V characteristics and event-based timing | Show
  thermal port` — Simplified event-based model. This action
  displays the thermal port **H** on the block icon, exposes
  **Thermal Port** parameters and additional
  **Main** parameters. To simulate thermal effects, you
  must provide additional tabulated data for turn-on and turn-off losses and
  define the collector-emitter on-state voltage as a function of both current
  and temperature.

Use the thermal port to simulate the effects of generated heat and device
temperature. For more information on using thermal ports and on the
**Thermal Port** parameters, see Simulating Thermal Effects in Semiconductors.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

This table shows the relationship between the capacitances of the block and the initial targets:

| Defined Capacitance | Initial Targets |
| --- | --- |
| Gate-emitter capacitance, *Cge* | Set the initial target for the gate-emitter capacitance voltage only. Set the initial target of the collector-emitter capacitance voltage to `0` or set its priority to `None`. |
| Collector-emitter capacitance, *Cce* | Set the initial target for the collector-emitter capacitance voltage only. Set the initial target of the gate-emitter capacitance voltage to `0` or set its priority to `None`. |
| Gate-collector capacitance, *Cgc* | Set the initial targets for the gate-collector voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and collector-emitter. |
| Gate-emitter capacitance, *Cge*, and gate-collector capacitance, *Cgc* | Set the initial targets for the gate-emitter and gate-collector voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |
| Gate-emitter capacitance, *Cge*, and collector-emitter capacitance, *Cce* | Set the initial target for the gate-emitter and the collector-emitter capacitance. |
| Gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | Set the initial targets for the gate-collector and collector-emitter voltages by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |
| Gate-emitter capacitance, *Cge*, gate-collector capacitance, *Cgc*, and collector-emitter capacitance, *Cce* | Set the initial targets for the gate-emitter, gate collector and collector-emitter capacitances by applying constraints on the gate-emitter and collector-emitter voltages. The initial condition of the gate-collector capacitance voltage is equal to the voltage between the gate-emitter and the collector-emitter. |

**Note**

Inside your model, the number of initial targets with **Priority** equal to `Low` or `High` must match the number of differential variables. The differential variables come from the inductors and the capacitances in the model.

### Plot Basic I-V Characteristics

You can plot the basic I-V characteristics of the N-Channel IGBT block without building a
complete model. Use the plots to explore the impact of your
parameter choices on device characteristics. If you parameterize the
block from a data sheet, you can compare your plots to the data
sheet to check that you parameterized the block correctly. If you
have a complete working model but do not know which manufactured
part to use, you can compare your plots to data sheets to help you
decide.

To enable this option, set the **Modeling option** parameter of
the N-Channel IGBT block to `Full I-V and capacitance characteristics | No
thermal port`. To plot the basic characteristics, right-click the
block and select **Electrical** > **Basic
characteristics** from the context menu. For more information about
the **Basic characteristics** option, see Plot Basic I-V Characteristics of Semiconductor Blocks.
