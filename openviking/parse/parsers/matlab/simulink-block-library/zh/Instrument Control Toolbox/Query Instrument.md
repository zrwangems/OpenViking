---
type: simulink-block
title: 'Query Instrument'
family: 'instrument-control-toolbox'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: 'Instrument Control Toolbox'
documentation_page: 'queryinstrument'
documentation_source_path: 'queryinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# Query Instrument

## 端口

R2025b 中未提供文档。

## 参数

**模块采样时间**
:   模块采样时间参数是对话框选项卡之外的唯一设置。默认值为 `1`。将该值设置为 `-1` 会使模块继承时序。正值用作采样周期。

### 硬件配置选项卡

**硬件配置**选项卡用于定义与仪器通信的设置。建立接口时，您有两种选择：

- 指定新的硬件配置。
- 使用 MATLAB® 工作区中的接口对象。

下图显示了**硬件配置**选项卡设置为使用串行端口接口指定新的硬件配置。

由于某些参数适用于多种接口类型，因此此处按字母顺序列出这些参数。

**波特率**
:   串行或 VISA serial 接口的比特传输速率。

**板卡索引**
:   GPIB、VISA GPIB、VISA TCPIP 或 VISA USB 仪器接口所用板卡的索引。

**板卡供应商**
:   用于仪器接口的 GPIB 板卡的供应商。可选项包括 Keysight®（前身为 Agilent®）、ICS Electronics™、Measurement Computing™ (MCC) 和 National Instruments™。

**机箱索引**
:   VXI 机箱的索引号。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**缓冲区大小**
:   读取操作期间可存储在软件输入缓冲区中的总字节数。

**接口**
:   选择仪器的硬件接口类型。可选项为 Instrument Control Toolbox™ 软件支持的接口。上图显示了串行端口接口的配置。

**逻辑地址**
:   VXI 仪器的逻辑地址。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**制造商 ID**
:   VISA USB 仪器的制造商 ID。有关详细信息，请参阅 ManufacturerID 属性。

**型号代码**
:   VISA USB 仪器的型号代码。有关详细信息，请参阅 ModelCode 属性。

**端口**
:   串行接口使用的端口：COM1、COM2 等。

**主地址**
:   仪器在 GPIB 上的主地址。

**远程主机**
:   仪器的主机名或 IP 地址。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**远程端口**
:   仪器或远程主机上用于通信的端口。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**次地址**
:   仪器在 GPIB 上的次地址。

**序列号**
:   以字符向量形式定义的 VISA USB 仪器序列号。有关详细信息，请参阅 SerialNumber 属性。

**超时时间**
:   允许完成查询操作的时间，以秒为单位。

**VISA 供应商**
:   为任意 VISA 接口类型选择 VISA 供应商。可选项包括 Keysight（前身为 Agilent）、National Instruments 和 Tektronix®。

**使用 MATLAB 工作区中的接口对象**
:   选择此选项以使用 MATLAB 工作区中的接口对象。

**工作区对象**
:   输入要使用的 MATLAB 工作区中的对象名称。

### 仪器初始化选项卡

**仪器初始化**选项卡用于定义首次打开与仪器的连接时要执行的操作。

**None**
:   默认初始化选项为 None。

**Send string**
:   作为仪器命令发送到仪器的字符串，用于初始化仪器或将其设置为已知状态。

**Execute function**
:   任何将表示仪器的接口对象作为其唯一参数的函数。您可以编写此函数，使其包含多条仪器命令和初始化数据。

### 查询选项卡

**查询**选项卡用于定义可选的查询命令、设置响应格式，以及定义模块在收到仪器初始响应后执行的操作。

**查询命令**
:   这是发送到仪器的查询命令，通常用于请求仪器状态或数据。*此命令为可选项*——如果您要从仪器检索信息或数据，且无需查询命令即可完成，则可以将此字段留空。

**数据格式**
:   可选项包括 `ASCII`、`Binary` 或 `Binblock`（二进制块——`binblock` 格式在 `binblockwrite` 函数参考页中介绍）。

**ASCII 格式字符串**
:   仅在格式为 `ASCII` 时可用，用于定义数据的格式字符串。有关格式列表，请参阅 `fscanf` 函数。

**精度**
:   用于二进制或 binblock 格式。可选项包括：

    - `8-bit integer`（默认）
    - `16-bit integer`
    - `32-bit integer`
    - `8-bit unsigned integer`
    - `16-bit unsigned integer`
    - `32-bit unsigned integer`
    - `32-bit float`
    - `64-bit float`

**字节顺序**
:   当以二进制或 binblock 格式使用超过 8 位的数据时，可以指定仪器采用的数据字节顺序。可选项包括 `Big Endian` 或 `Little Endian`。

**要读取的二进制值数量**
:   用于二进制格式。指定要从仪器读取的二进制值数量。

**从输入缓冲区中移除额外字节**
:   如果要在查询前从输入缓冲区中移除任何额外字节，请选择此选项。

**初始响应后的操作**
:   定义在收到仪器的首次响应后要执行的操作。可选项包括 Repeat query for new data、Recycle original data、Hold final value、Output zero 或 Stop simulation。

**启用帧输出**
:   帧是组合为单个向量的一系列采样。在基于帧的处理中，帧中的所有采样都会同时处理。在基于采样的处理中，采样会逐个处理。基于帧的处理的优点是可以大幅提高仿真速度。例如，如果要从仪器读取波形而不是单点测量，则可能会使用帧。

**帧大小**
:   帧大小决定一帧中的采样数。

**注意**

对话框中显示的硬件信息在您首次打开对话框时确定并缓存。要使用新值刷新显示，请重新启动 MATLAB。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2006a 之前推出**

### R2024b: 错误

将此模块添加到模型时会引发错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，模型无法进行仿真。您仍然可以打开模块参数对话框并查看参数值。

请改用以下接口专用模块：

- Serial Configuration
- Serial Receive
- Serial Send
- TCP/IP Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

与 Query Instrument 和 To Instrument 相比，这些接口专用模块均支持更多属性，并且性能有所提升。

### R2023b: 将被移除

Simulink 模块 Query Instrument 和 To Instrument 将被移除。

## 描述

（将被移除）查询或读取仪器数据

Query Instrument 模块配置并打开与仪器的接口，初始化仪器，并查询仪器以获取数据。配置和初始化在模型开始执行时进行。模块在模型运行期间查询仪器以获取数据。

该模块没有输入端口。该模块有一个输出端口，对应于从仪器接收的数据。

### 其他支持的功能

- 此模块支持使用加速器模式，但不支持 Rapid Accelerator 或代码生成。
- 该模块支持使用模型引用，因此您的模型可以将其他 Simulink® 模型作为模块化组件包含进来。

有关这些功能的详细信息，请参阅 Simulink 文档。
