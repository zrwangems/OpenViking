---
type: simulink-block
title: 'To Instrument'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'toinstrument'
documentation_source_path: 'toinstrument.html'
language: zh-CN
chinese_source: worker-translation
---

# To Instrument

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Block sample time**
:   Block sample time 参数是对话框选项卡之外的唯一设置。默认值 `-1` 将模块设置为继承时序。正值用作采样周期。

### Hardware Configuration 选项卡

**Hardware Configuration** 选项卡用于定义与仪器通信的设置。建立接口有两种选择：

- 指定新的硬件配置。
- 使用 MATLAB® 工作区中的接口对象。

下图显示了 **Hardware Configuration** 选项卡设置为使用串行端口接口指定新的硬件配置。

由于某些参数适用于多种接口类型，因此在此处按字母顺序排列。

**Baudrate**
:   串行或 VISA 串行接口传输比特的速率。

**Board index**
:   用于与仪器进行 GPIB、VISA GPIB、VISA TCPIP 或 VISA USB 接口通信的板卡索引。

**Board vendor**
:   用于与仪器接口通信的 GPIB 板卡供应商。可选值为 Keysight®（原 Agilent®）、ICS Electronics™、Measurement Computing™ (MCC) 和 National Instruments™。

**Chassis index**
:   VXI 机箱的索引号。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**Buffer size**
:   读取操作期间软件输出缓冲区可存储的总字节数。

**Interface**
:   选择与仪器通信的硬件接口类型。可选值为 Instrument Control Toolbox™ 软件支持的接口。上图显示了串行端口接口的配置。

**Logical address**
:   VXI 仪器的逻辑地址。用于 VISA VXI 和 VISA VXI-GPIB 接口类型。

**Manufacturer ID**
:   VISA USB 仪器的制造商 ID，定义为字符向量。有关详细信息，请参阅 ManufacturerID 属性。

**Model code**
:   VISA USB 仪器的型号代码，定义为字符向量。有关详细信息，请参阅 ModelCode 属性。

**Port**
:   串行接口的端口：COM1、COM2 等。

**Primary address**
:   仪器在 GPIB 上的主地址。

**Remote host**
:   仪器的主机名或 IP 地址。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**Remote port**
:   仪器或远程主机上用于通信的端口。用于 UDP、TCPIP 或 VISA TCPIP 接口类型。

**Secondary address**
:   仪器在 GPIB 上的辅助地址。

**Serial number**
:   VISA USB 仪器的序列号，定义为字符向量。有关详细信息，请参阅 SerialNumber 属性。

**Timeout**
:   完成查询操作所允许的时间，以秒为单位。

**VISA vendor**
:   用于任何 VISA 接口类型的 VISA 仪器供应商。可选值为 Keysight（原 Agilent）、National Instruments 和 Tektronix®。

**使用来自 MATLAB 工作区的接口对象**
:   选择此选项可使用 MATLAB 工作区中的接口对象。

**Workspace object**
:   输入要从 MATLAB 工作区使用的对象名称。

### Instrument Initialization 选项卡

**Instrument Initialization** 选项卡用于定义首次打开与仪器的连接时发生的情况。

**None**
:   默认初始化选项为 none。

**Send string**
:   作为仪器命令发送到仪器的字符串，用于初始化仪器或将其设置为已知状态。

**Execute function**
:   任何以表示仪器的接口对象作为唯一参数的函数。您可以编写此函数以包含多个仪器命令和初始化数据。

### 发送选项卡

**发送**选项卡用于定义发送到仪器的可选命令以及发送数据的格式。

**命令**
:   这是随 Simulink 数据一起发送到仪器的命令。*此命令是可选的*——如果将此字段留空，则 Simulink 数据将发送到仪器，不带任何前缀或附加格式。

**输出格式**
:   可选项为 `ASCII`、`Binary` 或 `Binblock`（二进制块——`binblock` 格式在 `binblockwrite` 函数参考页中有描述）。

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

**字节序**
:   当使用超过 8 位的二进制或 binblock 格式时，可以指定仪器数据的字节序。可选项为 `Big Endian` 或 `Little Endian`。

**提示**

对话框中显示的硬件信息在首次打开对话框时确定并缓存。要使用新值刷新显示，请重新启动 MATLAB。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前推出**

### R2024b：错误

此模块添加到模型时会抛出错误。打开任何包含此模块的现有模型都会导致错误。由于此错误，模型无法仿真。仍然可以打开模块参数对话框并查看参数值。

请改用接口专用模块：

- Serial Configuration
- Serial Receive
- Serial Send
- TCP/IP Receive
- TCP/IP Send
- UDP Receive
- UDP Send
- VISA

与 Query Instrument 和 To Instrument 相比，这些接口专用模块均支持附加属性并具有改进的性能。

### R2023b：将被移除

Query Instrument 和 To Instrument 模块将在未来版本中移除。

## 描述

（将被移除）将仿真数据发送到仪器

To Instrument 模块配置并打开与仪器的接口，初始化仪器，并将数据发送到仪器。配置和初始化在模型执行开始时进行。模块在模型运行期间将数据发送到仪器。

该模块没有输出端口。该模块有一个输入端口，对应发送到仪器的数据。此数据类型必须为双精度。

**注意**

To Instrument 模块可用于以下接口：VISA、GPIB、Serial、TCP/IP 和 UDP。以下接口不支持：SPI、I2C 和 Bluetooth。

### 其他支持的功能

- 此模块支持使用加速模式，但不支持 Rapid Accelerator 或代码生成。
- 此模块支持使用模型引用，因此您的模型可以将其他 Simulink® 模型作为模块化组件包含在内。

有关这些功能的详细信息，请参阅 Simulink 文档。
