---
type: simulink-block
title: 'Power Sensor (Three-Phase)'
family: 'sensors-transducers'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'powersensorthreephase'
documentation_source_path: 'ref/powersensorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Sensor (Three-Phase)

## 端口

### 守恒

### **~1** — 三相电气端口

可扩展三相电气端口。

### **~2** — 三相电气端口

可扩展三相电气端口。
### 输出

### **P** — 有功功率物理信号

与有功功率测量相关联的物理信号端口。

### **Q** — 无功功率物理信号

与无功功率测量相关联的物理信号端口。

## 参数

### **建模选项** — 是建模为复合三相端口还是扩展三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是建模为复合三相端口还是扩展三相端口。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图相对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **负载类型** — 负载类型 `Balanced`（默认）| `Unbalanced`

负载类型。如果三相支路平衡，则选择 `Balanced`；如果支路不平衡，则选择 `Unbalanced`。

### **额定频率** — 额定频率 `60` `Hz`（默认）| scalar

额定频率。

#### 依赖关系

要启用此参数，请将 **负载类型** 设置为 `Unbalanced`。

### **下游配置** — 下游配置 `Without neutral`（默认）| `With neutral`

下游配置是否带中性线。

#### 依赖关系

要启用此参数，请将 **负载类型** 设置为 `Unbalanced`。

### **中性线导体电阻除以相线导体电阻** — 中性线导体电阻与相线导体电阻之比 `1`（默认）| scalar

中性线导体电阻与相线导体电阻之比，RneutralRphase..

#### 依赖关系

要启用此参数，请将 **下游配置** 设置为 `With neutral`。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

三相理想有功和无功功率传感器

Power Sensor (Three-Phase) 模块实现了一个理想传感器，用于在平衡或不平衡三相支路中测量有功和无功功率。

对于平衡支路，该模块在所有时刻返回有功和无功功率的正确值。这是潮流分析的首选选项。

对于不平衡支路，为了估计幅值和相位，该模块通过使用单移动周期 Fourier 变换独立测量三个电压和电流的相量。因此，在第一个周期内，输出幅值和相位为零。

### 不平衡支路方程

等效平衡相电压、电流和视在功率为：

Ve=13VabRMS2+VbcRMS2+VcaRMS2Ie=IaRMS2+IbRMS2+IcRMS2+ρI2nRMS3Se=3VeIe

其中

- *VabRMS*、*VbcRMS* 和 *VcaRMS* 是三个相间 RMS 电压。
- *IaRMS*、*IbRMS* 和 *IcRMS* 是流过三个支路中每个支路的 RMS 电流。
- *ρ* 是中性线导体电阻与相线导体电阻之比，由 **中性线导体电阻除以相线导体电阻** 参数指定。
- *InRMS* 是 RMS 中性电流。

有功功率则定义为：

P=VaRMSIaRMScos(φVa−φIa)+VbRMSIbRMScos(φVb−φIb)+VcRMSIcRMScos(φVc−φIc),

其中：

- *VaRMS*、*VbRMS* 和 *VcRMS* 分别是 a、b 和 c 相的电压。
- *φVa*、*φVb* 和 *φVc* 是 *a* 相、*b* 相和 *c* 相电压的相移。
- *φIa*、*φIb* 和 *φIc* 是 *a* 相、*b* 相和 *c* 相电流的相移。

为了计算无功功率，该模块首先计算其绝对值，然后通过查看相移的符号来确定符号：

abs(Q)=Se2−P2sign(Q)=sign(φ)Q=abs(Q)\*sign(Q)

其中 *φ = φV\* - φI\**。*\** 符号表示 *[-π,π]* 范围中的中心相位。

### 潮流分析

如果该模块位于与频率-时间仿真模式兼容的网络中，则可以对该网络执行潮流分析。潮流分析提供稳态值，可用于初始化电机。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode。
