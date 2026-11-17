---
type: simulink-block
title: 'Power Sensor (Three-Phase)'
family: 'sps'
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
```yaml
ports:
- name: ~1
  summary: 三相端口电气
  direction: conserving
- name: ~2
  summary: 三相端口电气
  direction: conserving
- name: P
  summary: 有功功率物理信号
  direction: output
- name: Q
  summary: 无功功率物理信号
  direction: output
```

### 守恒端口

### **~1** — 三相端口电气

可扩展三相
电气端口。

### **~2** — 三相端口电气

可扩展三相
电气端口。
### 输出

### **P** — 有功功率物理信号

与有功功率
测量相关联的物理信号端口。

### **Q** — 无功功率物理信号

与无功功率
测量相关联的物理信号端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否对复合或扩展三相端口建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Load type
  summary: 负载类型 Balanced（默认）| Unbalanced
  group: ''
- name: Rated frequency
  summary: 额定频率 60 Hz（默认）| 标量
  group: ''
- name: Downstream configuration
  summary: 下游配置 Without neutral（默认）| With neutral
  group: ''
- name: Neutral conductor resistance divided by phase conductor resistance
  summary: 中性线导体电阻与相线导体电阻之比 1（默认）| 标量
  group: ''
```

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各相。

### **Load type** — 负载类型 `Balanced`（默认）| `Unbalanced`

负载类型。如果三相支路平衡，则选择 `Balanced`；如果支路不平衡，则选择 `Unbalanced`。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）| 标量

额定频率。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `Unbalanced`。

### **Downstream configuration** — 下游配置 `Without neutral`（默认）| `With neutral`

下游配置是否带中性线。

#### 依赖关系

要启用此参数，请将 **Load Type** 设置为 `Unbalanced`。

### **Neutral conductor resistance divided by phase conductor resistance** — 中性线导体电阻与相线导体电阻之比 `1`（默认）| 标量

中性线导体电阻与相线导体电阻之比，RneutralRphase。。

#### 依赖关系

要启用此参数，请将 **Downstream configuration** 设置为 `With neutral`。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

三相理想有功和无功功率传感器

Power Sensor (Three-Phase) 模块实现了用于在平衡或不平衡三相支路中测量有功和无功功率的理想传感器。

对于平衡支路，该模块在所有时刻返回正确有功和无功功率值。这是潮流分析的首选选项。

对于不平衡支路，为估计幅值和相位，该模块通过使用单移动周期傅里叶变换分别测量三个电压和电流的相量。因此，在第一个周期内，输出幅值和相位为零。

### 不平衡支路方程

等效平衡相电压、电流和视在功率为：

Ve=13VabRMS2+VbcRMS2+VcaRMS2Ie=IaRMS2+IbRMS2+IcRMS2+ρI2nRMS3Se=3VeIe

其中

- *VabRMS*、
  *VbcRMS*
  和
  *VcaRMS*
  是三个相间 RMS 电压。
- *IaRMS*、
  *IbRMS*
  和
  *IcRMS*
  是流过三个支路中每个支路的 RMS 电流。
- *ρ* 是中性线导体电阻与相线导体电阻之比，由 Neutral
  conductor resistance divided by phase conductor resistance
  参数指定。
- *InRMS*
  是 RMS 中性线电流。

有功功率则定义为：

P=VaRMSIaRMScos(φVa−φIa)+VbRMSIbRMScos(φVb−φIb)+VcRMSIcRMScos(φVc−φIc),

其中：

- *VaRMS*、
  *VbRMS*
  和 *VcRMS*
  分别是 a、b 和 c 相的电压。
- *φVa*、
  *φVb*
  和 *φVc*
  是 *a* 相、
  *b* 相和 *c* 相
  电压的相移。
- *φIa*、
  *φIb*
  和 *φIc*
  是 *a* 相、
  *b* 相和 *c* 相
  电流的相移。

为计算无功功率，该模块首先计算其绝对值，然后通过查看相移的符号来确定符号：

abs(Q)=Se2−P2sign(Q)=sign(φ)Q=abs(Q)\*sign(Q)

其中 *φ =
φV\* -
φI\**。*
*\** 符号表示
*[-π,π]* 范围内的中心相位。

### 潮流分析

如果该模块位于与频率-时间仿真模式兼容的网络中，您可以对该网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。
