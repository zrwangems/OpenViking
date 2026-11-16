---
type: simulink-block
title: 'Noise Figure Testbench'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'noisefiguretestbench'
documentation_source_path: 'ref/noisefiguretestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# Noise Figure Testbench

## 端口

在 R2025b 中未记录。

## 参数

#### 参数

### **使用内部 Configuration 模块** — 使用测试台内部 Configuration 模块 on（默认） | off

选择以使用测试台内部 Configuration 模块。清除此参数以指定您自己的 Configuration 模块。

**注意**

当使用您自己的 Configuration 模块时，步长、基波音调、谐波阶数和模拟噪声等参数可能会影响测量结果。

### **模拟噪声（激励和 DUT 内部）** — 启用激励信号中的噪声建模 on（默认） | off

选择以启用进入 DUT 的激励信号中以及 DUT 内部的噪声建模。在 NF testbench 中，此参数会永久禁用，因为要获得有意义的噪声计算，需要激励噪声。

#### 依赖关系

要启用此参数，请选择 **使用内部 Configuration 模块**。

### **输入功率幅度 (dBm)** — 输入到 DUT 的功率 `-30`（默认） | scalar

输入到 DUT 的功率，指定为以 dBm 为单位的 scalar。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值介于 -`90` dBm 和 `60` dBm 之间。

### **输入频率 (Hz)** — DUT 的载波频率 `2.1e9`（默认） | scalar

DUT 的载波频率，指定为以 Hz 为单位的 scalar。输入频率必须大于基带带宽。

### **输出频率 (Hz)** — DUT 的输出频率 `2.1e9`（默认） | scalar

DUT 的输出频率，指定为以 Hz 为单位的 scalar。输出频率必须大于基带带宽。

### **基带带宽 (Hz)** — 输入信号的基带带宽 `10e6`（默认） | scalar

输入信号的基带带宽，指定为以 Hz 为单位的 scalar。该值必须大于零。

### **源阻抗 (Ohm)** — 用于测量 DUT 的源阻抗 `50`（默认） | complex finite scalar

用于测量 DUT 的源阻抗，指定为以 ohms 为单位的 complex finite scalar。阻抗的实部必须为正。

### **清除噪声历史** — 清除噪声历史按钮（默认）

使用此按钮清除用于内部噪声测量的噪声历史。当 DUT 具有初始建立时间持续时间时，建议在此持续时间之后清除噪声历史。这会提高噪声测量的精度和收敛性。

### **显示响应频谱** — 在仿真期间使用频谱示波器查看响应频谱 on（默认） | off

选择以在仿真期间使用频谱示波器查看响应频谱。

### **接地并隐藏负端子** — 在内部接地并隐藏 RF 电路端子 on（默认） | off

选择以在内部接地并隐藏负端子。清除以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

测量系统的噪声系数

使用 `Noise Figure Testbench` 测量 RF 待测设备 (DUT) 的噪声系数 (NF)。
