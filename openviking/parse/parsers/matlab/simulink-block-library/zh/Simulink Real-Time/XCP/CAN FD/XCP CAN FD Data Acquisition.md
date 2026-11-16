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

由 A2L 文件定义名称和类型的输出测量样本。
选定的测量参数中的每个条目定义一个输出端口。每个仿真步的每个端口都提供一个样本。

## 参数

### **配置名称** — 指定 XCP CAN FD 会话名称，从列表中选择

选择要使用的 XCP 配置名称。此列表显示模型中 XCP CAN FD Configuration 模块中指定的所有可用名称。选择配置后，会显示此配置的 A2L 文件中可用的事件和测量。

**注意**

使用 XCP CAN FD Data Acquisition 模块只能获取一个事件的测量。对于要获取其测量的每个事件，使用一个模块。

### **事件名称** — 从列表中选择一个事件

从可用事件列表中选择一个事件。XCP CAN FD Configuration 模块使用指定的 A2L 文件填充事件列表。

### **所有测量** — 列出事件可用的所有测量

此列表显示所选事件可用的所有测量。选择要使用的测量，然后单击添加按钮，将其添加到选定的测量。在键盘上，按 **Ctrl** 键可选择多个测量。

在“模块参数”对话框中，在 **搜索** 框中键入要使用的测量名称。**所有测量** 列表将显示所有匹配名称的列表。单击 x 清除搜索。

### **选定的测量** — 列出选定的测量名称

此列表显示选定的测量。每个选定的测量都会向模块添加一个以该测量名称命名的输出端口。要从该列表中删除测量，请选择该测量，然后单击移除按钮。

在“模块参数”对话框中，使用移动按钮重新排序选定的测量。

### **模块输出设置** — 将端口输出设置为 Compu method 转换值或原始值 `Raw values as double (no Compu method conversion)`（默认） | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。模块输出设置参数选择端口输出 Compu method 转换值还是原始值。这些选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的原始值到物理值转换。对于此选项，模块端口设置基于底层 Compu method 转换设置为 `'double'` 或 `'string'`。例如，Compu method `IDENTICAL`、`LINEAR`、`RAT_FUNC`、`TAB_INTP` 和 `TAB_NOINTP` 的端口设置为 `'double'`，而 Compu method `TAB_VERB` 的端口设置为 `'string'`。Compu method 转换支持的最大字符串长度为 1024，如 ASAM XIL 规范所指定。

  不支持 FORM Compu method 转换。对于此类转换，Simulink 会发出警告，并对底层测量应用 IDENTICAL 转换。此外，由于 Simulink 仅支持标量字符串，因此 `TAB_VERB` 转换仅支持标量测量信号。

  选择此选项后，会在模块蒙版上的测量名称前显示物理单位（如果有）。该物理单位从测量和 Compu method 的 A2L 描述中获取。如果未指定物理单位，则仅显示测量名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维的 XCP 测量。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，并转换所有内部测量值。此选项在 Simulink 中支持最多三维的 XCP 测量。

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

模块中的维度支持适应了 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行主序矩阵。XCP 测量可以具有 `LAYOUT`，值为 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量为 `COLUMN_DIR`，模块会重新排列内存中的测量，并确保 MATLAB 中的矩阵（行 X，列 Y）与 ECU 上的（行 X，列 Y）引用同一条目。这种重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **DAQ 列表优先级** — 为服务器设备驱动程序指定优先级值

指定一个 0 到 255 的整数值，供服务器设备驱动程序用来确定数据包传输的优先级。服务器可以在向客户端传输之前累积较低优先级 DAQ 列表的 XCP 数据包。值 255 的优先级最高。`SET_DAQ_LIST_MODE` 命令将 **DAQ 列表优先级** 值从客户端传送到服务器。此通信方法不同于 Event Channel Priority 属性的规范，后者来自 A2L 文件。

### **采样时间** — 指定模块的采样时间 `-1`（默认）

指定仿真期间模块的采样时间，即仿真时间。此值定义仿真期间 XCP CAN FD Data Acquisition 模块运行的频率。如果模块位于触发子系统内或要继承采样时间，则可以将采样时间指定为 `–1`，这是默认值。还可以为采样时间指定 MATLAB 变量。有关详细信息，请参阅什么是采样时间？

### **启用时间戳** — 启用从传入 DTO 数据包读取时间戳 `off`（默认） | `on`

启用时间戳后，模块会从传入的 DTO 数据包读取时间戳，并将时间戳输出到 Simulink。当 A2L 文件支持该参数时，模块参数对话框中会显示 **启用时间戳** 复选框。

## 所属库

Vehicle Network Toolbox / XCP Communication / CAN FD Simulink Real-Time / XCP / CAN FD

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，只能在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅受支持且兼容的编译器。

## 版本历史

**在 R2022b 中引入**

## 描述

从配置的服务器连接获取选定的测量

XCP CAN FD Data Acquisition 模块基于您选择的测量，从配置的服务器连接获取数据。该模块使用 XCP CAN FD 传输层在指定的仿真时间步为选定的测量获取原始数据。配置 XCP 连接，并使用 XCP CAN FD Data Acquisition 模块为配置的服务器连接选择事件和测量。该模块将选定的测量显示为输出端口。

XCP 通信模块支持使用 Simulink® 加速模式和快速加速模式。您可以使用这些模式加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速。
