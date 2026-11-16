---
type: simulink-block
title: 'XCP UDP Data Acquisition'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / UDP'
documentation_page: 'xcpudpdataacquisition'
documentation_source_path: 'ug/xcpudpdataacquisition.html'
language: en
---

# XCP UDP Data Acquisition

## Ports

Not documented in R2025b.

## Parameters

### **Config name** — Specify XCP UDP session name select from list

Select the name of XCP configuration that you want to use. This list displays
all available names specified in the XCP UDP Configuration blocks
in the model. Selecting a configuration displays events and measurements available
in the A2L file of this configuration. You can acquire measurements for only one
event by using an XCP UDP Data Acquisition block. Use one block for
each event whose measurements you want to acquire.

### **Event name** — Select an event select from list

Select an event from the available list of events. The XCP UDP
Configuration block uses the specified A2L file to populate the events
list.

### **All Measurements** — List all measurements available for event measurements list

This list displays all measurements available for the selected event. Select
the measurement that you want to use and click the add button,
 to add it to the selected measurements. Hold the
`Ctrl` key on your keyboard to select multiple measurements.

In the **Block Parameters** dialog box, type the name of the
measurement you want to use in the **Search** box. The
**All Measurements** lists displays a list of all matching
names. Click the x to clear your search.

### **Selected Measurements** — List selected measurements measurement names

This list displays selected measurements. To remove a measurement from this
list, select the measurement and click the remove button,
.

In the **Block Parameters** dialog box, use the toggle buttons
 to reorder the selected measurements.

### **Block Output Settings** — Set the port output as Compu method conversion values or raw values `Raw values as double (no Compu method conversion)` (default) | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

This parameter enables support for XCP data types and dimensions as defined in
the ASAP2 standard. The Block Output Settings parameter selects whether the port
outputs Compu method conversion values or raw values. The options provide:

- `Physical values (apply Compu method conversion)`
  enables the raw-to-physical conversion of ECU measurement values. For this
  option, the block port settings are set either to
  `'double'` or `'string'`, based on the
  underlying Compu method conversion. For example, Compu method
  `IDENTICAL`, `LINEAR`,
  `RAT_FUNC`, `TAB_INTP`, and
  `TAB_NOINTP` port settings is
  `'double'` while Compu method
  `TAB_VERB` port settings is `'string'`.
  The maximum string length supported for Compu method conversion is 1024 as
  specified in the ASAM XIL
  specification.

  The FORM Compu method conversion is not supported. Simulink throws a
  warning for such a conversion and IDENTICAL conversion is applied to the
  underlying measurement. Also, only scalar measurement signals are supported
  for TAB\_VERB conversion as Simulink only supports scalar strings.

  Selecting this option shows the physical units (if any) in front of the
  measurement name on the block mask. This physical unit is acquired from the
  A2L description of the measurement and Compu method. If the physical unit is
  not specified, only the measurement name is displayed.
- `Raw values (no Compu method conversion)` sets the port
  data type according to the type definition in the A2L file and supports up
  to three-dimensional XCP measurements in Simulink.
- `Raw values as double (no Compu method conversion)` sets
  the port data type as `double`, converting all internal
  measurement values. This selection supports up to three-dimensional XCP
  measurements in Simulink.

These ASAP2 data types are supported by corresponding Simulink port data
types:

- `SBYTE`
- `UWORD`
- `SWORD`
- `ULONG`
- `SLONG`
- `A_UINT64`
- `A_INT64`
- `FLOAT32_IEEE`
- `FLOAT64_IEEE`

The dimension support in the block accommodates the different treatment of
matrices by MATLAB® and the ECU. The MATLAB default operation treats matrices as
row-major matrices. An XCP measurement can have a `LAYOUT` as
`COLUMN_DIR` or `ROW_DIR`. If a matrix
measurement is `COLUMN_DIR`, the blocks rearrange the measurement
in memory and ensure that the matrix (row X, col Y) in MATLAB refers to the same
entry as (row X, col Y) on the ECU. The rearrangement causes matrix entries that
are contiguous on the ECU to be noncontiguous in MATLAB and Simulink.

### **DAQ List Priority** — Specify a priority value for server device driver priority value

Specify a priority value as an integer from 0 to 255 for the server device
driver to prioritize transmission of data packets. The server can accumulate XCP
packets for lower priority DAQ lists before transmission to the client. A value of
255 has the highest priority. The `SET_DAQ_LIST_MODE` command
communicates the **DAQ List Priority** value from
client to server. This communication method differs from the specification of the
Event Channel Priority property, which comes from the A2L file.

### **Sample time** — Specify sampling time of block `-1` (default)

Specify the sampling time of the block during simulation, which is the
simulation time. This value defines the frequency at which the XCP UDP Data
Acquisition block runs during simulation. If the block is inside a
triggered subsystem or is to inherit sample time, you can specify
`–1` as your sample time, which is the default. You can also
specify a MATLAB variable for sample time. For information about simulation sample
timing, see Timing in Hardware Interface Models.

### **Enable Timestamp** — Enable reading timestamp from incoming DTO packets `off` (default) | `on`

When the Timestamp is enabled, the block reads the timestamp from incoming DTO
packets and outputs the timestamp to Simulink. The **Enable
Timestamp** check box appears in the block parameters dialog box when
the parameter is supported in the A2L file.

## Libraries

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The XCP communication blocks support code generation
with limited deployment portability that runs only on the host computer or Simulink
Real-Time™ targets.

Code generation requires a C++ compiler that is
compatible with the code generation target. For more information, see Supported and Compatible Compilers.

## Version History

**Introduced in R2019a**

### R2021b: Compu Method Conversion Support

To add Compu method conversion support, the **Force Datatypes and Allow
Non-Scalar** parameter for the XCP CAN Data Acquisition
block, XCP CAN Data Stimulation block, XCP UDP Data
Acquisition block, and XCP UDP Data Stimulation block has been
replaced with the **Block Input/ Output Settings** parameter. Using
this parameter, you can select whether to apply Compu method conversion to block input
or output.

## Description

Acquire selected measurements from configured server connection

The XCP UDP Data Acquisition block acquires data from the configured
server connection based on the measurements that you select. The block uses the XCP UDP
transport layer to obtain raw data for the selected measurements at the specified
simulation time step. Configure your XCP connection and use the XCP UDP Data
Acquisition block to select your event and measurements for the configured
server connection. The block displays the selected measurements as output ports.

The XCP communication blocks support the use of Simulink® accelerator mode and rapid accelerator mode. You can speed up the execution
of Simulink models by using these modes. For more information on these simulation modes,
see Acceleration (Simulink).
