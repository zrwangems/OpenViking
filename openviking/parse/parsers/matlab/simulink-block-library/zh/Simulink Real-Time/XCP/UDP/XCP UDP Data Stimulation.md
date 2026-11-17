---
type: simulink-block
title: 'XCP UDP Data Stimulation'
family: 'xcp'
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

### **配置名称** — 指定 XCP UDP 会话名称，从列表中选择

选择要使用的 XCP 配置名称。此列表显示模型中可用的 XCP UDP Configuration 模块内指定的所有可用名称。选择配置会显示此配置的 A2L 文件中可用的事件和测量。使用一个 XCP UDP Data Stimulation 模块只能激励一个事件的测量。对于要激励其测量的每个事件，使用一个模块。

### **事件名称** — 从列表中选择事件

从事件列表中选择事件。XCP UDP Configuration 模块使用指定的 A2L 文件填充事件列表。该模块使用 A2L 中的对应事件编号进行配置。

事件时间周期不控制激励数据包的传输。该模块每次执行时都会进行激励。在 Simulink 仿真中使用时，考虑启用仿真调速以避免自由运行的激励。

### **所有测量** — 列出事件测量列表可用的所有测量

此列表显示所选事件可用的所有测量。选择要使用的测量，然后单击添加按钮，将其移动到选定测量。按住键盘上的 `Ctrl` 键可选择多个测量。

在模块参数对话框中，键入要使用的测量名称。**所有测量**列表显示所有匹配名称的列表。单击 x 以清除搜索。

### **选定测量** — 列出选定测量的测量名称

此列表显示您选定的测量。要从该列表中移除测量，请选择该测量并单击移除按钮。

在**模块参数**对话框中，使用切换按钮  对选定的测量重新排序。

### **模块输入设置** — 将端口输入设置为 Compu method 转换值或原始值 `Raw values as double (no Compu method conversion)`（默认） | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。**模块输入设置**参数选择端口输出的是 Compu method 转换值还是原始值。选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的物理值到原始值转换。
  对于此选项，模块端口设置会根据底层 Compu method 转换设置为
  `'double'` 或 `'string'`。例如，Compu
  method `IDENTICAL`、`LINEAR`、
  `RAT_FUNC`、`TAB_INTP` 和
  `TAB_NOINTP` 的端口设置为
  `'double'`，而 Compu method
  `TAB_VERB` 的端口设置为
  `'string'`。Compu method 转换支持的最大字符串长度
  为 1024，如 ASAM XIL 规范中所指定。

  不支持 FORM Compu method 转换。Simulink 对此类转换会发出警告，并对底层
  测量应用 IDENTICAL 转换。此外，由于 Simulink 仅支持标量字符串，
  TAB\_VERB 转换仅支持标量测量信号。

  选择此选项会在模块掩码上的测量名称前面显示物理单位（如果有）。此物理单位从
  测量的 A2L 描述和 Compu method 中获取。如果未指定物理单位，则仅显示测量
  名称。
- `Raw values (no Compu method conversion)` 根据
  A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维的 XCP
  测量。
- `Raw values as double (no Compu method
  conversion)` 将端口数据类型设置为
  `double`，并转换所有内部测量值。此选择在 Simulink 中支持最多三维的 XCP
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

模块中的维度支持适应 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为
行主序矩阵。XCP 测量的 `LAYOUT`
可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵
测量为 `COLUMN_DIR`，模块会在内存中重新排列
测量，并确保 MATLAB 中的矩阵（行 X，列 Y）
与 ECU 上的（行 X，列 Y）指向同一条目。这种重新排列
会导致在 ECU 上连续的矩阵条目在
MATLAB 和 Simulink 中不连续。

### **启用时间戳** — 启用在 STIM DTO 数据包中发送 Simulink 时间戳 `off`（默认） | `on`

当启用时间戳时，模块从 Simulink 输入时间戳，并在 STIM DTO 数据包中发送该时间戳。当 A2L 文件支持该参数时，**启用时间戳**复选框会出现在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，
但部署可移植性有限，仅能在主机计算机或 Simulink
Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持的兼容编译器。

## 版本历史

**在 R2019a 中引入**

### R2021b：Compu Method 转换支持

为添加 Compu method 转换支持，XCP CAN Data Acquisition
模块、XCP CAN Data Stimulation 模块、XCP UDP Data
Acquisition 模块和 XCP UDP Data Stimulation 模块的
**强制数据类型并允许非标量** 参数已替换为 **模块输入/输出设置** 参数。
使用此参数，您可以选择是将 Compu method 转换应用于
模块输入还是输出。

## 描述

对选定的测量执行数据激励

XCP UDP Data Stimulation 模块将数据发送到选定的服务器
连接，用于您选择的事件测量。该模块使用 XCP UDP
传输层在指定的激励时间步输出所选测量的原始数据。配置您的 XCP 会话，并使用 XCP UDP Data
Stimulation 模块在已配置的服务器连接上选择事件和测量。该模块将选定的测量显示为输入端口。

XCP 通信模块支持 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速
Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration。
