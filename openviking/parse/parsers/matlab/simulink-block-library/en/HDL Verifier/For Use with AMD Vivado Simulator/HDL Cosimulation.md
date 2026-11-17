---
type: simulink-block
title: 'HDL Cosimulation'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with AMD Vivado Simulator'
documentation_page: 'hdlcosimulation'
documentation_source_path: 'ref/hdlcosimulation.html'
language: en
---

# HDL Cosimulation

## Ports
```yaml
ports:
- name: HDL_input_port_name
  summary: Signal passed from Simulink to HDL simulator scalar | vector
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | Fixed-point
- name: HDL_output_port_name
  summary: Signal passed from HDL simulator to Simulink scalar | vector
  direction: output
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | Fixed-point
```

### Input

### **HDL\_input\_port\_name** — Signal passed from Simulink to HDL simulator scalar | vector

The ports on the block correspond with ports on your HDL design. Add or remove ports on the **Ports** tab.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`
### Output

### **HDL\_output\_port\_name** — Signal passed from HDL simulator to Simulink scalar | vector

The ports on the block correspond with ports on your HDL design. Add or remove ports on the **Ports** tab.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`
## Parameters
```yaml
parameters:
- name: Block Info
  summary: 'Block information for Vivado cosimulation Read-only: block generation settings'
  group: ''
- name: Enable direct feedthrough
  summary: Work around algebraic loop warnings true (default) | false
  group: Ports
- name: Full HDL Name
  summary: Signal path name string
  group: Ports
- name: I/O Mode
  summary: Port direction Input | Output
  group: Ports
- name: HDL Type
  summary: 'Type of HDL port signal Read-only: Logic (default) | Vector'
  group: Ports
- name: HDL Dims
  summary: 'Dimension of HDL port signal Read-only: scalar | vector'
  group: Ports
- name: Sample Time
  summary: Time between reading samples on an output port 1 (default) | integer
  group: Ports
- name: Data Type
  summary: Simulink Data type for output signal Inherit (default) | Fixedpoint | Double | Single | Half
  group: Ports
- name: Sign
  summary: Sign component of output data type Unsigned (default) | Signed
  group: Ports
- name: Fraction Length
  summary: Number of fractional bits in output data type integer
  group: Ports
- name: Simulink Word Length
  summary: Bit width of Simulink port integer <129 | inherit
  group: Ports
- name: HDL Word Length
  summary: 'Bit width of HDL port Read-only: integer'
  group: Ports
- name: Time to run HDL simulator before cosimulation starts
  summary: time required for HDL simulation before cosimulation starts 0 (default) | nonnegative integer
  group: Clocks
- name: Full HDL Name
  summary: Signal path name string
  group: Clocks
- name: Active Clock Edge
  summary: HDL clock edge used to sample signals Rising (default) | Falling
  group: Clocks
- name: Waveform Type
  summary: Generate waveforms to drive clocks, resets, or enables to HDL design Rising (default) | Falling | Step 1 to 0 |
    Step 0 to 1
  group: Clocks
- name: Period/Duration
  summary: Clock period 2 (default) | integer
  group: Clocks
- name: Automatically determine timescale at start of simulation
  summary: When to calculate automatic timescale true (default) | false
  group: Timescales
- name: 1 second in Simulink corresponds to {} in the HDL simulator
  summary: Timing relationship between Simulink and HDL simulator integer and time units
  group: Timescales
- name: Connection mode
  summary: Connection between Simulink and HDL simulator Full Simulation (default) | Confirm Interface Only | No Connection
  group: Connection
- name: HDL simulator is running on this computer
  summary: Same host for HDL simulator and Simulink true (default) | false
  group: Connection
- name: Connection method
  summary: Connection between HDL simulator and Simulink Socket (default) | Shared memory
  group: Connection
- name: Host name
  summary: HDL simulator host machine string
  group: Connection
- name: Port number or service
  summary: Socket port number string
  group: Connection
- name: Show connection info on icon
  summary: Add connection parameters on block icon true (default) | false
  group: Connection
- name: Time to run HDL simulator before cosimulation starts
  summary: Offset that aligns Simulink with HDL simulator integer and time unit
  group: Simulation
- name: Pre-simulation Tcl commands
  summary: Commands to run in HDL simulator before cosimulation string
  group: Simulation
- name: Post-simulation Tcl commands
  summary: Commands to run in HDL simulator after cosimulation string
  group: Simulation
```

### **Block Info** — Block information for Vivado cosimulation Read-only: block generation settings

This parameter is read-only.

This section displays information after you generate this block using the
Cosimulation Wizard. It displays
the following items:

- HDL Simulator – Vivado simulator
- HDL Design Library – Location of HDL library files
- HDL Language – VHDL or Verilog
- HDL Time Precision – Time precision of HDL design
- HDL Waveform File – Name and path of waveform file

When generating a cosimulation block for Vivado simulator, you cannot change the names and directions of
ports, clocks, resets, or time precision using the block mask. To change
these items, open the Cosimulation Wizard and regenerate the
block.

#### Dependencies

This parameter is visible only when you use Vivado cosimulation.

### Ports

### **Enable direct feedthrough** — Work around algebraic loop warnings `true` (default) | `false`

Eliminates the one output-sample delay difference between the
cosimulation and Simulink that occurs when your model contains purely combinational
paths. Clear this check box if the HDL Cosimulation block
is in a feedback loop and generates algebraic loop warnings or errors.
When you simulate a sequential circuit that has a register on the data
path, specifying direct feedthrough does not affect the timing of that
data path.

#### Dependencies

### **Full HDL Name** — Signal path name string

Specify the signal path name using the HDL simulator path name syntax.
For example, `manchester.samp` for Xcelium HDL simulators. The signal can be at any level of the HDL
design hierarchy. The HDL Cosimulation block port
corresponding to the signal is labeled with this name.

For rules on specifying port and module path names in Simulink, see Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation.

You can copy signal path names directly from the HDL simulator
**wave** window and paste them into the
**Full HDL Name** field. Use the
*`Path.Name`* view and not
*`Db::Path.Name`* view. After pasting a
signal path name into **Full HDL Name**, click
**Apply** to complete the paste operation and
update the signal list.

#### Dependencies

If the block was generated from the Cosimulation
Wizard, this value should not be changed. For the
Vivado HDL Cosimulation block the parameter is
read-only.

### **I/O Mode** — Port direction `Input` | `Output`

To add a bidirectional port, add the port to the list twice, as both
input and output.

`Input` — HDL signals that Simulink drives. Simulink deposits values on the specified HDL simulator signal at
the specified sample rate.

**Note**

When you define a block input port, make sure that only one source
is set up to drive input to that signal. For example, avoid defining
an input port that has multiple instances. If multiple sources drive
input to a single signal, your simulation model produces unexpected
results.

`Output` — HDL signals that Simulink reads. For output signals, you must specify an explicit
sample time. You can also specify the data type, but the width must
match the width of the signal in HDL. For details on specifying a data
type, see the **Data Type** and **Fraction
Length** parameters.

Simulink signals do not have a tristate semantic because there is
no `'Z'` value. To interface with bidirectional
signals, connect to the input and enable signals of both the output
driver and the output signal of the input driver. This approach leaves
the actual tristate buffer in HDL, where resolution functions can handle
interfacing with other tristate buffers.

#### Dependencies

If the block was generated from the Cosimulation
Wizard, this value should not be changed. For the
Vivado HDL Cosimulation block the parameter is
read-only.

### **HDL Type** — Type of HDL port signal Read-only: `Logic` (default) | `Vector`

This parameter is read-only.

Displays the type of the HDL port signal, as configured by the
Cosimulation Wizard.

#### Dependencies

This parameter is visible only if the block was generated for use
with Vivado cosimulation.

### **HDL Dims** — Dimension of HDL port signal Read-only: scalar | vector

This parameter is read-only.

Displays the dimensions of the HDL port signal, as configured by the
Cosimulation Wizard.

#### Dependencies

This parameter is visible only if the block was generated for use
with Vivado cosimulation.

### **Sample Time** — Time between reading samples on an output port 1 (default) | integer

Time interval between consecutive samples applied to an output
port.

Simulink reads a value from the associated HDL simulator signal at
the sample rate specified here.

In general, Simulink handles port sample periods as follows:

- If you connect an input port to a signal that has an explicit
  sample period, based on forward propagation, Simulink applies that rate to the port.
- If you connect an input port to a signal that does not have an
  explicit sample period, Simulink assigns a sample period that is equal to the least
  common multiple (LCM) of all identified input port sample
  periods in the model.
- You must specify an explicit sample time for each output
  port.

The HDL time corresponding to the Simulink sample time hits depends on the
**Timescales** setting. See Simulation Timescales.

#### Dependencies

To enable this parameter, set **I/O Mode** to
`Output`.

### **Data Type** — Simulink Data type for output signal `Inherit` (default) | `Fixedpoint` | `Double` | `Single` | `Half`

Select `Inherit` to automatically determine
the data type. The block checks that the inherited word length matches
the word length queried from the HDL simulator. If they do not match,
Simulink generates an error message. For example, if you connect a
Signal Specification block to an output,
`Inherit` forces the data type specified by
the Signal Specification block onto the output
port.

If Simulink cannot determine the data type of the signal connected to
the output port, it queries the HDL simulator for the data type of the
port. As an example, if the HDL simulator returns the VHDL® data type `STD_LOGIC_VECTOR` for a signal
of size `N` bits, the data type
`ufixN` is forced on the output port. The implicit
fraction length is 0.

You can also assign an explicit data type, with optional
**Fraction Length**. By explicitly assigning a data
type, you can force fixed-point data types on output ports of the
HDL Cosimulation block. For example, for an 8-bit
output port, setting the **Sign** to
`Signed` and setting the **Fraction
Length** to `5` forces the data type to
`sfix8_En5`. You cannot force width. The width is
always inherited from the HDL simulator.

The **Data Type** and **Fraction
Length** properties apply only to the following types of
HDL signals:

- VHDL signals of any logic type, such as
  `STD_LOGIC` or
  `STD_LOGIC_VECTOR`
- Verilog® signals of `wire` or
  `reg` type

#### Dependencies

To enable this parameter, set **I/O Mode** to
`Output`.

During cosimulation with the Vivado simulator, this parameter is displayed as
**Simulink Data Type**.

### **Sign** — Sign component of output data type `Unsigned` (default) | `Signed`

Sign designation for explicit output port data type.

#### Dependencies

To enable this parameter, set **I/O Mode** to
`Output`, and set **Data
Type** to `Fixedpoint`.

### **Fraction Length** — Number of fractional bits in output data type integer

Size, in bits, of the fractional part of a fixed-point output signal.
For example, for an 8-bit output port, setting the
**Sign** to `Signed` and setting
the **Fraction Length** to `5` forces
the data type to `sfix8_En5`. You cannot force width;
the width is always inherited from the HDL simulator.

#### Dependencies

To enable this parameter, set **I/O Mode** to
`Output`, and **Data
Type** property to
`Fixedpoint`.

The **Data Type** and **Fraction
Length** properties apply only to the following types
of HDL signals:

- VHDL signals of any logic type, such as
  `STD_LOGIC` or
  `STD_LOGIC_VECTOR`
- Verilog signals of `wire` or
  `reg` type

### **Simulink Word Length** — Bit width of Simulink port integer <129 | `inherit`

Size of the Simulink port, specified as a positive integer smaller than 129.

**For input ports** — this value is set
to `inherit` (read only).

When the **HDL Word Length** parameter is greater
than 128 bits the Simulink port dimensions are determined at compile time by the data
type of the driving signal. For example:

- When **HDL Word Length** = 150 and
  **Simulink Word Length** = 50,
  HDL Verifier™ allows a Simulink port with data width of 50 bits, and dimensions of
  size 3 such as `sfix50(3)` or
  `ufix50(3)`.
- When **HDL Word Length** = 140 and
  **Simulink Word Length** = 50,
  HDL Verifier packs 150 bits of Simulink into 140 bits of HDL. HDL Verifier ignores the 10 most significant bits (MSB) of the
  last word.

  Three Simulink input words of 50 bits each are packed into an HDL input signal of 140 bits. The 10 MSB of the last Simulink word are ignored by the HDL server

**For output ports** — there are 2
cases.

- When the **HDL Word Length** parameter is
  less than 129 bits, this parameter matches the width of the HDL
  port, and it is read-only.
- When the **HDL Word Length** parameter is
  greater than 128 bits, HDL Verifier creates a vector of ports to represent this port.
  For example:

  - When **HDL Word Length** = 150
    and **Simulink Word Length** =
    50, HDL Verifier creates a Simulink port with data width of 50 bit. For
    example `sfix50(3)` or
    `ufix50(3)`.
  - When **HDL Word Length** = 150
    and **Simulink Word Length** =
    60, HDL Verifier creates a Simulink port with data width of 60, such as
    `sfix60(3)` or
    `ufix60(3)`. Since the HDL word
    has only 150 bits, and the Simulink port requires 180 bits, 30 bits are
    padded or sign extended.
  - When **HDL Word Length** = 140
    and **Simulink Word Length** =
    50, every 50 bits of the HDL output are represented
    as a Simulink word. The 10 MSB of the last
    Simulink word are unused and extended according
    to the **Sign** parameter.

    HDL output signal of 140 bits is packed into three Simulink words of 50 bits each. The last word uses only 40 bits, and 10 bits are extended

#### Dependencies

When **HDL Word Length** is smaller than 129,
this parameter is read-only.

### **HDL Word Length** — Bit width of HDL port Read-only: integer

This parameter is read-only.

Size, in bits, of the HDL port.

**Verilog or SystemVerilog example**: In
the code below, the input `In1` has an HDL word length
of 140 bits, and the output `Out1` has an HDL word
length of 160 bits.

```
input [1:0][69:0] In1;
output [159:0] Out1;
```

**VHDL example**: In the code below,
`In1` has an HDL word length of 120 bits, and
`In2` has an HDL word length of 1200 bits.

```
TYPE matrix_of_std_logic_vector120 IS ARRAY (NATURAL RANGE <>, NATURAL RANGE <>) OF std_logic_vector(119 DOWNTO 0);
In1: IN matrix_of_std_logic_vector120(0 TO 4, 0 TO 1);
In2: IN std_logic_vector(1199 DOWNTO 0);
```

### Clocks

**Note**

- During cosimulation with the Vivado simulator, this tab is named **Clocks, Resets,
  Enables**.
- During cosimulation with the VCS simulator, this tab is not available. Use the
  `PreSimulationTcl` property of the `launchVCS` function to define clock and reset
  signals.

Create optional rising-edge and falling-edge clocks that apply stimuli to your cosimulation
model. The scrolling list displays HDL clocks that drive values to the HDL signals
that you are modeling, using the deposit method. The clock signals must be
single-bit signals. Vector signals are not supported. For instructions on adding and
editing clock signals, see Creating Optional Clocks with the Clocks Pane of the HDL Cosimulation Block.

### **Time to run HDL simulator before cosimulation starts** — time required for HDL simulation before cosimulation starts `0` (default) | nonnegative integer

Specify the time required for the HDL simulation to run before
starting the cosimulation. Specify a nonnegative integer, and select
time units from the menu.

- `fs` – Femtoseconds
- `ps` – Picoseconds
- `ns` – Nanoseconds
- `us` – Microseconds
- `ms` – Milliseconds
- `s` – Seconds

#### Dependencies

To enable this parameter, generate this block for Vivado cosimulation.

### **Full HDL Name** — Signal path name string

Specify each clock as a signal path name, using the HDL simulator
path name syntax. For example: `/manchester/clk` or
`manchester.clk`.

For information about and requirements for path specifications in
Simulink, see Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation.

You can copy signal path names directly from the HDL simulator
**wave** window and paste them into the
**Full HDL Name** field. Use the
*`Path.Name`* view and not
*`Db::Path.Name`* view. After pasting a
signal path name into **Full HDL Name**, click
**Apply** to complete the paste operation and
update the signal list.

#### Dependencies

If the block was generated from the Cosimulation
Wizard, this value should not be changed. For the
Vivado HDL Cosimulation block the parameter is
read-only.

### **Active Clock Edge** — HDL clock edge used to sample signals `Rising` (default) | `Falling`

Select one of the following options.

- `Rising` – Specify a rising-edge
  clock.
- `Falling` – Specify a
  falling-edge clock.

The periods and durations are Simulink times. To relate Simulink times to HDL times, go to the
**Timescales** tab and click **Determine
Timescale Now**.

#### Dependencies

This parameter is visible only for ModelSim or Xcelium cosimulation.

### **Waveform Type** — Generate waveforms to drive clocks, resets, or enables to HDL design `Rising` (default) | `Falling` | `Step 1 to 0` | `Step 0 to 1`

For Vivado cosimulation, select one of the following options.

- `Active Rising Edge Clock` – Create a
  periodic signal with 50% duty cycle where the rising edge is
  offset from when Simulink drives the inputs.
- `Active Falling Edge Clock` – Create
  a periodic signal with 50% duty cycle where the falling edge is
  offset from when Simulink drives the inputs.
- `Step 0 to 1` – Create a step
  function that starts by driving a 0 for the specified duration,
  then transitions to 1.
- `Step 1 to 0` – Create a step
  function that starts by driving a 1 for the specified duration,
  then transitions to 0.

The periods and durations are Simulink times. To relate Simulink times to HDL times, go to the
**Timescales** tab and click **Show Times
and Suggest Timescale**.

#### Dependencies

This parameter is visible only for Vivado cosimulation.

### **Period/Duration** — Clock period 2 (default) | integer

To specify an explicit clock period, enter a sample time equal to or
greater than two resolution units (ticks).

If the clock period is not an even integer, Simulink cannot create a 50% duty cycle. Instead, the HDL Verifier software creates the falling edge at
`clockperiod/2` (rounded down to the nearest
integer).

For ModelSim or Xcelium periods and durations are specified as Simulink time, and for Vivado they are specified as HDL time.

#### Dependencies

This property is not available for cosimulation with VCS.

### Timescales

Choose a timing relationship between Simulink and the HDL simulator, either manually or automatically. These parameters specify a correspondence between one second of Simulink time and some quantity of HDL simulator time. This quantity of HDL simulator time can be expressed in one of the following ways:

- *Relative* timing relationship (Simulink seconds correspond to an HDL simulator precision, or
  "tick".
- *Absolute*  timing relationship (Simulink seconds correspond to an absolute unit of HDL simulator time)

For more information on calculating relative and absolute timing modes, see Defining the Simulink and HDL Simulator Timing Relationship.

For detailed information on the relationship between Simulink and the HDL simulator during cosimulation, and on the operation of relative and absolute timing modes, see Simulation Timescales.

To see the relationship between the Simulink times and HDL times of all of the ports, clocks, resets, and enables
click **Show Times and Suggest Timescale**. This action also
automatically determines a usable timescale if needed.

### **Automatically determine timescale at start of simulation** — When to calculate automatic timescale `true` (default) | `false`

If you select this option, HDL Verifier calculates the timescale when you start the Simulink simulation. If this option is not selected, click
**Determine Timescale Now** to calculate the
timescale immediately without starting a simulation. For Vivado cosimulation, this button shows as **Show Times
and Suggest Timescale**. Alternatively, you can manually
select a timescale. For guidance through the automatic timescale
calculation, see Specify Timing Relationship Automatically.

#### Dependencies

For VCS cosimulation, this parameter is disabled. You can
click **Show Timescale** after establishing a
connection between VCS and Simulink to open a dialog box with port time mapping
information. For more information about starting a VCS cosimulation, see Start VCS from MATLAB.

### **1 second in Simulink corresponds to {} in the HDL simulator** — Timing relationship between Simulink and HDL simulator integer and time units

This parameter consists of a *Time* value and a
*TimeUnit* value.

To configure relative timing mode for a cosimulation:

1. Verify that `Tick`, the default
   setting for *TimeUnit*, is selected. If it is
   not, then select it from the list on the right.
2. Enter a scale factor in the *Time* text box
   on the left. The default scale factor is 1.

To configure absolute timing mode for a cosimulation:

1. Set *TimeUnit* to a unit of absolute time:
   `fs` (femtoseconds), `ps`
   (picoseconds), `ns` (nanoseconds),
   `us` (microseconds), `ms`
   (milliseconds), or `s` (seconds).
2. Enter a scale factor in the *Time* text box
   on the left. The default scale factor is 1.

### Connection

This tab is not visible during cosimulation with the Vivado simulator.

### **Connection mode** — Connection between Simulink and HDL simulator `Full Simulation` (default) | `Confirm Interface Only` | `No Connection`

Type of connection between Simulink and the HDL simulator.

- `Full Simulation`: Confirm
  interface and run HDL simulation.
- `Confirm Interface Only`: Connect
  to the HDL simulator and check for signal names, dimensions,
  and data types, but do not run HDL simulation. During
  Simulink simulation, there is no contact with the HDL
  simulator.
- `No Connection`: Do not
  communicate with the HDL simulator. The HDL simulator does
  not need to be started.

### **HDL simulator is running on this computer** — Same host for HDL simulator and Simulink `true` (default) | `false`

When both applications run on the same computer, you can choose shared
memory or TCP sockets for the communication channel between the
applications. If you do not select this option, only TCP/IP socket mode
is available, and the **Connection method** list
becomes unavailable.

#### Dependencies

For VCS cosimulation, this parameter is disabled.

### **Connection method** — Connection between HDL simulator and Simulink `Socket` (default) | `Shared memory`

- `Socket`: Simulink and the HDL simulator communicate via a
  designated TCP/IP socket. TCP/IP socket mode is more
  versatile. You can use it for single-system and network
  configurations. This option offers the greatest scalability.
  For more on TCP/IP socket communication, see TCP/IP Socket Ports.
- `Shared memory`: Simulink and the HDL simulator communicate via shared
  memory. Shared memory communication provides optimal
  performance and is the default mode of communication.

#### Dependencies

- This parameter shows when you select **HDL
  Simulator is running on this computer**.
- VCS cosimulation supports only socket
  communication.

### **Host name** — HDL simulator host machine string

This parameter applies if you run Simulink and the HDL simulator on different computers.

#### Dependencies

For VCS cosimulation, this parameter is read-only.

### **Port number or service** — Socket port number string

Indicate a valid TCP socket port number or service for your computer
system, if you are not using shared memory. For information on choosing
TCP socket ports, see TCP/IP Socket Ports.

### **Show connection info on icon** — Add connection parameters on block icon `true` (default) | `false`

When you select this option, the HDL Cosimulation block
icon displays the current communication parameter settings. If you
select shared memory, the icon displays `SharedMem`. If
you select TCP socket communication, the icon displays
`Socket` and displays the host name and port number
in the format `hostname:port`.

This information can help you distinguish between multiple HDL
Cosimulation blocks, where each block is communicating to a
different instance of the HDL simulator.

### Simulation

This tab is not visible during cosimulation with the Vivado simulator.

### **Time to run HDL simulator before cosimulation starts** — Offset that aligns Simulink with HDL simulator integer and time unit

Specifies the amount of time to run the HDL simulator before beginning
simulation in Simulink. Specifying this time properly aligns the signal of the
Simulink block and the HDL signal so that they can be compared and
verified directly without additional delays.

This setting consists of a *PreRunTime* value and a
*PreRunTimeUnit* value.

- *PreRunTime*: Any valid time value. The
  default is 0.
- *PreRunTimeUnit*: Specifies the units of time
  for *PreRunTime*.

  - `Tick`
  - `s`
  - `ms`
  - `us`
  - `ns`
  - `ps`
  - `fs`

### **Pre-simulation Tcl commands** — Commands to run in HDL simulator before cosimulation string

The cosimulation tool executes these commands in the HDL simulator,
before simulating the HDL component of your Simulink model. If you enter multiple commands on one line, append
each command with a semicolon (;), the standard Tcl concatenation
operator.

For example, use this parameter to generate a one-line echo command to
confirm that a simulation is running, or a complex script that performs
an extensive simulation initialization and startup sequence. You cannot
use these commands to change simulation state.

You can specify any valid Tcl command. The Tcl command you specify
cannot include commands that load an HDL simulator project or modify
simulator state. For example, the character vector cannot include
commands such as `start`, `stop`, or
`restart` (for ModelSim) or `run`, `stop`, or
`reset` (for Xcelium).

#### Dependencies

For VCS cosimulation, this parameter is disabled. Use the
`PreSimulationTcl` property of the `launchVCS` function to define pre-simulation Tcl
commands.

### **Post-simulation Tcl commands** — Commands to run in HDL simulator after cosimulation string

The cosimulation tool executes these commands in the HDL simulator,
after simulating the HDL component of your Simulink model.

You can specify any valid Tcl command. The Tcl command you specify
cannot include commands that load an HDL simulator project or modify
simulator state. For example, the string cannot include commands such as
`start`, `stop`, or
`restart` (for ModelSim) or `run`, `stop`, or
`reset` (for Xcelium).

**Note**

After each ModelSim simulation, the simulator takes time to update the
coverage result. To prevent the potential conflict between this
process and the next cosimulation session, add a short pause between
each successive simulation.

#### Dependencies

For VCS cosimulation, this parameter is disabled. Use the
`PostSimulationTcl` property of the `launchVCS` function to define post-simulation Tcl
commands.
## Libraries

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder provides additional configuration options that affect HDL
implementation and synthesized logic. You can generate HDL code for cosimulation
blocks used with Siemens®
ModelSim, Cadence®
Xcelium, or AMD®
Vivado simulators.

Each of the HDL Cosimulation blocks cosimulates a hardware
component by applying input signals to, and reading output signals from, an HDL
model that executes under an HDL simulator. See Generate Cosimulation Model (HDL Coder).

For information about timing, latency, data typing, frame-based processing, and
other issues when setting up an HDL cosimulation, see Define HDL Cosimulation Block Interface.

You can use an HDL Cosimulation block with HDL Coder to generate an interface to your manually written or legacy HDL code.
When an HDL Cosimulation block is included in a model, the coder
generates a VHDL or Verilog interface, depending on the selected target language.

When the target language is VHDL, the generated interface includes:

- An entity definition. The entity defines ports (input, output, and clock)
  corresponding in name and data type to the ports configured on the
  HDL Cosimulation block. Clock enable and reset ports are
  also declared.
- An RTL architecture including a component declaration, a component
  configuration declaring signals corresponding to signals connected to the
  HDL Cosimulation ports, and a component
  instantiation.
- Port assignment statements as required by the model.

When the target language is Verilog, the generated interface includes:

- A module defining ports (input, output, and clock) corresponding in name
  and data type to the ports configured on the HDL Cosimulation
  block. The module also defines clock enable and reset ports, and
  `wire` declarations corresponding to signals connected
  to the HDL Cosimulation ports.
- A module instance.
- Port assignment statements as required by the model.

Before initiating code generation, check that the model meets the requirements for
code generation. To check the requirements for code generation, select the
**Debug** tab, and then click **Update
Model**.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

For implementation parameter descriptions, see Customize Black Box or HDL Cosimulation Interface (HDL Coder).

## Version History

**Introduced in R2008a**

### R2024b: Support added for VCS simulator

To create an HDL Cosimulation block for the Synopsys
VCS simulator, add this block to a Simulink testbench, and configure the parameters to match your HDL DUT: Specify
port names and properties, timescales, connection, and simulation options.

### R2022a: Support added for Vivado simulator

To create an HDL Cosimulation block for the Vivado simulator, use the Cosimulation Wizard to generate and configure an HDL
Cosimulation block. Then, use the generated block in a Simulink testbench.

## Description

Cosimulate HDL design by connecting Simulink with HDL simulator

The HDL Cosimulation block cosimulates a hardware component by applying input
signals to and reading output signals from an HDL model under simulation in the HDL
simulator. Configure and generate this block using the Cosimulation Wizard.

- When cosimulating with the Vivado® simulator, you must first generate this block using the Cosimulation Wizard.
- When cosimulating with VCS®, ModelSim™ or Xcelium™, you can optionally bypass the wizard and configure the block
  directly.

You can configure these options on the block:

- Mapping of the input and output ports of the block to correspond with signals
  (including internal signals) of an HDL module. You must specify a sample time
  for each output port. You can optionally specify a data type for each output
  port. Vivado cosimulation does not support mapping of internal signals.
- Type of communication and communication settings used to exchange data between simulators.
- The timing relationship between units of simulation time in Simulink® and the HDL simulator.
- Rising-edge or falling-edge clocks to apply to your model. You can specify the period for each clock signal.
- Tcl commands to run before and after the simulation.

You can use this block to model a source or sink device by configuring the block with
input or output ports only.

**Compatibility with Simulink Code Generation**

- This block participates in HDL code generation with HDL Coder™. The coder generates an interface to your manually written or legacy HDL code. It does not participate in C code generation with Simulink
  Coder™.
