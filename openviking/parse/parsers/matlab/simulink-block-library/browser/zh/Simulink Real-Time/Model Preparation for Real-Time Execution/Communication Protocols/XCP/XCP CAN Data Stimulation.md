---
type: simulink-block
title: 'XCP CAN Data Stimulation'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpcandatastimulation'
documentation_source_path: 'io_ref/xcpcandatastimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN Data Stimulation

## 端口

### 输入

### **Data** — 由 A2L 文件定义的数据激励输入样本

输入数据激励样本，其名称和类型由 A2L 文件定义。选定的测量参数中的每个条目定义一个输入端口。在仿真的每一步，每个端口都会写入一个样本。

## 参数

### **配置名称** — 从列表中选择指定的 XCP CAN 会话名称

选择要使用的 XCP 配置的名称。此列表显示模型中可用 XCP CAN Configuration 模块内指定的所有可用名称。选择配置会显示此配置的 A2L 文件中可用的事件和测量。使用一个 XCP CAN Data Stimulation 模块，只能针对一个事件激励测量。若要激励其测量，请为每个事件使用一个模块。

### **事件名称** — 从列表中选择一个事件

从事件列表中选择一个事件。XCP CAN Configuration 模块使用指定的 A2L 文件填充事件列表。该模块使用 A2L 中对应的事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块在每次执行时都会激励。若要在 Simulink 仿真中使用，请考虑启用仿真定步，以避免自由运行的激励。

### **所有测量** — 列出事件测量列表可用的所有测量

此列表显示所选事件可用的所有测量。选择要使用的测量，并单击添加按钮， 将其移动到选定的测量。按住键盘上的 `Ctrl` 键可选择多个测量。

在模块参数对话框中，在 **搜索** 框中键入要使用的测量名称。**所有测量** 列表显示所有匹配名称的列表。单击 x 以清除搜索。

### **选定的测量** — 列出选定的测量名称

此列表显示您选定的测量。每个选定的测量都会以测量名称为该模块添加一个输入端口。若要从该列表中移除测量，请选择该测量并单击移除按钮， 。

在 **模块参数** 对话框中，使用移动按钮  重新排序选定的测量。

### **模块输入设置** — 将端口输入设置为 Compu 方法转换值或原始值 `Raw values as double (no Compu method conversion)` (默认) | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数启用对 ASAP2 标准中定义的 XCP 数据类型和维度的支持。模块输入设置参数选择端口输出的是 Compu 方法转换值还是原始值。各选项提供：

- `Physical values (apply Compu method conversion)` 启用 ECU 测量值的物理到原始转换。对于此选项，模块端口设置基于底层 Compu 方法转换设置为 `'double'` 或 `'string'`。例如，Compu 方法 `IDENTICAL`、`LINEAR`、`RAT_FUNC`、`TAB_INTP` 和 `TAB_NOINTP` 的端口设置为 `'double'`，而 Compu 方法 `TAB_VERB` 的端口设置为 `'string'`。Compu 方法转换支持的最大字符串长度为 1024，如 ASAM XIL 规范所指定。

  不支持 FORM Compu 方法转换。对于此类转换，Simulink 会抛出警告，并对底层测量应用 IDENTICAL 转换。此外，由于 Simulink 仅支持标量字符串，TAB\_VERB 转换仅支持标量测量信号。

  选择此选项会在模块掩码上的测量名称前显示物理单位（如果有）。该物理单位从测量的 A2L 描述和 Compu 方法获取。如果未指定物理单位，则仅显示测量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维 XCP 测量。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，转换所有内部测量值。此选择在 Simulink 中支持最多三维 XCP 测量。

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

模块中的维度支持适应 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行优先矩阵。一个 XCP 测量可以将 `LAYOUT` 设置为 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量为 `COLUMN_DIR`，模块会重新排列内存中的测量，并确保 MATLAB 中的矩阵（行 X，列 Y）引用与 ECU 上的（行 X，列 Y）相同的条目。这种重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中变为非连续。

### **启用时间戳** — 在 STIM DTO 数据包中启用发送 Simulink 时间戳 `off` (默认) | `on`

当启用时间戳时，模块从 Simulink 输入一个时间戳，并在 STIM DTO 数据包中发送该时间戳。当 A2L 文件支持该参数时，**启用时间戳** 复选框会出现在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN Simulink Real-Time / XCP / CAN

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，其部署可移植性有限，仅能在主机计算机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2013a 中引入**

## 描述

对选定的测量执行数据激励

XCP CAN Data Stimulation 模块将数据发送到选定服务器连接，以用于所选事件测量。该模块使用 XCP CAN 传输层，在指定的激励时间步为所选测量输出原始数据。配置您的 XCP 会话，并使用 XCP CAN Data Stimulation 模块在配置的服务器连接上选择事件和测量。该模块将所选测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration。
