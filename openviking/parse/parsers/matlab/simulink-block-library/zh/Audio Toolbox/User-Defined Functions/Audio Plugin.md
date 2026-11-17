---
type: simulink-block
title: 'Audio Plugin'
family: 'user-defined-functions'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'audioplugin'
documentation_source_path: 'ref/audioplugin.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Plugin

## 端口

### 输入

### **x** — 插件输入列向量 | 矩阵

模块输入与原始音频插件输入相同，并接受相同的数据类型。如果原始插件有多个输入，则模块有多个输入端口。如果选择任何 **Specify *`parameter`* from input port** 参数，则模块有附加输入端口，其中 *`parameter`* 是可调参数的名称。

如果原始插件是源插件，则模块没有输入端口。源插件派生自 `audioPluginSource` 或 `externalAudioPluginSource`。

**注意**

对于在 MATLAB 中创作的音频插件，输入的数量和每个输入的通道数由插件 `audioPluginInterface` 中的 `InputChannels` 属性定义。

### 输出

### **y** — 插件输出标量 | 列向量 | 矩阵

模块输出与原始音频插件相同，并返回相同的数据类型。如果原始插件返回多个输出，则模块有多个输出端口。

**注意**

对于在 MATLAB 中创作的音频插件，输出的数量和每个输出的通道数由插件 `audioPluginInterface` 中的 `OutputChannels` 属性定义。

## 参数

**注意**

在你于对话框中指定音频插件之后，这些参数才属于该模块。

### **Inherit sample rate from input** — 指定输入采样率的来源 `off` (默认) | `on`

选择此参数时，模块从输入信号继承采样率。清除此参数时，在 **Input sample rate (Hz)** 中指定采样率。

如果音频插件是源插件，则模块没有此参数。

### **Input sample rate (Hz)** — 输入的采样率 正标量

输入的采样率，指定为正标量。默认值是 `getSampleRate` 方法为原始音频插件返回的值。

如果音频插件是源插件，则模块没有此参数。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Samples per frame** — 每帧采样数 正整数

模块输出的每帧采样数，指定为正标量。默认值是 `getSamplesPerFrame` 方法为原始音频插件返回的值。

仅当音频插件是源插件时，模块才有此参数。

### **Output data type** — 输出信号的数据类型 `double` (默认) | `single`

输出信号的数据类型，指定为 `double` 或 `single`。

仅当音频插件是源插件时，模块才有此参数。

### **Sample rate (Hz)** — 输出信号的采样率 正标量

输出信号的采样率，指定为正标量。此参数的默认值是 `getSampleRate` 方法为原始音频插件返回的采样率。

仅当音频插件是源插件时，模块才有此参数。

### **Simulate using** — 指定要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

- `Interpreted execution` —— 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不更改，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

## 所属库

Audio Toolbox / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busba` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesca` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或能力支持取决于模块实现。  b 有关详细信息，请参见非虚拟总线和 MATLAB System Block。  c 有关详细信息，请参见可变大小信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

从使用外部音频插件的模块生成代码有附加要求。外部音频插件包括使用 `loadAudioPlugin` 加载到 MATLAB 中的插件以及插件二进制文件，例如 VST 插件。

- Audio Plugin 模块除 System object 文件外还会生成文件以帮助代码生成。这些文件包括 `sysObjNamePluginLoader.m` 和 `sysObjNameInterface.m`，其中 *`sysObjName`* 是生成的 System object 的名称。如果插件有任何参数，模块还会生成 `sysObjNameTables.mat`。这些附加文件是代码生成以及在仿真中运行模块所必需的。
- 必须在 **Model Settings** 的 **Hardware Implementation** 窗格中选择 **Support long long (Simulink)** 参数。
- 如果你使用的是 ERT 目标，则必须在 **Model Settings** 中 **Code Generation** 窗格的 **Target selection** 部分下，将 **Language (Simulink Coder)** 参数设置为 `C++`。还必须选择 **Simulation Target** 窗格的 **Advanced parameters** 部分中的 **Dynamic memory allocation in MATLAB functions (Simulink)** 参数。
- 若要使用从带有外部插件的模块生成的独立可执行文件，你必须通过选择 **Model Settings** 中 **Code Generation** 窗格的 **Build process** 部分下的 **Package code and artifacts (Simulink Coder)** 参数，在 Windows® 上生成 `jucehost.dll` 文件，或在 macOS 上生成 `libjucehost.dylib` 文件。

  - 在 Windows 平台上，必须使 `jucehost.dll` 文件对独立可执行文件可见。为此，请将 `jucehost.dll` 文件的路径添加到 `PATH` 环境变量，或将 `jucehost.dll` 文件复制到独立可执行文件所在的同一文件夹。
  - 在 macOS 平台上，必须使 `libjucehost.dylib` 文件对独立可执行文件可见。为此，请将 `libjucehost.dylib` 文件放在 `/usr/lib` 目录中。

托管的 AUv3 插件不支持代码生成。

## 版本历史

**在 R2022b 中引入**

## 描述

在模型中包含音频插件

Audio Plugin 模块允许你将音频插件用作 Simulink® 模型中的模块。Audio Plugin 模块生成一个新模块，该模块具有所需插件的相同功能，你可以使用生成的模块在 Simulink 中处理音频信号。有关 MATLAB® 中音频插件的详细信息，请参见 Audio Plugins in MATLAB。

### 使用模块

要使用 Audio Plugin 模块，请将该模块放入你的模型，然后双击它打开对话框。

在 **Audio plugin** 字段中指定所需的音频插件。可以将音频插件指定为：

- 音频插件类的名称或文件路径。该类必须派生自 `audioPlugin` 或 `audioPluginSource`。
- `loadAudioPlugin` 支持的音频插件二进制文件。
- 音频插件类的实例。这可以是在 MATLAB 中创作的插件，也可以是由 `loadAudioPlugin` 返回的外部创作的插件。

Audio Plugin 模块从插件生成 System object™ 类文件，并使用该 System object 创建新模块。你可以选择使用 **Generated file name** 字段指定所生成 System object 的文件名和位置。有关 Audio Plugin 模块如何工作及其生成的 System object 的详细信息，请参见算法。

**注意**

生成的 System object 文件必须在 MATLAB 路径上，插件模块才能工作。如果插件是托管外部插件，则模块会生成生成的 System object 所需的附加文件。有关详细信息，请参见代码生成。

指定音频插件并点击 **OK** 后，你将拥有一个与音频插件具有相同功能的模块。

有关使用 Audio Plugin 模块的模型示例，请参见 Include an Audio Plugin in Simulink。

### 生成的模块参数

生成的模块具有与指定音频插件相同的参数。这些参数是可调参数，除非该参数是使用字符串或字符作为基础类型的枚举类。如果选择关联的 **Specify *`parameter`* from input port** 参数，则可以从输入端口指定每个可调参数，其中 *`parameter`* 是可调参数的名称。

**注意**

对于在 MATLAB 中创作的音频插件，参数必须在插件的 `audioPluginInterface` 中指定为 `audioPluginParameter`，才能显示在模块中。

除原始插件的参数外，生成的模块还有其他不可调参数，这些参数取决于插件是否为源插件。有关详细信息，请参见参数。
