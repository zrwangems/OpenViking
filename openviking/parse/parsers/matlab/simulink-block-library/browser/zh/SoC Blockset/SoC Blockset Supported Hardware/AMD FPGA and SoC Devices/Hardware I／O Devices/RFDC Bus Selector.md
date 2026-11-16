---
type: simulink-block
title: 'RFDC Bus Selector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdcbusselector'
documentation_source_path: 'ref/rfdcbusselector.html'
language: zh-CN
chinese_source: worker-translation
---

# RFDC Bus Selector

## 端口

### 输入

### **ctrlBus** — 输入控制总线 bus

输入控制总线，指定为总线。

**数据类型：** `RFDC2DUTRealTimeCtrlBusObj`
### 输出

### **overRange** — 超范围输出 `Boolean` 标量

超范围输出，以 Boolean 标量形式返回。此输出上的 `High` 表示信号超过数模转换器 (DAC) 或模数转换器 (ADC) 的满量程输入。

**数据类型：** `Boolean`

### **overThreshold1** — 超过阈值 1 输出 `Boolean` 标量

超过阈值 1 输出，以 Boolean 标量形式返回。此输出上的 `High` 表示信号幅度电平超过 RF Data Converter 模块中的 **Threshold1** 参数指定的阈值。

**数据类型：** `Boolean`

### **overThreshold2** — 超过阈值 2 输出 `Boolean` 标量

超过阈值 2 输出，以 Boolean 标量形式返回。此输出上的 `High` 表示信号幅度电平超过 RF Data Converter 模块中的 **Threshold2** 参数指定的阈值。

**数据类型：** `Boolean`

### **overVoltage** — 过压输出 `Boolean` 标量

过压输出，以 Boolean 标量形式返回。当信号远超正常工作输入范围时，会发生 `Over Voltage` 条件。有关详细信息，请参阅 Xilinx® 文档中的 Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3。

**数据类型：** `Boolean`

### **commonmodeOverVoltage** — 共模过压输出 `Boolean` 标量

共模过压输出，以 Boolean 标量形式返回。此输出上的 `High` 表示输入信号共模超过安全操作条件。有关详细信息，请参阅 Xilinx® 文档中的 Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3。

#### 依赖关系

要启用此端口，请选择 **Gen 3**。

**数据类型：** `Boolean`

### **commonmodeUnderVoltage** — 共模欠压输出 `Boolean` 标量

共模欠压输出，以 Boolean 标量形式返回。此输出上的 `High` 表示输入信号共模对于安全操作而言过低。有关详细信息，请参阅 Xilinx® 文档中的 Zynq UltraScale+ RFSoC RF Data Converter v2.6 Gen 1/2/3。

#### 依赖关系

要启用此端口，请选择 **Gen 3**。

**数据类型：** `Boolean`

## 参数

### **Gen 3** — 为 Gen 3 设备添加端口的选项 `off`（默认）| `on`

选择此参数可为 Gen 3 Zynq® UltraScale+™ RFSoC 设备添加端口。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2022a 中引入**

## 描述

将 RF Data Converter 实时接口兼容总线转换为控制信号

RFDC Bus Selector 模块将 RF Data Converter 实时接口兼容总线分离为一组控制信号。该模块接受总线并输出控制信号。
