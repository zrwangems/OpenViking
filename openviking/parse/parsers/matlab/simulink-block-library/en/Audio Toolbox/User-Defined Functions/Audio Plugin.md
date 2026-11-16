---
type: simulink-block
title: 'Audio Plugin'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'audioplugin'
documentation_source_path: 'ref/audioplugin.html'
language: en
---

# Audio Plugin

## Ports

### Input

### **x** — Plugin input column vector | matrix

The block input is the same as the original audio plugin input and accepts the
same data types. If the original plugin takes multiple inputs, the block has multiple
input ports. The block has additional input ports if you select any of the
**Specify *`parameter`* from input port**
parameters, where *`parameter`* is the name of a tunable
parameter.

The block does not have an input port if the original plugin is a source plugin.
Source plugins derive from `audioPluginSource` or `externalAudioPluginSource`.

**Note**

For audio plugins authored in MATLAB, the number of inputs and the number of channels per input are defined
by the `InputChannels` property in the plugin's
`audioPluginInterface`.
### Output

### **y** — Plugin output scalar | column vector | matrix

The block output is the same as the original audio plugin and returns the same
data types. If the original plugin returns multiple outputs, the block has multiple
output ports.

**Note**

For audio plugins authored in MATLAB, the number of outputs and the number of channels per output are
defined by the `OutputChannels` property in the
plugin's `audioPluginInterface`.

## Parameters

**Note**

These parameters are not part of the block until after you specify an audio plugin in
the dialog box.

### **Inherit sample rate from input** — Specify source of input sample rate `off` (default) | `on`

When you select this parameter, the block inherits its sample rate from the input
signal. When you clear this parameter, you specify the sample rate in **Input
sample rate (Hz)**.

The block does not have this parameter if the audio plugin is a source
plugin.

### **Input sample rate (Hz)** — Sample rate of input positive scalar

Sample rate of the input, specified as a positive scalar. The default is what the
`getSampleRate` method returns for the
original audio plugin.

The block does not have this parameter if the audio plugin is a source
plugin.

#### Dependencies

To enable this parameter, clear the **Inherit sample rate from
input** parameter.

### **Samples per frame** — Number of samples per frame positive integer

Number of samples per frame output by the block, specified as a positive scalar. The
default is what the `getSamplesPerFrame` method returns for the
original audio plugin.

The block has this parameter only if the audio plugin is a source plugin.

### **Output data type** — Data type of output signal `double` (default) | `single`

Data type of the output signal, specified as `double` or
`single`.

The block has this parameter only if the audio plugin is a source plugin.

### **Sample rate (Hz)** — Sample rate of output signal positive scalar

Sample rate of the output signal, specified as a positive scalar. The default value
of this parameter is the sample rate that the `getSampleRate` method returns for the original audio plugin.

The block has this parameter only if the audio plugin is a source plugin.

### **Simulate using** — Specify type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Interpreted execution` –– Simulate model using the
  MATLAB interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` –– Simulate model using generated C
  code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

## Libraries

Audio Toolbox / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesca` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation.  b See Nonvirtual Buses and MATLAB System Block for more information.  c See Variable-Size Signals for more information. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generating code from blocks that use external audio plugins has additional requirements.
External audio plugins include plugins loaded into MATLAB with `loadAudioPlugin` and plugin binaries such as
VST plugins.

- The Audio Plugin block generates files in addition to the System object file to aid in code generation. These files include
  `sysObjNamePluginLoader.m` and
  `sysObjNameInterface.m` where
  *`sysObjName`* is the name of the generated System object. The block also generates
  `sysObjNameTables.mat` if the plugin has
  any parameters. These additional files are required for code generation and running the
  block in simulation.
- You must select the **Support long
  long (Simulink)** parameter in the **Hardware Implementation** pane
  of the **Model Settings**.
- If you are using an ERT target, you must set the **Language (Simulink Coder)** parameter to `C++` under the
  **Target selection** section of the **Code
  Generation** pane in the **Model Settings**. You must also
  select the **Dynamic memory allocation in MATLAB
  functions (Simulink)** parameter in the **Advanced parameters**
  section of the **Simulation Target** pane.
- To use a standalone executable generated from a block with an external plugin, you
  must generate the `jucehost.dll` file on Windows® or the `libjucehost.dylib` file on macOS by selecting the **Package code and artifacts (Simulink Coder)** parameter under the **Build
  process** section of the **Code Generation** pane in the
  **Model Settings**.

  - On Windows platforms, you must make the `jucehost.dll` file
    visible to the standalone executable. To do this, add the path to the
    `jucehost.dll` file to the `PATH` environment
    variable or copy the `jucehost.dll` file to the same folder as the
    standalone executable.
  - On macOS platforms, you must make the `libjucehost.dylib` file
    visible to the standalone executable. To do this, place the
    `libjucehost.dylib` file in the `/usr/lib`
    directory.

Hosted AUv3 plugins do not support code generation.

## Version History

**Introduced in R2022b**

## Description

Include audio plugin in model

The Audio Plugin block allows you to use an audio plugin as a block in your
Simulink® model. The Audio Plugin block generates a new block that has the
same functionality as the desired plugin, and you can use the generated block to process audio
signals in Simulink. For more information about audio plugins in MATLAB®, see Audio Plugins in MATLAB.

### Using the Block

To use the Audio Plugin block, place the block in your model and
double-click it to open the dialog box.

Specify the desired audio plugin in the **Audio plugin** field. You can
specify the audio plugin as:

- The name or file path of an audio plugin class. The class must derive from `audioPlugin` or `audioPluginSource`.
- An audio plugin binary file that is supported by `loadAudioPlugin`.
- An instance of an audio plugin class. This can either be a plugin authored in
  MATLAB or an externally authored plugin that is returned by `loadAudioPlugin`.

The Audio Plugin block generates a System object™ class file from the plugin and uses that System object to create the new block. You can optionally specify the file name and location
of the generated System object with the **Generated file name** field. For more information
about how the Audio Plugin block works and the System object it generates, see Algorithms.

**Note**

The generated System object file must be on the MATLAB path for the plugin block to work. If the plugin is a hosted external
plugin, the block generates additional files required by the generated System object. For more information, see Code Generation.

After you specify an audio plugin and click **OK**, you have a block
with the same functionality as the audio plugin.

For an example with a model that uses the Audio Plugin block, see Include an Audio Plugin in Simulink.

### Generated Block Parameters

The generated block has the same parameters as the specified audio plugin. These
parameters are tunable, unless the parameter is an enumeration class that uses strings or
characters as the underlying type. Each tunable parameter can be specified from an input
port if you select the associated **Specify *`parameter`*
from input port** parameter, where *`parameter`* is the
name of the tunable parameter.

**Note**

For audio plugins authored in MATLAB, a parameter must be specified as an `audioPluginParameter` in the plugin's `audioPluginInterface` for it to show in the block.

In addition to the parameters of the original plugin, the generated block has other,
nontunable parameters that depend on whether the plugin is a source plugin or not. See Parameters for more
information.
