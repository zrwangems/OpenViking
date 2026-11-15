---
type: simulink-block
title: 'XCP CAN FD Data Stimulation'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / XCP'
documentation_page: 'xcpcanfddatastimulation'
documentation_source_path: 'io_ref/xcpcanfddatastimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN FD Data Stimulation

## 端口

### 输入

### **Data** — 由 A2L 文件定义的数据激励输入采样

输入数据激励采样，其名称和类型由 A2L 文件定义。Selected Measurements 参数中的每个条目定义一个输入端口。在仿真的每个步长，都会向每个端口写入一个采样。

## 参数

### **Config name** — 指定从列表中选择的 XCP CAN FD 会话名称

选择要使用的 XCP 配置的名称。此列表显示模型中可用的 XCP CAN FD Configuration 模块中指定的所有可用名称。选择某个配置会显示该配置的 A2L 文件中可用的事件和测量。使用一个 XCP CAN FD Data Stimulation 模块只能激励一个事件的测量。对于要激励其测量的每个事件，使用一个模块。

### **Event name** — 从列表中选择一个事件

从事件列表中选择一个事件。XCP CAN FD Configuration 模块使用指定的 A2L 文件填充事件列表。该模块使用 A2L 中对应的事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块在每次执行时进行激励。在 Simulink 仿真中使用时，考虑启用仿真步调以避免自由运行激励。

### **All Measurements** — 列出事件测量列表中可用的所有测量

此列表显示选定事件可用的所有测量。选择要使用的测量，然后单击添加按钮，将其移动到选定的测量。按住键盘上的 `Ctrl` 键可选择多个测量。

在模块参数对话框中，在 **Search** 框中键入要使用的测量名称。**All Measurements** 列表显示所有匹配名称的列表。单击 x 清除搜索。

### **Selected Measurements** — 列出选定的测量名称

此列表显示您选定的测量。每个选定的测量都会向模块添加一个以该测量名称命名的输入端口。要从该列表中删除某个测量，请选择该测量，然后单击移除按钮。

在 **Block Parameters** 对话框中，使用 shift 按钮重新排列选定的测量。

### **Block Input Settings** — 将端口输入设置为 Compu method 转换值或原始值 `Raw values as double (no Compu method conversion)`（默认） | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数启用对 ASAP2 标准中定义的 XCP 数据类型和维度的支持。Block Input Settings 参数选择端口输出 Compu method 转换值还是原始值。这些选项提供：

- `Physical values (apply Compu method conversion)` 启用 ECU 测量值的物理值到原始值转换。对于此选项，模块端口设置将基于底层 Compu method 转换设置为 `'double'` 或 `'string'`。例如，Compu method `IDENTICAL`、`LINEAR`、`RAT_FUNC`、`TAB_INTP` 和 `TAB_NOINTP` 的端口设置是 `'double'`，而 Compu method `TAB_VERB` 的端口设置是 `'string'`。Compu method 转换支持的最大字符串长度为 1024，如 ASAM XIL 规范所指定。

  FORM Compu method 转换不受支持。Simulink 会对这种转换引发警告，并对底层测量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

  选择此选项会在模块掩码上的测量名称前显示物理单位（如果有）。此物理单位从测量的 A2L 描述和 Compu method 获取。如果未指定物理单位，则仅显示测量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维的 XCP 测量。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，并转换所有内部测量值。此选择在 Simulink 中支持最多三维的 XCP 测量。

以下 ASAP2 数据类型由相应的 Simulink 端口数据类型支持：

- `SBYTE`
- `UWORD`
- `SWORD`
- `ULONG`
- `SLONG`
- `A_UINT64`
- `A_INT64`
- `FLOAT32_IEEE`
- `FLOAT64_IEEE`

模块中的维度支持兼顾 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行优先矩阵。XCP 测量的 `LAYOUT` 可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量为 `COLUMN_DIR`，模块会重新排列内存中的测量，并确保 MATLAB 中的矩阵（row X, col Y）引用与 ECU 上的（row X, col Y）相同的条目。这种重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **Enable Timestamp** — 启用将 Simulink 时间戳发送到 STIM DTO 数据包中 `off`（默认） | `on`

当 Timestamp 启用时，模块从 Simulink 输入时间戳，并在 STIM DTO 数据包中发送该时间戳。当 A2L 文件支持该参数时，**Enable Timestamp** 复选框会出现在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但其部署可移植性有限，只能运行在主机或 Simulink Real-Time™ 目标上。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2022b 中引入**

## 描述

对选定的测量执行数据激励

XCP CAN FD Data Stimulation 模块将数据发送到选定事件测量的选定服务器连接。该模块使用 XCP CAN FD 传输层，在指定的激励时间步为选定测量输出原始数据。配置 XCP 会话，并使用 XCP CAN FD Data Stimulation 模块在配置的服务器连接上选择事件和测量。该模块将选定的测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。使用这些模式可以加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅 Acceleration。
