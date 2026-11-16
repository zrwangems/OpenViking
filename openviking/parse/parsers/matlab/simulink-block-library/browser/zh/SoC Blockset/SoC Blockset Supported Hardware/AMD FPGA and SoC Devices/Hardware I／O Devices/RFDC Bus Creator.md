---
type: simulink-block
title: 'RFDC Bus Creator'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'rfdcbuscreator'
documentation_source_path: 'ref/rfdcbuscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# RFDC Bus Creator

## 端口

### 输入

### **NCOFrequency** — NCO 混频器的频率标量

用于数控振荡器 (NCO) 混频器的频率，指定为标量。NCO 频率值的范围为
–*F*s/2 到
*F*s/2，其中
*F*s 是以 Hz 为单位的采样率。

该模块将 RF Data Converter 实时接口兼容的 NCO 频率计算为 `NCOFrequency` x
(2*48* /
*F*s)。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`NCO` 或 `NCO and
threshold`。

**数据类型：** `fixdt(1,48,0)`

### **NCOPhase** — NCO 混频器输出的相位值标量

用于 NCO 混频器输出的相位值，指定为标量。NCO 相位值的范围为 –180 到 180 度。

该模块将 RF Data Converter 实时接口兼容的 NCO 相位计算为 `NCOPhase` x
(2*18* / 360)。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`NCO` 或 `NCO and
threshold`。

**数据类型：** `fixdt(1,18,0)`

### **NCOPhaseReset** — 重置 NCO 相位偏移的控制信号 `Boolean` 标量

重置 NCO 相位偏移的控制信号，指定为 Boolean
标量。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`NCO` 或 `NCO and
threshold`。

**数据类型：** `Boolean`

### **NCOUpdateEnable** — 确定要更新哪些 NCO 频率和相位位的控制信号，标量

确定要更新哪些 NCO 频率和相位位的控制信号，
指定为标量。将此信号中的位设置为 `High`，以更新
NCO 的频率和相位值的以下位。

- 位 5 — 将相位偏移重置为 `0`
- 位 4 — `NCOPhase[17:16]`
- 位 3 — `NCOPhase[15:0]`
- 位 2 — `NCOFrequency[47:32]`
- 位 1 — `NCOFrequency[31:16]`
- 位 0 — `NCOFrequency[15:0]`

例如，如果仅将
**NCOUpdateEnable** 的位 1 和位 0
设置为 `High`，则在更新事件中仅
NCO 频率的值会更新。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`NCO` 或 `NCO and
threshold`。

**数据类型：** `fixdt(0,6,0)`

### **PLEvent** — 清除阈值状态信号的控制信号 `Boolean` 标量

清除阈值状态信号的控制信号，指定为 Boolean
标量。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`Threshold` 或 `NCO and
threshold`。

**数据类型：** `Boolean`

### **clearOverRange** — 清除超范围信号的控制信号 `Boolean` 标量

清除超范围信号的控制信号，指定为 Boolean
标量。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`Threshold` 或 `NCO and
threshold`。

**数据类型：** `Boolean`

### **clearOverVoltage** — 清除过压信号的控制信号 `Boolean` 标量

清除过压信号的控制信号，指定为 Boolean
标量。

#### 依赖关系

要启用此端口，请将 **Control type** 设置为
`Threshold` 或 `NCO and
threshold`，并选择 **Gen 3**。

**数据类型：** `Boolean`
### 输出

### **ctrlBus** — 输出控制总线 总线

输出控制总线，以总线形式返回。

**数据类型：** `DUT2RFDCRealTimeCtrlBusObj`

## 参数

### **Control type** — 控制类型选择 `NCO`（默认） | `Threshold` | `NCO and threshold`

指定控制类型。

- `NCO` — 将 DUT NCO 控制信号连接到
  RF Data
  Converter 模块。
- `Threshold` — 将 DUT 阈值控制
  信号连接到 RF Data Converter 模块。
- `NCO and threshold` — 将 DUT NCO 和
  阈值控制信号连接到 RF Data Converter 模块。

该模块的输入端口根据您选择的 **Control
type** 类型而变化。有关更多详细信息，请参阅描述。

### **Gen 3** — 为 Gen 3 设备添加端口的选项 `off`（默认） | `on`

选择此参数可为 Gen 3 Zynq®
UltraScale+™ RFSoC 设备添加端口。

#### 依赖关系

要启用此参数，请将 **Control type** 设置为
`Threshold` 或 `NCO and
threshold`。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU111 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU216 SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU670

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用
SoC Builder
工具。

## 版本历史

**在 R2022a 中引入**

## 描述

将控制信号转换为 RF Data Converter 实时接口兼容总线

RFDC Bus Creator 模块将一组控制信号组合成
RF Data Converter 实时接口兼容总线。该模块接受
控制信号并输出总线。

此模块的端口配置因您选择控制类型而异。

| 参数配置 | 启用的输入端口 |
| --- | --- |
| 将 **Control type** 设置为 `NCO`。 | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| 将 **Control type** 设置为 `Threshold`。 | **PLEvent** |
| **clearOverRange** |
| 将 **Control type** 设置为 `Threshold` 并选择 **Gen 3**。 | **PLEvent** |
| **clearOverRange** |
| **clearOverVoltage** |
| 将 **Control type** 设置为 `NCO and threshold`。 | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| **PLEvent** |
| **clearOverRange** |
| 将 **Control type** 设置为 `NCO and threshold` 并选择 **Gen 3**。 | **NCOFrequency** |
| **NCOPhase** |
| **NCOPhaseReset** |
| **NCOUpdateEnable** |
| **PLEvent** |
| **clearOverRange** |
| **clearOverVoltage** |
