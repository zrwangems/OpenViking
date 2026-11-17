---
type: simulink-block
title: 'Query Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'queryinstrument'
documentation_source_path: 'queryinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# Query Instrument

## 端口

R2025b 中未记录。

## 参数

**Block sample time**
:   Block sample time 参数是对话框选项卡之外的唯一设置。默认值为 `1`。将值设置为 `-1` 会使模块继承时序。正值用作采样周期。

### 硬件配置选项卡

**Hardware Configuration** 选项卡用于定义与仪器通信的设置。建立接口有两种选择：

- 指定新的硬件配置。
- 使用 MATLAB® 工作区中的接口对象。

下图显示了 **Hardware Configuration** 选项卡设置为使用串行端口接口指定新的硬件配置。

由于某些参数适用于多种接口类型，因此此处按字母顺序显示。

**Baudrate**
:   串行或 VISA 串行接口传输比特的速率。

**Board index**
:   用于与仪器进行 GPIB、VISA GPIB、VISA TCPIP 或 VISA USB 接口通信的板卡索引。

**Board vendor**
:   用于与仪器接口通信的 GPIB 板卡供应商。可选值为 Keysight®（原 Agilent®）、ICS Electronics™、Measurement Computing™ (MCC) 和 National Instruments™。

**Chassis index**
:   VXI 机箱的索引号。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**Buffer size**
:   读取操作期间软件输入缓冲区中可存储的总字节数。

**Interface**
:   选择与仪器通信的硬件接口类型。选项为 Instrument Control Toolbox™ 软件支持的接口。上图显示了串行端口接口的配置。

**Logical address**
:   VXI 仪器的逻辑地址。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**Manufacturer ID**
:   VISA USB 仪器的制造商 ID。有关详细信息，请参阅 ManufacturerID 属性。

**Model code**
:   VISA USB 仪器的型号代码。有关详细信息，请参阅 ModelCode 属性。

**Port**
:   串行接口的端口：COM1、COM2 等。

**Primary address**
:   仪器在 GPIB 上的主地址。

**Remote host**
:   仪器的主机名或 IP 地址。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**Remote port**
:   用于通信的仪器或远程主机上的端口。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**Secondary address**
:   仪器在 GPIB 上的辅助地址。

**Serial number**
:   VISA USB 仪器的序列号，定义为字符向量。有关详细信息，请参阅 SerialNumber 属性。

**Timeout**
:   完成查询操作所允许的时间（秒）。

**VISA vendor**
:   用于任何 VISA 接口类型的 VISA 供应商。可选值为 Keysight（原 Agilent）、National Instruments 和 Tektronix®。

**使用来自 MATLAB 工作区的接口对象**
:   选择此选项可使用 MATLAB 工作区中的接口对象。

**Workspace object**
:   输入要从 MATLAB 工作区使用的对象名称。

### 仪器初始化选项卡

**Instrument Initialization** 选项卡用于定义首次打开与仪器的连接时发生的情况。

**None**
:   默认初始化选项为 none。

**Send string**
:   作为仪器命令发送到仪器的字符串，用于初始化仪器或将其设置为已知状态。

**Execute function**
:   任何以表示仪器的接口对象作为唯一参数的函数。您可以编写此函数以包含多个仪器命令和初始化数据。

### 查询选项卡

**查询**选项卡用于定义可选的查询命令、设置响应格式，以及定义模块在收到初始仪器响应后的行为。

**查询命令**
:   这是发送到仪器的查询命令。它通常是请求仪器状态或数据的命令。*此命令是可选的*——如果您正在从仪器检索信息或数据，且不需要查询命令即可完成该操作，则可以将此字段留空。

**数据格式**
:   您的选项为 `ASCII`、`Binary` 或 `Binblock`（二进制块——`binblock` 格式在 `binblockwrite` 函数参考页中有描述）。

**ASCII 格式字符串**
:   仅当格式为 `ASCII` 时可用，此项定义数据的格式字符串。有关格式列表，请参阅 `fscanf` 函数。

**精度**
:   用于二进制或 binblock 格式。您的选项为：

    - `8-bit integer`（默认）
    - `16-bit integer`
    - `32-bit integer`
    - `8-bit unsigned integer`
    - `16-bit unsigned integer`
    - `32-bit unsigned integer`
    - `32-bit float`
    - `64-bit float`

**字节序**
:   当使用超过 8 位的二进制或 binblock 格式时，您可以指定仪器数据的字节序。您的选项为 `Big Endian` 或 `Little Endian`。

**要读取的二进制值**
:   用于二进制格式。指定要从仪器读取的二进制值数量。

**从输入缓冲区中移除额外字节**
:   如果您希望在查询之前从输入缓冲区中移除任何额外字节，请选择此选项。

**初始响应之后**
:   此项定义在收到仪器首次响应后要执行的操作。您的选项为 Repeat query for new data、Recycle original data、Hold final value、Output zero 或 Stop simulation。

**启用帧输出**
:   帧是组合成单个向量的样本序列。在基于帧的处理中，帧中的所有样本同时处理。在基于样本的处理中，样本一次处理一个。基于帧的处理的优势在于它可以大幅提高仿真速度。例如，如果您要从仪器读取波形而不是单点测量值，则可以使用帧。

**帧大小**
:   帧大小决定一帧中的样本数量。

**注意**

对话框框中显示的硬件信息在您首次打开对话框时确定并缓存。要使用新值刷新显示，请重新启动 MATLAB。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2024b：错误

此模块在添加到模型时会抛出错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，模型无法仿真。您仍然可以打开模块参数对话框并查看参数值。

请改用特定接口模块：

- Serial Configuration
- Serial Receive
- Serial Send
- TCP/IP Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

与 Query Instrument 和 To Instrument 相比，这些特定接口模块都支持附加属性并具有改进的性能。

### R2023b：将被移除

Query Instrument 和 To Instrument Simulink 模块将被移除。

## 描述

（将被移除）查询或读取仪器数据

Query Instrument 模块配置并打开与仪器的接口，初始化仪器，并向仪器查询数据。配置和初始化在模型执行开始时进行。模块在模型运行期间向仪器查询数据。

该模块没有输入端口。该模块有一个输出端口，对应于从仪器接收的数据。

### 其他支持的功能

- 此模块支持使用加速模式，但不支持快速
  加速或代码生成。
- 此模块支持使用模型引用，因此您的模型
  可以将其他 Simulink® 模型作为模块化组件包含在内。

有关这些功能的更多信息，请参阅 Simulink 文档。
