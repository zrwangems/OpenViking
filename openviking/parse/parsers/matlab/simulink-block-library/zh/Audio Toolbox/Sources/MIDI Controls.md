---
type: simulink-block
title: 'MIDI Controls'
family: 'sources'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'midicontrolsblock'
documentation_source_path: 'ref/midicontrolsblock.html'
language: zh-CN
chinese_source: worker-translation
---

# MIDI Controls

## 端口

### 输出

### **Port\_1** — 输出信号矩阵

MIDI Controls 模块的输出大小由 **MIDI controls** 和 **MIDI control numbers** 参数决定。

输出数据类型由 **Output mode** 参数决定。

| 数据类型 | 输出模式 |
| --- | --- |
| `double` | `Normalized (0-1)` |
| `uint8` | `RAW MIDI (0-127)` |

**数据类型：** `double` | `uint8`

## 参数

### **MIDI device** — 模块监听的 MIDI 控制面 `Default`（默认） | `Specify other`

要设置默认 MIDI 设备，请使用 `setpref` 函数。例如，如果设备名为 `BCF2000`，请在 MATLAB 命令行中输入：

    setpref('midi','DefaultDevice','BCF2000');

### **MIDI device name** — 模块监听的 MIDI 控制面的设备名称 character vector

MIDI 设备名称由设备制造商或主机操作系统分配，并指定为 character vector。使用 `midiid` 以交互方式识别你的 MIDI 设备。

要启用此参数，请将 **MIDI device** 设置为 `Specify other`。

### **MIDI controls** — 指定模块是响应 MIDI 控制面上的所有控制器还是特定控制器 `Respond to any control`（默认） | `Respond to specified controls`

此参数还决定模块输出端口的大小。如果选择 `Respond to any control`，则模块输出为标量，对应于最近操作的控制器值。

### **MIDI control numbers** — 模块响应的 MIDI 控制面控制器关联的控制编号 `0`（默认） | integer | array of integers

使用 `midiid` 以交互方式识别你的 MIDI 设备的控制编号。将 **MIDI controls** 设置为 `Respond to specified controls` 时，此参数可用。

### **Initial values** — 模块响应的 MIDI 控制面控制器关联的控制编号 `0`（默认） | scalar | array

如果将 **Initial values** 指定为 scalar，则 **MIDI control numbers** 指定的所有控制器都会分配该值。

如果将 **Initial values** 指定为 array，则该数组的大小必须与 **MIDI control numbers** 相同。

### **Send initial values to device at start** — 将 MIDI 控制面与指定的初始值同步 `off`（默认） | `on`

选择此参数可在仿真开始时将 MIDI 设备与 **Initial values** 指定的值同步。如果你的 MIDI 设备能够接收并响应消息，它会按指定方式调整其控制器。仅当 **MIDI controls** 设置为 `Respond to specified controls` 时，此参数才有效。

许多 MIDI 设备不是双向的。对单向设备选择此参数没有效果。MIDI Controls 模块无法判断某个值是否成功发送到设备，甚至无法判断设备是否为双向。如果发送值失败，不会生成错误或警告。

### **Output Mode** — MIDI 控制值的输出模式 `Normalized (0-1)`（默认） | `RAW MIDI (0-127)`

MIDI 控制值的输出模式，指定为 `Normalized (0-1)` 或 `RAW MIDI (0-127)`。

## 所属库

Audio Toolbox / Sources DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（.dll 文件）。使用 `packNGo` 函数将从此对象生成的代码以及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，你可以在未安装 MATLAB 的其他开发环境中重新定位、解包并重建你的项目。有关更多详细信息，请参阅在 MATLAB 和 Simulink 外部运行音频 I/O 功能。

## 版本历史

未在 R2025b 中记录。

## 描述

从 MIDI 控制面上的控制器输出值

MIDI Controls 模块实时输出 MIDI 控制面上的控制器值。使用 MIDI Controls 模块与你的音频处理模型交互。

MIDI Controls 模块结合了 MATLAB® 中通用 MIDI 函数的功能：`midicontrols`、`midiread`、`midisync`。使用 MATLAB `midiid` 命令可发现 MIDI 设备名称或 MIDI 设备控制编号。
