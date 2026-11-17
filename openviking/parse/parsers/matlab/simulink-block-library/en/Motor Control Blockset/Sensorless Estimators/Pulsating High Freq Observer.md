---
type: simulink-block
title: 'Pulsating High Freq Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'pulsatinghighfreqobserver'
documentation_source_path: 'ref/pulsatinghighfreqobserver.html'
language: en
---

# Pulsating High Freq Observer

## Ports
```yaml
ports:
- name: Iab hf
  summary: PHF current response vector
  direction: input
  data_types: single | double | fixed point
- name: Enable
  summary: Input to trigger block operation scalar
  direction: input
  data_types: Boolean
- name: θin
  summary: Initial rotor position scalar
  direction: input
  data_types: single | double | fixed point
- name: IPEEn
  summary: Enable stage 1 initial position estimation (IPE) operation scalar
  direction: input
  data_types: Boolean
- name: Vαβ hf
  summary: PHF output scalar
  direction: output
  data_types: single | double | fixed point
- name: θest
  summary: Estimated rotor position scalar
  direction: output
  data_types: single | double | fixed point
- name: PosEn
  summary: Status of *θest* port scalar
  direction: output
  data_types: single | double | fixed point
- name: Info
  summary: Bus signal bus
  direction: output
```

### Input

### **Iab hf** — PHF current response vector

The high-frequency (phase a and b) current feedback from the motor in response to
the PHF voltage injection, in amperes or per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **Enable** — Input to trigger block operation scalar

Specify one of these inputs at this port:

- `1` — Enable block operation
- `0` — Disable block operation

**Data Types:** `Boolean`

### **θin** — Initial rotor position scalar

Initial rotor position input when the block skips the stage 1 initial position
estimation (IPE) operation. The position is expressed in radians, degrees, or
per-unit. For more information on the two stages that the block operates in, see Algorithm.

The unit depends on the **Position unit** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **IPEEn** — Enable stage 1 initial position estimation (IPE) operation scalar

Port for signal to enable stage 1 IPE operation. It supports one of the following
inputs:

- `1` — Enable the block to run the stage 1 IPE operation
  followed by the stage 2 closed-loop pulsating high-frequency (PHF) injection
  operation.
- `0` — Enable the block to skip stage 1 and directly run stage
  2 closed-loop PHF injection.

For more information on the two stages that the block operates in, see Algorithm.

**Data Types:** `Boolean`
### Output

### **Vαβ hf** — PHF output scalar

Pulsating high-frequency voltage (in *αβ* reference frame)
output, in per-unit.

**Data Types:** `single` | `double` | `fixed point`

### **θest** — Estimated rotor position scalar

The rotor position estimated by the block, in radians, degrees, or
per-unit.

The unit depends on the **Position unit** parameter.

**Data Types:** `single` | `double` | `fixed point`

### **PosEn** — Status of *θest* port scalar

The port provides one of the following outputs:

- `1` — Indicates that the block has successfully completed the
  stage 1 initial position estimation (IPE) and that the
  **θest** port displays the accurate
  rotor position.
- `0` — Indicates that the stage 1 IPE operation is still in
  progress (*θest* port output is not
  accurate as yet) or that the estimation has failed.

**Data Types:** `single` | `double` | `fixed point`

### **Info** — Bus signal bus

The bus signal contains these block calculations.

| Signal | | | | Description | Units |
| --- | --- | --- | --- | --- | --- |
| Sin *θest* and cos *θest* | | | | Sine and cosine of estimated rotor position | - |
| *Id* and *Iq* | | | | Stator direct axis and quadrature axis currents | A |
| Convergence | | | | Difference between current and previous sample of *θest* output.  A value closer to zero indicates saturation of *θest*. | rad |
| Status | | | 0 | Block is not enabled (**Enable** input port is 0) | - |
| 1 | Block is finding the best possible initial estimate (stage 1 part A) | - |
| 2 | Block is running the PHF method (stage 1 part B) | - |
| 3 | Block is running the DP method (stage 1 part C) | - |
| 4 | Block has successfully completed stage 1 and has started stage 2 closed-loop PHF injection | - |
| 5 | Stage 1 part B failed due to a large error in the estimated rotor position | - |
## Parameters
```yaml
parameters:
- name: Discrete step size (s)
  summary: Sample time after which block executes again 50e-6 (default) | scalar
  group: ''
- name: Input units
  summary: Unit of block inputs Per-unit (default) | SI
  group: ''
- name: Datatype
  summary: Input and output data type single (default) | double | fixed point
  group: ''
- name: Compute PHF parameters automatically using motor parameters
  summary: Automatically compute PHF parameters off (default) | on
  group: ''
- name: Compute DP parameters automatically using motor parameters
  summary: Automatically compute DP parameters off (default) | on
  group: ''
- name: Stator resistance (ohm)
  summary: Motor resistance 0.1458 (default) | scalar
  group: Motor Parameters
- name: Stator d-axis inductance (H)
  summary: Motor inductance 0.00013016 (default) | scalar
  group: Motor Parameters
- name: Stator q-axis inductance (H)
  summary: Motor inductance 0.00014098 (default) | scalar
  group: Motor Parameters
- name: Base voltage (V)
  summary: Rated voltage 13.8564 (default) | scalar
  group: Motor Parameters
- name: Base current (A)
  summary: Rated current 21.4286 (default) | scalar
  group: Motor Parameters
- name: Compute PHF parameters
  summary: Compute PHF parameters manually button
  group: Motor Parameters
- name: Compute DP parameters
  summary: Compute DP parameters manually button
  group: Motor Parameters
- name: PHF peak voltage (PU)
  summary: Peak voltage of PHF 0.2 (default) | scalar
  group: PHF Parameters
- name: PHF frequency (Hz)
  summary: PHF voltage frequency 2000 (default) | scalar
  group: PHF Parameters
- name: LP filter cutoff frequency (Hz)
  summary: Cutoff frequency for lowpass filter of PHF 131.9037 (default) | scalar
  group: PHF Parameters
- name: Select tuning parameters
  summary: Select control parameters for manual tuning Controller gains (default) | Time response variables
  group: PHF Parameters
- name: Proportional gain
  summary: Proportional gain for PI controller of PHF 1954.6647 (default) | scalar
  group: PHF Parameters
- name: Integral gain
  summary: Integral gain for PI controller of PHF 7392.5303 (default) | scalar
  group: PHF Parameters
- name: Expected settling time (s)
  summary: Expected settling time of estimated position 0.66794 (default) | scalar
  group: PHF Parameters
- name: Expected damping ratio
  summary: Expected damping ratio of block output *θest* 0.99 (default) | scalar
  group: PHF Parameters
- name: Compute Control Parameters
  summary: Compute disabled control parameters button
  group: PHF Parameters
- name: Open loop duration (s)
  summary: Duration of open-loop PHF injection during stage 1 part A 0.0066794 (default) | scalar
  group: PHF Parameters
- name: Closed loop duration (s)
  summary: Duration of closed-loop PHF injection during stage 1 part B 0.66794 (default) | scalar
  group: PHF Parameters
- name: Idle time (s)
  summary: Duration between algorithm steps 0.0066794 (default) | scalar
  group: PHF Parameters
- name: Error threshold (rad)
  summary: Minimum error threshold for *θerr* 4e-4 (default) | scalar
  group: PHF Parameters
- name: Pulse voltage (PU)
  summary: Amplitude of injected pulses 0.5 (default) | scalar
  group: DP Parameters
- name: Pulse duration (s)
  summary: Duration of injected pulses 0.00066955 (default) | scalar
  group: DP Parameters
- name: Idle time (s)
  summary: Duration between two pulses during dual-pulse injection 50e-3 (default) | scalar
  group: DP Parameters
```

### **Discrete step size (s)** — Sample time after which block executes again `50e-6` (default) | scalar

The time between two consecutive instances of block execution.

### **Input units** — Unit of block inputs `Per-unit` (default) | `SI`

Units of measure for the block inputs.

### **Datatype** — Input and output data type `single` (default) | `double` | `fixed point`

Data type of the block inputs and outputs.

### **Compute PHF parameters automatically using motor parameters** — Automatically compute PHF parameters `off` (default) | `on`

Selecting this parameter enables the block to automatically compute the following
PHF parameters (available on the **PHF Parameters** tab) using the
specified motor parameters:

- **PHF frequency (Hz)**
- **LP filter cutoff frequency (Hz)**
- **Proportional gain**
- **Integral gain**
- **Expected settling time (s)**
- **Expected damping ratio**
- **Open loop duration (s)**
- **Closed loop duration (s)**
- **Idle time (s)**

For more information about how the block computes these PHF parameters, see Compute PHF Parameters.

If you select this parameter, the block disables the **Compute PHF
parameters** button.

### **Compute DP parameters automatically using motor parameters** — Automatically compute DP parameters `off` (default) | `on`

Selecting this parameter enables the block to automatically compute the DP parameter
**Pulse duration (s)** (available on the **DP
Parameters** tab) using the specified motor parameters.

For more information about how the block computes the DP parameter, see Compute DP Parameters.

If you select this parameter, the block disables the **Compute DP
parameters** button.

### Motor Parameters

### **Stator resistance (ohm)** — Motor resistance `0.1458` (default) | scalar

Resistance of the stator (in ohms).

### **Stator d-axis inductance (H)** — Motor inductance `0.00013016` (default) | scalar

Inductance of the stator along the *d*-axis of the
*d-q* reference frame.

### **Stator q-axis inductance (H)** — Motor inductance `0.00014098` (default) | scalar

Inductance of the stator along the *q*-axis of the
*d-q* reference frame.

### **Base voltage (V)** — Rated voltage `13.8564` (default) | scalar

Rated voltage of the motor (in volts).

### **Base current (A)** — Rated current `21.4286` (default) | scalar

Rated current of the motor (in amperes).

### **Compute PHF parameters** — Compute PHF parameters manually `button`

When you click this button, the block computes the following PHF parameters
(available on the **PHF Parameters** tab) manually using the
specified motor parameters:

- **PHF frequency (Hz)**
- **LP filter cutoff frequency (Hz)**
- **Proportional gain**
- **Integral gain**
- **Expected settling time (s)**
- **Expected damping ratio**
- **Open loop duration (s)**
- **Closed loop duration (s)**
- **Idle time (s)**

For more information about how the block computes these PHF parameters, see Compute PHF Parameters.

#### Dependencies

To enable this parameter, clear the **Compute PHF parameters
automatically using motor parameters** parameter.

### **Compute DP parameters** — Compute DP parameters manually button

When you click this button, the block computes the DP parameter **Pulse
duration (s)** (available on the **PHF Parameters** tab)
manually using the specified motor parameters:

For more information about how the block computes the DP parameter, see Compute DP Parameters.

#### Dependencies

To enable this parameter, clear the **Compute DP parameters
automatically using motor parameters** parameter.

### PHF Parameters

### **PHF peak voltage (PU)** — Peak voltage of PHF `0.2` (default) | scalar

Peak amplitude of the PHF voltage applied by the block, in volts.

### **PHF frequency (Hz)** — PHF voltage frequency `2000` (default) | scalar

Frequency of the PHF voltage applied by the block, in Hz.

### **LP filter cutoff frequency (Hz)** — Cutoff frequency for lowpass filter of PHF `131.9037` (default) | scalar

Cutoff frequency of the lowpass filter for the PHF applied by the block, in
Hz.

### **Select tuning parameters** — Select control parameters for manual tuning `Controller gains` (default) | `Time response variables`

Select the control parameters that you want to manually tune.

- `Controller gains` — Select this option to enable
  these control parameters:

  - **Proportional gain**
  - **Integral gain**

  **Note**

  Selecting `Control gains` disables the time
  response variables.
- `Time response variables` — Select this option to
  enable these control parameters:

  - **Expected settling time (s)**
  - **Expected damping ratio**

  **Note**

  Selecting `Time response variables` disables the
  control gains variables.

To see the effects of the tuned parameters on the disabled control parameters, you
can click the **Compute Control Parameters** button. For more
details, see Compute Control Parameters.

### **Proportional gain** — Proportional gain for PI controller of PHF `1954.6647` (default) | scalar

Proportional PI controller gain, *Kp*, for
the PHF applied by the block.

#### Dependencies

To enable this parameter, set the **Select tuning parameters**
parameter to `Controller gains`.

### **Integral gain** — Integral gain for PI controller of PHF `7392.5303` (default) | scalar

Integral PI controller gain, *Ki*, for the
PHF applied by the block.

#### Dependencies

To enable this parameter, set the **Select tuning parameters**
parameter to `Controller gains`.

### **Expected settling time (s)** — Expected settling time of estimated position `0.66794` (default) | scalar

The expected time for the block output
*θest* to saturate during part B.

#### Dependencies

To enable this parameter, set the **Select tuning parameters**
parameter to `Time response variables`.

### **Expected damping ratio** — Expected damping ratio of block output *θest* `0.99` (default) | scalar

The expected damping ratio of the block output
*θest* dynamics.

#### Dependencies

To enable this parameter, set the **Select tuning parameters**
parameter to `Time response variables`.

### **Compute Control Parameters** — Compute disabled control parameters button

Compute the control parameters that are disabled in the **Control
Parameters** section. This parameter helps you update the disabled control
parameters according to the edits you made to the enabled control parameters. This
table describes the equations that the block uses to compute the disabled control
parameters.

| **Control Parameter** | **Expression or Value** | Remarks |
| --- | --- | --- |
| Proportional gain, *kp* | ln(20000)G⋅Tsettling | The **Compute Control Parameters** button computes these values when you enable the time response variables for manual edits. |
| Integral gain, *ki* | G(kp)24δ2 |
| Expected settling time (s), *Tsettling* | ln(20000)G⋅kp,when δ≤1ln(20000)G⋅kp(2δ(δ−δ2−1)),when δ>1 | The **Compute Control Parameters** button computes these values when you enable the controller gains for manual edits. |
| Expected damping ratio, *ẟ* | kp2Gki |

In the expressions:

- G=Vphf(Lq−Ld)4πfhLdLq
- *Vphf* is the peak amplitude value of
  the injected high frequency voltage signal (in volts).
- *Ld* and
  *Lq* are the *d* and
  *q* axis stator inductances (in henry).
- *fh* is the frequency of the injected
  high-frequency voltage.

**Note**

The expressions in this table use elements and values based on the reference
papers as well as experimental data.

### **Open loop duration (s)** — Duration of open-loop PHF injection during stage 1 part A `0.0066794` (default) | scalar

Duration of the open-loop PHF injection during stage 1 part A, in seconds.

### **Closed loop duration (s)** — Duration of closed-loop PHF injection during stage 1 part B `0.66794` (default) | scalar

Duration of the closed-loop PHF injection during stage 1 part B, in
seconds.

### **Idle time (s)** — Duration between algorithm steps `0.0066794` (default) | scalar

Duration (in seconds) between steps in the algorithm related to stage 1 part A and
stage 1 part B that allow for fading of transient dynamics. For example, this block
stops operating (for this duration) between each PHF injection (open loop or closed
loop).

### **Error threshold (rad)** — Minimum error threshold for *θerr* `4e-4` (default) | scalar

The minimum error value *θerr* at which
the convergence of estimated rotor position
*θest* completes.

### DP Parameters

### **Pulse voltage (PU)** — Amplitude of injected pulses `0.5` (default) | scalar

Voltage amplitude of the injected pulses, in volts.

### **Pulse duration (s)** — Duration of injected pulses `0.00066955` (default) | scalar

Duration of the injected pulses, in seconds.

### **Idle time (s)** — Duration between two pulses during dual-pulse injection `50e-3` (default) | scalar

Duration (in seconds) between two pulses during the dual-pulse injection (stage 1
part C).
## Libraries

Motor Control Blockset / Sensorless Estimators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Estimate initial rotor electrical position of interior PMSM using pulsating high frequency (PHF) injection

The Pulsating High Frequency Observer block estimates the initial position (in electrical
radians) of a stationary interior PMSM by using pulsating high-frequency (PHF) injection and
dual-pulse (DP) techniques. In addition, the block also detects the real-time position when
the rotor runs using (low-speed) closed-loop control.

For more information about the block algorithm, see Algorithm.
