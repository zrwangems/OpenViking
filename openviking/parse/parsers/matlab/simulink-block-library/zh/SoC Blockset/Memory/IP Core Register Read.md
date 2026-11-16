---
type: simulink-block
title: 'IP Core Register Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory'
documentation_page: 'ipcoreregisterread'
documentation_source_path: 'ref/ipcoreregisterread.html'
language: zh-CN
chinese_source: worker-translation
---

# IP Core Register Read

## 端口

### 输出

### **data** — 数据输出向量

此端口输出从处理器接收的数据向量，起始于 IP 核基地址的偏移地址。在 Hardware Mapping 工具中设置该偏移地址。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **寄存器名称** — 寄存器的名称 `RegA`（默认）| 字符向量

将此名称与 Register Write 模块中指定的 **寄存器名称** 参数匹配。

**示例：** `AddressReg1`

### **输出数据类型** — 输出数据的数据类型 `uint16`（默认）| `single` | `int8` | `uint8` | `int16` | `int32` | `uint32` | `boolean` | `fixed point data type`

选择输出数据的数据类型。此值必须与为 Register Write 模块选择的值匹配。

### **输出向量大小** — 输出数据的向量大小 `1`（默认）| 正整数

将输出数据的向量大小指定为正整数。此值必须与为 Register Write 模块选择的值匹配。

### **采样时间** — 采样的仿真间隔 `-1`（默认）| 非负标量

指定模块输出数据的离散时间间隔，以 seconds 为单位。如果此值为 `-1`（默认），则采样时间从模型继承。

## 所属库

SoC Blockset / Memory

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

若要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

对从软件到硬件的寄存器写入进行建模

IP Core Register Read 模块对从处理器到硬件逻辑的写入操作进行建模。该模块接收处理器通过 Register Write 模块发送的数据。您可以在 Hardware Mapping 工具中定义寄存器偏移。
