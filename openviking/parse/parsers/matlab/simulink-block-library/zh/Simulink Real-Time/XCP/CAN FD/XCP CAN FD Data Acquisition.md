---
type: simulink-block
title: 'XCP CAN FD Data Acquisition'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / CAN FD'
documentation_page: 'xcpcanfddataacquisition'
documentation_source_path: 'io_ref/xcpcanfddataacquisition.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP CAN FD Data Acquisition

## 端口

### 输出

### **Data** — 由 A2L 文件定义的输出测量样本

输出测量样本，其名称和类型由 A2L 文件定义。
Selected Measurements 参数中的每个条目定义一个输出端口。在仿真的每一步，每个端口都会有一个样本可用。

## 参数

### **Config name** — 指定 XCP CAN FD 会话名称，从列表中选择

选择要使用的 XCP 配置名称。此列表显示模型中 XCP CAN FD Configuration 模块指定的所有可用名称。选择某个配置后，将显示该配置的 A2L 文件中可用的事件和测量。

**注意**

使用一个 XCP CAN FD Data Acquisition 模块只能获取一个事件的测量。对于要获取其测量的每个事件，请使用一个单独的模块。

### **Event name** — 选择一个事件，从列表中选择

从可用事件列表中选择一个事件。XCP CAN FD Configuration 模块使用指定的 A2L 文件填充事件列表。

### **All Measurements** — 列出该事件可用的所有测量，测量列表

此列表显示所选事件可用的所有测量。选择要使用的测量，然后单击添加按钮，
将其添加到已选测量中。在键盘上，按 **Ctrl** 键可选择多个测量。

在“模块参数”对话框中，在 **Search** 框中键入要使用的测量名称。**All Measurements** 列表将显示所有匹配名称的列表。单击 x 可清除搜索。

### **Selected Measurements** — 列出已选测量，测量名称

此列表显示已选测量。每个已选测量都会为模块添加一个以该测量名称命名的输出端口。要从该列表中移除某个测量，请选择该测量并单击移除按钮，
。

在“模块参数”对话框中，使用移位按钮
 对已选测量重新排序。

### **Block Output Settings** — 将端口输出设置为 Compu method 转换值或原始值 `Raw values as double (no Compu method conversion)`（默认）| `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。Block Output Settings 参数选择端口输出 Compu method 转换值还是原始值。这些选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的原始值到物理值转换。对于此选项，模块端口设置根据底层 Compu method 转换设置为
  `'double'` 或 `'string'`。例如，Compu method
  `IDENTICAL`、`LINEAR`、
  `RAT_FUNC`、`TAB_INTP` 和
  `TAB_NOINTP` 的端口设置为
  `'double'`，而 Compu method
  `TAB_VERB` 的端口设置为 `'string'`。
  Compu method 转换支持的最大字符串长度为 1024，如 ASAM XIL
  规范中所指定。

  不支持 FORM Compu method 转换。Simulink 对此类转换抛出警告，并对底层测量应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

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

模块中的维度支持适应了 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行主序矩阵。XCP 测量的 `LAYOUT` 可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量为 `COLUMN_DIR`，模块会在内存中重新排列测量，并确保 MATLAB 中的矩阵（行 X，列 Y）与 ECU 上的（行 X，列 Y）指向同一条目。这种重新排列导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **DAQ List Priority** — 为服务器设备驱动程序优先级指定优先级值

指定一个 0 到 255 的整数优先级值，用于服务器设备驱动程序对数据包传输进行优先级排序。服务器可以在传输到客户端之前累积较低优先级 DAQ 列表的 XCP 数据包。值 255 具有最高优先级。`SET_DAQ_LIST_MODE` 命令将 **DAQ List Priority** 值从客户端传送到服务器。此通信方法不同于 Event Channel Priority 属性的规范，后者来自 A2L 文件。

### **Sample time** — 指定模块的采样时间 `-1`（默认）

指定仿真期间模块的采样时间，即仿真时间。此值定义了 XCP CAN FD Data Acquisition 模块在仿真期间运行的频率。如果模块位于触发子系统内或要继承采样时间，可以将采样时间指定为 `–1`，这是默认值。还可以为采样时间指定 MATLAB 变量。有关详细信息，请参阅 What Is Sample Time?。

### **Enable Timestamp** — 启用从传入 DTO 数据包读取时间戳 `off`（默认）| `on`

当启用 Timestamp 时，该模块从传入的 DTO 数据包中读取时间戳，并将时间戳输出到 Simulink。当 A2L 文件支持该参数时，**Enable Timestamp** 复选框会出现在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，仅能在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅 Supported and Compatible Compilers。

## 版本历史

**在 R2022b 中引入**

## 描述

从已配置的服务器连接获取选定的测量

XCP CAN FD Data Acquisition 模块根据您选择的测量，从已配置的服务器连接获取数据。该模块使用 XCP CAN FD 传输层，在指定的仿真时间步获取所选测量的原始数据。配置您的 XCP 连接，并使用 XCP CAN FD Data Acquisition 模块为已配置的服务器连接选择事件和测量。该模块将选定的测量显示为输出端口。

XCP 通信模块支持使用 Simulink® 加速模式和快速加速模式。您可以使用这些模式加速 Simulink 模型的执行。有关这些仿真模式的详细信息，请参阅 Acceleration。
