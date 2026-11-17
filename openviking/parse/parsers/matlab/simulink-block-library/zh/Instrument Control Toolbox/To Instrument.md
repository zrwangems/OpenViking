---
type: simulink-block
title: 'To Instrument'
family: 'instrument-control-toolbox'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Instrument Control Toolbox'
documentation_page: 'toinstrument'
documentation_source_path: 'toinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# To Instrument

## 端口

R2025b 中未提供文档。

## 参数

**模块采样时间**
:   模块采样时间参数是对话框选项卡之外的唯一设置。默认值 `-1` 使模块继承时序。正值用作采样周期。

### 硬件配置选项卡

**硬件配置**选项卡用于定义与仪器进行通信的设置。您可以通过以下两种方式建立接口：

- 指定新的硬件配置。
- 使用 MATLAB® 工作区中的接口对象。

下图显示了**硬件配置**选项卡设置为通过串行端口接口指定新的硬件配置。

由于某些参数适用于多种接口类型，因此此处按字母顺序列出这些参数。

**波特率**
:   串行或 VISA serial 接口的位传输速率。

**板卡索引**
:   用于与仪器连接的 GPIB、VISA GPIB、VISA TCPIP 或 VISA USB 接口的板卡索引。

**板卡供应商**
:   用于与仪器连接的接口的 GPIB 板卡供应商。可选项为 Keysight®（前身为 Agilent®）、ICS Electronics™、Measurement Computing™ (MCC) 和 National Instruments™。

**机箱索引**
:   VXI 机箱的索引编号。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**缓冲区大小**
:   读取操作期间可以存储在软件输出缓冲区中的字节总数。

**接口**
:   选择与仪器连接的硬件接口类型。可选项为 Instrument Control Toolbox™ 软件支持的接口。前图显示了串行端口接口的配置。

**逻辑地址**
:   VXI 仪器的逻辑地址。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**制造商 ID**
:   以字符向量形式定义的 VISA USB 仪器的制造商 ID。有关详细信息，请参阅 ManufacturerID 属性。

**型号代码**
:   以字符向量形式定义的 VISA USB 仪器的型号代码。有关详细信息，请参阅 ModelCode 属性。

**端口**
:   串行接口的端口：COM1、COM2 等。

**主地址**
:   仪器在 GPIB 上的主地址。

**远程主机**
:   仪器的主机名或 IP 地址。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**远程端口**
:   仪器或远程主机上用于通信的端口。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**辅地址**
:   仪器在 GPIB 上的辅地址。

**序列号**
:   以字符向量形式定义的 VISA USB 仪器的序列号。有关详细信息，请参阅 SerialNumber 属性。

**超时**
:   允许完成查询操作的时间，以秒为单位。

**VISA 供应商**
:   用于任意 VISA 接口类型的 VISA 仪器供应商。可选项为 Keysight（前身为 Agilent）、National Instruments 和 Tektronix®。

**使用 MATLAB 工作区中的接口对象**
:   选择此选项可使用 MATLAB 工作区中的接口对象。

**工作区对象**
:   输入要使用的 MATLAB 工作区中的对象名称。

### 仪器初始化选项卡

**仪器初始化**选项卡用于定义首次打开与仪器的连接时发生的操作。

**无**
:   默认初始化选项为无。

**发送字符串**
:   作为仪器命令发送到仪器的字符串，用于初始化仪器或将其设置为已知状态。

**执行函数**
:   任何仅以表示仪器的接口对象为唯一参数的函数。您可以编写此函数，使其包含多条仪器命令和初始化数据。

### 发送选项卡

**发送**选项卡用于定义发送到仪器的可选命令以及所发送数据的格式。

**命令**
:   这是与 Simulink 数据一起发送到仪器的命令。*此命令是可选的*——如果将此字段留空，Simulink 数据将在不带任何前缀或附加格式的情况下发送到仪器。

**输出格式**
:   可选项为 `ASCII`、`Binary` 或 `Binblock`（二进制数据块——`binblock` 格式在 `binblockwrite` 函数参考页中介绍）。

**ASCII 格式字符串**
:   仅当格式为 ASCII 时可用，用于定义数据的格式字符串。有关格式列表，请参阅 `fprintf` 函数。

**精度**
:   用于二进制或 binblock 格式。可选项为：

    - `8-bit integer`（默认）
    - `16-bit integer`
    - `32-bit integer`
    - `8-bit unsigned integer`
    - `16-bit unsigned integer`
    - `32-bit unsigned integer`
    - `32-bit float`
    - `64-bit float`

**字节顺序**
:   使用超过 8 位的二进制或 binblock 格式时，可以指定仪器的数据字节顺序。可选项为 `Big Endian` 或 `Little Endian`。

**提示**

对话框中显示的硬件信息在您首次打开对话框时确定并缓存。要使用新值刷新显示，请重新启动 MATLAB。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**R2006a 之前推出**

### R2024b: 错误

将此模块添加到模型中时，该模块会引发错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，模型无法仿真。您仍然可以打开模块参数对话框并查看参数值。

请改用特定于接口的模块：

- Serial Configuration
- Serial Receive
- Serial Send
- TCP/IP Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

与 Query Instrument 和 To Instrument 相比，这些特定于接口的模块均支持更多属性，并且性能有所改进。

### R2023b: 即将移除

Query Instrument 和 To Instrument 模块将在未来版本中移除。

## 描述

(即将移除) 将仿真数据发送到仪器

To Instrument 模块配置并打开与仪器之间的接口，初始化仪器，并向仪器发送数据。配置和初始化在模型开始执行时进行。模块在模型运行期间向仪器发送数据。

该模块没有输出端口。该模块有一个输入端口，与发送到仪器的数据相对应。此数据必须为双精度类型。

**注意**

To Instrument 模块可用于以下接口：VISA、GPIB、Serial、TCP/IP 和 UDP。不支持以下接口：SPI、I2C 和 Bluetooth。

### 其他支持的功能

- 此模块支持使用加速模式，但不支持 Rapid Accelerator 或代码生成。
- 该模块支持使用模型引用，因此您的模型可以将其他 Simulink® 模型作为模块化组件包含进来。

有关这些功能的详细信息，请参阅 Simulink 文档。
