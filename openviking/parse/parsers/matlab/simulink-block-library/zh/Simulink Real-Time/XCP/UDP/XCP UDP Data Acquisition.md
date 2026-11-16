---
type: simulink-block
title: 'XCP UDP Data Acquisition'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'XCP / UDP'
documentation_page: 'xcpudpdataacquisition'
documentation_source_path: 'io_ref/xcpudpdataacquisition.html'
language: zh-CN
chinese_source: worker-translation
---

# XCP UDP Data Acquisition

## 端口

R2025b 中未提供文档。

## 参数

### **Config name** — 从列表中选择 XCP UDP 会话名称

选择要使用的 XCP 配置名称。此列表显示模型中 XCP UDP Configuration 模块指定的所有可用名称。选择配置会显示此配置的 A2L 文件中可用的事件和测量值。使用一个 XCP UDP Data Acquisition 模块，只能获取一个事件的测量值。对于要获取其测量值的每个事件，请使用一个模块。

### **Event name** — 从列表中选择事件

从可用事件列表中选择一个事件。XCP UDP Configuration 模块使用指定的 A2L 文件填充事件列表。

### **All Measurements** — 列出事件可用的所有测量值 测量值列表

此列表显示所选事件的所有可用测量值。选择要使用的测量值，然后单击添加按钮，将其添加到选定的测量值中。按住键盘上的 `Ctrl` 键可选择多个测量值。

在 **Block Parameters** 对话框中，在 **Search** 框中键入要使用的测量值名称。**All Measurements** 列表显示所有匹配名称的列表。单击 x 以清除搜索。

### **Selected Measurements** — 列出选定的测量值 测量值名称

此列表显示选定的测量值。要从该列表中移除测量值，请选择该测量值，然后单击移除按钮。

在 **Block Parameters** 对话框中，使用切换按钮重新排列选定的测量值。

### **Block Output Settings** — 将端口输出设置为 Compu 方法转换值或原始值 `Raw values as double (no Compu method conversion)` (默认) | `Raw values (no Compu method conversion)` | `Physical values (apply Compu method conversion)`

此参数支持 ASAP2 标准中定义的 XCP 数据类型和维度。Block Output Settings 参数选择端口输出的是 Compu 方法转换值还是原始值。这些选项提供：

- `Physical values (apply Compu method conversion)`
  启用 ECU 测量值的原始值到物理值转换。对于此选项，根据底层 Compu 方法转换，模块端口设置设置为 `'double'` 或 `'string'`。例如，Compu 方法 `IDENTICAL`、`LINEAR`、`RAT_FUNC`、`TAB_INTP` 和 `TAB_NOINTP` 的端口设置为 `'double'`，而 Compu 方法 `TAB_VERB` 的端口设置为 `'string'`。Compu 方法转换支持的最大字符串长度为 1024，如 ASAM XIL 规范所指定。

  FORM Compu 方法转换不受支持。Simulink 对此类转换会发出警告，并对底层测量值应用 IDENTICAL 转换。此外，TAB\_VERB 转换仅支持标量测量信号，因为 Simulink 仅支持标量字符串。

  选择此选项会在模块掩码上的测量值名称前显示物理单位（如果有）。此物理单位从测量值和 Compu 方法的 A2L 描述中获取。如果未指定物理单位，则仅显示测量值名称。
- `Raw values (no Compu method conversion)` 根据 A2L 文件中的类型定义设置端口数据类型，并在 Simulink 中支持最多三维的 XCP 测量值。
- `Raw values as double (no Compu method conversion)` 将端口数据类型设置为 `double`，转换所有内部测量值。此选择在 Simulink 中支持最多三维的 XCP 测量值。

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

模块中的维度支持适应 MATLAB® 和 ECU 对矩阵的不同处理方式。MATLAB 默认操作将矩阵视为行优先矩阵。XCP 测量值的 `LAYOUT` 可以是 `COLUMN_DIR` 或 `ROW_DIR`。如果矩阵测量值为 `COLUMN_DIR`，模块会重新排列内存中的测量值，并确保 MATLAB 中的矩阵（行 X，列 Y）与 ECU 上的（行 X，列 Y）指向同一条目。这种重新排列会导致在 ECU 上连续的矩阵条目在 MATLAB 和 Simulink 中不连续。

### **DAQ List Priority** — 为服务器设备驱动指定优先级值

将优先级值指定为 0 到 255 的整数，以便服务器设备驱动对数据包的传输进行优先级排序。服务器可以在向客户端传输之前，为较低优先级的 DAQ 列表累积 XCP 数据包。值 255 具有最高优先级。`SET_DAQ_LIST_MODE` 命令将 **DAQ List Priority** 值从客户端传送到服务器。此通信方法不同于 Event Channel Priority 属性的规范，后者来自 A2L 文件。

### **Sample time** — 指定模块的采样时间 `-1` (默认)

指定模块在仿真期间的采样时间，即仿真时间。此值定义 XCP UDP Data Acquisition 模块在仿真期间运行的频率。如果模块位于触发子系统内，或者要继承采样时间，则可以将采样时间指定为 `–1`，这是默认值。也可以为采样时间指定 MATLAB 变量。有关仿真采样时序的信息，请参阅什么是采样时间？。

### **Enable Timestamp** — 启用从传入 DTO 数据包读取时间戳 `off` (默认) | `on`

启用时间戳后，模块从传入的 DTO 数据包读取时间戳，并将时间戳输出到 Simulink。当 A2L 文件支持该参数时，**Enable Timestamp** 复选框会出现在模块参数对话框中。

## 所属库

Vehicle Network Toolbox / XCP Communication / UDP Simulink Real-Time / XCP / UDP

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

XCP 通信模块支持代码生成，但部署可移植性有限，只能在主机或 Simulink Real-Time™ 目标上运行。

代码生成需要与代码生成目标兼容的 C++ 编译器。有关详细信息，请参阅支持的兼容编译器。

## 版本历史

**R2019a 中引入**

### R2021b：Compu 方法转换支持

为添加 Compu 方法转换支持，XCP CAN Data Acquisition 模块、XCP CAN Data Stimulation 模块、XCP UDP Data Acquisition 模块和 XCP UDP Data Stimulation 模块的 **Force Datatypes and Allow Non-Scalar** 参数已替换为 **Block Input/ Output Settings** 参数。使用此参数，可以选择是将 Compu 方法转换应用于模块输入还是输出。

## 描述

从已配置的服务器连接采集选定的测量值

XCP UDP Data Acquisition 模块根据您选择的测量值从已配置的服务器连接采集数据。该模块使用 XCP UDP 传输层，在指定的仿真时间步获取所选测量值的原始数据。配置 XCP 连接，并使用 XCP UDP Data Acquisition 模块为已配置的服务器连接选择事件和测量值。该模块将选定的测量值显示为输出端口。

XCP 通信模块支持使用 Simulink® 加速模式和快速加速模式。通过使用这些模式，可以加快 Simulink 模型的执行速度。有关这些仿真模式的详细信息，请参阅加速。
