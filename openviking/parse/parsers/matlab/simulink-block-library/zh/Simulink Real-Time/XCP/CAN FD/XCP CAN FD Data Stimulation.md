---
type: simulink-block
title: 'XCP CAN FD Data Stimulation'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / CAN FD'
documentation_page: 'xcpcanfddatastimulation'
documentation_source_path: 'io_ref/xcpcanfddatastimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN FD Data Stimulation

## 端口
```yaml
ports:
- name: Data
  summary: 由 A2L 文件定义的数据激励输入样本
  direction: input
```

### 输入

### **Data** — 由 A2L 文件定义的数据激励输入样本

数据激励输入样本，其名称和类型由 A2L 文件定义。Selected Measurements 参数中的每个条目定义一个输入端口。在仿真的每一步，每个端口都会写入一个样本。
## 参数
```yaml
parameters:
- name: Config name
  summary: 从列表中指定要选择的 XCP CAN FD 会话名称
  group: ''
- name: Event name
  summary: 从列表中选择一个事件
  group: ''
- name: All Measurements
  summary: 列出该事件可用的所有测量量 测量量列表
  group: ''
- name: Selected Measurements
  summary: 列出已选测量量 测量量名称
  group: ''
- name: 模块输入设置
  summary: 将端口输入设置为 Compu method 转换值或原始值 Raw values as double (no Compu method conversion)（默认）| Raw values (no Compu method
    conversion) | Physical values (apply Compu method conversion)
  group: ''
- name: 启用时间戳
  summary: 启用发送 Simulink 时间戳到 STIM DTO 数据包 off（默认）| on
  group: ''
```

### **Config name** — 从列表中指定要选择的 XCP CAN FD 会话名称

选择要使用的 XCP 配置名称。此列表显示模型中可用的 XCP CAN FD Configuration 模块中指定的所有可用名称。选择一个配置后，将显示该配置的 A2L 文件中可用的事件和测量量。使用一个 XCP CAN FD Data Stimulation 模块只能对一个事件的测量量进行激励。对于要激励其测量量的每个事件，请使用一个模块。

### **Event name** — 从列表中选择一个事件

从事件列表中选择一个事件。XCP CAN FD Configuration 模块使用指定的 A2L 文件填充事件列表。该模块使用 A2L 中对应的事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块在每次执行时进行激励。在 Simulink 仿真中使用时，请考虑启用仿真步调以避免自由运行的激励。

### **All Measurements** — 列出该事件可用的所有测量量 测量量列表

此列表显示所选事件可用的所有测量量。选择要使用的测量量，然后单击添加按钮，将其移动到已选测量量中。按住键盘上的 `Ctrl` 键可选择多个测量量。

在模块参数对话框中，在 **Search** 框中输入要使用的测量量名称。**All Measurements** 列表将显示所有匹配名称的列表。单击 x 以清除搜索。

### **Selected Measurements** — 列出已选测量量 测量量名称

此列表显示您已选择的测量量。每个已选测量量都会为模块添加一个以该测量量命名的输入端口。要从该列表中移除测量量，请选择该测量量并单击移除按钮，。

在 **Block Parameters** 对话框中，使用移位按钮 对已选测量量重新排序。

### **模块输入设置** — 将端口输入设置为 Compu method 转换值或原始值 `Raw values as double (no Compu method conversion)`（默认）| `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。模块输入设置参数选择端口输出 Compu method 转换值还是原始值。这些选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的物理值到原始值转换。
  对于此选项，模块端口设置根据底层 Compu method 转换设置为
  `'double'` 或 `'string'`。
  例如，Compu method `IDENTICAL`、`LINEAR`、
  `RAT_FUNC`、`TAB_INTP` 和
  `TAB_NOINTP` 的端口设置为
  `'double'`，而 Compu method
  `TAB_VERB` 的端口设置为
  `'string'`。Compu method 转换支持的最大字符串长度为 1024，如 ASAM XIL 规范中所指定。

  FORM Compu method 转换不受支持。Simulink 对此类转换抛出警告，并对底层测量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

  选择此选项会在模块掩码上的测量名称前显示物理单位（如果有）。此物理单位从测量的 A2L 描述和 Compu method 中获取。如果未指定物理单位，则仅显示测量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维 XCP 测量。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，转换所有内部测量值。此选项在 Simulink 中支持最多三维 XCP 测量。

这些 ASAP2 数据类型由相应的 Simulink 端口数据类型支持：

- `SBYTE`
- `UWORD`
- `SWORD`
- `ULONG`
- `SLONG`
- `A_UINT64`
- `A_INT64`
- `FLOAT32_IEEE`
- `FLOAT64_IEEE`

模块中的维度支持适应 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行主序矩阵。XCP 测量的 `LAYOUT` 可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量为 `COLUMN_DIR`，模块会重新排列内存中的测量，并确保 MATLAB 中的矩阵（行 X，列 Y）引用与 ECU 上的（行 X，列 Y）相同的条目。重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **启用时间戳** — 启用发送 Simulink 时间戳到 STIM DTO 数据包 `off`（默认）| `on`

当时间戳启用时，模块从 Simulink 输入时间戳，并在 STIM DTO 数据包中发送该时间戳。当 A2L 文件中支持该参数时，**启用时间戳**复选框会出现在模块参数对话框中。
## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，仅能在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持的兼容编译器。

## 版本历史

**在 R2022b 中引入**

## 描述

对选定的测量执行数据激励

XCP CAN FD Data Stimulation 模块将数据发送到选定的服务器连接，用于选定的事件测量。该模块使用 XCP CAN FD 传输层，在指定的激励时间步长下为选定的测量输出原始数据。配置您的 XCP 会话，并使用 XCP CAN FD Data Stimulation 模块在已配置的服务器连接上选择您的事件和测量。该模块将选定的测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式来加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration。
