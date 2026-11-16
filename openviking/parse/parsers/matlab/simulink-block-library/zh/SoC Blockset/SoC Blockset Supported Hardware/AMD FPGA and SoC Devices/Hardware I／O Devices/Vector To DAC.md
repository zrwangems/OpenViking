---
type: simulink-block
title: 'Vector To DAC'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'vectortodac'
documentation_source_path: 'ref/vectortodac.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector To DAC

## 端口

### 输入

### **vectorData** — 向量形式的 DAC 数据采样

DAC 数据采样，指定为列向量。该输入必须是 *N* 个采样的 *N* 元素列向量，其中第一个采样是较低有效位 (LSB)，最后一个采样是最高有效位 (MSB)。*N* 是由 **Shortened input word length** 参数设置的输入字长度。

**数据类型：** `int16` | `uint16`
### 输出

### **dacData** — DAC 数据采样，标量

DAC 数据采样，以标量形式返回。该模块返回 *N* x 16 bit 输出采样，其中 *N* 是由 **Shortened input word length** 参数设置的输入字长度。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Shortened input word length** — 输入字长度 `16` (default) | 1 到 16 的整数

将输入字长度指定为 1 到 16 的整数。该参数设置所需的输入向量大小以及输出采样的 bit 宽度。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2020b 中引入**

## 描述

将向量输入转换为拼接的 16-bit DAC 输出采样

Vector To DAC 模块将向量输入转换为拼接的 16-bit 数模转换器 (DAC) 输出采样。

该模块通过 **vectorData** 输入端口接受 *N* 个采样的向量，并根据 *N* 值通过 **dacData** 输出端口输出打包为 *N* x 16 bits 的 16-bit 采样。*N* 是输入字的长度。
