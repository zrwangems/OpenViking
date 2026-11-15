---
type: simulink-block
title: 'AXI Manager Read'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'HDL Verifier Supported Hardware / Intel FPGA Boards / AXI Manager'
documentation_page: 'aximanagerread'
documentation_source_path: 'ref/aximanagerread.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI Manager Read

## 端口

### 输出

### **data** — 从 FPGA 板读取的数据 标量 | 向量

从 FPGA 板读取的数据，以标量或向量形式返回。输出大小为 1×*`N`*，其中 *`N`* 是 **Output vector size** 参数值。**Output data type** 参数设置此输出的数据类型。从 FPGA 读取的数据的类型为 `uint32`、`int32`、`uint64` 或 `int64`，具体取决于 FPGA 上 AXI manager IP 的数据宽度。该模块将数据类型转换为 **Output data type** 参数指定的值。

**数据类型：** `uint8` | `int8` | `uint16` | `int16` | `half` | `uint32` | `int32` | `single` | `uint64` | `int64` | `double` | `fixed point`

## 参数

### 主要

### **Address** — 读取操作的起始地址 `0` (默认) | 非负整数，4 或 8 的倍数 | 非负十六进制值，4 或 8 的倍数

将读取操作的起始地址指定为非负整数或十六进制值。该模块支持 32、40 和 64 位的地址宽度。该模块根据 AXI manager IP 地址宽度将地址数据类型转换为 `uint32` 或 `uint64`。该地址必须指向由 FPGA 板上的 AXI manager IP 控制的 AXI 从属内存位置。

**内存映射指南**

- 如果 AXI manager IP 数据宽度为 32 位，则内存按 4 字节对齐，每个地址以 4 字节递增（`0x0`、`0x4`、`0x8`）。例如，地址 `0x1` 会返回错误。
- 如果 AXI manager IP 数据宽度为 64 位，则内存按 8 字节对齐，每个地址以 8 字节递增（`0x0`、`0x8`、`0x10`）。例如，指定地址 `0x1` 或 `0x4` 都无效，并会返回错误。
- 如果 AXI manager IP 数据宽度为 32 位，且 **Burst type** 参数设置为 `Increment`，则该模块将地址递增 4 字节。
- 如果 AXI manager IP 数据宽度为 64 位，且 **Burst type** 参数设置为 `Increment`，则该模块将地址递增 8 字节。
- 如果 AXI manager IP 数据宽度为 32 位，且 **Output data type** 参数设置为 `half`，则该模块读取低 2 字节并忽略高 2 字节。
- 如果 AXI manager IP 数据宽度为 64 位，且 **Output data type** 参数设置为 `half`，则该模块读取低 2 字节并忽略高 6 字节。
- 不要使用 64 位 AXI manager IP 访问 32 位寄存器。

**示例：** `0xa4`

### **Burst type** — AXI4 突发类型 `Increment` (默认) | `Fixed`

在 `Increment` 模式下，AXI manager 从指定地址开始的连续内存空间读取数据向量。在 `Fixed` 模式下，AXI manager 从同一地址读取所有数据。

**注意**

PCI Express® 接口不支持 `Fixed` 突发类型。请改用 `Increment` 突发类型。

### **Output data type** — 输出数据的数据类型 `uint32` (默认) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `fixdt(1,16,0)` | `<data type expression>`

该模块将从 FPGA 读出的数据转换为指定的数据类型。

### **Output vector size** — 要读取的内存位置数 `1` (默认) | 正整数

指定该模块要读取的内存位置数。默认情况下，该模块从连续地址块读取，并在每次操作时递增地址。要关闭地址递增模式并从同一位置重复读取，请将 **Burst type** 参数设置为 `Fixed`。

当您指定较大的操作大小（例如读取一块双倍数据速率 (DDR) 内存）时，该模块会自动将操作分解为多个突发，并使用支持的最大突发大小。支持的最大突发大小为 256 个字。

### **Sample time** — 读取采样时间 `-1` (默认) | 正标量

指定该模块的仿真采样时间。当您指定 `-1` (默认) 时，该模块从系统中的其他模块继承采样时间。

### **Vector register data with strobe synchronization** — 使用选通同步从寄存器读取数据 `off` (默认) | `on`

要启用使用选通同步从一组寄存器读取数据，请选择此参数。当您的 FPGA 设计包含由 HDL Coder™ 生成的选通同步时，请启用此参数。有关选通同步的详细信息，请参阅 IP Core User Guide (HDL Coder) 中的 “Vector Data Read/Write with Strobe Synchronization” 部分。

### **Strobe address** — 用于选通同步的选通地址 `0` (默认) | 非负整数，4 或 8 的倍数 | 非负十六进制值，4 或 8 的倍数

设置由 HDL Coder 生成的选通的绝对地址。绝对地址是基地址与 IP core 报告提供的选通偏移量之和。

**示例：** 如果基地址为 `0x41000000`，偏移量为 `0x110`，则绝对地址为 `0x41000110`。

#### 依赖关系

要启用此参数，请选择 **Vector register data with strobe synchronization**。

### 接口

### **Type** — 用于与 FPGA 板通信的接口类型 `JTAG` (默认) | `PCIe` | `PL Ethernet` | `PS Ethernet` | `USB Ethernet`

指定用于主机与 FPGA 之间通信的接口类型。

**注意**

AXI manager 仅对 AMD® Zynq® 设备支持 PS Ethernet 和 USB Ethernet 接口。

### AXI Manager 接口配置

要查看这些参数，请点击 **Configure global parameters** 打开 AXI Manager 接口配置对话框。可见参数取决于 **Type** 参数值。

全局参数应用于整个 Simulink® 模型。

### **Vendor** — FPGA 品牌名称 `Intel` | `AMD`

指定 FPGA 板的制造商。AXI manager IP 因 FPGA 板类型而异。

#### 依赖关系

要启用此参数，请点击 **Configure global parameters**。

### **AXI data width** — FPGA 上 AXI manager IP 的数据宽度 `32` (默认) | `64`

选择 FPGA 上 AXI manager IP 的数据宽度（以位为单位）。

对于 PCI Express、PS Ethernet 或 USB Ethernet，将此值设置为 `32`。对于 JTAG 或 PL Ethernet，将此值设置为 `32` 或 `64`。

#### 依赖关系

要启用此参数，请点击 **Configure global parameters**。

### **Cable type** — 用于与 FPGA 板通信的 JTAG 线缆类型（仅 AMD） `auto` (默认) | `FTDI`

指定用于与 FPGA 板通信的 JTAG 线缆类型。当主机连接了多个线缆时，请使用此参数。

当您将此参数设置为 `auto` (默认) 时，该模块会自动检测 JTAG 线缆类型。该模块优先搜索 Digilent® 线缆，并使用以下过程检测线缆类型。

1. AXI Manager Write 模块搜索 Digilent 线缆。如果该模块找到：

   - 恰好一根 Digilent 线缆，则它使用该线缆与 FPGA 板通信。
   - 多于一根 Digilent 线缆 – 它会返回错误。要解决此错误，请使用 **Cable name** 参数指定所需的线缆。
   - 没有 Digilent 线缆，则它搜索 FTDI 线缆。
2. 如果未找到 Digilent 线缆，AXI Manager Write 模块会搜索 FTDI 线缆。如果该模块找到：

   - 恰好一根 FTDI 线缆，则它使用该线缆与 FPGA 板通信。
   - 多于一根 FTDI 线缆，它会返回错误 – 要解决此错误，请使用 **Cable name** 参数指定所需的线缆。
   - 没有 FTDI 线缆，它会返回错误 – 要解决此错误，请连接一根 Digilent 或 FTDI 线缆。
3. 如果它找到两根类型不同的线缆，则会优先使用 Digilent 线缆。要使用 FTDI 线缆，请将此参数设置为 `FTDI`。

当您将此参数设置为 `FTDI` 时，该模块会搜索 FTDI 线缆。如果该对象找到：

- 恰好一根 FTDI 线缆，则它使用该线缆与 FPGA 板通信。
- 多于一根 FTDI 线缆，它会返回错误 – 要解决此错误，请使用 **Cable name** 参数指定所需的线缆。
- 没有 FTDI 线缆，它会返回错误 – 要解决此错误，请连接一根 Digilent 或 FTDI 线缆。

有关更多详细信息，请参阅 Select from Multiple JTAG Cables for AMD Boards。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Cable name** — 用于与 FPGA 板通信的 JTAG 线缆名称 `auto` (默认) | 已连接 JTAG 线缆的名称

如果主机连接了多根相同类型的 JTAG 线缆，请指定此参数。如果主机连接了多根 JTAG 线缆，而您未指定此参数，则该模块会返回错误。错误消息包含可用 JTAG 线缆的名称。有关更多详细信息，对于 Intel® 板，请参阅 Select from Multiple JTAG Cables for Intel Boards。对于 AMD 板，请参阅 Select from Multiple JTAG Cables for AMD Boards。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`。

### **Clock frequency in MHz** — JTAG 时钟频率 `15` (默认) | 正标量

指定 JTAG 时钟频率，以 MHz 为单位。JTAG 频率取决于线缆类型以及 FPGA 板支持的最大时钟频率。请查看板文档以了解支持的频率范围。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`。

### **Chain position** — FPGA 在 JTAG 链中的位置（仅 AMD） `auto` (默认) | 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 设备，请将此参数值指定为非负整数。否则，请选择 `auto` (默认) 以自动检测链位置。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Instruction registers before FPGA** — 目标 FPGA 之前所有设备的指令寄存器长度之和（仅 AMD） `0` (默认) | 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 设备，请将此参数值指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Instruction registers after FPGA** — 目标 FPGA 之后所有设备的指令寄存器长度之和（仅 AMD） `0` (默认) | 非负整数

如果 JTAG 链上有多个 FPGA 或 Zynq 设备，请将此参数值指定为非负整数。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `JTAG`，并将 **Vendor** 设置为 `AMD`。

### **Device address** — FPGA 板上 Ethernet 端口或 USB Ethernet gadget 的 IP 地址 点分四段值

指定 FPGA 板上 Ethernet 端口或 USB Ethernet gadget 的 IP 地址。目标 IP 地址必须是由点分隔的四组数字，每组数字由 [0, 255] 范围内的整数组成。PL Ethernet 或 PS Ethernet 接口的默认 IP 地址为 `192.168.0.2`。USB Ethernet 接口的默认 IP 地址为 `192.168.1.2`。

**示例：** `192.168.0.10`

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `PL Ethernet`、`PS Ethernet` 或 `USB Ethernet`。

### **Port** — FPGA 板的 UDP 端口号 `50101` (默认) | 255 到 65,535 的整数

将目标 FPGA 的用户数据报协议 (UDP) 端口号指定为 255 到 65,535 的整数。

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

### R2024a：支持 USB Ethernet

AXI Manager Read 模块支持 AMD Zynq 板的 USB Ethernet 接口。要使用此接口，请在 **接口** 选项卡上，将 **Type** 设置为 `USB Ethernet`。

### R2024a：PL Ethernet 或 PS Ethernet 取代 Ethernet 接口

PL Ethernet 或 PS Ethernet 接口取代了 Ethernet 接口。要选择 Ethernet 接口，请在 **接口** 选项卡上，根据您的硬件板将 **Type** 设置为 `PL Ethernet` 或 `PS Ethernet`。`Ethernet` 接口类型已移除。

### R2023b：UDP 重命名为 Ethernet

UDP 接口已重命名为 Ethernet 接口。要选择 Ethernet 接口，请在 **接口** 选项卡上，将 **Type** 设置为 `Ethernet`。`UDP` 接口类型已移除。

### R2023a：支持 half 数据类型

该模块从 FPGA 板上的内存位置读取 `half` 数据。读取操作的地址必须指向由 FPGA 板上的 AXI manager IP 控制的 AXI 从属内存位置。

- 如果 AXI manager IP 数据宽度为 32 位，则内存按 4 字节对齐，地址以 4 字节递增（`0x0`、`0x4`、`0x8`）。在这种情况下，该模块读取低 2 字节并忽略高 2 字节。
- 如果 AXI manager IP 数据宽度为 64 位，则内存按 8 字节对齐，地址以 8 字节递增（`0x0`、`0x8`、`0x10`）。在这种情况下，该模块读取低 2 字节并忽略高 6 字节。

### R2022a：AXI Master Read 重命名为 AXI Manager Read

AXI Master Read 模块已重命名为 AXI Manager Read 模块。在软件和文档中，术语 "manager" 和 "subordinate" 分别取代 "master" 和 "slave"。

在 R2022a 中，您不能使用包含 AXI Master Read 模块的 Simulink 模型。请在 R2022a 中使用 AXI Manager Read 模块重新创建您的模型。

## 描述

从 Simulink 读取 FPGA 板上的内存位置

AXI Manager Read 模块在 FPGA 板上运行时与 AXI manager IP 通信。该模块将读取命令转发到 IP，以访问 FPGA 板上的内存映射位置。

**注意**

AXI Master Read 模块已重命名为 AXI Manager Read 模块。有关更多信息，请参阅版本历史。

使用此模块之前，您必须创建 AXI manager IP 并将其集成到您的 FPGA 设计中。有关更多信息，请参阅 Set Up AXI Manager。
