---
type: simulink-block
title: 'XCP UDP Data Stimulation'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / UDP'
documentation_page: 'xcpudpdatastimulation'
documentation_source_path: 'io_ref/xcpudpdatastimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP UDP Data Stimulation

## 端口

R2025b 中未记录。

## 参数

### **Config name** — 指定 XCP UDP 会话名称 从列表中选择

选择您要使用的 XCP 配置名称。此列表显示模型中可用的 XCP UDP Configuration 模块中指定的所有可用名称。选择某个配置后，将显示该配置的 A2L 文件中可用的事件和测量量。使用一个 XCP UDP Data Stimulation 模块只能为一个事件激励测量量。对于每个要激励其测量量的事件，请使用一个模块。

### **Event name** — 选择事件 从列表中选择

从事件列表中选择一个事件。XCP UDP Configuration 模块使用指定的 A2L 文件来填充事件列表。该模块使用 A2L 中对应的事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块每次执行时都会进行激励。在 Simulink 仿真中使用时，请考虑启用仿真步调以避免自由运行的激励。

### **All Measurements** — 列出事件可用的所有测量量 测量量列表

此列表显示所选事件可用的所有测量量。选择您要使用的测量量，然后单击添加按钮，将其移动到已选测量量中。按住键盘上的 `Ctrl` 键可选择多个测量量。

在模块参数对话框中，输入您要使用的测量量名称。**All Measurements** 列表将显示所有匹配的名称。单击 x 以清除搜索。

### **Selected Measurements** — 列出已选测量量 测量量名称

此列表显示您已选择的测量量。要从该列表中移除某个测量量，请选择该测量量并单击移除按钮。

在 **Block Parameters** 对话框中，使用切换按钮对已选测量量重新排序。

### **模块输入设置** — 将端口输入设置为 Compu 方法转换值或原始值 `Raw values as double (no Compu method conversion)`（默认）| `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数用于支持 ASAP2 标准中定义的 XCP 数据类型和维度。模块输入设置参数用于选择端口输出 Compu 方法转换值还是原始值。各选项提供以下功能：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的物理值到原始值转换。
  对于此选项，模块端口设置根据底层 Compu 方法转换设置为
  `'double'` 或 `'string'`。
  例如，Compu 方法 `IDENTICAL`、`LINEAR`、
  `RAT_FUNC`、`TAB_INTP` 和
  `TAB_NOINTP` 的端口设置为
  `'double'`，而 Compu 方法
  `TAB_VERB` 的端口设置为
  `'string'`。Compu 方法转换支持的最大字符串长度为 1024，如 ASAM XIL 规范中所规定。

  不支持 FORM Compu 方法转换。Simulink 对此类转换会抛出
  警告，并对底层测量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

  选择此选项后，模块掩码上的测量名称前方会显示物理单位（如果有）。此物理单位
  从测量的 A2L 描述和 Compu
  方法中获取。如果未指定物理单位，则仅显示测量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义
  设置端口数据类型，并在
  Simulink 中支持最多三维的 XCP 测量。
- `Raw values as double (no Compu method
  conversion)` 将端口数据类型设置为
  `double`，转换所有内部测量
  值。此选项在 Simulink 中支持最多三维的 XCP
  测量。

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

模块中的维度支持兼顾了 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为
行主序矩阵。XCP 测量的 `LAYOUT`
可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵
测量为 `COLUMN_DIR`，模块会重新排列
内存中的测量数据，确保 MATLAB 中的矩阵（行 X，列 Y）
与 ECU 上的（行 X，列 Y）指向同一条目。这种重新排列
会导致在 ECU 上连续的矩阵条目在
MATLAB 和 Simulink 中变为非连续。

### **启用时间戳** — 启用通过 STIM DTO 数据包发送 Simulink 时间戳 `off`（默认）| `on`

当启用时间戳时，模块从 Simulink 输入时间戳，并通过 STIM DTO 数据包发送该时间戳。当 A2L 文件中支持该参数时，**启用
时间戳**复选框会显示在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，
但部署可移植性有限，仅能在主机或 Simulink
Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关更多信息，请参阅支持的兼容编译器。

## 版本历史

**在 R2019a 中引入**

### R2021b：Compu 方法转换支持

为添加 Compu 方法转换支持，XCP CAN Data Acquisition 模块、XCP CAN Data Stimulation 模块、XCP UDP Data Acquisition 模块和 XCP UDP Data Stimulation 模块的 **Force Datatypes and Allow Non-Scalar** 参数已替换为 **Block Input/ Output Settings** 参数。使用此参数，您可以选择是将 Compu 方法转换应用于模块输入还是输出。

## 描述

对选定的测量执行数据激励

XCP UDP Data Stimulation 模块将数据发送到所选服务器连接，用于您选择的事件测量。该模块使用 XCP UDP 传输层，在指定的激励时间步长输出所选测量的原始数据。配置您的 XCP 会话，并使用 XCP UDP Data Stimulation 模块在已配置的服务器连接上选择事件和测量。该模块将选定的测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration。
