---
type: simulink-block
title: 'Average-Value Rectifier (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluerectifierthreephase'
documentation_source_path: 'ref/averagevaluerectifierthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value Rectifier (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口电气
  direction: unspecified
- name: a
  summary: '*a* 相电气'
  direction: unspecified
- name: b
  summary: '*b* 相电气'
  direction: unspecified
- name: c
  summary: '*c* 相电气'
  direction: unspecified
- name: +
  summary: 正极端子电气
  direction: unspecified
- name: '-'
  summary: 负极端子电气
  direction: unspecified
```

### 守恒

### **~** — 三相端口电气

可扩展三相端口

#### 依赖

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子电气

与正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与负极端子相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: AC frequency
  summary: 交流频率 Variable（默认）| Constant
  group: ''
- name: Rated AC voltage
  summary: 额定交流电压 4160 V（默认）
  group: ''
- name: Rated electrical frequency
  summary: 额定电气频率 60 Hz | 标量
  group: ''
- name: Fixed power loss
  summary: 固定功率损耗 1e3 W（默认）
  group: ''
```

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **AC frequency** — 交流频率 `Variable`（默认）| `Constant`

选择使用可变交流频率还是恒定交流频率：

- `Variable` — 如果交流侧频率变化，此选项仅在时间仿真模式下工作。
- `Constant` — 如果交流侧频率恒定，此选项在时间仿真模式和频率-时间仿真模式下均可工作。

### **Rated AC voltage** — 额定交流电压 `4160` `V`（默认）

交流系统的额定电压。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz` | 标量

额定电气频率。此参数的值必须等于模型中其他正弦电源的额定电气频率值（如果存在）。

#### 依赖

要启用此参数，请将 **AC frequency** 设置为 `Constant`。

### **Fixed power loss** — 固定功率损耗 `1e3` `W`（默认）

在额定交流电压下交流侧汲取的最小功率。当瞬时交流电压等于 **Rated AC voltage** 指定的值时，交流功率需求等于 **Fixed power loss** 指定的值加上直流功率需求。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

带固定功率损耗的平均值三相交流电压到直流电压转换器

Average-Value Rectifier (Three-Phase) 模块对平均值、全波、六脉冲整流器进行建模。它将瞬时三相交流电压转换为直流电压，并将直流功率需求转换为三相交流功率需求。相应的交流功率需求等于固定功率损耗与直流功率需求之和。

您只能将 Average-Value Rectifier (Three-Phase) 模块用作六脉冲整流器。您不能组合两个 Average-Value Rectifier 模块来表示十二脉冲整流器。

该图展示了整流器作为全波、六脉冲整流器的等效电路。然而，Average-Value Rectifier (Three-Phase) 模块不会产生通常与详细表示相关联的谐波，因为它执行的是平均值功率转换。

此模块可在时间仿真模式和频率-时间仿真模式下工作。如果将 **AC frequency** 参数设置为 `Variable`，此模块仅在时间仿真模式下工作。如果选择 `Constant`，此模块在时间仿真模式和频率-时间仿真模式下均可工作。有关详细信息，请参阅 Frequency and Time Simulation Mode。

### 电气定义方程

电压定义为：

vref=va+vb+vc3,

VRMS=(va−vb)2+(vb−vc)2+(vc−va)23,

vDC=32πVRMS,

vp=vref+vDC2,

以及

vn=vref−vDC2,

其中：

- *va*、*vb*、*vc* 分别是交流相电压。
- *vref* 是交流侧的直流偏移。在无直流偏置的平衡交流电力系统中，*vDC* 为 `0` V。
- *VRMS* 是交流线电压的 RMS 值。
- *v*DC 是整流器正极端子与负极端子之间的电压差。
- 32/π 是全波、六脉冲整流器的 *vDC*/*VRMS* 比值。
- *vp*、*vn* 分别是整流器正极端子和负极端子处的电压。

电阻、功率和电流定义为

Rfixed=VRated2Pfixed,

PDC=−vpip−vnin,

RAC=VRMS2PDC+VRMS2Rfixed,

以及

[iaibic]=[vavbvc]−vrefRAC,

其中：

- *VRated* 是您在模块掩码上指定的额定交流电压。
- *Pfixed* 是您在模块掩码上指定的固定功率损耗。
- *Rfixed* 是等效星形连接负载中的固定每相串联电阻。
- *ip*、*in* 是流入整流器正极端子和负极端子的电流。
- *PDC* 是直流侧的输出功率。*PDC* 的最小限值为 `0` W。
- *RAC* 是等效星形连接负载中的每相串联电阻。
- *ia*、*ib*、*ic* 分别是流入整流器的交流相电流。
