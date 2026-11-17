---
type: simulink-block
title: 'IIP2 Testbench'
family: 'circuit-envelope'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'iip2testbench'
documentation_source_path: 'ref/iip2testbench.html'
language: zh-CN
chinese_source: worker-translation
---

# IIP2 Testbench

## 端口

R2025b 中未记录。

## 参数

#### 参数

### **使用内部 Configuration block** — 使用测试台内部配置模块 on（默认）| on

选中以使用测试台内部配置模块。清除此参数以指定您自己的配置模块。

**注意**

使用您自己的配置模块时，步长、基波音、谐波阶数和仿真噪声等参数可能会影响测量结果。

### **仿真噪声（激励和 DUT 内部）** — 启用激励信号中的噪声建模 on（默认）| off

选中以启用进入 DUT 的激励信号中以及 DUT 内部的噪声建模。

#### 依赖关系

要启用此参数，请选中 **使用内部 Configuration block**。

### **输入功率幅度 (dBm)** — DUT 的输入功率 `-30`（默认）| scalar

DUT 的输入功率，指定为以 dBm 为单位的 scalar。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口的可用功率。有效值介于 -90 dBm 和 60 dBm 之间。

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

用于测量 DUT 的负载电阻，指定为以 ohms 为单位的 positive real scalar。

### **显示响应频谱** — 在仿真期间使用频谱示波器查看响应频谱 on（默认）| off

选中以在仿真期间使用频谱示波器查看响应频谱。

**注意**

要使用 Spectrum Analyzer 查看响应频谱，您需要 DSP System Toolbox™ 许可证。

### **接地并隐藏负端子** — 在内部将 RF 电路端子接地并隐藏 on（默认）| off

选中以在内部将负端子接地并隐藏。清除以暴露负端子。通过暴露这些端子，可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量系统的输入二阶截点

使用 `IIP2 Testbench` 测量被测 RF 器件 (DUT) 的输入二阶截点 (IIP2)。
