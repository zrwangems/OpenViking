---
type: simulink-block
title: 'PWM Generator (Multilevel)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratormultilevel'
documentation_source_path: 'ref/pwmgeneratormultilevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Generator (Multilevel)

## 端口

### 输入

### **ref** — 参考信号向量

用于计算多电平变流器每个功率子模块 PWM 的参考信号，指定为向量。

### 输出

### **PWM** — PWM 信号向量

每个子模块的脉宽调制信号，以向量形式返回。

如果将 **Converter topology** 参数设置为 `Half-bridge`，则输出为如下指定的向量：

G={G1\_SM1, G2\_SM1, G1\_SM2, G2\_SM2, … , G1\_SMN, G2\_SMN}。

如果将 **Converter topology** 参数设置为 `Full-bridge`，则输出为如下指定的向量：

G={G1\_SM1, G2\_SM1, G3\_SM1, G4\_SM1, G1\_SM2, G2\_SM2, G3\_SM2, G4\_SM2, … , G1\_SMN, G2\_SMN, G3\_SMN, G4\_SMN}，

其中 *Gi\_SMj* 是控制第 *j* 个功率子模块第 *i* 个门极的参考信号。在半桥拓扑中，*i* 的范围为 `1` 到 `2`；在全桥拓扑中，*i* 的范围为 `1` 到 `4`。*j* 的范围为 `1` 到 *N*，其中 *N* 是在 **Number of power submodules** 参数中指定的功率子模块数量。

**数据类型：** `single` | `double`

## 参数

### **Converter topology** — 模块化多电平变流器拓扑 `Half-bridge`（默认）| `Full-bridge`

模块化多电平变流器的拓扑。

### **Number of power submodules** — 模块化多电平子模块数量 `1`（默认）| 正标量

模块化多电平变流器的功率子模块数量。

### **Timer period (s)** — PWM 周期 `0.001`（默认）| 正标量

PWM 定时器周期。**Timer period (s)** 参数指定为 12fsw，其中 fsw 是开关频率。

### **Sample time** — 模块采样时间 `5e-5`（默认）| 正标量

模块的采样时间。对于连续时间仿真，设置为零。对于离散时间仿真，为确保生成信号具有足够的分辨率，请指定一个小于或等于 `10 * Tper` 的正值，其中 *Tper* 是 **Timer period (s)**。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

为模块化多电平变流器生成脉宽调制信号或波形

PWM Generator (Multilevel) 模块为模块化多电平变流器实现脉宽调制（PWM）发生器。PWM 技术通过在满功率传输和无功率传输之间快速切换来控制从一个电气组件到另一个电气组件的功率传输。

该模块基于功率子模块数量以及两种变流器拓扑（半桥和全桥）计算模块化多电平变流器的门极脉冲。您可以分别使用 **Number of power submodules** 和 **Converter topology** 参数指定功率子模块数量和变流器拓扑。
