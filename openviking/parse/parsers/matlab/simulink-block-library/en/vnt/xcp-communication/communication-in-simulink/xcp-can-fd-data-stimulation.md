---
type: simulink-block
title: 'XCP CAN FD Data Stimulation'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / Communication in Simulink'
documentation_page: 'xcpcanfddatastimulation'
documentation_source_path: 'ug/xcpcanfddatastimulation.html'
language: en
---

# XCP CAN FD Data Stimulation

## Ports

### Input

### **Data** — Input samples for data stimulation defined by A2L file

Input data stimulation samples, with names and types defined by the
A2L file. Each entry in the Selected
Measurements parameter defines an input port. A sample is
written at every port for every step of the simulation.

## Parameters

### **Config name** — Specify XCP CAN FD session name select from list

Select the name of XCP configuration that you want to use. This list
displays all available names specified in the available XCP CAN FD
Configuration blocks in the model. Selecting a configuration
displays events and measurements available in the A2L file of this
configuration. You can stimulate measurements for only one event by using an
XCP CAN FD Data Stimulation block. Use one block for each
event whose measurements you want to stimulate.

### **Event name** — Select an event select from list

Select an event from the event list. The XCP CAN FD
Configuration block uses the specified A2L file to populate the
events list. The block is configured with the corresponding event number
from the A2L.

The event time cycle does not control transmission of stimulation packets.
The block stimulates each time it executes. For use in Simulink simulation,
consider enabling simulation pacing to avoid free-running
stimulation.

### **All Measurements** — List all measurements available for event measurements list

This list displays all measurements available for the selected event.
Select the measurement that you want to use and click the add button,
 to move it to the selected measurements.
Hold the `Ctrl` key on your keyboard to select multiple
measurements.

In the block parameters dialog box, type the name of the measurement you
want to use in the **Search** box. The **All
Measurements** lists displays a list of all matching names.
Click the x to clear your search.

### **Selected Measurements** — List selected measurements measurement names

This list displays your selected measurements. Each selected measurement
adds an input port to the block with the measurement name. To remove a
measurement from this list, select the measurement and click the remove
button, .

In the **Block Parameters** dialog box, use the shift
buttons  to reorder the selected
measurements.

### **Block Input Settings** — Set the port input as Compu method conversion values or raw values `Raw values as double (no Compu method conversion)` (default) | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

This parameter enables support for XCP data types and dimensions as
defined in the ASAP2 standard. The Block Input Settings parameter selects
whether the port outputs Compu method conversion values or raw values. The
options provide:

- `Physical values (apply Compu method conversion)`
  enables the physical-to-raw conversion of ECU measurement values.
  For this option, the block port settings are set either to
  `'double'` or `'string'`,
  based on the underlying Compu method conversion. For example, Compu
  method `IDENTICAL`, `LINEAR`,
  `RAT_FUNC`, `TAB_INTP`, and
  `TAB_NOINTP` port settings is
  `'double'` while Compu method
  `TAB_VERB` port settings is
  `'string'`. The maximum string length supported
  for Compu method conversion is 1024 as specified in the ASAM XIL
  specification.

  The FORM Compu method conversion is not supported. Simulink throws
  a warning for such a conversion and IDENTICAL conversion is applied
  to the underlying measurement. Also, only scalar measurement signals
  are supported for TAB\_VERB conversion as Simulink only supports
  scalar strings.

  Selecting this option shows the physical units (if any) in front
  of the measurement name on the block mask. This physical unit is
  acquired from the A2L description of the measurement and Compu
  method. If the physical unit is not specified, only the measurement
  name is displayed.
- `Raw values (no Compu method conversion)` sets
  the port data type according to the type definition in the A2L file
  and supports up to three-dimensional XCP measurements in
  Simulink.
- `Raw values as double (no Compu method
  conversion)` sets the port data type as
  `double`, converting all internal measurement
  values. This selection supports up to three-dimensional XCP
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
row-major matrices. An XCP measurement can have a `LAYOUT`
as `COLUMN_DIR` or `ROW_DIR`. If a matrix
measurement is `COLUMN_DIR`, the blocks rearrange the
measurement in memory and ensure that the matrix (row X, col Y) in MATLAB
refers to the same entry as (row X, col Y) on the ECU. The rearrangement
causes matrix entries that are contiguous on the ECU to be noncontiguous in
MATLAB and Simulink.

### **Enable Timestamp** — Enable sending Simulink timestamp in STIM DTO packets `off` (default) | `on`

When the Timestamp is enabled, the block inputs a timestamp from Simulink
and sends the timestamp in the STIM DTO packets. The **Enable
Timestamp** check box appears in the block parameters dialog
box when the parameter is supported in the A2L file.

## Libraries

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

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

**Introduced in R2022b**

## Description

Perform data stimulation on selected measurements

The XCP CAN FD Data Stimulation block sends data to the selected server
connection for the selected event measurements. The block uses the XCP CAN FD transport
layer to output raw data for the selected measurements at the specified stimulation time
step. Configure your XCP session and use the XCP CAN FD Data Stimulation
block to select your event and measurements on the configured server connection. The
block displays the selected measurements as input ports.

The XCP communication blocks support Simulink® accelerator mode and rapid accelerator mode. You can speed up the
execution of Simulink models by using these modes. For more information about these
simulation modes, see Acceleration (Simulink).
