---
type: simulink-block
title: 'C28x eQEP'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c28xeqep'
documentation_source_path: 'ref/c28xeqep.html'
language: en
---

# C28x eQEP

## Ports
```yaml
ports:
- name: swi
  summary: Dynamically update initialization value for position counter scalar
  direction: input
  data_types: Boolean
- name: cmp
  summary: Value for comparing position scalar
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: iel
  summary: Software index marker scalar
  direction: input
  data_types: Boolean
- name: qposcnt
  summary: Position counter signal scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: pcef
  summary: Position counter error flag on error scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qdf
  summary: Direction flag of quadrature module scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qctmr
  summary: Capture timer signal scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qcprd
  summary: Capture period signal scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: coef
  summary: eQEP overflow error flag scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: cdef
  summary: Direction change error flag scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qctmrlat
  summary: Capture timer latched value scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qcprdlat
  summary: Capture timer period latched value scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposlat
  summary: Position counter latched value scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposilat
  summary: Latches position counter on index event scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: qposslat
  summary: Latches position counter on strobe event scalar
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
```

### Input

### **swi** — Dynamically update initialization value for position counter scalar

If the input is `true`, the position counter is
initialized to the value in the **Initialization value
(0~4294967295)** parameter.

#### Dependencies

This port appears only when, in the **Position
counter** tab, you select **Enable
software initialization** and set **Software
initialization source** to `Input
port`.

**Data Types:** `Boolean`

### **cmp** — Value for comparing position scalar

Input value that generates the position compare sync signal.

#### Dependencies

This port appears only when, in the **Compare
output** tab, you select **Enable
position-compare sync signal output** and set
**Compare value source** to
`Input port`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **iel** — Software index marker scalar

Software index event marker for latching the position counter.

#### Dependencies

This port appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on the
  maximum position` or `Reset
  on the first index event`.
- You select **Output latch position counter
  on index event**.
- You set **Index event latch of position
  counter** to `Software index
  marker via input port`.

**Note**

In **Compare output** tab, if
**Sync output pin selection** is set
to `Index pin is used for sync output`,
then the **Index event latch of position
counter** parameter cannot be set to
`Software index marker via input
port`.

**Data Types:** `Boolean`
### Output

### **qposcnt** — Position counter signal scalar

Position counter signal (PCSOUT) received from the position counter
and control unit (PCCU).

#### Dependencies

This port appears only when, in the **Position
counter** tab, you select **Output
position counter**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **pcef** — Position counter error flag on error scalar

Outputs the position counter error flag on an error.

- `0` — No error occurred during the last
  index transition.
- `1` — Position counter error.

#### Dependencies

This port appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on an index
  event`.
- You select **Output position counter error
  flag**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qdf** — Direction flag of quadrature module scalar

Direction flag of the quadrature module.

- `0` — counterclockwise rotation (or
  reverse movement).
- `1` — clockwise rotation (or forward
  movement).

#### Dependencies

This port appears only when, in the
**General** tab, you select
**Quadrature direction flag output
port**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmr** — Capture timer signal scalar

Outputs the eQEP capture timer signal.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Output capture
timer**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprd** — Capture period signal scalar

Outputs the capture period signal, which holds the period count value
between the last successive eQEP position events.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Output capture
period timer**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **coef** — eQEP overflow error flag scalar

Outputs overflow error flag (COEF flag) in the event of capture timer
overflow between unit position events.

- `0` — Overflow has not occurred.
- `1` — Overflow occurred in the eQEP
  capture timer register (QEPCTMR).

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Enable and output
overflow error flag**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **cdef** — Direction change error flag scalar

Outputs the direction change error flag.

- `0` — Capture direction error has not
  occurred.
- `1` — Direction change occurred between
  two capture position events.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Enable and output
direction change error flag**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qctmrlat** — Capture timer latched value scalar

Outputs the capture timer latched value from the QCTMRLAT
register.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Output capture timer
latched value**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qcprdlat** — Capture timer period latched value scalar

Outputs the capture timer period latched value from the QCPRDLAT
register.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Output capture timer
period latched value**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposlat** — Position counter latched value scalar

Outputs position counter latched value from the QPOSLAT
register.

#### Dependencies

This port appears only when, in the **Speed
calculation** tab, you select **Enable
eQEP capture** and **Output position
counter latched value**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposilat** — Latches position counter on index event scalar

eQEP index input can be configured to latch the position counter
register (QPOSCNT) as output on the occurrence of a definite event on
this pin.

#### Dependencies

This port appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on the
  maximum position` or `Reset
  on the first index event`.
- You select **Output latch position counter
  on index event**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **qposslat** — Latches position counter on strobe event scalar

eQEP strobe input can be configured to latch the position counter
register (QPOSCNT) as output on the occurrence of a definite event on
this pin.

#### Dependencies

This port appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on the
  maximum position` or `Reset
  on the first index event`.
- You select **Output latch position counter
  on strobe event**.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Module
  summary: eQEP module to obtain position, direction, and speed eQEP1 (default) | eQEP2 | eQEP3
  group: General
- name: Position counter mode
  summary: Mode that matches how input to eQEP peripheral is encoded Quadrature-count (default) | Direction-count | Up-count
    | Down-count
  group: General
- name: Positive rotation
  summary: Direction of rotation Clockwise (default) | Counterclockwise
  group: General
- name: External clock rate
  summary: 'Measurement resolution 2x resolution: Count the rising/falling edge (default) | 1x resolution: Count the rising
    edge only'
  group: General
- name: Quadrature direction flag output port
  summary: Creates port for direction flag off (default) | on
  group: General
- name: Invert input QEPxX polarity
  summary: Inverts polarity of eQEP input off (default) | on
  group: General
- name: Index pulse gating option
  summary: Enables gating of index pulse with strobe input off (default) | on
  group: General
- name: Sample time
  summary: Frequency at which block reads position counter 0.0001 (default) | -1 | scalar
  group: General
- name: Output position counter
  summary: Outputs position counter signal on (default) | off
  group: Position counter
- name: Maximum position counter value (0~4294967295)
  summary: Specifies maximum position counter value 4294967295 (default) | integer in [0, 4,294,967,295]
  group: Position counter
- name: Enable set to init value on index event
  summary: Enables option to set initialization value for position counter off (default) | on
  group: Position counter
- name: Set to init value on index event
  summary: Initialization value for position counter Rising edge (default) | Falling edge
  group: Position counter
- name: Enable set to init value on strobe event
  summary: Enables option to set initialization value for position counter off (default) | on
  group: Position counter
- name: Set to init value on strobe event
  summary: Sets initialization value for position counter Rising edge (default) | Depending on direction
  group: Position counter
- name: Enable software initialization
  summary: Enables option to set initialization value for position counter off (default) | on
  group: Position counter
- name: Software initialization source
  summary: Specifies initialization source of position counter Input port (default) | Set to init value at start up
  group: Position counter
- name: Initialization value (0~4294967295)
  summary: Initialization value for position counter 2147483648 | integer in [0, 4,294,967,295]
  group: Position counter
- name: Position counter reset mode
  summary: Resets position counter Reset on an index event (default) | Reset on the maximum position | Reset on the first
    index event | Reset on a time unit event
  group: Position counter
- name: Output position counter error flag
  summary: Outputs position counter error flag on error off (default) | on
  group: Position counter
- name: Output latch position counter on index event
  summary: Latches position counter on index event off (default) | on
  group: Position counter
- name: Index event latch of position counter
  summary: Configures position counter to latch on an event Rising edge (default) | Falling edge | Software index marker via
    input port
  group: Position counter
- name: Output latch position counter on strobe event
  summary: Latches position counter on strobe event off (default) | on
  group: Position counter
- name: Strobe event of latched position counter
  summary: Configures position counter to latch on strobe Rising edge (default) | Depending on direction
  group: Position counter
- name: Enable QEP capture
  summary: Enables edge capture unit off (default) | on
  group: Speed calculation
- name: Output capture timer
  summary: Outputs capture timer off (default) | on
  group: Speed calculation
- name: Output capture period timer
  summary: Outputs capture period off (default) | on
  group: Speed calculation
- name: eQEP capture timer prescaler
  summary: Prescales capture timer clock frequency 128 (default) | 1 | 2 | 4 | 8 | 16 | 32 | 64
  group: Speed calculation
- name: Unit position event prescaler
  summary: Prescales quadrature clock 128 (default) | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 256 | 512 | 1024 | 2048
  group: Speed calculation
- name: Enable and output overflow error flag
  summary: Outputs overflow error flag when capture timer overflows off (default) | on
  group: Speed calculation
- name: Enable and output direction change error flag
  summary: Outputs direction change error flag off (default) | on
  group: Speed calculation
- name: Capture timer and position
  summary: QEP capture latch mode On position counter read (default) | On unit time-out event
  group: Speed calculation
- name: Unit timer period (0~4294967295)
  summary: Sets unit timer period 100000000 (default) | value in the range [0, 4,294,967,295]
  group: Speed calculation
- name: Output capture timer latched value
  summary: Outputs capture timer latched value off (default) | on
  group: Speed calculation
- name: Output capture timer period latched value
  summary: Outputs capture timer period latched value off (default) | on
  group: Speed calculation
- name: Output position counter latched value
  summary: Outputs position counter latched value off (default) | on
  group: Speed calculation
- name: Enable position-compare sync signal output
  summary: Enables position compare sync signal output off (default) | on
  group: Compare output
- name: Sync output pin selection
  summary: GPIO pin used for sync signal Index pin is used for sync output (default) | Strobe pin is used for sync output
  group: Compare output
- name: Compare value source
  summary: Source of value for position comparison Specify via dialog (default) | Input port
  group: Compare output
- name: Position compare shadow load mode
  summary: Shadow mode for generating position compare sync signal Load on QPOSCNT=0 (default) | Shadow disabled(load immediate)
    | Load on QPOSCNT=QPOSCMP
  group: Compare output
- name: Position compare value (0~4294967295)
  summary: Value for comparing postiton 4294967295 (default) | value in the range [0, 4,294,967,295]
  group: Compare output
- name: Sync output pulse width (1~4096)
  summary: Pulse width of position compare sync output signal 1 (default) | value in the range [0, 4,096]
  group: Compare output
- name: Polarity of sync output
  summary: Polarity of sync output Active high (default) | Active low
  group: Compare output
- name: Watchdog timer enable
  summary: Enables watchdog time-out flag off (default) | on
  group: Watchdog unit
- name: Watchdog timer
  summary: Time-out value for watchdog timer 65535 (default) | value in the range [0, 65,535]
  group: Watchdog unit
- name: Position counter error interrupt enable
  summary: Enables position counter error interrupts off (default) | on
  group: Interrupt
- name: Quadrature phase error interrupt enable
  summary: Enables quadrature phase error interrupts off (default) | on
  group: Interrupt
- name: Quadrature direction change interrupt enable
  summary: Enables quadrature direction change interrupt off (default) | on
  group: Interrupt
- name: Watchdog timeout interrupt enable
  summary: Enables watchdog timeout interrupts off (default) | on
  group: Interrupt
- name: Position counter underflow interrupt enable
  summary: Enables position counter underflow interrupts off (default) | on
  group: Interrupt
- name: Position counter overflow interrupt enable
  summary: Enables position counter overflow interrupts off (default) | on
  group: Interrupt
- name: Position-compare ready interrupt enable
  summary: Enables position compare ready interrupts off (default) | on
  group: Interrupt
- name: Position-compare match interrupt enable
  summary: Enables position compare match interrupts off (default) | on
  group: Interrupt
- name: Strobe event latch interrupt enable
  summary: Enables strobe event latch interrupts off (default) | on
  group: Interrupt
- name: Index event latch interrupt enable
  summary: Enables index event latch interrupts off (default) | on
  group: Interrupt
- name: Unit timeout interrupt enable
  summary: Enables unit timeout interrupts off (default) | on
  group: Interrupt
```

### General

### **Module** — eQEP module to obtain position, direction, and speed `eQEP1` (default) | `eQEP2` | `eQEP3`

The eQEP peripheral module used to obtain position, direction, and
speed information. The number of eQEP modules supported varies for
different C2000™ processors.

### **Position counter mode** — Mode that matches how input to eQEP peripheral is encoded `Quadrature-count` (default) | `Direction-count` | `Up-count` | `Down-count`

The eQEP peripheral inputs are QEPA, QEPB, QEPI, and QEPS. Configure
the GPIO pins for these inputs by navigating to **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** > **eQEP**.

Input signals QEPA and QEPB to the eQEP peripheral are processed by
the quadrature decoder unit (QDU) in the eQEP peripheral to produce
clock (QCLK) and direction (QDIR) signals. Choose the position counter
mode that matches the way the input to the eQEP module is encoded:

- `Quadrature-count` — Two square
  signals (A and B) 90 degrees out of phase are sent to the
  eQEP peripheral. The QDU uses the phase relationship of
  these two inputs to generate quadrature clock and direction
  signals.
- `Direction-count` — Direction and
  clock signals are directly sent to the eQEP peripheral. The
  QEPA pin provides the clock input, and the QEPB pin provides
  the direction input.
- `Up-count` — The position counter
  is used to measure the frequency of the signal in the QEPA
  pin. The direction is hard-wired for up count in this
  mode.
- `Down-count` — The position
  counter is used to measure the frequency of the signal in
  the QEPA pin. The direction is hard-wired for down count in
  this mode.

### **Positive rotation** — Direction of rotation `Clockwise` (default) | `Counterclockwise`

Set the direction of rotation.

If `Clockwise` is selected, the quadrature
count operation is performed without swapping the quadrature clock
inputs fed to the QDU.

If `Counterclockwise` is selected, reverse
counting is performed by swapping the quadrature clock inputs fed to the
QDU. The quadrature decoder reverses the counting direction.

#### Dependencies

This parameter appears only when you set **Position
counter mode** to
`Quadrature-count` on the
**General** tab.

### **External clock rate** — Measurement resolution `2x resolution: Count the rising/falling edge` (default) | `1x resolution: Count the rising edge only`

Select the resolution of the clock generator that the position counter
uses as input so that the counting occurs on both rising and falling
edges of the QEPA input or on the rising edge only. Choosing the former
increases the measurement resolution by a factor of 2.

#### Dependencies

This parameter appears only when you set **Position
counter mode** to
`Direction-count`,
`Up-count`, or
`Down-count`.

### **Quadrature direction flag output port** — Creates port for direction flag `off` (default) | `on`

Creates a port (qdf) on the block that gives the direction flag of the
quadrature module.

#### Dependencies

This parameter appears only when, in the
**General** tab, **Position
counter mode** is set to
`Quadrature-count`.

### **Invert input QEPxX polarity** — Inverts polarity of eQEP input `off` (default) | `on`

Inverts the polarity of the eQEP peripheral inputs. The
**Invert input QEPxA polarity** checkbox
corresponds to QEPA, **Invert input QEPxB
polairty** corresponds to QEPB, and so on.

### **Index pulse gating option** — Enables gating of index pulse with strobe input `off` (default) | `on`

Enables the gating of the peripheral input index signal with the
peripheral input strobe signal. In this case, the internal index signal
is high only when both the peripheral input signals eQEPxI and eQEPxS
are high.

### **Sample time** — Frequency at which block reads position counter `0.0001` (default) | `-1` | scalar

Sample time for the block in seconds. To execute this block
asynchronously, set this parameter to `-1`.

### Position counter

### **Output position counter** — Outputs position counter signal `on` (default) | `off`

Outputs the position counter signal PCSOUT from the position counter
and control unit (PCCU). The position counter register counts up or down
on every eQEP pulse based on the direction of the input. The count value
is proportional to the position from a given reference point.

### **Maximum position counter value (0~4294967295)** — Specifies maximum position counter value `4294967295` (default) | integer in [0, 4,294,967,295]

Enter a maximum value (QPOSMAX) for the position counter. If the
position counter reaches QPOSMAX, the position counter is set to
`0` on the next increment of the counter. If the
position counter is `0`, the position counter is set to
QPOSMAX on the next decrement of the counter.

### **Enable set to init value on index event** — Enables option to set initialization value for position counter `off` (default) | `on`

Enables option to set the position counter to its initialization value
on an index event.

### **Set to init value on index event** — Initialization value for position counter `Rising edge` (default) | `Falling edge`

Sets the position counter to its initialization value on the rising
edge or falling edge of the index event.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you select **Enable set to
init value on index event**.

### **Enable set to init value on strobe event** — Enables option to set initialization value for position counter `off` (default) | `on`

Enables option to set the position counter to its initialization value
on a strobe event.

### **Set to init value on strobe event** — Sets initialization value for position counter `Rising edge` (default) | `Depending on direction`

The `Rising edge` option sets the position
counter to its initialization value on the rising edge of the strobe
input. The `Depending on direction` option sets
the position counter to its initialization value on the:

- rising edge of the strobe input, in the forward
  direction.
- falling edge of the strobe input, in the reverse
  direction.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you select **Enable set to
init value on strobe event**.

### **Enable software initialization** — Enables option to set initialization value for position counter `off` (default) | `on`

Allows the position counter to be set to its initialization value
using the software.

### **Software initialization source** — Specifies initialization source of position counter `Input port` (default) | `Set to init value at start up`

Choose the `Set to init value at start up`
option to initialize the position counter to the value entered in
**Initialization value** at the start of the
execution of the program. Choose the `Input
port` option to update the initialization value
dynamically based on an input initialization signal (input port
**swi**). If the input
**swi** is `true`, the
position counter is initialized to the **Initialization
value**.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you select **Enable software
initialization**.

### **Initialization value (0~4294967295)** — Initialization value for position counter `2147483648` | integer in [0, 4,294,967,295]

Enter the initialization value for the position counter.

#### Dependencies

This parameter appears only when you select **Enable set
to init value on index event**, **Enable set to
init value on strobe event**, or **Enable
software initialization**.

### **Position counter reset mode** — Resets position counter `Reset on an index event` (default) | `Reset on the maximum position` | `Reset on the first index event` | `Reset on a time unit event`

Position counter reset mode, depending on the nature of the system the
eQEP module is working with.

- `Reset on an index event` — If the
  index event occurs during the forward direction, then the
  position counter is reset to 0 on the next eQEP clock. If the
  index event occurs during the reverse direction, then the
  position counter is reset to the value in the QPOSMAX register
  on the next eQEP clock.
- `Reset on the maximum position` —
  During the forward direction, when the position counter is equal
  to QPOSMAX, the position counter is reset to 0 on the next eQEP
  clock, and the position counter overflow flag is set. During the
  reverse direction, when the position counter is equal to 0, the
  position counter is reset to QPOSMAX on the next QEP clock, and
  the position counter underflow flag is set.
- `Reset on the first index event` — If
  the index event occurs during the forward direction, the
  position counter is reset to 0 on the next eQEP clock. If the
  index event occurs during the reverse direction, the position
  counter is reset to the value in the QPOSMAX register on the
  next eQEP clock. The position counter is reset using the
  `Reset on the first index event`
  option only on the first index event occurrence. After the first
  index event occurrence, the position counter is reset based on
  the maximum position.
- `Reset on a unit time event` — The
  QPOSCNT value is latched to the QPOSLAT register on a unit time
  event. The QPOSCNT register is then reset to 0 for the forward
  direction and QPOSMAX for the reverse direction. You can use
  this option for frequency measurement.

### **Output position counter error flag** — Outputs position counter error flag on error `off` (default) | `on`

Outputs the position counter error flag on error. When you select this
option, the output port **pcef** is
created.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you set **Position counter
reset mode** to `Reset on an index
event`.

### **Output latch position counter on index event** — Latches position counter on index event `off` (default) | `on`

When this option is enabled, the position counter QPOSCNT latches into
QPOSLAT on the occurrence of an event on the strobe pin.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you set **Position counter
reset mode** to `Reset on the maximum
position` or `Reset on the first index
event`.

### **Index event latch of position counter** — Configures position counter to latch on an event `Rising edge` (default) | `Falling edge` | `Software index marker via input port`

Configures the eQEP position counter to latch on the index event
selected.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on the maximum
  position` or `Reset on the first
  index event`.
- You select **Output latch position counter on
  index event**.

### **Output latch position counter on strobe event** — Latches position counter on strobe event `off` (default) | `on`

The eQEP strobe input can be configured to latch the position counter
(QPOSCNT) into QPOSSLAT on occurrence of a definite event on this pin.
This option latches the position counter on each strobe event.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab, you set **Position counter
reset mode** to `Reset on the maximum
position` or `Reset on the first index
event`.

### **Strobe event of latched position counter** — Configures position counter to latch on strobe `Rising edge` (default) | `Depending on direction`

`Rising edge` latches on the rising edge of
the strobe event input. `Depending on
direction` latches on the rising edge in the forward
direction and the falling edge in the reverse direction.

#### Dependencies

This parameter appears only when, in the **Position
counter** tab:

- You set **Position counter reset
  mode** to `Reset on the maximum
  position` or `Reset on the first
  index event`.
- You select **Output latch position counter on
  strobe event**.

### Speed calculation

To view the other parameters of this tab, select the **Enable QEP
capture** option.

### **Enable QEP capture** — Enables edge capture unit `off` (default) | `on`

The eQEP peripheral includes an integrated edge capture unit to
measure the elapsed time between the unit position events. This option
enables the edge capture unit.

### **Output capture timer** — Outputs capture timer `off` (default) | `on`

Outputs the capture timer value from the QCTMR register.

### **Output capture period timer** — Outputs capture period `off` (default) | `on`

Outputs the period count value between the last successive eQEP
position events from the QCPRD register.

### **eQEP capture timer prescaler** — Prescales capture timer clock frequency `128` (default) | `1` | `2` | `4` | `8` | `16` | `32` | `64`

The eQEP capture timer runs from prescaled SYSCLKOUT. The capture
timer clock frequency is the frequency of SYSCLKOUT divided by the value
you choose for this parameter.

### **Unit position event prescaler** — Prescales quadrature clock `128` (default) | `1` | `2` | `4` | `8` | `16` | `32` | `64` | `256` | `512` | `1024` | `2048`

The timing of the unit position event is determined by prescaling the
quadrature clock (QCLK). QCLK is divided by the prescalar value you
choose for this parameter.

### **Enable and output overflow error flag** — Outputs overflow error flag when capture timer overflows `off` (default) | `on`

Enables and outputs the eQEP overflow error flag (COEF) in the event
of capture timer overflow between unit position events.

### **Enable and output direction change error flag** — Outputs direction change error flag `off` (default) | `on`

Enables and outputs the direction change error flag (CDEF) when
direction change occurs between the unit position events.

### **Capture timer and position** — QEP capture latch mode `On position counter read` (default) | `On unit time-out event`

Event that triggers the latching of the capture timer and capture
period register:

- `On position counter read` —
  Latch on position counter read by the processor. The capture
  timer and capture period values are latched into the
  QCTMRLAT and QCPRDLAT registers when the processor reads the
  QPOSCNT register.
- `On unit time-out event` — Latch
  on unit time-out. The position counter, capture timer, and
  capture period values are latched into the QPOSLAT,
  QCTMRLAT, and QCPRDLAT registers on unit time-out.

### **Unit timer period (0~4294967295)** — Sets unit timer period `100000000` (default) | value in the range [0, 4,294,967,295]

Set the unit timer period.

#### Dependencies

This parameter appears only when you set **Capture timer
and position** to `On unit time-out
event`.

### **Output capture timer latched value** — Outputs capture timer latched value `off` (default) | `on`

Outputs the capture timer latched value from the QCTMRLAT register at
the output port **qctmrlat**.

### **Output capture timer period latched value** — Outputs capture timer period latched value `off` (default) | `on`

Outputs the capture timer period latched value from the QCPRDLAT
register at the output port **qcprdlat**.

### **Output position counter latched value** — Outputs position counter latched value `off` (default) | `on`

Outputs the position counter latched value from the QPOSLAT register
at the output port **qposlat**.

### Compare output

To view the other parameters of this tab, select the **Enable
position-compare sync signal output** option.

### **Enable position-compare sync signal output** — Enables position compare sync signal output `off` (default) | `on`

The eQEP peripheral includes a position compare unit that generates
the position compare sync signal when the position counter register
(QPOSCNT) and the position compare register (QPOSCMP) values match. This
option enables the position compare sync signal output. The sync signal
can be output using an index pin or strobe pin of the eQEP
peripheral.

### **Sync output pin selection** — GPIO pin used for sync signal `Index pin is used for sync output` (default) | `Strobe pin is used for sync output`

The GPIO pin used for the sync signal output. Use the index pin or
strobe pin of the eQEP peripheral to output the position compare sync
signal.

### **Compare value source** — Source of value for position comparison `Specify via dialog` (default) | `Input port`

Source of the value to be used for the position compare register
(QPOSCMP). When this parameter is set to `Input
port` the input port **cmp** is
created.

### **Position compare shadow load mode** — Shadow mode for generating position compare sync signal `Load on QPOSCNT=0` (default) | `Shadow disabled(load immediate)` | `Load on QPOSCNT=QPOSCMP`

This parameter lets you enable or disable shadow mode for updating the
position compare (QPOSCMP) register. When shadow mode is enabled, you
can also choose an event to trigger the loading of the shadow register
value into the active register. When shadow mode is disabled, the
processor directly loads the value into the active register.

`Load on QPOSCNT=0` loads on a position
counter zero event, and `Load on
QPOSCNT=QPOSCMP` loads when the QPOSCNT and QPOSCMP
values match. When you select these options, shadow mode is
enabled.

### **Position compare value (0~4294967295)** — Value for comparing postiton `4294967295` (default) | value in the range [0, 4,294,967,295]

This value is loaded into the position compare register
(QPOSCMP).

#### Dependencies

This parameter appears only when you set **Compare value
source** to `Specify via
dialog`.

### **Sync output pulse width (1~4096)** — Pulse width of position compare sync output signal `1` (default) | value in the range [0, 4,096]

The pulse stretcher logic in the position compare unit generates a
programmable position compare sync pulse output on the position compare
match.

A value from `1` to `4096` that
determines the pulse width of the position compare sync output signal.
The width of the output pulse, measured in SYSCKOUT cycles, is four
times the entered value.

### **Polarity of sync output** — Polarity of sync output `Active high` (default) | `Active low`

Select the polarity of the sync output signal generated.

### Watchdog unit

### **Watchdog timer enable** — Enables watchdog time-out flag `off` (default) | `on`

The eQEP peripheral contains a watchdog timer that monitors the
quadrature clock to indicate that the motion-control system is
operating. The timer is reset on an edge transition of the quadrature
clock. The watchdog unit generates an interrupt, which you can enable in
the **Interrupt** tab.

### **Watchdog timer** — Time-out value for watchdog timer `65535` (default) | value in the range [0, 65,535]

The time period after which the watchdog unit generates an
interrupt.

#### Dependencies

This parameter appears only when you select **Watchdog
timer enable**.

### Signal Data Types

When you select signals as output in the other tabs, the corresponding signals
appear in this tab. For example, when you select the **Output position
counter** option on the **Position counter**
tab, the **Position counter value data type** option appears on
this tab. Using this tab, you can select the data types of the signals.

The valid data types are `auto`,
`double`, `single`,
`int8`, `uint8`,
`int16`, `uint16`,
`int32`, `uint32`, and
`boolean`.

The following table summarizes the options for which you can set the data type in
the **Signal data types** tab:

| Pane | Option |
| --- | --- |
| General | Quadrature direction flag output port |
| Position counter | Output position counter (selected by default) |
| Output position counter error flag |
| Output latch position counter on index event |
| Output latch position counter on strobe event |
| Speed calculation | Output capture timer |
| Output capture period timer |
| Enable and output overflow error flag |
| Enable and output direction change error flag |
| Output capture timer latched value |
| Output capture timer period latched value |
| Output position counter latched value |

### Interrupt

Interrupts corresponding to specific events are enabled or disabled based on the
settings in this tab. The generated interrupts are used with the C28x Hardware Interrupt.

### **Position counter error interrupt enable** — Enables position counter error interrupts `off` (default) | `on`

Enables position counter error interrupts. The position counter
interrupt is generated only in index event reset mode. When eQEP is
configured in this mode, the position counter value is latched to the
QPOSILAT register, and the direction information is recorded on every
index event marker. If the latched value is not equal to 0 or QPOSMAX,
the position counter error interrupt is generated.

### **Quadrature phase error interrupt enable** — Enables quadrature phase error interrupts `off` (default) | `on`

Enables quadrature phase error interrupts. In quadrature count mode,
the quadrature inputs QEPA and QEPB are expected to be 90 degrees out of
phase. The quadrature phase error interrupt is generated when edge
transition is detected simultaneously on the QEPA and QEPB
signals.

### **Quadrature direction change interrupt enable** — Enables quadrature direction change interrupt `off` (default) | `on`

When the direction of counting changes, the quadrature direction
change interrupt is generated.

### **Watchdog timeout interrupt enable** — Enables watchdog timeout interrupts `off` (default) | `on`

The eQEP peripheral contains a watchdog timer that monitors the
quadrature clock. If no quadrature clock event is detected until the
watchdog timer matches the watchdog period, time-out occurs and the
watchdog timeout interrupt is generated.

### **Position counter underflow interrupt enable** — Enables position counter underflow interrupts `off` (default) | `on`

Enables position counter underflow interrupts. In the reverse
direction, if the position counter reaches 0, then the position counter
is reset to QPOSMAX on the next QEP clock and the position counter
underflow interrupt is generated.

### **Position counter overflow interrupt enable** — Enables position counter overflow interrupts `off` (default) | `on`

Enables position counter overflow interrupts. In the forward
direction, if the position counter reaches QPOSMAX, the position counter
is reset to 0 on the next QEP clock, and the position counter overflow
interrupt is generated.

### **Position-compare ready interrupt enable** — Enables position compare ready interrupts `off` (default) | `on`

Enables position compare ready interrupts. When the position compare
register is configured for shadow mode, the position compare ready
interrupt is generated after the shadow register value is loaded into
the active register.

### **Position-compare match interrupt enable** — Enables position compare match interrupts `off` (default) | `on`

Enables position compare match interrupts. The position compare match
interrupt is generated when the position counter value QPOSCNT matches
with the active position compare register QPOSCMP.

### **Strobe event latch interrupt enable** — Enables strobe event latch interrupts `off` (default) | `on`

Enables strobe event latch interrupts. The strobe event latch
interrupt is generated when the position counter is latched to the
QPOSSLAT register during a strobe event latch.

### **Index event latch interrupt enable** — Enables index event latch interrupts `off` (default) | `on`

Enables index event latch interrupts. The strobe event latch interrupt
is generated when the position counter is latched to the QPOSILAT
register during an index event latch.

### **Unit timeout interrupt enable** — Enables unit timeout interrupts `off` (default) | `on`

Enables unit timeout interrupts. The unit time-out interrupt is
generated when the unit timer matches the unit period.
## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Quadrature encoder pulse block used to derive position, direction, and speed

The enhanced quadrature encoder pulse (eQEP) block is used along with a linear or
rotary incremental encoder to get position, direction, and speed information from a
rotating machine.

The eQEP peripheral module inputs include QEPA, QEPB, QEPI (index), and QEPS
(strobe).

To configure your device to work with the block, navigate to **Model Configuration Parameters** > **Hardware Implementation**, select your device at **Hardware board**, and
expand **Target hardware resources**.
