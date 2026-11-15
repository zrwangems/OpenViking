---
type: simulink-block
title: 'Aurora 64B66B'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'aurora64b66b'
documentation_source_path: 'ref/aurora64b66b.html'
language: zh-CN
chinese_source: worker-translation
---

# Aurora 64B66B

## 端口

### 输入

### **M\_AXIS\_wrReady** — 来自下游接口的就绪信号 `0` | `1`

控制信号，指示模块是否可以向该下游接口发送流数据。当该值为 `1`（`true`）时，下游模块已准备好接收数据。

**数据类型：** `Boolean`

### **S\_AXIS\_rdData** — 输入流数据标量

来自数据源的输入流数据。将此值指定为标量。

**数据类型：** `uint64`

### **S\_AXIS\_rdValid** — 有效输入流数据的指示 `0` | `1`

控制信号，指示来自数据源的输入数据是否有效。当该值为 `1`（`true`）时，模块接受 **S\_AXIS\_rdData** 输入端口上的值。当该值为 `0`（`false`）时，模块忽略 **S\_AXIS\_rdData** 输入端口上的值。

**数据类型：** `Boolean`

### **S\_AXIS\_rdLast** — 突发中最后一个节拍的指示 `0` | `1`

控制信号，指示来自上游 IP 的数据的最后一个节拍。

**数据类型：** `Boolean`

### **loopback** — 环回模式选择标量

选择环回模式。

- `0` — 模块不环回发送的数据。
- `2` — 模块将发送的数据环回到收发器中。

有关环回模式的更多信息，请参阅 Xilinx 网站上的 UltraScale Architecture GTY Transceivers。

**数据类型：** `fixdt(0,3,0)`

### 输出

### **M\_AXIS\_wrData** — 输出流数据标量

输出到下游目标 IP 的流数据。

**数据类型：** `uint64`

### **M\_AXIS\_wrValid** — 有效输出流数据的指示 `0` | `1`

控制信号，指示输出流数据是否有效。当该值为 `1`（`true`）时，模块在 **M\_AXIS\_wrData** 输出端口上返回有效数据。当该值为 `0`（`false`）时，**M\_AXIS\_wrData** 输出端口上的值无效。

**数据类型：** `Boolean`

### **M\_AXIS\_wrLast** — 突发中最后一个节拍的指示 `0` | `1`

控制信号，指示输出流数据现在具有突发的最后一个节拍数据。

**数据类型：** `Boolean`

### **S\_AXIS\_rdReady** — 到上游接口的就绪信号 `0` | `1`

控制信号，指示模块是否可以从上游接口接收流数据。

**数据类型：** `Boolean`

## 参数

### **Simulate using** — 仿真模式选择 `Code generation`（默认） | `Interpreted execution`

选择仿真模式。

- `Code generation` — 在首次模型运行时，为模块进行仿真并生成代码。如果模块的结构不发生变化，后续模型运行不会重新生成代码。
- `Interpreted execution` — 使用 MATLAB® 执行引擎仿真模块。选择此选项可能会降低仿真性能。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成：使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2023a 中引入**

## 描述

使用 Xilinx Aurora 接口提供高速串行通信

Aurora 64B66B 模块使用 Xilinx® Aurora 64B/66B 内核提供高速串行通信。

有关 Aurora 64B/66B 内核的更多信息，请参阅 Xilinx 网站上的 Aurora 64B/66B。
