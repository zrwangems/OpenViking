---
type: simulink-block
title: 'Average-Value Rectifier (Three-Phase)'
family: 'semiconductors-converters'
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

### 守恒

### **~** — 三相端口电气

可扩展三相端口

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子电气

与正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与负极端子相关联的电气守恒端口。

## 参数

### **电气连接** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是使用复合三相端口还是扩展三相端口。

### **交流频率** — 交流频率 `Variable`（默认）| `Constant`

交流频率是可变的还是恒定的：

- `Variable` — 如果交流侧的频率变化，此选项仅在时间仿真模式下工作。
- `Constant` — 如果交流侧的频率恒定，此选项在时间和频率-时间仿真模式下均能工作。

### **额定交流电压** — 额定交流电压 `4160``V`（默认）

交流系统的额定电压。

### **额定电气频率** — 额定电气频率 `60` `Hz` | scalar

额定电气频率。如果模型中存在其他正弦源，此参数的值必须等于这些正弦源的额定电气频率值。

#### 依赖关系

要启用此参数，请将 **交流频率** 设置为 `Constant`。

### **固定功率损耗** — 固定功率损耗 `1e3``W`（默认）

在额定交流电压下交流侧汲取的最小功率。当瞬时交流电压等于为 **额定交流电压** 指定的值时，交流功率需求等于为 **固定功率损耗** 指定的值加上直流功率需求。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

带固定功率损耗的平均值三相交流电压到直流电压转换器

Average-Value Rectifier (Three-Phase) 模块对平均值、全波、六脉冲整流器进行建模。它将瞬时三相交流电压转换为直流电压，并将直流功率需求转换为三相交流功率需求。相应的交流功率需求等于固定功率损耗与直流功率需求之和。

只能将 Average-Value Rectifier (Three-Phase) 模块用作六脉冲整流器。不能组合两个 Average-Value Rectifier 模块来表示十二脉冲整流器。

该图展示了全波、六脉冲整流器的等效电路。但 Average-Value Rectifier (Three-Phase) 模块不会产生通常与详细表示相关的谐波，因为它执行的是平均值功率转换。

此模块可在时间和频率-时间两种仿真模式下工作。如果将 **交流频率** 参数设置为 `Variable`，则此模块仅在时间仿真模式下工作。如果选择 `Constant`，则此模块在时间和频率-时间仿真模式下均能工作。有关详细信息，请参阅频率和时间仿真模式。

### 电气定义方程

电压定义为：

vref=va+vb+vc3,

VRMS=(va−vb)2+(vb−vc)2+(vc−va)23,

vDC=32πVRMS,

vp=vref+vDC2,

以及

vn=vref−vDC2,

其中：

- *va*、
  *vb*、
  *vc* 分别是各相交流相电压。
- *vref* 是交流侧的直流偏置。在无直流偏置的平衡交流电力系统中，*vDC* 为 `0` V。
- *VRMS* 是 RMS 交流线间电压。
- *v*DC 是整流器正极端子和负极端子之间的电压差。
- 32/π 是全波、六脉冲整流器的 *vDC*/*VRMS* 比值。
- *vp*、*vn* 是整流器正极端子和负极端子处的电压。

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
- *PDC* 是直流侧的输出功率。*PDC* 的最小限制为 `0` W。
- *RAC* 是等效星形连接负载中的每相串联电阻。
- *ia*、*ib*、*ic* 分别是流入整流器的各相交流相电流。
