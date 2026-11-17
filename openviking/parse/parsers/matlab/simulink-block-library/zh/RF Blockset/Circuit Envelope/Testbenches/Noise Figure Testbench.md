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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Use Internal Configuration block
  summary: 使用测试台内部配置模块 on（默认）| off
  group: ''
- name: Simulate noise (both stimulus and DUT internal)
  summary: 在激励信号中启用噪声建模 on（默认）| off
  group: ''
- name: Input power amplitude (dBm)
  summary: DUT 的输入功率 -30（默认）| 标量
  group: ''
- name: Input frequency (Hz)
  summary: DUT 的载波频率 2.1e9（默认）| 标量
  group: ''
- name: Output frequency (Hz)
  summary: DUT 的输出频率 2.1e9（默认）| 标量
  group: ''
- name: Baseband bandwidth (Hz)
  summary: 输入信号的基带带宽 10e6（默认）| 标量
  group: ''
- name: Source impedance (Ohm)
  summary: 用于测量 DUT 的源阻抗 50（默认）| 复有限标量
  group: ''
- name: Clear noise history
  summary: 清除噪声历史记录按钮（默认）
  group: ''
- name: Show Response spectrum
  summary: 在仿真期间使用频谱示波器查看响应频谱 on（默认）| off
  group: ''
- name: Ground and hide negative terminals
  summary: 在内部接地并隐藏 RF 电路端子 on（默认）| off
  group: ''
```

#### 参数

### **Use Internal Configuration block** — 使用测试台内部配置模块 on（默认）| off

选择以使用测试台内部配置模块。清除此参数以指定您自己的配置模块。

**注意**

使用您自己的配置模块时，步长、基频音、谐波阶数和模拟噪声等参数可能会影响测量结果。

### **Simulate noise (both stimulus and DUT internal)** — 在激励信号中启用噪声建模 on（默认）| off

选择以在进入 DUT 的激励信号中以及 DUT 内部启用噪声建模。在 NF 测试台中，此参数永久禁用，因为激励噪声是有意义的噪声计算所必需的。

#### 依赖关系

要启用此参数，请选择 **Use internal Configuration block**。

### **Input power amplitude (dBm)** — DUT 的输入功率 `-30`（默认）| 标量

DUT 的输入功率，指定为以 dBm 为单位的标量。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值介于 -`90` dBm 和 `60` dBm 之间。

### **Input frequency (Hz)** — DUT 的载波频率 `2.1e9`（默认）| 标量

DUT 的载波频率，指定为以 Hz 为单位的标量。输入频率必须大于基带带宽。

### **Output frequency (Hz)** — DUT 的输出频率 `2.1e9`（默认）| 标量

DUT 的输出频率，指定为以 Hz 为单位的标量。输出频率必须大于基带带宽。

### **Baseband bandwidth (Hz)** — 输入信号的基带带宽 `10e6`（默认）| 标量

输入信号的基带带宽，指定为以 Hz 为单位的标量。该值必须大于零。

### **Source impedance (Ohm)** — 用于测量 DUT 的源阻抗 `50`（默认）| 复有限标量

用于测量 DUT 的源阻抗，指定为以欧姆为单位的复有限标量。阻抗的实部必须为正。

### **Clear noise history** — 清除噪声历史记录按钮（默认）

使用此按钮可清除用于内部噪声测量的噪声历史记录。当 DUT 具有初始建立时间持续时间时，建议在此持续时间之后清除噪声历史记录。这可以提高噪声测量的精度和收敛性。

### **Show Response spectrum** — 在仿真期间使用频谱示波器查看响应频谱 on（默认）| off

选择以在仿真期间使用频谱示波器查看响应频谱。

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

测量系统的噪声系数

使用 `Noise Figure Testbench` 测量被测 RF 设备（DUT）的噪声系数（NF）。
