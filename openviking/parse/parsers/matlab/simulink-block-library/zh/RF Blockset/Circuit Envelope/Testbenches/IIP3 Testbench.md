---
type: simulink-block
title: 'IIP3 Testbench'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'iip3testbench'
documentation_source_path: 'ref/iip3testbench.html'
language: zh-CN
chinese_source: worker-translation
---

# IIP3 Testbench

## 端口

R2025b 中未记录。

## 参数

#### 参数

### **Use Internal Configuration block** — 使用测试平台内部配置模块 on（默认）| off

选择以使用测试平台内部配置模块。清除此参数以指定您自己的配置模块。

**注意**

使用您自己的配置模块时，步长、基频音调、谐波阶数和模拟噪声等参数可能会影响测量结果。

### **Simulate noise (both stimulus and DUT internal)** — 在激励信号中启用噪声建模 on（默认）| off

选择以在进入 DUT 的激励信号中以及 DUT 内部启用噪声建模。

#### 依赖关系

要启用此参数，请选择 **Use internal Configuration block**。

### **Input power amplitude (dBm)** — DUT 的输入功率 `-30`（默认）| 标量

DUT 的输入功率，指定为以 dBm 为单位的标量。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值介于 -90 dBm 和 60 dBm 之间。

### **Input frequency (Hz)** — DUT 的载波频率 `2.1e9`（默认）| 标量

DUT 的载波频率，指定为以 Hz 为单位的标量。输入频率必须大于基带带宽。

### **Output frequency (Hz)** — DUT 的输出频率 `2.1e9`（默认）| 标量

DUT 的输出频率，指定为以 Hz 为单位的标量。输出频率必须大于基带带宽。

### **Baseband bandwidth (Hz)** — 输入信号的基带带宽 `10e6`（默认）| 标量

输入信号的基带带宽，指定为以 Hz 为单位的标量。该值必须大于零。

### **Ratio of test tone frequency to baseband bandwidth** — 测试音调的位置 `1/8`（默认）| 标量

测试音调的位置，指定为标量。

### **Source resistance (Ohm)** — 用于测量 DUT 的源电阻 `50`（默认）| 正有限标量

用于测量 DUT 的源电阻，指定为以欧姆为单位的正有限标量。

### **Load resistance (Ohm)** — 用于测量 DUT 的负载电阻 `50`（默认）| 正有限标量

用于测量 DUT 的负载电阻，指定为以欧姆为单位的正有限标量。

### **Show Response spectrum** — 在仿真期间使用频谱示波器查看响应频谱 on（默认）| off

选择以在仿真期间使用频谱示波器查看响应频谱。

**注意**

要使用 Spectrum Analyzer 查看响应频谱，您需要 DSP System Toolbox™ 许可证。

### **Ground and hide negative terminals** — 在内部接地并隐藏 RF 电路端子 on（默认）| off

选择以在内部接地并隐藏负端子。清除以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量系统的输入三阶截点

使用 `IIP3 Testbench` 测量被测 RF 器件（DUT）的输入三阶截点（IIP3）。
