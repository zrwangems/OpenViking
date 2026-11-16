---
type: simulink-block
title: 'ePWM Type 1-4'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Control Peripherals'
documentation_page: 'epwmtype14'
documentation_source_path: 'ref/epwmtype14.html'
language: en
---

# ePWM Type 1-4

## Ports

Not documented in R2025b.

## Parameters

### General

### **Allow use of 16 HRPWMs (for C28044) instead of 6 PWMs** — Enable HRPWM when PWM resolution is too low `off` (default) | `on`

Enable all 16 high-resolution PWM modules (HRPWM) on the C28044
digital signal controller when the PWM resolution is too low.

**Note**

Select this parameter only if you are using a C28044
processor.

For example, the Spectrum Digital eZdsp™ F28044 board has a system
clock of 100 MHz (200-kHz switching). At these frequencies, conventional
PWM resolution is too low, approximately 9 bits or 10 bits. By
comparison, the HRPWM resolution for the same board is 14.8 bits.

#### Dependencies

When you enable this parameter:

- Use the HRPWM parameters under the ePWMA tab to make
  additional configuration changes.
- Most of the configuration parameters under the ePWMB tab
  are unavailable.
- Your model can contain up to 16 C280x/C2803x/C2833x ePWM
  blocks, provided you configure each one for a separate
  module. (For example, **Module** is
  `ePWM1`, `ePWM2`, and
  so on.)
- Select this parameter only if you are using a C28044
  processor. To enable HRPWM for other processors, first
  determine how many HRPWM modules are available by consulting
  the Texas Instruments documentation for your processor. Then
  use the HRPWM parameters under the ePWMA tab to enable and
  configure the HRPWM.

### **Module** — Indicates which ePWM module to use `ePWM1` (default) | `ePWM2` | `ePWM3` | `…`

Select the appropriate ePWM module.
`ePWMx`, where
*x* can be 1,2,3....

**Note**

Number of module available will vary for different
processors.

### **ePWMLink TBPRD** — Indicates TBPRD linking of ePWM module `Not Linked` (default) | `ePWM2` | `ePWM3` | `…`

Select an ePWM module to which you want to link the current ePWM
module for timer period. When you link the two modules, the timer period
value in the linked ePWM module sets the value of the **Timer
period** parameter in the current module. The
**Timer period units**, **Specify timer
period via** , and the **Timer period**
parameters do not show when you select linking to another ePWM
module.

However, the linking has no effect when you link an ePWM module to a
module that does not exist in your model.

**Note**

This parameter is available only with some TI C2000™
processors.

### **Timer period units** — Indicates time period units `Clock cycles` (default) | `Seconds`

Specify the units of the **Timer period** or
**Timer initial period** parameters in
`Clock cycles` or `Seconds`. When
the parameter is set to `Seconds`, the software
converts the  **Timer period** or **Timer
initial period** from a value in seconds to a value in
clock cycles. For best results, select `Clock cycles`.
Doing so reduces the number of calculations and rounding errors.

#### Dependencies

- If you set **Timer period units** to
  `Seconds`, enable support for
  floating-point numbers. In the model window, select
  **Modeling > Model
  Settings**.
- In the Configuration Parameters dialog box, select
  **Code Generation >
  Interface**. Under **Software
  Environment**, enable **floating-point
  numbers**.

### **Specify timer period via** — Configure source of timer period value `Specify via dialog` (default) | `Input port`

When you select `Input port`, the
**Timer period** parameter changes to
**Timer initial period** and creates a timer period
input port, **T**, on the block.

### **Timer period** — Indicates period of ePWM counter `64000` (default)

Set the period of the ePWM counter waveform. The resultant ePWM
waveform period depends on the settings of the **Action when
counter=** parameters on the **ePWMx**
tab.

When you enable the HRPWM, you can enter a high-precision
floating-point value. The time-base period high resolution register
(TBPRDHR) stores the high-resolution portion of the timer period
value.

The timer period is calculated based on the **Counting
mode** selection and **Timer period
units**, as shown.

| Count Mode | Timer period units | Calculation | Example |
| --- | --- | --- | --- |
| Up or Down | Clock cycles | The value entered in clock cycles is used to calculate time-base period (TBPRD) for the ePWM timer register. The period of the ePWM timer TCTR = (TBPRD + 1) \* TBCLK. Where TCTR is the timer period in seconds, and TBCLK is the time-base clock. | For ePWM clock (EPWMCLK) frequency = 200 MHz and TBCLK = 5 ns.  EPWMCLK will be equal to SYSCLKOUT or SYSCLKOUT/2 depending on the **EPWM clock divider (EPWMCLKDIV)** parameter setting.  When the timer period is entered in clock cycles TBPRD = 9999, and the ePWM timer period is calculated as TCTR = 50 µs.  For the default action settings on the **ePWMx** tab, the ePWM period = 50 µs. |
| Seconds | The value entered in seconds is used to calculate the time-base period (TBPRD) for the ePWM timer register. The TBPRD value entered in the register is TBPRD = (TCTR / TBCLK) – 1. Where, TCTR is the timer period in seconds and TBCLK is the time-base clock.  For the default action settings on the **ePWMx** tab, the ePWM period is the same as the timer period (in seconds) entered. | For EPWMCLK frequency = 200 MHz and TBCLK = 5 ns.  When the timer period is entered in seconds TCTR = 50 µs and the time based period is calculated as TBPRD = 9999.  For the default action settings in the **ePWMx** tab, the ePWM period = 50 µs. |
| Up-Down | Clock cycles | The value entered in clock cycles is used to calculate the time-base period (TBPRD) for the ePWM timer register. The period of the ePWM timer, TCTR = 2 \* TBPRD \* TBCLK. Where TCTR is the timer period in seconds and TBCLK is the time-base clock. | For EPWMCLK frequency = 200 MHz and TBCLK = 5 ns.  When the timer period is entered in clock cycles, TBPRD = 10000, and the ePWM timer period is calculated as TCTR = 100 µs.  For the default action settings on the **ePWMx** tab, the ePWM period = 100 µs. |
| Seconds | The value entered in seconds is used to calculate the time-base period (TBPRD) for the ePWM timer register. The TBPRD value entered in the register is TBPRD = TCTR / TBCLK. Where TCTR is the timer period in seconds and TBCLK is the time-base clock.  For the default action settings on the **ePWMx** tab, the ePWM period is two times the timer period (in seconds) entered. | For EPWMCLK frequency = 200 MHz and TBCLK = 5 ns.  When the timer period is entered in seconds TCTR = 50 µs, and the time based period is calculated as TBPRD = 10000.  For the default action settings on the **ePWMx** tab, the ePWM period = 100 µs. |

### **Timer initial period** — Indicates initial ePWM period of the waveform `64000` (default) | `0` | `...`

The initial period of the waveform from the time the PWM peripheral
starts operation until the ePWM input port, **T**,
receives a new value for the period. Use **Timer period
units** to measure the period in clock cycles or in
seconds. The timer period is calculated similar to the **Timer
period** parameter.

#### Dependencies

To enable this parameter, set the **Specify timer period
via** parameter to `Input
port`.

### **Active period register load option (PRDLD)** — Event at which counter period register is reloaded `Counter equals to zero` (default) | `Counter equals to zero or SYNC event` | `SYNC event` | `Immediate without using shadow`

This parameter provides an option to select the appropriate event to
update the time period register with a new value.

- `Counter equals to zero` - The
  counter period refreshes when the value of the counter is
  0.
- `Counter equals to zero or SYNC
  event` - When counter is 0 or when there is
  a synchronization event.
- `SYNC event` - The parameter is
  in synchronization.
- `Immediate without using shadow`
  - The counter period refreshes immediately.

### **Counting mode** — Indicates counting mode of ePWM counter `Up-Down` (default) | `Up` | `Down`

Specify the counting mode. This PWM module can operate in three
distinct counting modes: `Up`,
`Down`, and
`Up-Down`.

This illustration shows the waveforms that correspond to these three modes:

#### Dependencies

The `Down` option is not compatible with
HRPWM. To avoid an error when you build the model, do not set the
**Counting mode** parameter to
`Down` and select the **Enable
HRPWM (Period)** parameter.

### **Synchronization action** — Specify source of phase offset `Disable` (default) | `Set counter to phase value specified via dialog` | `Set counter to phase value specified via input port`

Specify the source of a phase offset to apply to the time-base
synchronization input signal EPWMxSYNCI from the
**SYNC** input port.

- `Set counter to phase value specified via
  dialog` - Specify this option to create the
  **Phase offset value** parameter.

  **Note**

  - The ePWM block expects the phase value in
    the range of 0 to 360 deg values scaled with clock
    cycles as input to the phase values. Hence for the
    negative values you need to add 360 deg to bring
    it to the range of 0 to 360 deg phase. Example,
    for -90 deg value, you will have to provide (360 -
    90) = 270 deg scaled with clock cycles as
    input.
  - For any values greater than 360 deg you need
    to consider the logic to wrap the value to the
    scale of 0 to 360 deg. For example, 120 + (360 -
    90) = 390 should be wrapped as (390 - 360) = 30
    deg before scaling it with clock cycles and
    providing it as input to ePWM.
- `Set counter to phase value specified via input
  port` - Specify this option to create a phase
  input port, **PHS**, on the block.
- `Disable` - Specify this option to
  prevent the application of phase offsets to the TB
  module.

### **Counting direction after phase synchronization** — Counter direction after phase synchronization `Count down after sync` (default) | `Count up after sync`

Configure the timer to count up or down, following synchronization.
This parameter corresponds to the phase direction (PHSDIR) field of the
Time-base Control Register (TBCTL).

#### Dependencies

This parameter appears when **Counting mode** is
`Up-Down` and **Synchronization
action** is `Set counter to phase value
specified via dialog` or `Input port`.

### **Phase offset value (TBPHS)** — Specify Phase offset value (TBPHS) `0` (default)

The specified offset value is loaded in the time base counter on a
synchronization event.

To enable this parameter, select the `Set counter to phase
value specified via dialog` in the
**Synchronization action** parameter.

Enter the `Phase offset value (TBPHS)` in
**TBCLK** cycles from 0 to 65535. While using
HRPWM, you may enter decimal values.

**Note**

- The ePWM block expects the phase value to be in the
  range of 0 to 360 degrees scaled with clock cycles. For
  the negative values you need to add 360 degrees to bring
  it to the range of 0 to 360 degrees phase range. For
  example, for -90 degrees value, you will have to provide
  (360 - 90) = 270 degrees scaled with clock cycles as an
  input.
- For any values greater than 360 degrees you need to
  consider the logic to wrap the value to the scale of 0
  to 360 degrees. For example, 120 + (360 - 90) = 390
  should be wrapped as (390 - 360) = 30 degrees before
  scaling it with clock cycles and providing it as an
  input.

This parameter corresponds to the Time-Base Phase Register
(TBPHS).

### **Specify software synchronization via input port (SWFSYNC)** — Indicates phase offset value `off` (default) | `on`

Create an input port, **SYNC**, for a time-base
synchronization input signal, EPWMxSYNCI. Select this parameter to
achieve precise synchronization across multiple ePWM modules by
daisy-chaining multiple time-base (TB) submodules.

### **Enable digital compare A event1 synchronization (DCAEVT1)** — Synchronize ePWM time based on DCAEVT1 digital compare event `off` (default) | `on`

Select this parameter to synchronize this PWM module to the time base
of another PWM module. Fine-tune the synchronization between the two
modules using the **Phase offset value**. Enabling
HRPWM disables this option.

**Note**

This parameter is available only for specific
`C28x` devices.

### **Enable digital compare B event1 synchronization (DCBEVT1)** — Synchronize ePWM time based on DCBEVT1 digital compare event `off` (default) | `on`

Select this parameter to synchronize this PWM module to the time base
of another PWM module. Fine-tune the synchronization between the two
modules using the **Phase offset value**. This option
is not compatible with `HRPWM`. Enabling
`HRPWM` disables this option.

**Note**

This parameter is available only for specific
`C28x` devices.

### **Synchronization output (SYNCO)** — Event which generates a time base synchronization output signal `Disable` (default) | `Pass through (EPWMxSYNCI or SWFSYNC)` | `Counter equals to zero (CTR=Zero)` | `Counter equals to compare B (CTR=CMPB)` | `Counter equals to compare C (CTR=CMPC)` | `Counter equals to compare D (CTR=CMPD)` | `Enable DCBEVT1 sync event to SYNCO signal` | `Enable DCAEVT1 sync event to SYNCO signal` | `Enable counter equals to compare D (CTR=CMPD) event to set SYNCO signal` | `Enable counter equals to compare C (CTR=CMPC) event to set SYNCO signal` | `Enable counter equals to compare B (CTR=CMPB) event to set SYNCO signal` | `Enable counter equals to zero (CTR=ZERO) event to set SYNCO signal` | `Enable SWFSYNC event to set SYNCO signal`

Time-base counter synchronization allows for increased flexibility of
synchronization of the ePWM modules. The clock synchronization scheme
allows ePWM modules to operate as a single system when required.
Additionally, this synchronization scheme can be extended to the capture
peripheral submodules (eCAP). In Type 4 ePWM, there are two types of
time-base counter synchronization scheme available. For more
information, see Time-Base Counter Synchronization.

You can configure additional SYNCO options in Configuration
Parameters. For more, see C28x-ePWM.

This parameter corresponds to the SYNCOSEL field in the Time-Base
Control Register (TBCTL).

**Note**

The parameters for synchronization output (SYNCO) vary based
on the processor selected.

The following parameters are available only for
`F2837x`, `F2807x`,
`F28004x` and specific `C28x`
processors.

- `Pass through (EPWMxSYNCI or SWFSYNC)` —
  synchronization input pulse or software-forced
  synchronization pulse, respectively. You can use this option
  to achieve precise synchronization across multiple ePWM
  modules by daisy-chaining multiple time-base (TB)
  submodules.
- `Counter equals to zero (CTR=Zero)` —
  Time-base counter equal to zero (TBCTR = 0x0000)
- `Counter equals to compare B (CTR=CMPB)`
  — Time-base counter equal to counter-compare B (TBCTR =
  CMPB)
- `Counter equals to compare C (CTR=CMPC)`
  — Time-base counter equal to counter-compare C (TBCTR =
  CMPC)
- `Counter equals to compare D (CTR=CMPD)`
  — Time-base counter equal to counter-compare D (TBCTR =
  CMPD)
- `Disable` — Disable the EPWMxSYNCO output
  (the default)

The following parameters are only specific to F2838x, F28002x and
F28003x processors.

- `Enable DCBEVT1 sync event to SYNCO
  signal` - Select to synchronize digital
  compare event B to the synchronization output.
- `Enable DCAEVT1 sync event to SYNCO
  signal` - Select to synchronize digital
  compare event A to the synchronization output.
- `Enable counter equals to compare D (CTR=CMPD)
  event to set SYNCO signal` - enables the
  counter equals to compare D (CTR=CMPD) event to set the
  SYNCO signal
- `Enable counter equals to compare C (CTR=CMPC)
  event to set SYNCO signal` - enables the
  counter equals to compare C (CTR=CMPC) event to set the
  SYNCO signal
- `Enable counter equals to compare B (CTR=CMPB)
  event to set SYNCO signal` - enables the
  counter equals to compare B (CTR=CMPB) event to set the
  SYNCO signal
- `Enable counter equals to zero (CTR=ZERO)
  event to set SYNCO signal` - enables the
  counter equals to zero (CTR=ZERO) event to set the SYNCO
  signal
- `Enable SWFSYNC event to set SYNCO
  signal` - enables the software-forced
  synchronization pulse (SWFSYNC) event to set the SYNCO
  signal

### **Peripheral synchronization event (PWMSYNCSEL)** — Time-Base Counter Peripheral Synchronization `Counter equals to period (CTR=PRD)` (default) | `Counter equals to zero (CTR=Zero)` | `Counter is incrementing and equals to compare C register (CTRU=CMPC)` | `Counter is decrementing and equals to compare C register (CTRD=CMPC)` | `Counter is incrementing and equals to compare D register (CTRU=CMPD)` | `Counter is decrementing and equals to compare D register (CTRD=CMPD)`

Each ePWM module has a peripheral synchronization output (SYNCPER).
This output signal is used to synchronize the CMPSS to the EPWM. For
more information, see Time-Base Counter Peripheral Synchronization.

**Note**

This parameter is available only with some specific
`C28x` processors.

### **Time base clock (TBCLK) prescaler divider** — Time base clock (TBCLK) prescaler divider corresponding to CLKDIV `1` (default) | `2` | `4` | `…`

Use the **Time base clock (TBCLK) prescaler divider**
(CLKDIV) and the **High speed time base clock (HSPCLKDIV)
prescaler divider** (HSPCLKDIV) to configure the Time-base
clock speed (TBCLK) for the ePWM module. Calculate TBCLK using this
equation:

TBCLK in Hz = PWM clock in Hz/(HSPCLKDIV \* CLKDIV)

For example, the default values of both CLKDIV and HSPCLKDIV are 1,
and the default frequency of PWM clock is 100 MHz, so:

TBCLK in Hz = 100 MHz/(1 \* 1) = 100 MHz

TBCLK in seconds = 1/TBCLK in Hz = 1/100 MHz = 0.01 μs

The choices for the **Time base clock (TBCLK) prescaler
divider** are: `1`,
`2`, `4`,
`8`, `16`,
`32`, `64`, and
`128`.

The **Time block clock (TBCLK) prescaler divider**
parameter corresponds to the CLKDIV field of the Time-base Control
Register (TBCTL).

The PWM clock is the SYSCLKOUT or a clock derived from SYSCLKOUT using
the PWM clock divider. For a few TI C2000 processors, there is a PWM
clock divider that divides the SYSCLKOUT to derive the PWM module clock.
Check the technical reference manual of your processor for more details.

The frequency of SYSCLKOUT depends on the oscillator frequency and the
configuration of the PLL-based clock module. Changing the value of
SYSCLOCKOUT affects the timing of all the ePWM modules. If there is a
PWM clock prescale available in the processor, changing its value also
affects the PWM timing.

### **High speed time base clock (HSPCLKDIV) prescaler divider** — High speed time base clock (HSPCLKDIV) prescaler divider `1` (default) | `2` | `4` | `...`

The choices for the **High speed time base clock (HSPCLKDIV)
prescaler divider** are: `1`,
`2`, `4`,
`6`, `8`,
`10`, `12`, and
`14`.

Selecting **Enable high resolution PWM (HRPWM –
period)** sets the value of this parameter to
`1`.

This parameter corresponds to the HSPCLKDIV field of the Time-base
Control Register (TBCTL).

### **Enable swap module A and B** — Swap output signals for module A and B `off` (default) | `on`

Swap the ePWMA and ePWMB outputs. When you select this parameter, the
block outputs the ePWMA signals on the ePWMB outputs and the ePWMB
signals on the ePWMA outputs.

This parameter, sets the SWAPB field in the HRPWM Configuration
Register (HRCNFG). This option works in for ePWMs that support HRPMW as
it uses the HRCNFG register.

**Note**

This parameter is available only for specific
`C28x` devices.

### ePWMA and ePWMB

You can perform waveform generation configuration in ePWMA/ePWMB tab along with
Counter compare tab.

The ePWM hardware module can generate waveforms for A and B channels followed by
Deadband module and HRPWM module for waveform generation.

During waveform generation you can generate waveform for ePWMA and ePWMB but these
waveform options can be overridden by the options selected in Deadband
configuration. For example, you can choose not to configure the eWPMB in waveform
generation module but use eWPMA waveform to create Deadband outputs for both ePWMA
and ePWMB channels.

### **Enable ePWM#x** — Enables ePWMx output signals `off` (default) | `on`

Enables the ePWMA and/or ePWMB output signals for the ePWM module
selected on the **General** tab. In this case, #
represents the ePWM module and x represents A or B. By default,
**Enable ePWM#A** is enabled, and **Enable
ePWM#B** is disabled.

Each ePWM module has two outputs, ePWMA and ePWMB. The ePWMA output
tab and ePWMB output tab include the same settings, although the default
values vary in some cases.

#### Dependencies

When you select **Enable ePWM#A** or
**Enable ePWM#B**, enable support for
floating-point numbers by browsing to **Configuration
Parameters** > **Code
Generation** >
**Interface** > **Software
Environment**.

### **Action when counter=ZERO, Action when counter=period (PRD), Action when counter=CMPA on up-count (CAU), Action when counter=CMPA on down-count (CAD), Action when counter=CMPB on up-count (CBU), Action when counter=CMPB on down-count (CBD)** — Determine Action Qualifier (AQ) submodule behavior `Set` (default)

This group of parameters on the **ePWMA
output** and **ePWMB output**
tabs determine the behavior of the Action Qualifier (AQ) submodule. The
AQ module determines which events are converted into one of the various
action types, producing the required switched waveforms of the ePWM#A
and ePWM#B output signals.

These parameters can be specified as `Do
nothing`, `Clear`,
`Set`, or
`Toggle`.

The default values vary between the **ePWMA**
and **ePWMB** tabs.

This table shows the default value for each of these tabs when you set
the **Counting mode** to `Up`
or `Up-Down`:

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Set | Clear |
| period (PRD) | Clear | Set |
| CMPA on up-count (CAU) | Clear | Set |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on up-count (CBU) | Do nothing | Clear |
| CMPB on down-count (CBD) | Do nothing | Set |

This table shows the defaults for each of these tabs when you set
**Counting mode** to
`Down`:

| Action when counter = | ePWMA | ePWMB |
| --- | --- | --- |
| ZERO | Do nothing | Do nothing |
| period (PRD) | Clear | Clear |
| CMPA on down-count (CAD) | Set | Do nothing |
| CMPB on down-count (CBD) | Do nothing | Set |

For a detailed discussion on the AQ submodule, consult
the *TMS320x280x Enhanced Pulse Width Modulator (ePWM) Module
Reference Guide* (SPRU791), available on the Texas Instruments website.

### **Add continuous software force input port, Continuous software force logic, Reload condition for software force** — Determines how action-qualifier (AQ) submodule handles S/W force event `Load on counter equals to zero (CTR=Zero)` (default)

These parameters determine how the action-qualifier (AQ) submodule
handles the S/W force event, an asynchronous event initiated by software
(CPU) via control register bits.

**Compare value reload condition** determines if and
when to reload the action-qualifier S/W force register from a shadow
register. You can specify one of the following `Load on
counter equals to zero (CTR=Zero)` (default),
`Load on counter equals to period
(CTR=PRD)`, `Load on either`,
and `Freeze`.

**Add continuous software force input port** creates
an input port, **SFA**, which you can use to control
the software force initial logic. Send one of the following values to
**SFA** as an unsigned integer data type:

- 0 = `Forcing disable`: Do
  nothing(default).
- 1 = `Forcing low`: Clear
  low
- 2 = `Forcing high`: Set
  high
- 3 = `Forcing disable`: Do
  nothing

**Continuous software force logic** - If you did not
create the **SFA** input port, you can use to select
which type of software force initial logic to apply. You can specify one
of the following:

- `Forcing disable`: Do nothing
  (default).
- `Forcing low`: Clear low
- `Forcing high`: Set high

**Reload condition for software force**

You can specify one of the following `Counter equals to
zero (CTR=Zero)` (default), `Counter equals
to period (CTR=PRD)`, `Either period or
zero`, and `Immediate`.

### **Inverted version of ePWM#A** — Invert ePWM#A signal `off` (default) | `on`

Invert the ePWM#A signal and output it on the ePWM#B outputs.

This parameter sets the SELOUTB field in the HRPWM Configuration
Register (HRCNFG) and will work for ePWMs with HRPWM support as it uses
the HRCNFG register.

**Note**

This parameter is available only for ePWM modules which have
HRPWM submodule. Enabling this parameter inverts ePWM#B
irrespective of whether HRPWM is enabled or not in the
module.

### **Enable high resolution PWM (HRPWM)** — Enables high resolution PWM settings `off` (default) | `on`

#### Dependencies

- This parameter is available only for
  **ePWMx** tabs for C280x and C2833x
  processors and in **HRPWM** tab for the
  rest of the processors. For more information, refer to
  HRPWM tab section.
- Similarly, parameters such as **High
  resolution PWM (HRPWM) loading mode**,
  **High resolution PWM (HRPWM) control
  mode**, **High resolution PWM
  (HRPWM) edge control mode** and
  **Use scale factor optimizer (SFO)
  software** feature in
  **ePWMx** tabs for C280x and C2833x
  processors and in **HRPWM** tab for
  rest of the processors. For more information, refer to
  HRPWM tab section.

### Counter Compare

### **ePWMLink CMPx** — Linking of ePWM module `Not Linked` (default) | `ePWM1` | `ePWM2` | `...`

In ePWMx, where x ranges from 1 to 12

Select an ePWM module to which you want to link the current ePWM
module for counter value. In this case for CMPx, x represents A, B, C,
or D. When you link the counter value of an ePWM module with another,
the **CMPx value** of the linked ePWM module is used in
the current module. The **CMPx**, **Specify
CMPx via**, and **CMPx value** parameters
do not appear when you select another ePWM module for linking.

However, the linking has no effect when you link an ePWM module to a
module that does not exist in your model.

**Note**

This parameter is available only with some of the TI's C2000
processors.

### **CMPx Units** — Units used by compare registers `Clock cycles` (default) | `Percentages`

The four compare registers CMPA, CMPB, CMPC, and CMPD are compared
with the time-base counter value to generate appropriate events. CMPA
and CMPB events are used for controlling the PWM duty cycle by selecting
appropriate actions on the **ePWMA** and
**ePWMB** tabs. These events can also be used to
generate an interrupt to the CPU and/or a start of conversion pulse to
the ADC. You can refer to the **Event Trigger** tab to
select the events to be triggered.

Compare registers **CMPC** and
**CMPD** are present only in the latest
processors.

**Notes**

- The term *clock cycles* refers to the
  time-base clock on the processor. See the **TB clock
  prescaler divider** topic for an explanation of
  time-base clock speed calculations.
- Percentages use additional computation time in generated
  code and can decrease accuracy of the results.

#### Dependencies

If you set ***CMPx units***
to `Percentages`, enable support for
floating-point numbers by browsing to **Configuration
Parameters** > **Code
Generation** >
**Interface** > **Software
Environment**. In this case, x represents A, B, C, or
D.

### **Specify CMPx Via** — Pulse width source `Specify via dialog` (default) | `Input port`

Specify the source of the pulse width. If you select
`Specify via dialog` (the default), enter a
value for the **CMPx value** parameter. If you select
`Input port`, the block creates a new Input
port with name WA, WB, WC or WD on the block. If you select
`Input port`, make sure to set the
**CMPx initial value** parameter. In this case, x
represents A, B, C, or D.

### **CMPx Value/CMPx Initial Value** — Pulse width value `32000` (default)

**CMPx Value** field appears when you set
**CMPx source** to `Specify via
dialog`. **CMPx Initial Value** field
appears when you set **CMPx source** to
`Input port`. Enter a value that specifies
the pulse width, in the units specified in **CMPx
units**. In this case, x represents A, B, C, or D.

Enter the initial pulse width of CMPA or CMPB that the PWM peripheral
uses when it starts operation. Subsequent inputs to the
**WA** or **WB** ports change the
CMPA or CMPB pulse width.

### **Reload for compare x Register (SHDWxMODE)** — Time at which the counter period is reset `Counter equals to zero (CTR=Zero)` (default) | `Counter equals to period (CTR=PRD)` | `Counter equals to Zero or period (CTR=Zero or CTR=PRD)` | `...`

The time at which the counter period is reset. In this case, x
represents A, B, C, or D.

- `Counter equals to zero
  (CTR=Zero)` — Refreshes the counter
  period when the value of the counter is 0.
- `Counter equals to period
  (CTR=PRD)` — Refreshes the counter
  period when the value of the counter is period.
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` — Refreshes the counter
  period when the value of the counter is 0 or period.
- `Freeze` — Refreshes the
  counter period when the value of the counter is
  freeze.
- `Counter equals to zero or SYNC
  event` — Refreshes the counter
  period when the value of the counter is zero or SYNC.
- `Counter equals to period or SYNC
  event` — Refreshes the counter
  period when the value of the counter is 0 or SYNC.
- `Counter equals to zero or period or SYNC
  event` — Refreshes the counter
  period when the value of the counter is 0 or period or
  SYNC.
- `SYNC event` — Refreshes
  the counter period when the value of the counter is
  SYNC.
- `Immediate without using shadow`
  — Refreshes the counter period immediately.

### Deadband Unit

### **Use deadband for ePWM#A, Use deadband for ePWM#B** — Enables deadband area `off` (default) | `on`

Enables a deadband area of rising edge delay or falling edge delay
cycles without signal overlap between pairs of ePWM output signals.
Ensure that the corresponding **ePWMx (x=A or B)** are
enabled on the ePWMx tabs to generate the DB for the same.

### **Enable half-cycle clocking** — Double deadband resolution `off` (default) | `on`

Enable half-cycle clocking to double the deadband resolution. This
option clocks the deadband counters at TBCLK\*2 I.e it will divide the
clock value in seconds by 2, which in turn doubles the frequency.

When you disable this option, the deadband counters use full-cycle
clocking (TBCLK\*1).

**Note**

This parameter is available only specific C28x devices.

### **Deadband Polarity** — ePWM output state at deadband time `Active high (AH)` (default) | `Active low (AL)` | `Active high complementary (AHC)` | `Active low complementary (ALC)`

When you enable only one ePWM for deadband polarity, you will see the
options `Positive` and
`Negative`.

When you enable both the ePWM for deadband polarity, then you will see
the options `Active high (AH)`,
`Active low (AL)` , `Active
high complementary (AHC)` or `Active low
complementary (ALC)`.

AT the deadband time, both the ePWMA and ePWMB outputs have to set to
an inactive state. Depending on your hardware settings, the inactive
states can correspond to a high or a low logic value. Active high means
that the system is active when the ePWM output is set to a high logic
value. Active low means that the system is active when the ePWM output
is set to a low logic value. Use the Complementary option when the B
signal needs to be the inverse of A. For more information, refer to the
ePWM technical reference guide of your processor.

This diagram shows the waveforms for typical cases where 0% < duty
< 100%.

### **Signal source for rising edge (RED)** — Raising edge source `ePWMxA` (default) | `ePWMxB`

Select the signal source to which rising edge delay (RED) has to be
applied. You can either select ePWMxA or ePWMxB for raising edge.

### **Signal source for falling edge (FED)** — Falling edge source `ePWMxA` (default) | `ePWMxB`

Select the signal source to which falling edge delay (FED) has to be
applied. You can either select ePWMxA or ePWMxB for falling edge.

### **Deadband period units** — Indicates deadband period units `Clock cycles` (default) | `Seconds`

Specify the units of the **Deadband period** as
`Clock cycles` or `Seconds`. When
**Deadband period units** is set to
`Seconds`, the software converts the **Deadband period** from a value in seconds to a value in
clock cycles. For best results, select `Clock cycles`.
Doing so reduces calculations and rounding errors.

#### Dependencies

- If you set **Deadband period units**
  to `Seconds`, enable support
  for floating-point numbers. In the model window, select
  **Simulation > Model Configuration
  Parameters**.

  In the Configuration Parameters dialog box, select
  Code Generation > Interface. Under **Software
  Environment**, enable
  **floating-point numbers**.
- This parameter is available only with some of the TI’s
  C2000™ processors.

### **Deadband period source** — Source of control logic `Specify via dialog` (default) | `Input port`

Select the source of the **Deadband period** as
`Specify via dialog` or `Input
port`.

### **Deadband Rising edge (RED) period (0-16383)** — RED delay time value `0` (default)

The value you enter in the field specifies the deadband delay in
time-base clock.

The outcome of the **Deadband rising edge period
(0-16383)** parameter depends on the `Deadband
period units` and `Deadband period
source`.

The following table illustrates the deadband rising edge period result
based on the selection of `deadband unit`,
`deadband source` and the
`processor` selected.

| Deadband period units | Deadband period source | Deadband rising edge(RED) period |
| --- | --- | --- |
| Clock cycles | Specify via dialog | Deadband Rising edge (RED) period (0~16383) |
| Deadband Rising edge (RED) period (0~1023) |
| Clock cycles | Input port | Deadband Rising edge (RED) initial period (0~16383) |
| Deadband Rising edge (RED) initial period (0~1023) |
| Seconds | Specify via dialog | Deadband Rising edge (RED) period |
| Deadband Rising edge (RED) period |
| Seconds | Input port | Deadband Rising edge (RED) initial period: |
| Deadband Rising edge (RED) initial period: |

### **Deadband Falling edge (FED) period** — FED delay time value `0` (default)

The value you enter in the field specifies the dead band delay in
time-base clock.

The parameter **Deadband falling edge period**
outcome depends on the `Deadband period units` and
`Deadband period source`. The **Deadband
falling edge period** values are similar to
**Deadband rising edge period**. For more
information refer to deadband rising edge (RED) period parameter.

### **Reload for DBRED register (SHDWDBRED), Reload for DBFED register (SHDWDBFED)** — Event at which shadow register is transferred to active register `Immediate without using shadow` (default) | `Freeze` | `Counter equals to zero (CTR=Zero)` | `Counter equals to period (CTR=PRD)` | `Counter equals to either zero or period (CTR=Zero or CTR=PRD)` | `...`

The event at which the shadow register is transferred to the active
register and the counter period is reset.

- `Immediate without using shadow`
  — Refreshes the counter period immediately.
- `Counter equals to zero
  (CTR=Zero)` — Refreshes the counter
  period when the value of the counter is 0.
- `Counter equals to period
  (CTR=PRD)` — Refreshes the counter
  period when the value of the counter is period.
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` — Refreshes the counter
  period when the value of the counter is 0 or period.
- `Freeze` — Refreshes the
  counter period when the value of the counter is
  freeze.

#### Dependencies

**SHDWDBRED** and **SHDWDBFED**
are available only when the**Use deadband for
ePWM#A** or **Use deadband for
ePWM#B** is selected.

### Event Trigger

### **Enable ADC start of conversion for module A** — Start of ADC conversion event `off` (default) | `on`

When you select this option, ADC Start of Conversion Event (ePWMSOCxA)
is generated when the event selected in the **Start of
conversion for module A event selection** parameter occurs.

### **Number of event for start of conversion for Module A (SOCA) to be generated** — Event start number `First event` (default) | `Second event` | `Third event` | `...`

When you select **Enable ADC start of conversion for module
A**, this field specifies the number of the event that
triggers ADC Start of Conversion for Module A (SOCA).

`First event` triggers ADC start of conversion
with every event (the default). `Second event`
triggers ADC start of conversion with every second event.
`Third event` triggers ADC start of
conversion with every third event.

Event triggers ranges from `First event` to
`Fifteenth event` based on the processor
selected.

### **Start of conversion for module A event selection** — Indicates counter match condition that triggers ADC start of conversion event `Counter equals to zero (CTR=Zero)` (default) | `Digital Compare Module A Event 1 start of conversion (DCAEVT1.soc)` | `...`

This parameter specifies the counter match condition that triggers an
ADC start of conversion event. The choices are:

- `Digital Compare Module A Event 1 start of
  conversion (DCAEVT1.soc)(For specific C28x devices
  only)` - When the ePWM asserts a DCAEVT1 or
  DCBEVT1 digital compare event. Use this feature to
  synchronize the selected PWM module to the time base of
  another PWM module. Fine-tune the synchronization between
  the two modules using the **Phase offset
  value** parameter.
- `Counter equals to zero (CTR=Zero)` -
  When the ePWM counter reaches zero (the default for few
  processors).
- `Counter equals to period (CTR=PRD)` -
  When the ePWM counter reaches the period value.
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - When the time base counter reaches
  zero (TBCTR = 0x0000) or when the time base counter reaches
  the period (TBCTR = TBPRD).
- `Counter is incrementing and equals to the compare
  x register (CTRU=CMPx)` - The ePWM counter
  reaches the compare value x on the way up. In this case, x
  represents A, B, C, or D.
- `Counter is decrementing and equals to the compare
  x register (CTRD=CMPx)` - The ePWM counter
  reaches the compare value x on the way down. In this case, x
  represents A, B, C, or D.

### **Enable ADC start of conversion for module B** — Start of ADC conversion event `off` (default) | `on`

When you select this option, ADC Start of Conversion Event (ePWMSOCxB)
is generated when the event selected in the **Start of
conversion for module B event selection** parameter occurs.

### **Number of event for start of conversion for Module B (SOCB) to be generated** — Event start number `First event` (default) | `Second event` | `Third event` | `...`

When you select **Enable ADC start of conversion for module
B**, this field specifies the number of the event that
triggers ADC Start of Conversion for Module B (SOCB).

`First event` triggers ADC start of conversion
with every event (the default). `Second event`
triggers ADC start of conversion with every second event.
`Third event` triggers ADC start of
conversion with every third event.

Event triggers ranges from `First event` to
`Fifteenth event` based on the processor
selected.

### **Start of conversion for module B event selection** — Indicates the counter match condition that triggers an ADC start of conversion event `Counter equals to zero (CTR=Zero)` (default) |

When you select **Enable ADC start of conversion for module
B**, this field specifies the counter match condition that
triggers an ADC start of conversion event. The choices are:

- `Digital Compare Module B Event 1 start of
  conversion (DCBEVT1.soc) (For specific C28x devices
  only)` - When the ePWM asserts a DCAEVT1 or
  DCBEVT1 digital compare event. Use this feature to
  synchronize the selected PWM module to the time base of
  another PWM module. Fine-tune the synchronization between
  the two modules using the **Phase offset
  value**.
- `Counter equals to zero (CTR=Zero)` -
  When the ePWM counter reaches zero (the default for few
  processors).
- `Counter equals to period (CTR=PRD)` -
  When the ePWM counter reaches the period value.
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - When the time base counter reaches
  zero (TBCTR = 0x0000) or when the time base counter reaches
  the period (TBCTR = TBPRD).
- `Counter is incrementing and equals to the compare
  x register (CTRU=CMPx)` - The ePWM counter
  reaches the compare value x on the way up. In this case, x
  represents A, B, C, or D.
- `Counter is decrementing and equals to the compare
  x register (CTRD=CMPx)` - The ePWM counter
  reaches the compare value x on the way down. In this case, x
  represents A, B, C, or D.

### **Enable ePWM interrupt** — Generates ePWM interrupts `Disabled` (default) | `Enabled`

Select this option to generate ePWM interrupts based on different
events defined by **Number of event for interrupt to be
generated** and **Interrupt counter match event
condition**. By default, the software clears (disables)
this option.

### **Number of event for interrupt to be generated** — Specifies the number of the event that triggers the ePWM interrupt `First event` (default) | `Second event to fifteenth event`

When you select ***Enable ePWM
interrupt***, this field specifies the number of
the event that triggers the ePWM interrupt: `First
event` triggers ePWM interrupt with every event (the
default), `Second event` triggers ePWM
interrupt with every second event, and `Third
event` triggers ePWM interrupt with every third
event.

**Note**

Event triggers ranges from `First event` to
`Fifteenth event` based on the processor
selected.

### **Interrupt counter match event condition** — Indicates the counter match condition that triggers ePWM interrupt `Counter equals to zero (CTR=Zero)` (default)

When you select ***Enable ePWM
interrupt***, this field specifies the counter
match condition that triggers ePWM interrupt. The choices are the same
as for **Module A counter match event condition**. The
choices are:

- `Counter equals to zero (CTR=Zero)` -
  When the ePWM counter reaches zero (the default for few
  processors).
- `Counter equals to period (CTR=PRD)` -
  When the ePWM counter reaches the period value.
- `Counter equals to zero or period (CTR=Zero or
  CTR=PRD)` - When the time base counter reaches
  zero (TBCTR = 0x0000) or when the time base counter reaches
  the period (TBCTR = TBPRD).
- `Counter is incrementing and equals to the compare
  x register (CTRU=CMPx)` - The ePWM counter
  reaches the compare value x on the way up. In this case, x
  represents A, B, C, or D.
- `Counter is decrementing and equals to the compare
  x register (CTRD=CMPx)` - The ePWM counter
  reaches the compare value x on the way down. In this case, x
  represents A, B, C, or D.

### HRPWM Tab

During HR (High Resolution) configuration for F2837xD processor, the ePWM modules
only exists on ePWM1 and SFO only runs on CPU1. Therefore if you want to use HRPWM,
then ePWM1 must be allocated to CPU1 and if SFO is enabled, it must run on
CPU1.

For F2838xD device, even though CPU and EWPM1 still do the calibration for HRPWM,
each EPWM module clocks its own HRPWM, and use the same values of HRMSTEP calculated
by the SFO. This allows HRPWM to function correctly with CPU2.

### **Enable High Resolution Period on ePWM#A (HRPWM - period), Enable High Resolution Period on ePWM#B (HRPWM - period)** — Indicates the effective resolution for conventionally generated PWM `off` (default) | `on`

When the effective resolution for the conventionally generated PWM is
insufficient, consider using High Resolution PWM (HRPWM). The resolution
of PWM is normally dependent upon the PWM frequency and the underlying
system clock frequency. To address this limitation, HRPWM uses
**Micro Edge Positioner (MEP)** technology to
position edges more finely by dividing each coarse system clock. The
accuracy of the subdivision is on the order of `150ps`.
The following figure shows the relationship between one system clock and
edge position in terms of **MEP** steps:

When this parameter is enabled, the block accepts decimal values for
the timer period of the ePWM Module. The Extension Register for the
HRPWM Period (TBPRDHR) provides an 8 bit representation of the decimal
part of the **Timer period** value. This parameter
enables the **Enable high resolution PWM (HRPWM -
duty)** parameter, and displays the **HRPWM loading
mode**, **HRPWM control mode**, and
**HRPWM edge control** mode parameters.

Selecting Enable HRPWM (Period) forces **TB clock prescaler
divider** and **High Speed TB clock prescaler
divider** to `1`. These settings
match the HRPWM time base clock with the SYSCLKOUT frequency.

The `Down` option in the **Counting
mode** parameter is not compatible with HRPWM. To avoid an
error when you build the model, do not set the **Counting
mode** parameter to `Down` and
select the **Enable HRPWM (Period)** parameter
checkbox.

**Note**

This parameter is available only for specific C28x
devices.

### **Enable HRPWM Duty on ePWM#A(HRPWM - duty)** — Indicates decimal part of the compare value `off` (default) | `on`

When this parameter is enabled, decimal values will be accepted for
the Compare A value (CMPA) of the ePWM Module. The Extension Register
for the HRPWM Compare A (CMPAHR) provides an 8 bit representation of the
decimal part of the compare value.

This parameter also enables **HRPWM control mode**.

**Note**

This parameter only appears for specific C28x devices.

### **High resolution PWM (HRPWM) Load mode on ePWM#A** — Determines when to transfer CMPAHR shadow value to active register `Counter equals to period (CTR=PRD)` (default) | `Counter equals to zero (CTR=ZERO)` | `Counter equals to either zero or period (CTR=ZERO or CTR=PRD)`

This parameter appears when **Enable high resolution PWM
(HRPWM - period)** or **Enable high resolution PWM
(HRPWM - duty)** is selected. Determine when to transfer
the value of the CMPAHR shadow to the active register:

- `Counter equals to zero (CTR=ZERO)`
  — Transfers the value when the time base counter equals
  zero (TBCTR = 0x0000).
- `Counter equals to period (CTR=PRD)`
  — Transfers the value when the time base counter equals
  the period (TBCTR = TBPRD).
- `Counter equals to either zero or period (CTR=ZERO
  or CTR=PRD)` — Transfers the value when
  either case is true.

This parameter configures the HRLOAD shadow mode bit in the HRPWM
configuration register (HRCNFG).

### **High resolution PWM (HRPWM) control mode on ePWM#A** — Indicates the control mode `Duty control mode` (default) | `Phase control mode`

This parameter appears when **Enable high resolution PWM
(HRPWM - period)** or **Enable high resolution PWM
(HRPWM - duty)** is selected. Select which register
controls the Micro Edge Positioner (MEP) step size. The **High
resolution PWM (HRPWM) control mode** option configures the
CTLMODE control mode bits.

- `Duty control mode` — Uses the
  Extension Register for HRPWM Duty (CMPAHR) or the Extension
  Register for HRPWM Period (TBPRDHR) to control the MEP edge
  position.
- `Phase control mode` — Uses
  the Time Base Phase High Resolution Register (TBPHSHR) to
  control the MEP edge position.

### **High resolution PWM (HRPWM) edge control mode** — Indicates the edge control mode `Both Edge` (default) | `Rising Edge` | `Falling Edge`

Select the register that controls the MEP precise position control on
the edge type.

- `Rising Edge` — MEP
  control of rising edge
- `Falling Edge` — MEP
  control of falling edge
- `Both Edge` — MEP control
  of both edges

The **High resolution PWM (HRPWM) edge control
mode** option configures the EDGMODE edge mode bits in the
HRPWM configuration register (HRCNFG).

#### Dependencies

This parameter appears when **Enable high resolution PWM
(HRPWM - period)** or **Enable high resolution
PWM (HRPWM - duty)** is selected.

### **Enable high resolution deadband rising edge (RED), Enable high resolution deadband falling edge (FED)** — Enables HRPWM capabilities on Deadband Rising Edge Delay and Falling Edge Delay `off` (default) | `on`

These parameters enable HRPWM capabilities on Deadband Rising Edge
Delay and Falling Edge Delay. High-resolution deadband RED and FED
requires half-cycle clocking mode.

#### Dependencies

These parameters appear when **Use deadband for
ePWM#A** or **Use deadband for
ePWM#B** is selected.

**Note**

These parameters are available only for specific F28x
devices. The PWM chopper module is disabled when these
parameters are selected.

### **Use scale factor optimizer (SFO) software** — Indicates scale factor `off` (default) | `on`

Enable scale factor optimizing (SFO) software with HRPWM. This
software dynamically determines the scaling factor for the MEP step
size. The step size varies depending on operating conditions such as
temperature and voltage. The SFO software reduces variability due to
these conditions. For more information, see the Scale Factor Optimizing
Software (SFO) section of the *TMS320x2802x, 2803x Piccolo High
Resolution Pulse Width Modulator (HRPWM) Reference
Guide*.

#### Dependencies

- **Use scale factor optimizer (SFO)
  software** parameter is enabled, read-only
  and visible, only if the **Enable auto
  convert**, and **Enable high
  resolution PWM (HRPWM - period)** parameters
  are selected.
- **Use scale factor optimizer (SFO)
  software** parameter is editable, only if
  the **Enable auto convert** parameter
  is unselected.

### **Enable auto convert** — Indicates auto convert `off` (default) | `on`

Apply the scaling factor calculated by the SFO software to the
controlling period or duty cycle. (Use the **HRPWM duty
mode** to select controlling period or duty cycle.) This
parameter sets the AUTOCONV field in the HRPWM Configuration Register
(HRCNFG).

#### Dependencies

- **Enable auto convert**
  parameter only appears for specific C28x devices.
- **Enable auto convert** parameter
  is enabled, read-only and visible, only if
  **Enable high resolution PWM (HRPWM -
  period)** parameter is selected.
- **Enable auto convert** parameter
  is enabled, and editable, only if **Enable high
  resolution PWM (HRPWM - duty)** parameter
  is selected.

### PWM Chopper Control Tab

### **Chopper module enable** — Enables chopper module `off` (default) | `on`

Select to enable the chopper module.

### **Chopper frequency divider** — Determines frequency of chopper clock `1` (default) | `2` | `...`

Set the prescaler value that determines the frequency of the chopper
clock. The system clock speed is divided by this value to determine the
chopper clock frequency. Choose an integer value in the range
`1` to `8`.

### **Chopper clock cycles width of first pulse** — High-energy first pulse to turn on hard and fast power switch `1` (default) | `2` | `...`

Choose an integer value in the range `1` to
`16` to set the width of the first pulse.
This feature provides a high-energy first pulse to turn on the hard and
fast power switch.

### **Chopper pulse duty cycle** — Determines duty cycles of second and subsequent pulses `12.5%` (default) | `25%` | `...`

The duty cycles of the second and subsequent pulses are also
programmable. The duty cycle can be varied in steps of
`12.5%` from
`12.5%` to
`87.5%`.

### Trip Zone Unit

### **Trip zone source** — Determines source of control logic for trip zone signals `Specify via dialog` (default) | `Input port`

Specify the source of the control logic for the trip zone signals.
Select `Specify via dialog` (the default) to
enable specific trip zone signals in the block dialog. Choose
`Input port` to enable specific trip-zone
signals using a block input port **TZSEL**.

The **Trip Zone unit** tab lets you specify
parameters for the Trip-zone (TZ) submodule. Each ePWM module receives
TZ signals from the GPIO MUX. The number of Trip zone signals vary based
on C28x processor families. These signals can be used to force the ePWM
output into a specific state based on an event like an external fault.
Use the settings on this tab to program the ePWM outputs to respond to
external events.

If you select `Input port`, use this bit
operation to determine the value of the 16-bit integer to send to the
**TZSEL** input port:

`TZSEL INPUT VALUE = (DCBEVT1*2 15
+ DCAEVT1*2 14 +
OSHT6*213 +
OSHT5*212 +
OSHT4*211 +
OSHT3*210 +
OSHT2*29 +
OSHT1*28 + DCBEVT2*2
7 + DCAEVT2*2
6 +
CBC6*25 +
CBC5*24 +
CBC4*23 +
CBC3*22 +
CBC2*21 +
CBC1*20)`

The software uses the higher 8 bits for the **One shot
TZ1-TZ6** (OSHT1–6) and the lower 8 bits for
**Cyclic TZ1-TZ6** (CBC1–6). You can set up a group
of TZ sources (1~6), use a bit operation to combine them into an
integer, and then feed the integer to TZSEL.

For example, to enable One Shot TZ6 (OSHT6) and One Shot TZ5 (OSHT5)
as trip zone sources, set OSHT6 and OSHT5 to 1 and leave the remaining
values as 0.

TZSEL INPUT VALUE = (1\*215 +
1\*214 + 1\*213
+ 1\*212 + 0\*211
…)

TZSEL INPUT VALUE = (8192 + 4096 + 0 …)

TZSEL INPUT VALUE = 12288

When the block receives this value, it applies it to the TZSEL
register as a binary value: `0011000000000000`.

For more information, see the Trip-Zone Submodule Control and Status
Registers section of the TMS320x28xx, 28xxx Enhanced Pulse Width
Modulator (ePWM) Module Reference Guide.

### **Enable one-shot Trip-zone# (TZ#)** — Enables corresponding trip zone signal in one-shot mode `off` (default) | `on`

Select this parameter to enable the corresponding trip zone signal in
one-shot mode. In this mode, when the trip event is active, the trip
zone module performs the corresponding action on the EPWM#A/B output
immediately and latches the condition.

When an one-shot trip event occurs, the one-shot trip event flag
`TZFLG[OST]` is set. A corresponding flag for the
event that caused the one-shot trip event is also set in register
`TZOSTFLG` using the register read/write block. To
clear the one-shot trip condition, manually write to the
`TZCLR[OST]` bit using the register read/write
block. Similarly, to clear the `TZOSTFLG` register bit,
manually write to the corresponding bit in the
`TZOSTCLR` register using the register read/write
block.

For example, to clear the `OST1` trip event in ePWM1,
use register read/write blocks to write 1 to
`EPwm1Regs.TZCLR.bit.OST` and
`EPwm1Regs.TZOSTCLR.bit.OST1` bits.

#### Dependencies

This option is available only when the **Trip zone source**is `Specify via dialog`.

### **Enable one-shot digital compare A event 1 (DCAEVT1), Enable one-shot digital compare B event 1 (DCBEVT1)** — Enables corresponding event signal as OST trip source for event 1 `off` (default) | `on`

Select these parameter to enable the corresponding event signal as an
OST trip source for event 1. In this mode, if the digital compare A or
digital compare B event 1 is active, the trip zone module performs the
corresponding action on the EPWM#A/B output immediately and latches the
condition. You can unlatch the condition using the software control.

#### Dependencies

- This option is available only when the **Trip
  zone source** is `Specify via
  dialog`.
- This parameter is available only for specific C28x
  processors.

### **Enable cyclic Trip-zone# (TZ#)** — Enables corresponding trip zone signal in cycle-by-cycle mode `off` (default) | `on`

Select this parameter to enable the corresponding trip zone signal in
cycle-by-cycle mode. In this mode, when the trip event is active, the
trip zone module performs the corresponding action on the EPWM#A/B
output immediately and latches the condition. In cycle-by-cycle mode,
the trip zone module automatically clears condition when the ePWM
Counter reaches zero. Therefore, in cycle-by-cycle mode, every ePWM
cycle resets or clears the trip event.

#### Dependencies

This option is available only when the **Trip zone source**is `Specify via dialog`.

### **Enable cyclic digital compare A event 2 (DCAEVT2), Enable cyclic digital compare B event 2 (DCBEVT2)** — Enables corresponding event signal as cyclic trip source for event 2 `off` (default) | `on`

Select these parameters to enable the corresponding event signal as a
cyclic trip source for event 2. In this mode, if the digital compare A
or digital compare B event 2 is active, the Trip zone module performs
the corresponding action on the EPWM#A/B output immediately and latches
the condition. In Cycle-by-Cycle Mode, the Trip zone module
automatically clears condition when the ePWM Counter reaches zero.
Therefore, in Cycle-by-Cycle Mode, every ePWM cycle resets or clears the
trip event.

#### Dependencies

- This option is available only when the **Trip
  zone source** is `Specify via
  dialog`.
- This parameter is available only for specific C28x
  processors.

### **Enable trip-zone one-shot interrupt (OST)** — Enables trip zone one-shot interrupt `off` (default) | `on`

Generate an interrupt when any of the enabled one shot (OST)
triggering events occur.

**Note**

`TZFLG.INT` is cleared in the post processing
of ISR. However, if the interrupt flag is cleared when either
`CBC` or `OST` is set,
then another interrupt pulse will be generated. Clearing all
flag bits will prevent further interrupts. This bit is cleared
by writing the appropriate value to the `TZCLR`
register.

### **Enable trip-zone cycle-by-cycle interrupt (CBC)** — Enables trip-zone cycle-by-cycle interrupt `off` (default) | `on`

Generate an interrupt when any of the enabled cyclic or cycle-by-cycle
(CBC) triggering events
occur.

**Note**

`TZFLG.INT` is cleared in the post processing
of ISR. However, if the interrupt flag is cleared when either
`CBC` or `OST` is set,
then another interrupt pulse will be generated. Clearing all
flag bits will prevent further interrupts. This bit is cleared
by writing the appropriate value to the `TZCLR`
register.

### **Digital comparator output A event 1 interrupt enable (DCAEVT1), Digital comparator output A event 2 interrupt enable (DCAEVT2), Digital comparator output B event 1 interrupt enable (DCBEVT1), Digital comparator output B event 2 interrupt enable (DCBEVT2)** — Enables digital comparator output `off` (default) | `on`

Generate an interrupt when Digital Comparator Output A or Digital
Comparator Output B for event 1 or 2 occurs.

**Note**

These parameters are available only for specific C28x
processors.

### **Clear cycle-by-cycle trip latch at** — Select clear cycle by cycle trip latch `Counter equals to zero (CTR=Zero)` (default) | `Counter equals to period (CTR=Prd)` | `Counter equals to zero or period (CTR=Zero or CTR=Prd)` | `Latch not cleared`

Select the event options to clear cycle by cycle trip latch.

#### Dependencies

- To enable this parameter, set trip zone source
  parameter to **Input port**
  or trip zone source to **Specify via
  dialog**. Then enable either **Enable cyclic trip-zine#** or
  **Enable cyclic digital compare
  A event 2 (DCAEVT2), Enable cyclic digital compare B
  event 2 (DCBEVT2)** .
- These parameters are available only for specific C28x
  processors.

### **ePWM#A forced (TZ) to, ePWM#B forced (TZ) to, ePWM#A forced (DCAEVT#) to, ePWM#B forced (DCBEVT#) to** — Determines action to consider on ePWM output `No action` (default) | `High` | `Low` | `Hi-Z (High Impedance)`

These parameters decide the actions you can take on the ePWM outputs
in a trip zone condition. The trip zone module overrides and forces the
ePWM#A and/or ePWM#B (TZ or DCAEVTx) output to one of these states:
`No action`
(the default), `High`,
`Low`, or `Hi-Z (High
Impedance)`.

### Digital Compare

### **Source for digital compare A high signal (DCAH), Source for digital compare B high signal (DCBH)** — Source for digital compare high signal `GPTRIP1SEL/(TZ1) for DCAH/GPTRIP1SEL/(TZ1) for DCBH` (default) | `GPTRIP3SEL/(TZ3) for DCAH/GPTRIP7SEL for DCBH` | `...`

Select the appropriate TZ or COMP signal to generate high logic value
for the Digital compare A/B high signal. Use the **Digital
compare output A event # selection**, **Digital
compare output B event # selection**, **DCAEVT#
source select**, **DCBEVT# source select**
parameters to determine the impact of DCAH/DCBH on DCAEVT# and DCBEVT#.

Each digital compare (DC) submodule receives three TZ signals (TZ1 to
TZ3) from the GPIO MUX, and three COMP signals from the COMP (For
specific C28x devices only). These signals indicate fault or trip
conditions that are external to the ePWM submodule. Use the settings in
this tab to output specific DC events in response to those external
signals. These DC events feed directly into the time base, trip zone,
and event trigger submodules.

For more information, see the *Digital Compare (DC)
Submodule* section of the *Piccolo Enhanced Pulse
Width Modulator (ePWM) Module Reference Guide*.

### **Source for digital compare A low signal (DCAL), Source for digital compare B low signal (DCBL)** — Source for digital compare low signal `GPTRIP1SEL/(TZ1) for DCAL/GPTRIP1SEL/(TZ1) for DCBL` (default) | `TRIPIN1(ECCDBLERR) for DCAL/Select From DCBLTRIPSEL for DCBL` | `...`

Select the appropriate TZ or COMP signal to generate low logic value
for the Digital compare A/B low signal. Use the **Digital
compare output A event # selection**, **Digital
compare output B event # selection**, **DCAEVT#
source select**, **DCBEVT# source select**
options to determine the impact of DCAL/DCBL on DCAEVT# and DCBEVT#.

### **Digital compare output A event # selection (DCAEVT#), Digital Compare output B event # selection (DCBEVT#)** — Qualify signals that generate DC events `Event disabled` (default) | `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

Qualify the signals that generate DC events, such as DCAEVT# or
DCBEVT#. To disable this feature, choose the `Event
disabled` option. Based on the source selection for the
signals, the event can be triggered. Event selection can be based on the
combination of conditions High, Low and Don't care.

### **DCAEVT# source select, DCBEVT# source select** — Digital compare event source `Event disabled` (default) | `DCAH=low and DCAL=don’t care/DCBH=low and DCBL=don’t care` | `...`

This parameter controls two separate aspects of triggering DC
events:

- Triggering filtered or unfiltered DC event

  - The DC event can be a filtered or unfiltered signal
    that can be passed to other submodules.
  - Configures EVT1SRCSEL and EVT2SRCSEL in both DCACTL
    and DCBCTL registers.
  - Options that begin with `DCAEVT# with
    sync` or `DCAEVT# with
    async` do not apply filtering to DC
    events. Qualified DC signals pass directly to trigger DC
    events without any filtering.
  - Options that begin with `DCEVTFILT
    sync` apply filtering to DC events.
    Qualified signals pass through filtering circuits before
    triggering DC events. For more information, refer to the
    *Event Filtering* section of the
    *Piccolo Enhanced Pulse Width Modulator
    (ePWM) Module Reference Guide*.
- Trigger the DC event synchronously or asynchronously

  - The DC event signal can be synchronized with TBCLK or
    can remain asynchronously.
  - Configures EVT1SRCSEL and EVT2SRCSEL in both DCACTL
    and DCBCTL registers.
  - Options that end with `async`
    trigger DC events asynchronously. When the qualified or
    filtered signals exist, the DC submodule triggers the DC
    event immediately.
  - Options that end with `sync`
    trigger DC events synchronously. Once the qualified or
    filtered signals exist, the DC submodule triggers the DC
    event in sync with the TBCLK signal.

    **Note**

    The above fields appear only when the
    corresponding DCAEVT# is enabled.

**Note**

The following fields appear when you select `DCEVTFILT with
sync` or `DCEVTFILT with async`
for the **DCAEVTX source select** or **DCBEVTX
source select**.

For more details about the following parameters, refer to the Technical
Reference Manual for Enhanced Pulse Width Modulator (ePWM) Module Reference
Guide.

### **Pulse select** — Indicates blanking window which filters out event occurrences `Counter equals to zero (CTR=Zero)` (default) | `Counter equals to period (CTR=PRD)`

The blanking window which filters out
event occurrences on the signal while active. Set this parameter is
aligned to either a CTR = PRD pulse or a CTR = Zero pulse.

### **Blanking window inverted** — Indicates the inverted blanking window `off` (default) | `on`

Select this parameter to enable the inverted blanking window.

### **Blanking window offset** — Indicates offset blanking window `0` (default)

The number of TBCLK cycles to determine the point after the
**Pulse select** event to start the blanking window
for filtering

### **Blanking window width** — Indicates duration of blanking window `0` (default)

The number of TBCLK cycles to determine the point after the
**Pulse select** event to start the blanking window
for filtering.

The blanking window will start based on the occurrence **Pulse
select** event with additional TBCLK cycles as offset as
per the **Blanking offset window**.

During the blanking window all the events are ignored. The events can
trigger sync or async events before and after the blanking window is
applied.

### **Filter output DCEVTFILT** — Indicates source select for filter `Filtered version of DCAEVT1 (DCAEVT1FILT)` (default) | `Filtered version of DCAEVT2 (DCAEVT2FILT)` | `Filtered version of DCBEVT1 (DCBEVT1FILT)` | `Filtered version of DCBEVT2 (DCBEVT2FILT)`

Use this parameter to select a source for filtering, which forms the
DCEVTFILT signal.

### **Enable counter capture** — Indicates counter capture `off` (default) | `on`

Enabling this option allows to capture the TBCTR value of the trip
event.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x C2000 Microcontroller Blockset / F29H85x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Generate enhanced Pulse Width Modulated (ePWM) waveforms

Configures the Type 1 to Type 4 enhanced Pulse Width Modulator (ePWM) to generate PWM
waveforms. The number of available ePWM modules (ePWM1-ePWM16) vary between C2000
processors. For more information on ePWM type, refer to C2000 Real-Time Control
Peripheral Reference Guide.

Use this block to generate ePWM waveforms. Multiple ePWM modules are
available on C28x devices. Each module generates two PWM signals ePWMA and ePWMB.

When you enable the high-resolution pulse width modulator (HRPWM), the ePWM block uses
the scale factor optimizing (SFO) software library. The SFO library can
“dynamically determine the number of micro edge positioner (MEP) steps per system
clock (SYSCLKOUT) period.” For more information, see `TMS320x28xx, 28xxx
High-Resolution Pulse Width Modulator (HRPWM) Reference Guide`, available
on the Texas Instruments® web site.

This block is common to various C28x devices. Available parameters vary based on the
library from which you select the block. The blue label on the top right corner of the
block displays the family. As the block is a superset of functionalities available on
different devices, not all parameters will be relevant to your model.
