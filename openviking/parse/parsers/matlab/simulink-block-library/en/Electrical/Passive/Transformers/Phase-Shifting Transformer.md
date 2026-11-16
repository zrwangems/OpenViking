---
type: simulink-block
title: 'Phase-Shifting Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'phaseshiftingtransformer'
documentation_source_path: 'ref/phaseshiftingtransformer.html'
language: en
---

# Phase-Shifting Transformer

## Ports

### Conserving

### **~1** — Primary winding terminal electrical

Electrical conserving port associated with the primary winding.

### **~2** — First secondary winding terminal electrical

Electrical conserving port associated with the first secondary winding.

### **~3** — Second secondary winding terminal electrical

Electrical conserving port associated with the second secondary winding.

### **~4** — Third secondary winding terminal electrical

Electrical conserving port associated with the third secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`18-pulse`, `24-pulse`, or
`48-pulse`.

### **~5** — Fourth secondary winding terminal electrical

Electrical conserving port associated with the fourth secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`24-pulse` or `48-pulse`.

### **~6** — Fifth secondary winding terminal electrical

*Since R2024b*

Electrical conserving port associated with the fifth secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`48-pulse`.

### **~7** — Sixth secondary winding terminal electrical

*Since R2024b*

Electrical conserving port associated with the sixth secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`48-pulse`.

### **~8** — Seventh secondary winding terminal electrical

*Since R2024b*

Electrical conserving port associated with the seventh secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`48-pulse`.

### **~9** — Eighth secondary winding terminal electrical

*Since R2024b*

Electrical conserving port associated with the eighth secondary winding.

#### Dependencies

To enable this port, set **Number of pulses** parameter to
`48-pulse`.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of pulses** — Number of pulses `12-pulse` (default) | `18-pulse` | `24-pulse` | `48-pulse`

Number of pulses of the transformer:

- `12-pulse` —
  The transformer generates two different three-phase voltages with a phase shift of
  30 degrees from each other. *(since R2024b)*
- `18-pulse` — The transformer generates three
  different three-phase voltages with a phase shift of 20 degrees from each
  other.
- `24-pulse` — The transformer generates four different
  three-phase voltages with a phase shift of 15 degrees from each other.
- `48-pulse` —
  The transformer generates eight different three-phase voltages with a phase shift
  of 7.5 degrees from each other. *(since R2024b)*

### **Rated apparent power** — Apparent power at rated capacity `100e6` `A*V` (default) | positive scalar

Apparent power that flows through the transformer when it operates at the rated
capacity.

### **Rated electrical frequency** — Connected network electrical frequency `60` `Hz` (default) | positive scalar

Rated or nominal frequency of the AC network to which the transformer
connects.

### **Primary rated voltage** — RMS line voltage applied to the primary winding `4160` `V` (default) | positive scalar

Root-mean-square line voltage that the block applies to the primary winding under
normal operating conditions.

### **Primary winding resistance (pu)** — Power loss in primary winding `0.01` (default) | positive scalar

Per-unit power loss in the primary winding.

### **Primary leakage reactance (pu)** — Magnetic flux loss in primary winding `0.05` (default) | positive scalar

Per-unit magnetic flux loss in the primary winding.

### **Secondary winding resistance (pu)** — Power loss in secondary windings `0.01` (default) | positive scalar

Per-unit power loss in the secondary windings.

### **Secondary leakage reactance (pu)** — Magnetic flux loss in secondary windings `0.05` (default) | positive scalar

Per-unit magnetic flux loss in the first secondary windings.

### **Magnetizing resistance (pu)** — Losses in transformer core `500` (default) | positive scalar

Per-unit losses in the transformer core.

### **Magnetizing reactance (pu)** — Magnetic effects of transformer core `500` (default) | positive scalar

Per-unit magnetic effects of the transformer core.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2024b: Model 12-pulse and 48-pulse phase-shifting transformers

You can now model a 12-pulse or a 48-pulse phase-shifting transformer. To select between
a 12-pulse or 48-pulse transformer, set the **Number of pulses** parameter to:

- `12-pulse` — The transformer generates two different
  three-phase voltages with a phase shift of 30 degrees from each other.
- `48-pulse` — The transformer generates eight different
  three-phase voltages with a phase shift of 7.5 degrees from each other.

## Description

12-pulse, 18-pulse, 24-pulse, or 48-pulse phase-shifting transformer

The Phase-Shifting Transformer block represents a 12-pulse,
18-pulse, 24-pulse, or 48-pulse phase-shifting transformer. Phase-shifting transformers are
used in multi-pulse rectifiers in high-power and variable-load applications.

To select between a 12-pulse, 18-pulse, 24-pulse, or 48-pulse transformer, set the
**Number of pulses** parameter to:

- `12-pulse` — The transformer generates two different
  three-phase voltages with a phase shift of 30 degrees from each other.
- `18-pulse` — The transformer generates three different
  three-phase voltages with a phase shift of 20 degrees from each other.
- `24-pulse` — The transformer generates four different
  three-phase voltages with a phase shift of 15 degrees from each other.
- `48-pulse` — The transformer generates eight different
  three-phase voltages with a phase shift of 7.5 degrees from each other.

### 12-Pulse Transformer

*Since R2024b*

The 12-pulse transformer generates two different three-phase voltages with a 30 degree
phase shift from each other at its secondary side:

- The phase angle of the three-phase voltage at the **~2** port leads the
  phase angle of the three-phase voltage at the **~3** port by 30
  degrees.
- The phase angle of the three-phase voltage of the port at the primary side,
  **~1**, lags the phase angle of the three-phase voltage at the
  **~2** port by 15 degrees.

### 18-Pulse Transformer

The 18-pulse transformer generates three different three-phase voltages with a 20 degree
phase shift from each other at its secondary side:

- The phase angle of the three-phase voltage at the **~2** port leads the
  phase angle of the three-phase voltage at the **~3** port by 20
  degrees.
- The phase angle of the three-phase voltage at the **~3** port leads the
  phase angle of the three-phase voltage at the **~4** port by 20
  degrees.
- The phase angle of the three-phase voltage at the **~3** port is the same
  as the phase angle of the three-phase voltage of the port at the primary side,
  **~1**.

### 24-Pulse Transformer

The 24-pulse transformer generates four different three-phase voltages with a 15 degree
phase shift from each other at its secondary side:

- The phase angle of the three-phase voltage at the **~2** port leads the
  phase angle of the three-phase voltage at the **~3** port by 15
  degrees.
- The phase angle of the three-phase voltage at the **~3** port leads the
  phase angle of the three-phase voltage at the **~4** port by 15
  degrees.
- The phase angle of the three-phase voltage at the **~4** port leads the
  phase angle of the three-phase voltage at the **~5** port by 15
  degrees.
- The phase angle of the three-phase voltage of the port at the primary side,
  **~1**, lags the phase angle of the three-phase voltage at the
  **~3** port by 7.5 degrees.

### 48-Pulse Transformer

*Since R2024b*

The 48-pulse transformer generates eight different three-phase voltages with a 7.5
degree phase shift from each other at its secondary side:

- The phase angle of the three-phase voltage at the **~2** port leads the
  phase angle of the three-phase voltage at the **~3** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~3** port leads the
  phase angle of the three-phase voltage at the **~4** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~4** port leads the
  phase angle of the three-phase voltage at the **~5** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~5** port leads the
  phase angle of the three-phase voltage at the **~6** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~6** port leads the
  phase angle of the three-phase voltage at the **~7** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~7** port leads the
  phase angle of the three-phase voltage at the **~8** port by 7.5
  degrees.
- The phase angle of the three-phase voltage at the **~8** port leads the
  phase angle of the three-phase voltage at the **~9** port by 7.5
  degrees.
- The phase angle of the three-phase voltage of the port at the primary side,
  **~1**, lags the phase angle of the three-phase voltage at the
  **~5** port by 3.75 degrees.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
