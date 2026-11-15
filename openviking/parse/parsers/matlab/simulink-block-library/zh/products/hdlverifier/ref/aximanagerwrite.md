---
type: simulink-block
title: 'AXI Manager Write'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'HDL Verifier Supported Hardware / Intel FPGA Boards / AXI Manager'
documentation_page: 'aximanagerwrite'
documentation_source_path: 'ref/aximanagerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI Manager Write

## 端口

### 输入

### **data** — 要写入 FPGA 板的数据字 scalar | vector

要写入 FPGA 板的输入数据，指定为标量或向量。在将写请求发送到 FPGA 之前，该模块会将输入数据转换为 `uint32`、`int32`、`uint64` 或 `int64`。数据类型转换遵循以下规则。

- 如果输入数据为 `double` 类型，则该模块会根据 AXI manager IP 的数据宽度将数据转换为 `int32` 或 `int64` 类型。
- 如果输入数据为 `single` 类型，则该模块会根据 AXI manager IP 数据宽度将数据转换为 `uint32` 或 `uint64` 类型。
- 如果输入数据为 `half` 类型，则该模块会将数据转换为 `uint16` 类型，然后根据 AXI manager IP 数据宽度将数据打包为 `uint32` 或 `uint64` 类型。
- 如果输入数据类型的位宽小于 AXI manager IP 数据宽度，则数据会扩展到 AXI manager IP 数据宽度的宽度。
- 如果输入数据类型的位宽大于 AXI manager IP 数据宽度，则该模块会将数据转换为 `int32`、`uint32`、`int64`、`uint64` 类型，以匹配 AXI manager IP 的数据宽度以及原始数据类型的符号性。
- 如果输入数据为定点数据类型，则该模块写入数据的存储整数值。

当您指定较大的操作大小（例如写入一块 double data rate (DDR) 内存）时，该模块会自动将该操作拆分为多个 burst，并使用最大支持的 burst 大小。最大支持的 burst 大小为 256 words。

**数据类型：** `uint8` | `int8` | `uint16` | `int16` | `half` | `uint32` | `int32` | `single` | `uint64` | `int64` | `double` | `fixed point`

## 参数

### 主要

### **Address** — 写操作的起始地址 `0`（默认）| 为 4 或 8 的倍数的非负整数 | 为 4 或 8 的倍数的非负十六进制值

将写操作的起始地址指定为非负整数或十六进制值。该模块支持 32、40 和 64 bits 的地址宽度。该模块会根据 AXI manager IP 地址宽度将地址数据类型转换为 `uint32` 或 `uint64`。该地址必须指向由 FPGA 板上的 AXI manager IP 控制的 AXI subordinate 内存位置。

**内存映射指南**

- 如果 AXI manager IP 数据宽度为 32 bits，则内存按 4 bytes 对齐，并且每个地址以 4-byte 递增（`0x0`、`0x4`、`0x8`）。例如，地址 `0x1` 会返回错误。
- 如果 AXI manager IP 数据宽度为 64 bits，则内存按 8 bytes 对齐，并且每个地址以 8-byte 递增（`0x0`、`0x8`、`0x10`）。例如，指定地址 `0x1` 或 `0x4` 都是无效的，并会返回错误。
- 如果 AXI manager IP 数据宽度为 32 bits 且 **Burst type** 参数设置为 `Increment`，则该模块将地址递增 4 bytes。
- 如果 AXI manager IP 数据宽度为 64 bits 且 **Burst type** 参数设置为 `Increment`，则该模块将地址递增 8 bytes。
- 如果 AXI manager IP 数据宽度为 32 bits 且输入数据为 `half`，则该模块将数据写入低 2 bytes，并用零填充高 2 bytes。
- 如果 AXI manager IP 数据宽度为 64 bits 且输入数据为 `half`，则该模块将数据写入低 2 bytes，并用零填充高 6 bytes。
- 不要使用 64-bit AXI manager IP 来访问 32-bit 寄存器。

**示例：** `0xa4`

### **Burst type** — AXI4 burst 类型 `Increment`（默认）| `Fixed`

在 `Increment` 模式下，AXI manager 将数据向量写入从指定地址开始的连续内存空间。在 `Fixed` 模式下，AXI manager 将所有数据写入同一地址。

**注意**

`Fixed` burst 类型不支持 PCI Express® 接口。请改用 `Increment` burst 类型。

### **Vector register data with strobe synchronization** — 通过 strobe 同步将数据写入寄存器 `off`（默认）| `on`

要启用通过 strobe 同步将数据写入一组寄存器，请选择此参数。当您的 FPGA 设计包含由 HDL Coder™ 生成的 strobe 同步时，请启用此参数。有关 strobe 同步的详细信息，请参阅 IP Core User Guide (HDL Coder) 中的“Vector Data Read/Write with Strobe Synchronization”一节。

### **Strobe address** — 用于 strobe 同步的 strobe 地址 `0`（默认）| 为 4 或 8 的倍数的非负整数 | 为 4 或 8 的倍数的非负十六进制值

设置由 HDL Coder 生成的 strobe 的绝对地址。绝对地址是基地址与 IP core 报告提供的 strobe 偏移量之和。

**示例：** 如果基地址为 `0x41000000`，偏移量为 `0x110`，则绝对地址为 `0x41000110`。

#### 依赖关系

要启用此参数，请选择 **Vector register data with strobe synchronization**。

### 接口

### **Type** — 用于与 FPGA 板通信的接口类型 `JTAG`（默认）| `PCIe` | `PL Ethernet` | `PS Ethernet` | `USB Ethernet`

指定用于在主机和 FPGA 之间通信的接口类型。

**注意**

AXI manager 仅对 AMD® Zynq® 器件支持 PS Ethernet 和 USB Ethernet 接口。

### AXI Manager 接口配置

要查看这些参数，请点击 **Configure global parameters** 打开 AXI Manager 接口配置对话框。可见参数取决于 **Type** 参数值。

全局参数适用于整个 Simulink® 模型。

### **Vendor** — FPGA 品牌名称 `Intel` | `AMD`

指定您的 FPGA 板制造商。AXI manager IP 因 FPGA 板类型而异。

#### 依赖关系

要启用此参数，请点击 **Configure global parameters**。

### **AXI data width** — FPGA 上 AXI manager IP 的数据宽度 `32`（默认）| `64`

选择 FPGA 上 AXI manager IP 的数据宽度，单位为 bits。

对于 PCI Express、PS Ethernet 或 USB Ethernet，请将此值设置为 `32`。对于 JTAG 或 PL Ethernet，请将此值设置为 `32` 或 `64`。

#### 依赖关系

要启用此参数，请点击 **Configure global parameters**。

### **Cable type** — 用于与 FPGA 板通信的 JTAG 电缆类型（仅 AMD）`auto`（默认）| `FTDI`

指定用于与 FPGA 板通信的 JTAG 电缆类型。当主机连接了多根电缆时，请使用此参数。

当您将此参数设置为 `auto`（默认）时，该模块会自动检测 JTAG 电缆类型。该模块优先搜索 Digilent® 电缆，并使用以下过程检测电缆类型。

1. AXI Manager Write 模块搜索 Digilent 电缆。如果该模块找到：

   - 恰好一根 Digilent 电缆，则使用该电缆与 FPGA 板通信。
   - 多于一根 Digilent 电缆 – 则返回错误。要解决此错误，请使用 **Cable name** 参数指定所需的电缆。
   - 没有 Digilent 电缆，则搜索 FTDI 电缆。

2. 如果未找到 Digilent 电缆，则 AXI Manager Write 模块搜索 FTDI 电缆。如果该模块找到：

   - 恰好一根 FTDI 电缆，则使用该电缆与 FPGA 板通信。
   - 多于一根 FTDI 电缆，则返回错误 – 要解决此错误，请使用 **Cable name** 参数指定所需的电缆。
   - 没有 FTDI 电缆，则返回错误 – 要解决此错误，请连接 Digilent 或 FTDI 电缆。

3. 如果找到两种不同类型的电缆，则优先使用 Digilent 电缆。要使用 FTDI 电缆，请将此参数设置为 `FTDI`。

当您将此参数设置为 `FTDI` 时，该模块搜索 FTDI 电缆。如果该对象找到：

- 恰好一根 FTDI 电缆，则使用该电缆与 FPGA 板通信。
- 多于一根 FTDI 电缆，则返回错误 – 要解决此错误，请使用 **Cable name** 参数指定所需的电缆。
- 没有 FTDI 电缆，则返回错误 – 要解决此错误，请连接 Digilent 或 FTDI 电缆。

有关更多详细信息，请参阅 Select from Multiple JTAG Cables for AMD Boards。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Cable name** — 用于与 FPGA 板通信的 JTAG 电缆名称 `auto`（默认）| 已连接 JTAG 电缆的名称

如果主机连接了多根相同类型的 JTAG 电缆，请指定此参数。如果主机连接了多根 JTAG 电缆，而您未指定此参数，则该模块会返回错误。错误消息包含可用 JTAG 电缆的名称。有关更多详细信息，对于 Intel® 板，请参阅 Select from Multiple JTAG Cables for Intel Boards。对于 AMD 板，请参阅 Select from Multiple JTAG Cables for AMD Boards。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`。

### **Clock frequency in MHz** — JTAG 时钟频率 `15`（默认）| 正标量

指定 JTAG 时钟频率，单位为 MHz。JTAG 频率取决于电缆类型以及 FPGA 板支持的最大时钟频率。请查看板文档以了解支持的频率范围。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`。

### **Chain position** — FPGA 在 JTAG 链中的位置（仅 AMD）`auto`（默认）| 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 器件，请将此参数值指定为非负整数。否则，请选择 `auto`（默认）以自动检测链位置。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Instruction registers before FPGA** — 目标 FPGA 之前所有器件的指令寄存器长度之和（仅 AMD）`0`（默认）| 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 器件，请将此参数值指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Instruction registers after FPGA** — 目标 FPGA 之后所有器件的指令寄存器长度之和（仅 AMD）`0`（默认）| 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 器件，请将此参数值指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Device address** — FPGA 板上 Ethernet 端口或 USB Ethernet gadget 的 IP 地址 dotted quad 值

指定 FPGA 板上 Ethernet 端口或 USB Ethernet gadget 的 IP 地址。目标 IP 地址必须是由点分隔的四组数字组成，其中整数范围为 [0, 255]。PL Ethernet 或 PS Ethernet 接口的默认 IP 地址为 `192.168.0.2`。USB Ethernet 接口的默认 IP 地址为 `192.168.1.2`。

**示例：** `192.168.0.10`

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `PL Ethernet`、`PS Ethernet` 或 `USB Ethernet`。

### **Port** — FPGA 板的 UDP 端口号 `50101`（默认）| 从 255 到 65,535 的整数

将目标 FPGA 的用户数据报协议 (UDP) 端口号指定为从 255 到 65,535 的整数。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `PL Ethernet`。

## 所属库

HDL Verifier Support Package for Intel Boards HDL Verifier Support Package for AMD FPGA and SoC Devices

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2024a: 支持 USB Ethernet

AXI Manager Write 模块支持 AMD Zynq 板的 USB Ethernet 接口。要使用此接口，请在 **Interface** 选项卡上，将 **Type** 设置为 `USB Ethernet`。

### R2024a: PL Ethernet 或 PS Ethernet 取代 Ethernet 接口

PL Ethernet 或 PS Ethernet 接口取代了 Ethernet 接口。要选择 Ethernet 接口，请在 **Interface** 选项卡上，根据您的硬件板将 **Type** 设置为 `PL Ethernet` 或 `PS Ethernet`。`Ethernet` 接口类型已移除。

### R2023b: UDP 重命名为 Ethernet

UDP 接口重命名为 Ethernet 接口。要选择 Ethernet 接口，请在 **Interface** 选项卡上，将 **Type** 设置为 `Ethernet`。`UDP` 接口类型已移除。

### R2023a: 支持 half 数据类型

该模块将 `half` 数据写入 FPGA 板上的内存位置。在将写请求发送到 FPGA 之前，该函数将 `half` 数据类型转换为 `uint16`，然后根据 AXI manager IP 数据宽度将数据打包为 `uint32` 或 `uint64`。

写操作的地址必须指向由您 FPGA 板上的 AXI manager IP 控制的 AXI subordinate 内存位置。

- 如果 AXI manager IP 数据宽度为 32 bits，则内存按 4 bytes 对齐，并且地址以 4-byte 递增（`0x0`、`0x4`、`0x8`）。在这种情况下，该模块将数据写入低 2 bytes，并用零填充高 2 bytes。
- 如果 AXI manager IP 数据宽度为 64 bits，则内存按 8 bytes 对齐，并且地址以 8-byte 递增（`0x0`、`0x8`、`0x10`）。在这种情况下，该模块将数据写入低 2 bytes，并用零填充高 6 bytes。

### R2022a: AXI Master Write 重命名为 AXI Manager Write

AXI Master Write 模块已重命名为 AXI Manager Write 模块。在软件和文档中，术语 "manager" 和 "subordinate" 分别取代 "master" 和 "slave"。

在 R2022a 中，您不能使用包含 AXI Master Write 模块的 Simulink 模型。请在 R2022a 中使用 AXI Manager Write 模块重新创建您的模型。

## 描述

从 Simulink 写入 FPGA 板上的内存位置

AXI Manager Write 模块在 FPGA 板上运行时与 AXI manager IP 通信。该模块将写命令转发到 IP，以访问 FPGA 板上的内存映射位置。

**注意**

AXI Master Write 模块已重命名为 AXI Manager Write 模块。有关更多信息，请参阅版本历史。

使用此模块之前，您必须创建 AXI manager IP 并将其集成到您的 FPGA 设计中。有关更多信息，请参阅 Set Up AXI Manager。
