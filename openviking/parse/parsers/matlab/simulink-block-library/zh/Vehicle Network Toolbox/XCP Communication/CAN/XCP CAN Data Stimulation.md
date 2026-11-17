---
type: simulink-block
title: 'XCP CAN Data Stimulation'
family: 'vnt'
product_id: 'vnt'
product_name: 'Vehicle Network Toolbox'
documentation_release: R2025b
official_category: 'XCP Communication / CAN'
documentation_page: 'xcpcandatastimulation'
documentation_source_path: 'ug/xcpcandatastimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN Data Stimulation

## 端口
```yaml
ports:
- name: Data
  summary: 由 A2L 文件定义的数据激励输入样本
  direction: input
```

### 输入

### **Data** — 由 A2L 文件定义的数据激励输入样本

输入数据激励样本，其名称和类型由 A2L 文件定义。Selected Measurements 参数中的每个条目定义一个输入端口。在仿真的每一步，每个端口都会写入一个样本。
## 参数
```yaml
parameters:
- name: Config name
  summary: 指定 XCP CAN 会话名称，从列表中选择
  group: ''
- name: Event name
  summary: 选择一个事件，从列表中选择
  group: ''
- name: All Measurements
  summary: 列出该事件可用的所有测量量，测量量列表
  group: ''
- name: Selected Measurements
  summary: 列出已选测量量，测量量名称
  group: ''
- name: Block Input Settings
  summary: 将端口输入设置为 Compu 方法转换值或原始值 Raw values as double (no Compu method conversion)（默认）| Raw values (no Compu method conversion)
    | Physical values (apply Compu method conversion)
  group: ''
- name: Enable Timestamp
  summary: 启用发送 Simulink 时间戳到 STIM DTO 数据包 off（默认）| on
  group: ''
```

### **Config name** — 指定 XCP CAN 会话名称，从列表中选择

选择要使用的 XCP 配置名称。此列表显示模型中可用的 XCP CAN Configuration 模块中指定的所有可用名称。选择某个配置后，会显示该配置的 A2L 文件中可用的事件和测量量。使用一个 XCP CAN Data Stimulation 模块只能激励一个事件的测量量。对于每个要激励其测量量的事件，请使用一个模块。

### **Event name** — 选择一个事件，从列表中选择

从事件列表中选择一个事件。XCP CAN Configuration 模块使用指定的 A2L 文件填充事件列表。该模块使用 A2L 中对应的事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块在每次执行时进行激励。在 Simulink 仿真中使用时，请考虑启用仿真步调以避免自由运行的激励。

### **All Measurements** — 列出该事件可用的所有测量量，测量量列表

此列表显示所选事件可用的所有测量量。选择要使用的测量量，然后单击添加按钮，将其移动到已选测量量中。按住键盘上的 `Ctrl` 键可选择多个测量量。

在模块参数对话框中，在 **Search** 框中输入要使用的测量量名称。**All Measurements** 列表会显示所有匹配名称的列表。单击 x 清除搜索。

### **Selected Measurements** — 列出已选测量量，测量量名称

此列表显示已选的测量量。每个已选测量量都会为模块添加一个以该测量量名称命名的输入端口。要从该列表中移除测量量，请选择该测量量并单击移除按钮，。

在 **Block Parameters** 对话框中，使用移位按钮 对已选测量量重新排序。

### **Block Input Settings** — 将端口输入设置为 Compu 方法转换值或原始值 `Raw values as double (no Compu method conversion)`（默认）| `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。Block Input Settings 参数选择端口输出 Compu 方法转换值还是原始值。各选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的物理值到原始值的转换。
  对于此选项，模块端口设置根据底层 Compu 方法转换设置为
  `'double'` 或 `'string'`。
  例如，Compu 方法 `IDENTICAL`、`LINEAR`、
  `RAT_FUNC`、`TAB_INTP` 和
  `TAB_NOINTP` 的端口设置为
  `'double'`，而 Compu 方法
  `TAB_VERB` 的端口设置为
  `'string'`。Compu 方法转换支持的最大字符串长度为 1024，如 ASAM XIL 规范中所指定。

  FORM Compu 方法转换不受支持。Simulink 对此类转换抛出
  警告，并对底层测量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持
  标量字符串。

  选择此选项会在模块掩码上的测量名称前显示物理单位（如果有）。此物理单位
  从测量的 A2L 描述和 Compu
  方法中获取。如果未指定物理单位，则仅显示测量
  名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义
  设置端口数据类型，并在
  Simulink 中支持最多三维 XCP 测量。
- `Raw values as double (no Compu method
  conversion)` 将端口数据类型设置为
  `double`，转换所有内部测量
  值。此选项在 Simulink 中支持最多三维 XCP
  测量。

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

模块中的维度支持适应了 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为
行主序矩阵。XCP 测量的 `LAYOUT`
可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵
测量为 `COLUMN_DIR`，模块会重新排列
内存中的测量，并确保 MATLAB 中的矩阵（行 X，列 Y）
与 ECU 上的（行 X，列 Y）指向同一条目。这种重新排列
导致在 ECU 上连续的矩阵条目在
MATLAB 和 Simulink 中变为非连续。

### **Enable Timestamp** — 启用发送 Simulink 时间戳到 STIM DTO 数据包 `off`（默认）| `on`

当启用 Timestamp 时，模块从 Simulink 输入时间戳，
并在 STIM DTO 数据包中发送该时间戳。当 A2L 文件中支持该参数时，**Enable
Timestamp** 复选框会出现在模块参数对话框
中。
## 所属库

Vehicle Network Toolbox / XCP Communication / CAN Simulink Real-Time / XCP / CAN

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，
但部署可移植性有限，仅能在主机或 Simulink
Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关更多信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2013a 中引入**

## 描述

对选定的测量执行数据激励

XCP CAN Data Stimulation 模块将数据发送到选定的服务器连接，用于选定的事件测量。该模块使用 XCP CAN 传输层，在指定的激励时间步长下输出所选测量的原始数据。配置您的 XCP 会话，并使用 XCP CAN Data Stimulation 模块在已配置的服务器连接上选择事件和测量。该模块将选定的测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration (Simulink)。
