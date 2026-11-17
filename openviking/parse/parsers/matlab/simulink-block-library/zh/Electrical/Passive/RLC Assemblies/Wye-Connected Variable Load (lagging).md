---
type: simulink-block
title: 'Wye-Connected Variable Load (lagging)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'wyeconnectedvariableloadlagging'
documentation_source_path: 'ref/wyeconnectedvariableloadlagging.html'
language: zh-CN
chinese_source: worker-translation
---

# Wye-Connected Variable Load (lagging)

## 端口
```yaml
ports:
- name: P
  summary: 有功功率物理信号
  direction: input
- name: Q
  summary: 无功功率物理信号
  direction: input
- name: '~'
  summary: 三相电气端口
  direction: input
- name: n
  summary: 中性相电气端口
  direction: input
```

### 输入

### **P** — 有功功率物理信号

与有功功率关联的物理信号输入端口。

### **Q** — 无功功率物理信号

与无功功率关联的物理信号输入端口。
### 守恒

### **~** — 三相电气端口

可扩展三相
电气守恒端口。

### **n** — 中性相电气端口

与中性相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否对复合或扩展三相端口建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated voltage
  summary: 额定线电压 24e3 V（默认）
  group: 主
- name: Rated electrical frequency
  summary: 标称交流电频率 60 Hz（默认）
  group: 主
- name: Minimum real power
  summary: 最小有功功率 1e3 W（默认）| 正标量
  group: 主
- name: Minimum reactive power
  summary: 最小无功功率 1e3 V*A（默认）| 正标量
  group: 主
- name: Parasitic parallel conductance
  summary: 寄生并联电导 1e-6 1/Ohm（默认）
  group: 寄生参数
```

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电力系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### 主

### **Rated voltage** — 额定线电压 `24e3` `V`（默认）

用于电阻方程的 RMS 额定线电压。

### **Rated electrical frequency** — 标称交流电频率 `60` `Hz`（默认）

用于电感方程的标称交流电频率。

### **Minimum real power** — 最小有功功率 `1e3` `W`（默认）| 正标量

三相负载在额定电压供电时消耗的最小有功功率。该值必须大于 0。

### **Minimum reactive power** — 最小无功功率 `1e3` `V*A`（默认）| 正标量

三相负载在额定电压供电时消耗的最小无功功率。该值必须大于 0。

### 寄生参数

### **Parasitic parallel conductance** — 寄生并联电导 `1e-6` `1/Ohm`（默认）

模块并联添加到串联 RL 的电导。
## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

以星形配置接线的三相可变感性负载

Wye-Connected Variable Load (lagging) 模块对以星形配置接线的三相可变感性负载建模。负载的每一相包含一个串联连接的电阻器 (R) 和一个电感器 (L)。该模块计算在您指定的额定电压和额定频率下，抽取物理信号输入 P 和 Q 的有功功率和无功功率所需的电阻和电感。因此，该模块可以表示一个实际的有功和感性无功负载。

为确保电阻和电感始终大于零，您需要指定负载消耗的最小有功功率和无功功率。最小有功功率和无功功率必须大于零。

### 电气定义方程

每相串联电阻和电感定义为

R=PVRated2P2+Q2

以及

L=QVRated22πFRated(P2+Q2),

其中：

- *R* 是每相串联电阻。
- *L* 是每相串联电感。
- *VRated* 是 RMS 额定线电压。
- *FRated* 是标称交流电频率。
- *P* 是所需的三相有功功率。
- *Q* 是所需的三相感性无功功率。

电感定义为磁通量 φ 与稳态电流之比：

L(i)=ϕ(i)i.

因此，电感器的电流-电压关系为：

v=dLdti+Ldidt.

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
