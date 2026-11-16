---
type: simulink-block
title: 'XCP CAN FD Data Acquisition'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / CAN FD'
documentation_page: 'xcpcanfddataacquisition'
documentation_source_path: 'ug/xcpcanfddataacquisition.html'
language: zh-CN
chinese_source: official
---

# XCP CAN FD Data Acquisition

## 端口

### 输出

### **Data** — 输出测量变量采样 由 A2L 文件定义

输出测量变量采样，其名称和类型由 A2L 文件定义。Selected Measurements 参数中的每个条目定义一个输出端口。对于仿真的每一步，每个端口都可使用一个采样。

## 参数

### **配置名称** — 指定 XCP CAN FD 会话名称 从列表中选择

选择要使用的 XCP 配置的名称。此列表显示模型中 XCP CAN FD Configuration 模块中指定的所有可用名称。选择一项配置将显示此配置的 A2L 文件中可用的事件和测量变量。

**注意**

一个 XCP CAN FD Data Acquisition 模块仅能用于采集一个事件的测量变量。因此，针对要采集其测量变量的每个事件，请分别使用一个模块。

### **事件名称** — 选择事件 从列表中选择

从可用的事件列表中选择一个事件。XCP CAN FD Configuration 模块使用指定的 A2L 文件填充事件列表。

### **所有测量变量** — 列出事件的所有可用测量变量 测量变量列表

此列表显示所选事件的所有可用测量变量。选择要使用的测量变量，然后点击添加按钮  将其添加到所选测量变量。在键盘上，按住 **Ctrl** 键可选择多个测量变量。

在“模块参数”对话框中，在**搜索**框中键入要使用的测量变量的名称。**所有测量变量**列表显示所有匹配的名称的列表。点击 x 可清除您的搜索。

### **所选测量变量** — 列出选定的测量变量 测量变量名称

此列表显示选定的测量变量。每个所选测量变量都会将一个输出端口添加到具有该测量变量名称的模块中。要从这个列表中删除一个测量变量，请选择该测量变量并点击删除按钮 。

在“模块参数”对话框中，使用切换按钮  可对所选测量变量重新排序。

### **模块输出设置** — 将端口输出设置为 Compu 方法转换值或原始值 `Raw values as double (no Compu method conversion)` (默认) | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。“模块输出设置”参数选择端口是输出 Compu 方法转换值还是原始值。选项提供：

- `Physical values (apply Compu method conversion)` 支持 ECU 测量变量值的原始到物理转换。对于此选项，根据基础 Compu 方法转换，模块端口设置设置为 `'double'` 或 `'string'`。例如，Compu 方法 `IDENTICAL`、`LINEAR`、`RAT_FUNC`、`TAB_INTP` 和 `TAB_NOINTP` 端口设置为 `'double'`，而 Compu 方法 `TAB_VERB` 端口设置为 `'string'`。Compu 方法转换支持的最大字符串长度是 ASAM XIL 规范中指定的 1024。

  不支持 FORM Compu 方法转换。Simulink 会对这种转换发出警告，并且对涉及到的测量变量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

  选择此选项会在模块封装上的测量变量名称前显示物理单位（如果有）。此物理单位是从测量变量和 Compu 方法的 A2L 描述中获得的。如果未指定物理单位，则仅显示测量变量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并支持在 Simulink 中进行最多三维的 XCP 测量变量。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，从而转换所有内部测量变量值。此选项支持在 Simulink 中进行最多三维的 XCP 测量变量。

这些 ASAP2 数据类型由对应的 Simulink 端口数据类型支持：

- `SBYTE`
- `UWORD`
- `SWORD`
- `ULONG`
- `SLONG`
- `A_UINT64`
- `A_INT64`
- `FLOAT32_IEEE`
- `FLOAT64_IEEE`

模块中的维度支持能够适应 MATLAB® 和 ECU 对矩阵的不同处理。MATLAB 默认运算将矩阵视为行优先矩阵。XCP 测量变量的 `LAYOUT` 可以为 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量变量为 `COLUMN_DIR`，则模块会在内存中重新排列测量变量，并确保 MATLAB 中的矩阵 (row X, col Y) 与 ECU 上的矩阵 (row X, col Y) 引用相同的条目。这种重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **DAQ 列表优先级** — 指定服务器设备驱动的优先级值 优先级值

指定一个 0 到 255 之间的整数作为优先级值，服务器设备驱动使用该值确定数据包的传输顺序。服务器可以累积较低优先级 DAQ 列表的 XCP 数据包，然后再传输给客户端。值 255 具有最高优先级。`SET_DAQ_LIST_MODE` 命令将 **DAQ 列表优先级**值从客户端传送到服务器。此通信方法不同于“事件通道优先级”属性的设定，后者来自 A2L 文件。

### **采样时间** — 指定模块的采样时间 `-1` (默认)

指定在仿真期间模块的采样时间，即仿真时间。该值定义在仿真期间 XCP CAN FD Data Acquisition 模块运行的频率。如果模块位于触发子系统内或要继承采样时间，则可以将 `–1` 指定为采样时间，这是默认值。您还可以为采样时间指定一个 MATLAB 变量。有关详细信息，请参阅硬件接口模型中的计时。

### **启用时间戳** — 启用从传入的 DTO 数据包中读取时间戳 `off` (默认) | `on`

启用时间戳后，模块从传入的 DTO 数据包中读取时间戳，并将时间戳输出到 Simulink。当 A2L 文件支持参数时，模块参数对话框中会出现**启用时间戳**复选框。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

XCP 通信模块支持仅在主机或 Simulink Real-Time™ 目标上运行的具有有限部署可移植性的代码生成。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持和兼容的编译器。

## 版本历史

**在 R2022b 中推出**

## 描述

从配置的服务器连接采集选定的测量变量

XCP CAN FD Data Acquisition 模块根据您选择的测量变量从配置的服务器连接采集数据。该模块使用 XCP CAN FD 传输层在指定的仿真时间步获得所选测量变量的原始数据。请配置 XCP 连接，使用 XCP CAN FD Data Acquisition 模块为配置的服务器连接选择事件和测量变量。该模块将选定的测量变量显示为输出端口。

XCP 通信模块支持使用 Simulink® 加速模式和快速加速模式。使用这些模式可以加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速 (Simulink)。
