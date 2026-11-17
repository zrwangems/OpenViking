---
type: simulink-block
title: 'Transducer Gain Testbench'
family: 'circuit-envelope'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'transducergaintestbench'
documentation_source_path: 'ref/transducergaintestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# Transducer Gain Testbench

## 端口

R2025b 中未记录。

## 参数

#### 参数

### **使用内部 Configuration 模块** — 使用测试台内部 Configuration 模块 on（默认） | off

选择此项以使用测试台内部 Configuration 模块。清除此参数以指定您自己的配置模块。

**注意**

使用您自己的配置模块时，步长、基波音调、谐波阶数和模拟噪声等参数可能会影响测量结果。

### **模拟噪声（激励和 DUT 内部）** — 启用激励信号中的噪声建模 on（默认） | off

选择此项以在进入 DUT 的激励信号中以及 DUT 内部启用噪声建模。

#### 依赖关系

要启用此参数，请选择 **使用内部 Configuration 模块**。

### **输入功率幅度 (dBm)** — DUT 的输入功率 `-30`（默认） | scalar

DUT 的输入功率，以 dBm 为单位指定为 scalar。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值介于 -90 dBm 和 60 dBm 之间。

### **输入频率 (Hz)** — DUT 的载波频率 `2.1e9`（默认） | scalar

DUT 的载波频率，以 Hz 为单位指定为 scalar。输入频率必须大于基带带宽。

### **输出频率 (Hz)** — DUT 的输出频率 `2.1e9`（默认） | scalar

DUT 的输出频率，以 Hz 为单位指定为 scalar。输出频率必须大于基带带宽。

### **基带带宽 (Hz)** — 输入信号的基带带宽 `10e6`（默认） | scalar

输入信号的基带带宽，以 Hz 为单位指定为 scalar。该值必须大于零。

### **源电阻 (Ohm)** — 用于测量 DUT 的源电阻 `50`（默认） | positive finite scalar

用于测量 DUT 的源电阻，以 ohms 为单位指定为 positive finite scalar。

### **负载电阻 (Ohm)** — 用于测量 DUT 的负载电阻 `50`（默认） | positive finite scalar

用于测量 DUT 的负载电阻，以 ohms 为单位指定为 positive finite scalar。

### **显示响应频谱** — 在仿真期间使用频谱示波器查看响应频谱 on（默认） | off

选择此项以在仿真期间使用频谱示波器查看响应频谱。

**注意**

要使用 Spectrum Analyzer 查看响应频谱，您需要 DSP System Toolbox™ 许可证。

### **接地并隐藏负端子** — 在内部将 RF 电路端子接地并隐藏 on（默认） | off

选择此项以在内部将负端子接地并隐藏。清除此项以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量系统的转换增益

使用 `Transducer Gain Testbench` 测量 RF 被测器件（DUT）的转换增益 (GT)。
