---
type: simulink-block
title: 'OTAVA DTRX2'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Hardware I/O Devices'
documentation_page: 'otavadtrx2'
documentation_source_path: 'ref/otavadtrx2.html'
language: zh-CN
chinese_source: worker-translation
---

# OTAVA DTRX2

## 端口

### 输入

### **RFIn*`x`*** — RX 输入数据 标量 | 列向量

RX 输入数据，指定为标量或列向量，长度在
[1, *N*] 范围内，其中 *N* 是每个
时钟周期的样本数。

***`x`*** 表示 RX 通道编号。
***`x`*** 的值范围为 1 到 2。
**RFIn** 端口的数量取决于您在模块中启用的 RX 通道数。

**数据类型：** `uint16` | `uint32` | `uint64` | `fixed point`

### **IFIn*`x`*** — TX 输入数据 列向量

TX 输入数据，指定为列向量。

***`x`*** 表示 TX 通道编号。
***`x`*** 的值范围为 1 到 2。
**IFIn** 端口的数量取决于您在模块中启用的 TX 通道数。

**数据类型：** `int16`

### 输出

### **IFOut*`x`*** — RX 输出数据 列向量

RX 输出数据，以列向量形式返回。

***`x`*** 表示 RX 通道编号。
***`x`*** 的值范围为 1 到 2。
**IFOut** 端口的数量取决于您在模块中启用的 RX 通道数。

**数据类型：** `int16` | `uint16`

### **RFOut*`x`*** — TX 输出数据 标量 | 列向量

TX 输出数据，以标量或列向量形式返回，长度在
[1, *N*] 范围内，其中 *N* 是每个
时钟周期的样本数。

***`x`*** 表示 TX 通道编号。
***`x`*** 的值范围为 1 到 2。
**RFOut** 端口的数量取决于您在模块中启用的 TX 通道数。

**数据类型：** `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### RX 通道

### **启用通道 1** — 启用 RX1 通道的选项 `on`（默认） | `off`

选择此参数以启用 RX1 通道。

### **启用通道 2** — 启用 RX2 通道的选项 `on`（默认） | `off`

选择此参数以启用 RX2 通道。

### **中心频率 (GHz)** — RX 通道的中心频率 `27.5`（默认） | 范围 [19, 31] 内的有限标量

将 RX 通道的中心频率指定为范围
[19, 31] 内的有限标量。

### **中频 (GHz)** — RX 通道的 IF `3.7`（默认） | 范围 [3.4, 4.3] 内的有限标量

将 RX 通道的中频 (IF) 指定为范围 [3.4, 4.3] 内的有限标量。

### **IF 信号带宽 (MHz)** — IF 信号的带宽 `50`（默认） | 最大为 800 的有限标量

将 IF 信号的带宽以 MHz 为单位指定为最大为 800 的有限标量。

### **IF DSA 衰减 (dB)** — IF DSA 的衰减 `31`（默认） | 范围 [0, 31] 内的有限标量

将 IF 数字步进衰减器 (DSA) 的衰减指定为范围 [0, 31] 内的有限标量。
您可以将此参数的值增大或减小，步长为 1。

### **RF DSA 衰减 (dB)** — RF DSA 的衰减 `14`（默认） | 范围 [0, 14] 内的有限标量

将射频 (RF) DSA 的衰减指定为范围 [0, 14] 内的有限标量。
您可以将此参数的值增大或减小，步长为 2。

### **启用 IF LNA** — 启用 IF LNA 的选项 `on`（默认） | `off`

选择此参数以启用 IF 低噪声放大器 (LNA)。

### **启用 RF LNA** — 启用 RF LNA 的选项 `on`（默认） | `off`

选择此参数以启用 RF LNA。

### TX 通道

### **启用通道 1** — 启用 TX1 通道的选项 `on`（默认） | `off`

选择此参数以启用 TX1 通道。

### **启用通道 2** — 启用 TX2 通道的选项 `on`（默认） | `off`

选择此参数以启用 TX2 通道。

### **中心频率 (GHz)** — TX 通道的中心频率 `27.5`（默认） | 范围 [19, 31] 内的有限标量

将 TX 通道的中心频率指定为范围
[19, 31] 内的有限标量。

### **中频 (GHz)** — TX 通道的 IF `4.3`（默认） | 范围 [3.4, 4.3] 内的有限标量

将 TX 通道的 IF 指定为范围 [3.4,
4.3] 内的有限标量。

### **IF 信号带宽 (MHz)** — IF 信号的带宽 `50`（默认） | 最大为 800 的有限标量

将 IF 信号的带宽以 MHz 为单位指定为最大为 800 的有限标量。

### **DSA 衰减 (dB)** — DSA 的衰减 `15`（默认） | 范围 [0, 15] 内的有限标量

将 DSA 的衰减指定为范围 [0, 15] 内的有限标量。
您可以将此参数的值增大或减小，步长为 1。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / RFSoC / ZCU208

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。

## 版本历史

**在 R2023a 中引入**

## 描述

将 OTAVA DTRX2 毫米波无线电卡与 ZCU208 板集成

OTAVA DTRX2 模块将 OTAVA DTRX2 毫米波无线电卡与
Xilinx®
Zynq®
UltraScale+™ RFSoC ZCU208 Evaluation Kit 集成。该模块在
毫米波 (mmWave) 频段提供 RF 前端接口，以便在 ZCU208
板上实现您的 RF 应用。

该模块支持 19 至 31 GHz 范围内的毫米波频段。使用此模块可
面向 5G、雷达和 Ka 或 Ku 频段卫星通信中的应用。

该模块通过
**IFIn***`x`* 端口接受 *N* 个样本的向量，并通过
**RFOut***`x`* 端口输出长度为 [1, *N*] 范围内的列向量形式的 16 位样本。
*N* 是每个时钟周期的样本数，*`x`* 为 1 或 2。该模块通过
**RFIn***`x`* 端口接受长度为 [1, *N*] 范围内的列向量形式的 16 位
样本，并根据 *N* 的值通过 **IFOut***`x`*
端口输出 *N* 个样本的向量。

在生成时，SoC Builder 工具会映射
DTRX2 无线电卡在硬件上配置的控制路径接口。

该模块最多支持两个发送 (TX) 和两个接收 (RX) 通道。这些
通道对应于 DTRX2 无线电卡的 TX 和 RX 通道。

| 模块通道 | DTRX2 无线电卡通道 |
| --- | --- |
| **IFIn1** - **RFOut1** | TX1 |
| **IFIn2** - **RFOut2** | TX2 |
| **RFIn1** - **IFOut1** | RX1 |
| **RFIn2** - **IFOut2** | RX2 |

要将 OTAVA DTRX2 模块与 RF Data Converter
模块集成，请遵循以下说明。

- 将 TX1 与 **Tile 0** 中的 **DAC 1** 连接。
- 将 TX2 与 **Tile 0** 中的 **DAC 0** 连接。
- 将 RX1 与 **Tile 3** 中的 **ADC 1** 连接。
- 将 RX2 与 **Tile 3** 中的 **ADC 0** 连接。

**注意**

- 当卡电源开关关闭时，不要将任何信号定向到 DTRX2 无线电卡。
  在将该卡作为目标之前，请打开电源开关。
- 为了抑制参考时钟杂散，请在 CLK104 输出与 DTRX2 无线电卡的 REF\_CLK\_IN 输入之间使用 10 dB 同轴衰减器或截止值大于 122.88 MHz 的低通滤波器。
- 使用 50 ohms 2.92 mm 终端端接 DTRX2 无线电卡所有未使用的 RF 通道输入和输出连接器。

有关设置和使用毫米波无线电卡的详细说明，请参阅 Avnet® 网站上的 Wideband mmWave Radio Dev Kit for RFSoC Gen-3。
