---
type: simulink-block
title: 'OIP2 Testbench'
family: 'circuit-envelope'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'oip2testbench'
documentation_source_path: 'ref/oip2testbench.html'
language: zh-CN
chinese_source: worker-translation
---

# OIP2 Testbench

## 端口

R2025b 中未记录。

## 参数

#### 参数

### **使用内部 Configuration block** — 使用 testbench 内部 Configuration block on（默认）| off

选择以使用 testbench 内部 Configuration block。清除此参数以指定您自己的 Configuration block。

**注意**

当使用您自己的 Configuration block 时，诸如步长、基波音、谐波阶数和仿真噪声等参数可能会影响测量结果。

### **仿真噪声（激励和 DUT 内部）** — 在激励信号中启用噪声建模 on（默认）| off

选择以在进入 DUT 的激励信号中和 DUT 内部启用噪声建模。

#### 依赖关系

要启用此参数，请选择 **使用内部 Configuration block**。

### **输入功率幅度 (dBm)** — DUT 的输入功率 `-30`（默认）| scalar

输入到 DUT 的功率，指定为以 dBm 为单位的 scalar。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值介于 -90 dBm 和 60 dBm 之间。

### **输入频率 (Hz)** — DUT 的载波频率 `2.1e9`（默认）| scalar

DUT 的载波频率，指定为以 Hz 为单位的 scalar。输入频率必须大于基带带宽。

### **输出频率 (Hz)** — DUT 的输出频率 `2.1e9`（默认）| scalar

DUT 的输出频率，指定为以 Hz 为单位的 scalar。输出频率必须大于基带带宽。

### **基带带宽 (Hz)** — 输入信号的基带带宽 `10e6`（默认）| scalar

输入信号的基带带宽，指定为以 Hz 为单位的 scalar。该值必须大于零。

### **测试音频率与基带带宽之比** — 测试音的位置 `1/8`（默认）| scalar

测试音的位置，指定为 scalar。

### **源电阻 (Ohm)** — 用于测量 DUT 的源电阻 `50`（默认）| positive finite scalar

用于测量 DUT 的源电阻，指定为以 ohms 为单位的 positive finite scalar。

### **负载电阻 (Ohm)** — 用于测量 DUT 的负载电阻 `50`（默认）| positive finite scalar

用于测量 DUT 的负载电阻，指定为以 ohms 为单位的 positive finite scalar。

### **显示响应频谱** — 在仿真期间使用频谱示波器查看响应频谱 on（默认）| off

选择以在仿真期间使用频谱示波器查看响应频谱。

**注意**

要使用 Spectrum Analyzer 查看响应频谱，您需要 DSP System Toolbox™ 许可证。

### **接地并隐藏负极端子** — 在内部接地并隐藏 RF 电路端子 on（默认）| off

选择以在内部接地并隐藏负极端子。清除以暴露负极端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量系统的输出二阶截点

使用 `OIP2 Testbench` 模块测量 RF 被测设备（DUT）的输出二阶截点（OIP2）。
