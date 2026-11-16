---
type: simulink-block
title: 'ADC To Vector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'adctovector'
documentation_source_path: 'ref/adctovector.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC To Vector

## 端口

### 输入

### **adcData** — ADC 数据采样标量

ADC 数据采样，指定为标量。此输入的大小必须为
*N* x 16 bits，其中 *N* 是由 **Samples per clock** 参数设置的每个 clock cycle 的采样数。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **vectorData** — 以向量形式表示的 ADC 数据采样 vector

ADC 数据采样，以向量形式返回。该模块将数据返回为
*N* 元素列向量，其中 *N* 是由 **Samples per clock**
参数设置的每个 clock cycle 的采样数。

例如，考虑 *N* = 2 且 **adcData** 端口的输入大小为 32 bits 的情况。在这种情况下，该模块返回向量
[*S*0,
*S*1]，其中
*S*0 是从 **adcData** 端口输入数据的 0 到 15
bits 切片的 16-bit 值，且
*S*1 是从 **adcData** 端口输入数据的 16 到 31
bits 切片的 16-bit 值。

**数据类型：** `int16` | `uint16`

## 参数

### **Samples per clock** — 每个 clock cycle 的采样数 `4`（默认值）| 从 1 到 16 的整数

将每个 clock cycle 的采样数指定为从 1 到 16 的整数。此参数设置输入采样所需的 bit 宽度，并设置输出向量大小。

### **Output data type** — 输出数据类型 `fixdt(1,16,0)`（默认值）| `int16` | `uint16`

将输出数据类型指定为有符号或无符号 fixed point 或整数数据类型。有关如何指定输出数据类型的更多信息，请参阅 Specify Data Types Using Data Type Assistant。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2020b 中引入**

## 描述

将拼接的 16-bit ADC 输入采样转换为向量输出

ADC To Vector 模块将拼接的 16-bit 模数转换器 (ADC) 输入采样转换为向量输出。

该模块接受通过 **adcData** 输入端口打包为 *N* x 16 bits 的 16-bit 采样，并通过 **vectorData** 输出端口输出 *N* 个采样的向量。*N* 是每个 clock cycle 的采样数。
