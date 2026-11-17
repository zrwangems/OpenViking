---
type: simulink-block
title: 'Open-Loop PID Autotuner'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'openlooppidautotuner'
documentation_source_path: 'ug/openlooppidautotuner.html'
language: en
---

# Open-Loop PID Autotuner

## Ports
```yaml
ports:
- name: u
  summary: Signal from controller scalar
  direction: input
  data_types: single | double
- name: y
  summary: Plant output scalar
  direction: input
  data_types: single | double
- name: start/stop
  summary: Start and stop the autotuning experiment scalar
  direction: input
  data_types: single | double
- name: bandwidth
  summary: Target bandwidth for tuning scalar
  direction: input
  data_types: single | double
- name: target PM
  summary: Target phase margin for tuning scalar
  direction: input
  data_types: single | double
- name: sine Amp
  summary: Amplitudes of injected sinusoidal signals scalar | vector
  direction: input
  data_types: single | double
- name: step Amp
  summary: Amplitude of injected step signal scalar
  direction: input
  data_types: single | double
- name: u+Δu
  summary: Signal for plant input scalar
  direction: output
  data_types: single | double
- name: '% conv'
  summary: Convergence of FRD estimation during experiment scalar
  direction: output
  data_types: single | double
- name: pid gains
  summary: Tuned PID coefficients bus
  direction: output
  data_types: single | double
- name: estimated PM
  summary: Estimated phase margin with tuned controller scalar
  direction: output
- name: frd
  summary: Estimated frequency response vector
  direction: output
- name: dcgain
  summary: Estimated DC gain of plant scalar
  direction: output
- name: nominal
  summary: Plant input and output at nominal operating point vector
  direction: output
```

### Input

### **u** — Signal from controller scalar

Insert the block into your system such that this port accepts a control signal from a
source. Typically, this port accepts the signal from the PID controller in your system.

**Data Types:** `single` | `double`

### **y** — Plant output scalar

Connect this port to the plant output.

**Data Types:** `single` | `double`

### **start/stop** — Start and stop the autotuning experiment scalar

To start and stop the autotuning process, provide a signal at the
`start/stop` port. When the value of the signal changes
from:

- Negative or zero to positive, the experiment starts
- Positive to negative or zero, the experiment stops

When the experiment is not running, the block passes signals unchanged from
**u** to **u+Δu**. In this state, the
block has no impact on plant or controller behavior.

Typically, you can use a signal that changes from 0 to 1 to start the experiment, and from 1
to 0 to stop it. Some points to consider when configuring the
**start/stop** signal include:

- Start the experiment when the plant is at the desired equilibrium
  operating point. Use the initial controller to drive the plant to
  the operating point. If you have no initial controller (open-loop
  tuning only) you can use a source block connected to
  **u** to drive the plant to the operating
  point.
- Avoid any load disturbance to the plant during the experiment. Load disturbance can distort the plant output and reduce the accuracy of the frequency-response estimation.
- Let the experiment run long enough for the algorithm to collect
  sufficient data for a good estimate at all frequencies it probes.
  There are two ways to determine when to stop the experiment:

  - Determine the experiment duration in advance. A
    conservative estimate for the experiment duration is
    200/*ωc*
    for closed-loop tuning, or
    100/*ωc*
    for open-loop tuning, where
    *ωc* is
    your target bandwidth.
  - Observe the signal at the `% conv`
    output, and stop the experiment when the signal
    stabilizes near 100%.
- When you stop the experiment, the block computes tuned PID gains and
  updates the signal at the `pid gains`
  port.

You can configure any logic appropriate for your application to
control the start and stop times of the experiment.

**Data Types:** `single` | `double`

### **bandwidth** — Target bandwidth for tuning scalar

Supply a value for the `Target bandwidth (rad/sec)` parameter. See that parameter for details.

#### Dependencies

To enable this port, in the Tuning tab, next to `Target bandwidth (rad/sec)`, select **Use external source**.

**Data Types:** `single` | `double`

### **target PM** — Target phase margin for tuning scalar

Supply a value for the `Target phase margin (degrees)` parameter. See that parameter for details.

#### Dependencies

To enable this port, in the Tuning tab, next to `Target phase margin (degrees)`, select **Use external source**.

**Data Types:** `single` | `double`

### **sine Amp** — Amplitudes of injected sinusoidal signals scalar | vector

Supply a value for the `Sine Amplitudes` parameter. See that parameter for details.

#### Dependencies

To enable this port, in the Experiment tab, next to `Sine Amplitudes`, select **Use external source**.

**Data Types:** `single` | `double`

### **step Amp** — Amplitude of injected step signal scalar

Supply a value for the `Step Amplitude` parameter.
See that parameter for details.

#### Dependencies

To enable this port, in the Experiment tab, next to `Step
Amplitudes`, select **Use external
source**.

**Data Types:** `single` | `double`
### Output

### **u+Δu** — Signal for plant input scalar

Insert the block into your system such that this port feeds the input
signal to your plant.

- When the experiment is running
  (`start/stop` positive), the block
  injects test signals into the plant at this port. The test
  signal is the value at u when the experiment begins plus the
  experiment perturbation. If you have any saturation or rate
  limit protecting the plant, feed the signal from
  **u+Δu** into it.
- When the experiment is not running
  (`start/stop` zero or negative), the
  block passes signals unchanged from **u** to
  **u+Δu**.

**Data Types:** `single` | `double`

### **% conv** — Convergence of FRD estimation during experiment scalar

When the experiment is running (`start/stop` positive), the block
injects test signals into the plant and measures the plant response at
`y`. It uses these signals to estimate the frequency response of
the plant at several frequencies around the target bandwidth for tuning. `%
conv` indicates how close to completion the estimation of the plant
frequency response is. Typically, this value quickly rises to about 90% after the
experiment begins, and then gradually converges to a higher value. Stop the experiment
when it levels off near 100%.

**Data Types:** `single` | `double`

### **pid gains** — Tuned PID coefficients bus

This 4-element bus signal contains the tuned PID gains *P*,
*I*, *D*, and the filter coefficient
*N*. These values correspond to the `P`,
`I`, `D`, and `N` parameters in
the expressions given in the `Form` parameter. Initially, the values
are 0, 0, 0, and 100, respectively. The block updates the values when the experiment
ends. This bus signal always has four elements, even if you are not tuning a PIDF
controller.

If you have a PID controller associated with the block, you can update that controller with these values after the experiment ends. To do so, in the Block tab, click **Update PID Block**.

**Data Types:** `single` | `double`

### **estimated PM** — Estimated phase margin with tuned controller scalar

This port outputs the estimated phase margin achieved by the tuned controller, in degrees. The block updates this value when the tuning experiment ends. The estimated phase margin is calculated from the angle of *G*(*jωc*)*C*(*jωc*), where *G* is the estimated plant, *C* is the tuned controller, and *ωc* is the crossover frequency (bandwidth). The estimated phase margin might differ from the target phase margin specified by the `Target phase margin (degrees)` parameter. It is an indicator of the robustness and stability achieved by the tuned system.

- Typically, the estimated phase margin is near the target phase margin. In general, the larger the value, the more robust is the tuned system, and the less overshoot there is.
- A negative phase margin indicates that the closed-loop system might be unstable.

#### Dependencies

To enable this port, in the Tuning tab, select **Output estimated phase margin achieved by tuned controller**.

### **frd** — Estimated frequency response vector

This port outputs the frequency-response data estimated by the
experiment. Initially, the value at `frd` is [0, 0,
0, 0]. During the experiment, the block injects signals at frequencies [1/3, 1, 3,
10]*ωc*, where *ωc* is
the target bandwidth. At each sample time during the experiment, the
block updates `frd` with a vector containing the
complex frequency response at each of these frequencies, respectively.
You can use the progress of the response as an alternative to
`% conv` to examine the convergence of the
estimation. When the experiment stops, the block updates
`frd` with the final estimated frequency response
used for computing the PID gains.

#### Dependencies

To enable this port, in the Experiment tab, select **Plant
frequency responses near bandwidth**.

### **dcgain** — Estimated DC gain of plant scalar

If you select **Estimate DC gain with step signal**
in the Experiment tab, the block estimates the DC gain of the plant by
including a step signal in the injected perturbation. When the
experiment stops, the block updates this port with the estimated DC gain
value.

#### Dependencies

To enable this port, in the Experiment tab, select **Plant
DC Gain**.

### **nominal** — Plant input and output at nominal operating point vector

This port outputs a vector containing the plant input (**u+Δu**) and plant
output (**y**) when the experiment begins. These values are the plant
input and output at the nominal operating point at which the block performs the
experiment.

#### Dependencies

To enable this port, in the Experiment tab, select **Plant nominal input and output**.
## Parameters
```yaml
parameters:
- name: Type
  summary: PID controller actions PI (default) | PID | PIDF | ...
  group: ''
  block_parameter: PIDType
  type: character vector
  values: '''P'' | ''I'' | ''PI'' | ''PD'' | ''PDF'' | ''PID'' | ''PIDF'''
  default: '''PI'''
- name: Form
  summary: PID controller form Parallel (default) | Ideal
  group: ''
  block_parameter: PIDForm
  type: character vector
  values: '''Parallel'' | ''Ideal'''
  default: '''Parallel'''
- name: Time Domain
  summary: PID controller time domain discrete-time (default) | continuous-time
  group: ''
  block_parameter: TimeDomain
  type: character vector
  values: '''discrete-time'' | ''continuous-time'''
  default: '''discrete-time'''
- name: Controller sample time (sec)
  summary: Sample time of PID controller 0.1 (default) | positive scalar | –1
  group: ''
  block_parameter: DiscreteTs
  type: scalar
  values: positive scalar | –1
  default: '0.1'
- name: Experiment sample time (sec)
  summary: Sample time for experiment 0.02 (default) | positive scalar
  group: ''
  block_parameter: ContinuousTs
  type: positive scalar
  default: '0.02'
- name: Integrator method
  summary: Discrete integration formula for integrator term Forward Euler (default) | Backward Euler | Trapezoidal
  group: ''
  block_parameter: IntegratorFormula
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Filter method
  summary: Discrete integration formula for derivative filter term Forward Euler (default) | Backward Euler | Trapezoidal
  group: ''
  block_parameter: FilterFormula
  type: character vector
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Target bandwidth (rad/sec)
  summary: Target crossover frequency of tuned response 1 (default) | positive scalar
  group: ''
  block_parameter: Bandwidth
  type: positive scalar
  default: '1'
- name: Target phase margin (degrees)
  summary: Target minimum phase margin of open-loop response 60 (default) | scalar in range 0–90
  group: ''
  block_parameter: TargetPM
  type: scalar
  values: 0–90
  default: '60'
- name: Sine Amplitudes
  summary: Amplitude of sinusoidal perturbations 1 (default) | scalar | vector of length 4
  group: ''
  block_parameter: AmpSine
  type: scalar, vector of length 4
  default: '1'
- name: Estimate DC gain with step signal
  summary: Inject step signal into plant on (default) | off
  group: ''
  block_parameter: EstimateDCGain
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
- name: Step Amplitude
  summary: Amplitude of step perturbation 1 (default) | scalar
  group: ''
  block_parameter: AmpStep
  type: scalar
  default: '1'
- name: Reduce memory and avoid task overrun (external mode only)
  summary: Deploy tuning algorithm only off (default) | on
  group: ''
  block_parameter: DeployTuningModule
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Configure block for PLC Coder
  summary: Configure block for code generation with Simulink PLC Coder off (default) | on
  group: ''
- name: Data Type
  summary: Floating point precision double (default) | single
  group: ''
  block_parameter: BlockDataType
  type: character vector
  values: '''double'' | ''single'''
  default: '''double'''
- name: Clicking "Update PID Block" writes tuned gains to the PID block connected to "u" port
  summary: Automatically detect target for writing tuned PID coefficients on (default) | off
  group: ''
- name: Specify PID block path
  summary: Target PID controller block for writing tuned coefficients [] (default) | block path
  group: ''
- name: Update PID Block
  summary: Write tuned PID gains to target controller block button
  group: ''
- name: Export to MATLAB
  summary: Send experiment and tuning results to MATLAB workspace button
  group: ''
```

#### Tuning Tab

### **Type** — PID controller actions `PI` (default) | `PID` | `PIDF` | ...

Specify the type of the PID controller in your system. The controller type indicates what
actions are present in the controller. The following controller types are available for
PID autotuning:

- `P` — Proportional only
- `I` — Integral only
- `PI` — Proportional and integral
- `PD` — Proportional and derivative
- `PDF` — Proportional and derivative with derivative filter
- `PID` — Proportional, integral, and derivative
- `PIDF` — Proportional, integral, and derivative with derivative filter

When you update a PID Controller block or custom PID controller with tuned parameter values, make sure the controller type matches.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PIDType` |
| **Type:** character vector |
| **Values:** `'P'` | `'I'` | `'PI'` | `'PD'` | `'PDF'` | `'PID'` | `'PIDF'` |
| **Default:** `'PI'` |

### **Form** — PID controller form `Parallel` (default) | `Ideal`

Specify the controller form. The controller form determines the interpretation of the PID coefficients *P*, *I*, *D*, and *N*.

- `Parallel` — In `Parallel`
  form, the transfer function of a discrete-time PIDF controller is:

  C=P+IFi(z)+D[N1+NFd(z)],

  where *Fi*(*z*) and *Fd*(*z*) are the integrator and filter formulas (see
  `Integrator method` and `Filter
  method`). The transfer function of a continuous-time parallel-form
  PIDF controller is:

  C=P+I(1s)+D(Nss+N).

  Other controller actions amount to setting *P*,
  *I*, or *D* to zero.
- `Ideal` — In `Ideal` form, the transfer function of a discrete-time PIDF controller is:

  C=P[1+IFi(z)+D(N1+NFd(z))].

  The transfer function of a continuous-time ideal-form PIDF controller is:

  C=P[1+I(1s)+D(Nss+N)].

  Other controller actions amount to setting *D* to zero or setting, *I* to `Inf`. (In ideal form, the controller must have proportional action.)

When you update a PID Controller block or custom PID controller with tuned parameter values, make sure the controller form matches.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `PIDForm` |
| **Type:** character vector |
| **Values:** `'Parallel'` | `'Ideal'` |
| **Default:** `'Parallel'` |

**Tunable:** Yes

### **Time Domain** — PID controller time domain discrete-time (default) | continuous-time

Specify whether your PID controller is a discrete-time or continuous-time
controller.

- For discrete time, you must specify the sample time of your PID controller
  using the **Controller sample time (sec)** parameter.
- For continuous time, you must also specify a sample time for the PID
  autotuning experiment using the **Experiment sample time
  (sec)** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TimeDomain` |
| **Type:** character vector |
| **Values:** `'discrete-time'` | `'continuous-time'` |
| **Default:** `'discrete-time'` |

### **Controller sample time (sec)** — Sample time of PID controller 0.1 (default) | positive scalar | –1

Specify the sample time of your PID controller in seconds. This value also sets the
sample time for the experiment performed by the block.

To perform PID tuning, the block measures frequency-response information up to a
frequency of 10 times the target bandwidth. To ensure that this frequency is less than
the Nyquist frequency, the target bandwidth,
*ωc*, must satisfy *ωc**Ts*
≤ 0.3, where *Ts*
*ωc* is the controller sample time that you
specify with the **Controller sample time (sec)** parameter.

When you update a PID Controller block or custom PID controller with
tuned parameter values, make sure the controller sample time matches.

#### Tips

If you want to run the deployed block with different sample times in your
application, set this parameter to –1 and put the block in a Triggered Subsystem. Then, trigger
the subsystem at the desired sample time. If you do not plan to change the sample
time after deployment, specify a fixed and finite sample time.

#### Dependencies

To enable this parameter, set **Time Domain** to
`discrete-time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiscreteTs` |
| **Type:** scalar |
| **Value** positive scalar | –1 |
| **Default:** 0.1 |

### **Experiment sample time (sec)** — Sample time for experiment 0.02 (default) | positive scalar

Even when you tune a continuous-time controller, you must specify a sample time for
the experiment performed by the block. In general, continuous-time controller tuning is
not recommended for PID autotuning against a physical plant. If you want to tune in
continuous time against a Simulink model of the plant, use a fast experiment sample time, such as
0.02/*ωc*.

#### Dependencies

This parameter is enabled when the **Time Domain** is
`continuous-time`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ContinuousTs` |
| **Type:** positive scalar |
| **Default:** 0.02 |

### **Integrator method** — Discrete integration formula for integrator term `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

Specify the discrete integration formula for the integrator term in your controller. In discrete time, the PID controller transfer function assumed by the block is:

C=P+IFi(z)+D[N1+NFd(z)],

in parallel form, or in ideal form,

C=P[1+IFi(z)+D(N1+NFd(z))].

For a controller sample time *Ts*, the
`Integrator method` parameter determines the formula
*Fi* as follows:

| Integrator method | *Fi* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

For more information about the relative advantages of each method, see the Discrete PID Controller block reference
page.

When you update a PID Controller block or custom PID controller with tuned parameter values, make sure the integrator method matches.

#### Dependencies

This parameter is enabled when the **Time Domain** is `discrete-time` and the controller includes integral action.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntegratorFormula` |
| **Type:** character vector |
| **Values:** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **Default:** `'Forward Euler'` |

**Tunable:** Yes

### **Filter method** — Discrete integration formula for derivative filter term `Forward Euler` (default) | `Backward Euler` | `Trapezoidal`

Specify the discrete integration formula for the derivative filter term in your controller. In discrete time, the PID controller transfer function assumed by the block is:

C=P+IFi(z)+D[N1+NFd(z)],

in parallel form, or in ideal form,

C=P[1+IFi(z)+D(N1+NFd(z))].

For a controller sample time *Ts*, the
`Filter method`  parameter determines the formula
*Fd* as follows:

| Filter method | *Fd* |
| --- | --- |
| `Forward Euler` | Tsz−1 |
| `Backward Euler` | Tszz−1 |
| `Trapezoidal` | Ts2z+1z−1 |

For more information about the relative advantages of each method, see the Discrete PID
Controller block reference page.

When you update a PID Controller block or custom PID controller with tuned parameter values, make sure the filter method matches.

#### Dependencies

This parameter is enabled when the **Time Domain** is
`discrete-time` and the controller includes a derivative filter
term.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FilterFormula` |
| **Type:** character vector |
| **Values:** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **Default:** `'Forward Euler'` |

**Tunable:** Yes

### **Target bandwidth (rad/sec)** — Target crossover frequency of tuned response 1 (default) | positive scalar

The target bandwidth, specified in rad/sec, is the target value for the 0-dB gain crossover
frequency of the tuned open-loop response *CP*, where
*P* is the plant response, and *C* is the
controller response. This crossover frequency roughly sets the control bandwidth.
For a rise-time *τ* seconds, a good guess for the target bandwidth
is 2/*τ* rad/sec.

To perform PID tuning, the autotuner block measures frequency-response information up to a
frequency of 10 times the target bandwidth. To ensure that this frequency is less
than the Nyquist frequency, the target bandwidth,
*ωc*, must satisfy *ωc**Ts*
≤ 0.3, where *Ts* is the
controller sample time that you specify with the **Controller sample time
(sec)** parameter. Because of this condition, the fastest rise time
you can enforce for tuning is about
6.67*Ts*. If this rise time does not meet
your design goals, consider reducing
*Ts*.

To provide the target bandwidth via an input port, select **Use
external source**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Bandwidth` |
| **Type:** positive scalar |
| **Default:** `1` |

### **Target phase margin (degrees)** — Target minimum phase margin of open-loop response 60 (default) | scalar in range 0–90

Specify a target minimum phase margin for the tuned open-loop response at the crossover
frequency. The target phase margin reflects desired robustness of the tuned system.
Typically, choose a value in the range of about 45°–60°. In general, higher phase margin
improves overshoot, but can limit response speed. The default value, 60°, tends to
balance performance and robustness, yielding about 5–10% overshoot, depending on the
characteristics of your plant.

To provide the target phase margin via an input port, select **Use external source**.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TargetPM` |
| **Type:** scalar |
| **Values:** 0–90 |
| **Default:** 60 |

#### Experiment Tab

### **Sine Amplitudes** — Amplitude of sinusoidal perturbations 1 (default) | scalar | vector of length 4

During the tuning experiment, the block injects a sinusoidal signal into
the plant at the frequencies [1/3, 1, 3, 10]*ωc*
 , where *ωc* is
the target bandwidth for tuning. Use **Sine Amplitudes** to
specify the amplitude of each of these injected signals. Specify a:

- Scalar value to inject the same amplitude at each frequency
- Vector of length 4 to specify a different amplitude at each of [1/3, 1, 3,
  10]*ωc*

In a typical plant with typical target bandwidth, the magnitudes of the plant
responses at the experiment frequencies do not vary widely. In such cases, you can
use a scalar value to apply the same magnitude perturbation at all frequencies.
However, if you know that the response decays sharply over the frequency range,
consider decreasing the amplitude of the lower-frequency inputs and increasing the
amplitude of the higher-frequency inputs. It is numerically better for the
estimation experiment when all the plant responses have comparable magnitudes.

The perturbation amplitudes must be:

- Large enough that the perturbation overcomes any deadband in the plant
  actuator and generates a response above the noise level
- Small enough to keep the plant running within the approximately linear
  region near the nominal operating point, and to avoid saturating the
  plant input or output

In the experiment, the sinusoidal signals are superimposed (with the step perturbation, if
any, in the case of open-loop tuning). Thus, the perturbation can be at least as
large as the sum of all amplitudes. Therefore, to obtain appropriate values for the
amplitudes, consider:

- Actuator limits. Make sure that the largest possible perturbation is
  within the range of your plant actuator. Saturating the actuator can
  introduce errors into the estimated frequency response.
- How much the plant response changes in response to a given actuator
  input at the nominal operating point for tuning. For instance,
  suppose that you are tuning a PID controller used in engine-speed
  control. You have determined that at frequencies around the target
  bandwidth, a 1° change in throttle angle causes a change of about
  200 rpm in the engine speed. Suppose further that to preserve linear
  performance the speed must not deviate by more than 100 rpm from the
  nominal operating point. In this case, choose amplitudes to ensure
  that the perturbation signal is no greater than 0.5 (assuming that
  value is within actuator limits).

To provide the sine amplitudes via an input port, select **Use
external source**.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AmpSine` |
| **Type:** scalar, vector of length 4 |
| **Default:** 1 |

### **Estimate DC gain with step signal** — Inject step signal into plant `on` (default) | `off`

When this option is selected, the experiment includes an estimation of the
plant DC gain. The block performs this estimation by injecting a step signal
into the plant.

**Caution**

If your plant has a single integrator, clear this option. For plants
with multiple integrators or unstable poles, do not use the
Open-Loop PID Autotuner block.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `EstimateDCGain` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'on'` |

### **Step Amplitude** — Amplitude of step perturbation 1 (default) | scalar

If **Estimate DC gain with step signal** is selected, the
block estimates the DC gain by injecting a step signal into the plant. Use
this parameter to set the amplitude of the signal. The considerations for
choosing a step amplitude are the same as the considerations for specifying
**Sine Amplitudes**.

To provide the step amplitude via an input port, select **Use
external source**.

**Tunable:** Yes

#### Dependencies

This parameter is enabled when **Estimate DC gain with step
signal** is selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AmpStep` |
| **Type:** scalar |
| **Default:** 1 |

#### Block Tab

### **Reduce memory and avoid task overrun (external mode only)** — Deploy tuning algorithm only `off` (default) | `on`

The block contains two modules, one that performs the real-time frequency-response
estimation, and one that uses the resulting estimated response to tune the PID gains. When you
run a Simulink model containing the block in the external simulation mode, by default both
modules are deployed. You can save memory on the target hardware by deploying the estimation
module only (see Control Real-Time PID Autotuning in Simulink). In this case, the
tuning algorithm runs on the Simulink host computer instead of the target hardware. When this option is selected, the
deployed algorithm uses about a third as much memory as when the option is cleared.

The PID gain calculation demands more computational load than the frequency-response
estimation. For fast controller sample times, some hardware might not finish the gain
calculation within one execution cycle. Therefore, when using hardware with limited computing
power, selecting this option lets you tune a PID controller with a fast sample time.

Additionally, when you enable this option, there can be a delay of several sampling
periods between when the tuning experiment ends and when the new PID gains arrive at the
**pid gains** output port. Before pushing gains to the controller, first
confirm the change at the **pid gains** output port instead of using
**start/stop** signal as the trigger for the update.

If you intend to deploy the block and perform PID tuning without using external simulation
mode, do not select this option.

**Caution**

When you use this option, the model must be configured such that numeric block
parameters are tunable in generated code, not inlined. To specify tunable parameters:

- In the model editor: In **Configuration Parameters**, in **Code Generation** > **Optimization**, set **Default parameter behavior** to
  `Tunable`.
- At the command line: Use
  `set_param(mdl,'DefaultParameterBehavior','Tunable')`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DeployTuningModule` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Configure block for PLC Coder** — Configure block for code generation with Simulink PLC Coder off (default) | on

Select this parameter if you are using Simulink
PLC Coder to generate code for the autotuner block. Clear the parameter for code
generation with any other MathWorks® code-generation product.

Selecting this parameter affects internal block configuration only, for compatibility with Simulink
PLC Coder. The parameter has no operative effect on generated code.

### **Data Type** — Floating point precision `double` (default) | `single`

Specify the floating-point precision based on simulation environment or hardware
requirements.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BlockDataType` |
| **Type:** character vector |
| **Values:** `'double'` | `'single'` |
| **Default:** `'double'` |

### **Clicking "Update PID Block" writes tuned gains to the PID block connected to "u" port** — Automatically detect target for writing tuned PID coefficients `on` (default) | `off`

Under some conditions, the autotuner block can write tuned gains to a standard or
custom PID controller block. To indicate that the target PID controller is the block
connected to the **u** port of the autotuner block, select this option.
To specify a PID controller that is not connected to **u**, clear this
option.

To write tuned gains from the autotuner block to a PID controller anywhere in the
model, the target block must be either:

- A PID
  Controller or Discrete
  PID Controller block.
- A masked subsystem in which the PID coefficients are mask parameters named
  `P`, `I`, `D`, and
  `N`, or whatever subset of these parameters exist in the
  your controller. For example, if you use a custom PI controller, then you only
  need mask parameters `P` and `I`.

### **Specify PID block path** — Target PID controller block for writing tuned coefficients `[]` (default) | block path

Under some conditions, the autotuner block can write tuned gains to a standard or custom PID
controller block. Use this parameter to specify the path of the target PID controller.

To write tuned gains from the autotuner block to a PID controller anywhere in the model, the
target block must be either:

- A PID
  Controller or Discrete
  PID Controller block.
- A masked subsystem in which the PID coefficients are mask parameters named
  `P`, `I`, `D`, and
  `N`, or whatever subset of these parameters exist in your
  controller

#### Dependencies

This parameter is enabled when **Clicking "Update PID Block" writes tuned gains to the
PID block connected to "u" port** is selected.

### **Update PID Block** — Write tuned PID gains to target controller block button

The block does not automatically push the tuned gains to the target PID block. If your PID controller block meets the criteria described in the `Specify PID block path` parameter description, after tuning, click this button to transfer the tuned gains to the block.

You can update the PID block while the simulation is running, including when running in external mode. Doing so is useful for immediately validating tuned PID gains. At any time during simulation, you can change parameters, start the experiment again, and push the new tuned gains to the PID block. You can then continue to run the model and observe the behavior of your plant.

### **Export to MATLAB** — Send experiment and tuning results to MATLAB workspace button

When you click this button, the block creates a structure in the
MATLAB® workspace containing the experiment and tuning results. This
structure, `OnlinePIDTuningResult`, contains the following
fields:

- `P`, `I`, `D`,
  `N` — Tuned PID gains. The structure contains
  whichever of these fields are necessary for the controller type you
  are tuning. For instance, if you are tuning a PI controller, the
  structure contains `P` and `I`,
  but not `D` and `N`.
- `TargetBandwidth` — The value you specified in
  the **Target bandwidth (rad/sec)** parameter of the
  block.
- `TargetPhaseMargin` — The value you specified in
  the **Target phase margin (degrees)** parameter of
  the block.
- `EstimatedPhaseMargin` — Estimated phase margin
  achieved by the tuned system.
- `Controller` — The tuned PID controller, returned
  as a `pid` (for parallel
  form) or `pidstd` (for ideal
  form) model object.
- `Plant` — The estimated plant, returned as an
  `frd` model object.
  This `frd` contains the response data obtained at
  the experiment frequencies [1/3, 1, 3,
  10]*ωc*.
- `PlantNominal` — The plant input and output at
  the nominal operating point when the experiment begins, specified as
  a structure having fields `u` (input) and
  `y` (output).
- `PlantDCGain` — The estimated DC gain of the
  system in absolute units, if **Estimate DC gain with step
  signal** is selected during tuning.

You can export to the MATLAB workspace while the simulation is running, including when
running in external mode.
## Libraries

Simulink Control Design / Autotuning

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced in R2017b**

### R2023b: Library location changed

The Open-Loop PID Controller block is now in the **Simulink
Control Design/Autotuner** sublibrary.

In R2023b, when you open a model saved in a previous release, the library links
for Open-Loop PID Controller blocks update automatically.

## Description

Automatically tune PID gains based on plant frequency responses estimated from open-loop experiment in real time

The Open-Loop PID Autotuner block lets you tune a PID controller in
real time against a physical plant. The block can tune a PID controller to achieve a
specified bandwidth and phase margin without a parametric plant model or an initial
controller design. If you have a code-generation product such as Simulink®
Coder™, you can generate code that implements the tuning algorithm on hardware,
letting you tune in real time with or without using Simulink to manage the autotuning process.

If you have a plant model in Simulink, you can also use the block to obtain an initial PID design. Doing so lets
you preview plant response and adjust the settings for PID autotuning before tuning the
controller in real time.

To achieve model-free tuning, the Open-Loop PID Autotuner block:

1. Injects a test signal into the plant at the nominal operating point to collect plant input-output data and estimate frequency response in real time. The test signal is a combination of sine and step perturbation signals added on top of the nominal plant input measured when the experiment starts. If the plant is part of a feedback loop, the block opens the loop during the experiment.
2. At the end of the experiment, tunes PID controller parameters based on estimated plant
   frequency responses near the open-loop bandwidth.
3. Updates a PID Controller block or a custom PID controller with the tuned parameters, allowing you to validate closed-loop performance in real time.

Because the block performs an open-loop estimation experiment, do not use this block
with an unstable plant or a plant with multiple integrators.

To use the algorithm, you do not need an initial PID controller design. However, you
must have some way to get the plant to a nominal operating point for the
frequency-response estimation experiment. If you have an initial controller design, you
can use the Closed-Loop PID
Autotuner. For a comparison of closed-loop and open-loop PID autotuning, see
When to Use PID Autotuning.

The block supports code generation with Simulink
Coder, Embedded Coder®, and Simulink
PLC Coder™. It does not support code generation with HDL Coder™.

For more information about using the Open-Loop PID Autotuner block, see:

- PID Autotuning for a Plant Modeled in Simulink
- PID Autotuning in Real Time

For more general information about PID autotuning and a comparison of the closed-loop
and open-loop approaches, see When to Use PID Autotuning.
