---
type: simulink-block
title: 'MIDI Controls'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'midicontrolsblock'
documentation_source_path: 'ref/midicontrolsblock.html'
language: en
---

# MIDI Controls

## Ports
```yaml
ports:
- name: Port_1
  summary: Output signal matrix
  direction: output
  data_types: double | uint8
```

### Output

### **Port\_1** — Output signal matrix

The output size of the MIDI Controls block is
determined by the **MIDI controls** and **MIDI
control numbers** parameters.

The output data type is determined by the **Output
mode** parameter.

| Data Type | Output Mode |
| --- | --- |
| `double` | `Normalized (0-1)` |
| `uint8` | `RAW MIDI (0-127)` |

**Data Types:** `double` | `uint8`
## Parameters
```yaml
parameters:
- name: MIDI device
  summary: MIDI control surface your block listens to Default (default) | Specify other
  group: ''
- name: MIDI device name
  summary: Device name of MIDI control surface your block listens to character vector
  group: ''
- name: MIDI controls
  summary: Specify if block responds to all controllers or specific controllers on MIDI surface Respond to any control (default)
    | Respond to specified controls
  group: ''
- name: MIDI control numbers
  summary: Control numbers associated with MIDI surface controllers that your block responds to 0 (default) | integer | array
    of integers
  group: ''
- name: Initial values
  summary: Control numbers associated with MIDI surface controllers that your block responds to 0 (default) | scalar | array
  group: ''
- name: Send initial values to device at start
  summary: Synchronize MIDI surface with values specified initial values off (default) | on
  group: ''
- name: Output Mode
  summary: Output mode for MIDI control value Normalized (0-1) (default) | RAW MIDI (0-127)
  group: ''
```

### **MIDI device** — MIDI control surface your block listens to `Default` (default) | `Specify other`

To set the default MIDI device, use the `setpref`
function. For example, if the device is named `BCF2000`, at
the MATLAB command line, enter:

```
setpref('midi','DefaultDevice','BCF2000');
```

### **MIDI device name** — Device name of MIDI control surface your block listens to character vector

The MIDI device name is assigned by the device manufacturer or host
operating system, and specified as a character vector. Use `midiid` to interactively
identify your MIDI device.

To enable this parameter, set **MIDI device** to
`Specify other`.

### **MIDI controls** — Specify if block responds to all controllers or specific controllers on MIDI surface `Respond to any control` (default) | `Respond to specified controls`

This parameter also determines the size of the block output port. If you
choose `Respond to any control`, then the block
output is a scalar corresponding to the value of the most recently
manipulated control.

### **MIDI control numbers** — Control numbers associated with MIDI surface controllers that your block responds to `0` (default) | integer | array of integers

Use `midiid` to interactively identify the control
numbers of your MIDI device. This parameter is available when you set
**MIDI controls** to `Respond to specified
controls`.

### **Initial values** — Control numbers associated with MIDI surface controllers that your block responds to `0` (default) | scalar | array

If you specify **Initial values** as a scalar, all
controls specified by **MIDI control numbers** are assigned
that value.

If you specify **Initial values** as an array, the array
must be the same size as **MIDI control numbers**.

### **Send initial values to device at start** — Synchronize MIDI surface with values specified initial values `off` (default) | `on`

Select this parameter to synchronize a MIDI device with values specified
by the **Initial values** when simulation starts. If your
MIDI device can receive and respond to messages, it adjusts its controls as
specified. This parameter is valid only when **MIDI
controls** is set to `Respond to specified
controls`.

Many MIDI devices are not bidirectional. Selecting this parameter with a
unidirectional device has no effect. The MIDI Controls block
cannot tell whether a value is successfully sent to a device or even whether
the device is bidirectional. If sending a value fails, no errors or warnings
are generated.

### **Output Mode** — Output mode for MIDI control value `Normalized (0-1)` (default) | `RAW MIDI (0-127)`

Output mode for MIDI control value, specified as `Normalized
(0-1)` or `RAW MIDI
(0-127)`.
## Libraries

Audio Toolbox / Sources DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The executable generated from this block relies on prebuilt dynamic library files
(.dll files) included with MATLAB. Use the `packNGo` function to package the code
generated from this object and all the relevant files in a compressed zip file.
Using this zip file, you can relocate, unpack, and rebuild your project in another
development environment where MATLAB is not installed. For more details, see Run Audio I/O Features Outside MATLAB and Simulink.

## Version History

Not documented in R2025b.

## Description

Output values from controls on MIDI control surface

The MIDI Controls block outputs values from controls on a MIDI control
surface in real time. Use the MIDI Controls block to interact with your audio processing
model.

The MIDI Controls block combines the functionality of the general MIDI functions in
MATLAB®: `midicontrols`, `midiread`, `midisync`. Use the MATLAB
`midiid` command to discover MIDI device
names or MIDI device control numbers.
