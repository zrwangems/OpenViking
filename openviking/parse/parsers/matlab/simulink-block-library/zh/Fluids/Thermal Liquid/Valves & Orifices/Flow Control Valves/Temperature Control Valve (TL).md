---
type: simulink-block
title: 'Temperature Control Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'temperaturecontrolvalvetl'
documentation_source_path: 'ref/temperaturecontrolvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Control Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口 热液体
  direction: conserving
- name: B
  summary: 液体端口 热液体
  direction: conserving
- name: T
  summary: 传感端口 热液体 | 热
  direction: conserving
```

### 守恒端口

### **A** — 液体端口 热液体

与阀门液体入口或出口点相关联的热液体守恒端口。

### **B** — 液体端口 热液体

与阀门液体入口或出口点相关联的热液体守恒端口。

### **T** — 传感端口 热液体 | 热

与温度传感相关联的热液体或热守恒端口。通过此端口没有质量或能量流动。当 **Temperature sensing** 为 `Thermal liquid sensing port` 时，端口 **T** 为热液体传感端口。当 **Temperature sensing** 为 `Thermal sensing port` 时，端口 **T** 为热传感端口。

#### 依赖关系

要启用此端口，请将 **Temperature sensing** 设置为 `Thermal liquid sensing port` 或 `Thermal sensing port`。
## 参数
```yaml
parameters:
- name: Valve operation
  summary: 由升温引起的开口面积变化的符号 Opens above activation temperature（默认）| Closes above activation temperature
  group: ''
- name: Temperature sensing
  summary: 控制阀门温度传感的方法 Valve inlet temperature（默认）| Thermal liquid sensing port | Thermal sensing port
  group: ''
- name: Activation temperature
  summary: 开启机构触发的温度 330 K（默认）| 正标量
  group: ''
- name: Temperature regulation range
  summary: 阀门温度范围 8 K（默认）| 正标量
  group: ''
- name: Sensor time constant
  summary: 温度变化在入口传感器处记录所需的时间 1.5 s（默认）| 非负标量
  group: ''
- name: Maximum opening area
  summary: 由于密封缺陷导致的完全打开位置处的开口面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Leakage area
  summary: 由于密封缺陷导致的最大关闭位置处的开口面积 1e-10 m^2（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 守恒端口处的孔口面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
```

### **Valve operation** — 由升温引起的开口面积变化的符号 `Opens above activation temperature`（默认）| `Closes above activation temperature`

由升温引起的开口面积变化的符号。开口面积可以随温度升高而扩大，也可以收缩。该变化从激活温度开始，并在阀门的整个温度调节范围内随升温条件持续进行。

默认设置对应于随温度升高而开启的常闭阀门；替代设置对应于随温度升高而关闭的常开阀门。

### **Temperature sensing** — 控制阀门温度传感的方法 `Valve inlet temperature`（默认）| `Thermal liquid sensing port` | `Thermal sensing port`

模块用于测量控制阀门的温度的方法：

- 当您将 **Temperature sensing** 设置为 `Valve inlet temperature` 时，阀门使用阀门内部的平均流体温度来控制阀门。
- 当您将 **Temperature sensing** 设置为 `Thermal liquid sensing port` 时，模块启用端口 **T**，该端口为热液体传感端口。将此端口连接到热液体网络，以使用该温度来控制阀门。模块仅使用端口 **T** 进行传感，没有流入或流出的流量。
- 当您将 **Temperature sensing** 设置为 `Thermal sensing port` 时，模块启用热传感端口 **T**。将此端口连接到热网络的任何部分，以使用该温度来控制阀门。模块仅使用端口 **T** 进行传感，与环境没有热交换。

### **Activation temperature** — 开启机构触发的温度 `330` `K`（默认）| 正标量

开启机构触发的温度。高于此温度的升温将打开或关闭阀门，具体取决于 **Valve operation** 参数的设置。开口面积在阀门的整个温度调节范围内保持可变。

### **Temperature regulation range** — 阀门温度范围 `8` `K`（默认）| 正标量

阀门开口面积变化的温度区间。该区间从 **Activation temperature** 参数的值开始。

### **Sensor time constant** — 温度变化在入口传感器处记录所需的时间 `1.5` `s`（默认）| 非负标量

温度变化在入口传感器处记录的特征时间。此参数确定变化开始与变化稳定测量之间的延迟。值为 `0` 表示传感器对温度变化瞬时响应。

### **Maximum opening area** — 由于密封缺陷导致的完全打开位置处的开口面积 `1e-4` `m^2`（默认）| 正标量

阀门处于完全打开位置时的开口面积，即阀门处于压力调节范围上限时。模块使用此参数在整个压力调节范围内缩放阀门开度。

### **Leakage area** — 由于密封缺陷导致的最大关闭位置处的开口面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。

### **Cross-sectional area at ports A and B** — 守恒端口处的孔口面积 `0.01` `m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过孔口的质量流率的压力-流量方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：选择额外的温度控制选项

您现在可以使用 **Temperature sensing** 参数来指定模块用于控制阀门的温度数据。

## 描述

热液体网络中的温度控制阀

Temperature Control Valve (TL) 模块将带有恒温器的孔口建模为流量控制机构。恒温器包含一个温度传感器和一个黑箱开启机构——其几何形状和力学特性不如其效果重要。传感器对温度变化做出响应，并具有由一阶时间滞后捕获的轻微延迟。

当传感器读取到超过预设激活值的温度时，开启机构启动，阀门开始打开或关闭，具体取决于 **Valve operation** 参数指定的操作模式。开口面积的变化持续到阀门温度范围的极限，超过该极限后开口面积为常数。在温度范围内，开口面积是温度的线性函数。

平滑函数允许阀门开口面积在完全关闭和完全打开位置之间平滑变化。平滑函数通过消除零位和最大球位置处的突然开口面积变化来实现这一点。

### 质量平衡

阀门中的质量守恒方程为

m˙A+m˙B=0,

其中：

- m˙A 是通过端口 **A** 流入阀门的质量流率。
- m˙B 是通过端口 **B** 流入阀门的质量流率。

### 动量平衡

阀门中的动量守恒方程为

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss,

其中：

- *pA* 和 *pB* 分别是端口 **A** 和端口 **B** 处的压力。
- m˙ 是质量流率。
- m˙cr 是临界质量流率，

  m˙cr=RecrμAvgπ4SR。
- *ρAvg* 是平均液体密度。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *SR* 是阀门开口面积。
- *PRLoss* 是压力比，

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S)。

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *ϕA* 是通过端口 **A** 流入阀门的能量流率。
- *ϕB* 是通过端口 **B** 流入阀门的能量流率。

### Valve Opening Area

阀门开度面积计算基于线性表达式

SLinear=(SEnd−SStartTRange)(TSensor−TActivation)+SStart，

其中：

- *SLinear* 是线性阀门开度面积。
- *SStart* 是温度致动范围开始时的阀门开度面积。该面积取决于 **Valve operation** 参数设置：

  SStart={SLeak,Valve opens above activation temperatureSMax,Valve closes above activation temperature
- *SEnd* 是温度致动范围结束时的阀门开度面积。该面积取决于 **Valve operation** 参数设置：

  SEnd={SMax,Valve opens above activation temperatureSLeak,Valve closes above activation temperature
- *SMax* 是 **Maximum opening area** 参数的值。
- *SLeak* 是 **Leakage area** 参数的值。
- *TRange* 是 **Temperature regulation range** 参数的值。
- *TActivation* 是 **Activation temperature** 参数的值
- *TSensor* 是传感器温度读数。

  - 当 **Temperature sensing** 为 `Valve inlet temperature` 时，*TSensor* 是阀门内部的平均温度。
  - 当 **Temperature sensing** 为 `Thermal liquid sensing port` 时，*TSensor* 是热液体网络在连接到端口 **T** 处的温度。
  - 当 **Temperature sensing** 为 `Thermal sensing port` 时，*TSensor* 是热网络在连接到端口 **T** 处的温度。

阀门模型通过微分方程考虑测得阀门温度中的一阶滞后

ddt(TSensor)=TAvg−TSensorτ，

其中：

- *TAvg* 是阀门端口温度的算术平均值，

  TAvg=TA+TB2，

  其中 *TA* 和 *TB* 是端口 **A** 和 **B** 处的温度。
- *τ* 是 **Sensor time constant** 参数的值。

当阀门处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，则该模块会在 *SLeak* 和 *SMax* 之间平滑地饱和阀门面积。有关详细信息，请参阅 Numerical Smoothing。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
