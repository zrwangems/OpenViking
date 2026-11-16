---
type: simulink-block
title: 'Temperature Control Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Valves and Orifices / Flow Control Valves'
documentation_page: 'temperaturecontrolvalvetl'
documentation_source_path: 'ref/temperaturecontrolvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Control Valve (TL)

## 端口

### 守恒

### **A** — 液体端口 thermal liquid

与阀门液体进入或离开点关联的 thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

与阀门液体进入或离开点关联的 thermal liquid 守恒端口。

### **T** — 传感端口 thermal liquid | thermal

与温度传感关联的 thermal liquid 或 thermal 守恒端口。此端口没有质量或能量流。当 **温度传感** 为 `Thermal liquid sensing port` 时，端口 **T** 是 thermal liquid 传感端口。当 **温度传感** 为 `Thermal sensing port` 时，端口 **T** 是 thermal 传感端口。

#### 依赖关系

要启用此端口，请将 **温度传感** 设置为 `Thermal liquid sensing port` 或 `Thermal sensing port`。

## 参数

### **阀门操作** — 由升温引起的开度面积变化的符号 `Opens above activation temperature`（默认） | `Closes above activation temperature`

由升温引起的开度面积变化的符号。开度面积可随温度升高而增大，也可随温度升高而收缩。该变化从激活温度开始，并在升温条件下持续贯穿阀门的整个温度调节范围。

默认设置对应于常闭阀，其随温度升高而打开；替代设置对应于常开阀，其随温度升高而关闭。

### **温度传感** — 控制阀门温度传感的方法 `Valve inlet temperature`（默认） | `Thermal liquid sensing port` | `Thermal sensing port`

模块用于测量控制阀门的温度的方法：

- 当将 **温度传感** 设置为 `Valve inlet temperature` 时，阀门使用阀门内部流体的平均温度来控制阀门。
- 当将 **温度传感** 设置为 `Thermal liquid sensing port` 时，模块启用端口 **T**，该端口是 thermal liquid 传感端口。将此端口连接到 thermal liquid 网络，以使用该温度控制阀门。模块仅将端口 **T** 用于传感，并且没有流入或流出的流量。
- 当将 **温度传感** 设置为 `Thermal sensing port` 时，模块启用 thermal 传感端口 **T**。将此端口连接到 thermal 网络的任意部分，以使用该温度控制阀门。模块仅将端口 **T** 用于传感，并且与环境没有热交换。

### **激活温度** — 开启机构触发的温度 `330` `K`（默认） | 正标量

开启机构触发的温度。高于此温度的升温将打开或关闭阀门，具体取决于 **阀门操作** 参数的设置。开度面积在阀门的整个温度调节范围内保持可变。

### **温度调节范围** — 阀门温度范围 `8` `K`（默认） | 正标量

阀门开度面积变化的温度区间。该区间从 **激活温度** 参数的值开始。

### **传感器时间常数** — 温度变化在入口传感器处登记所需的时间 `1.5` `s`（默认） | 非负标量

温度变化在入口传感器处登记的特征时间。此参数确定变化开始与对该变化的稳定测量之间的延迟。值为 `0` 表示传感器对温度变化瞬时响应。

### **最大开度面积** — 完全打开位置处由密封不完善导致的开度面积 `1e-4` `m^2`（默认） | 正标量

当阀门处于压力调节范围的上限时，阀门在完全打开位置的开度面积。模块使用此参数在整个压力调节范围内缩放阀门开度。

### **泄漏面积** — 最大关闭位置处由密封不完善导致的开度面积 `1e-10` `m^2`（默认） | 正标量

当阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。这通过保持流动的连续性来增强数值稳定性。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层逐渐变化。

### **端口 A 和 B 的横截面积** — 守恒端口处的孔口面积 `0.01` `m^2`（默认） | 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过孔口的质量流量的压力-流量方程。

### **流量系数** — 流量系数 `0.64`（默认） | 正标量

用于考虑理论流动中排放损失的修正因子。

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认） | 正标量

通过阀门的层流的上限雷诺数。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2023b：选择其他温度控制选项

现在可以使用 **温度传感** 参数指定模块用于控制阀门的温度数据。

## 描述

thermal liquid 网络中的温度控制阀

Temperature Control Valve (TL) 模块将带有恒温器的孔口建模为流量控制机构。恒温器包含一个温度传感器和一个黑箱开启机构——其几何形状和力学特性不如其效应重要。传感器对温度变化做出响应时略有延迟，该延迟由一阶时间滞后捕获。

当传感器读取到超过预设激活值的温度时，开启机构动作，阀门开始打开或关闭，具体取决于 **阀门操作** 参数指定的操作模式。开度面积的变化持续到阀门温度范围的极限，超过该极限后开度面积为常数。在温度范围内，开度面积是温度的线性函数。

平滑函数使阀门开度面积在完全关闭和完全打开位置之间平滑变化。平滑函数通过消除零和最大球位置处的开度面积突变来实现这一点。

### 质量平衡

阀门中的质量守恒方程为

m˙A+m˙B=0,

其中：

- m˙A 是通过端口 **A** 流入阀门中的质量流量。
- m˙B 是通过端口 **B** 流入阀门中的质量流量。

### 动量平衡

阀门中的动量守恒方程为

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss,

其中：

- *pA* 和 *pB* 是端口 **A** 和端口 **B** 处的压力。
- m˙ 是质量流量。
- m˙cr 是临界质量流量，

  m˙cr=RecrμAvgπ4SR.
- *ρAvg* 是平均液体密度。
- *Cd* 是 **流量系数** 参数的值。
- *S* 是 **端口 A 和 B 的横截面积** 参数的值。
- *SR* 是阀门开度面积。
- *PRLoss* 是压力比，

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S).

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *ϕA* 是通过端口 **A** 流入阀门中的能量流率。
- *ϕB* 是通过端口 **B** 流入阀门中的能量流率。

### 阀门开度面积

阀门开度面积计算基于线性表达式

SLinear=(SEnd−SStartTRange)(TSensor−TActivation)+SStart,

其中：

- *SLinear* 是线性阀门开度面积。
- *SStart* 是温度致动范围开始时的阀门开度面积。此面积取决于 **阀门操作** 参数设置：

  SStart={SLeak,Valve opens above activation temperatureSMax,Valve closes above activation temperature
- *SEnd* 是温度致动范围结束时的阀门开度面积。此面积取决于 **阀门操作** 参数设置：

  SEnd={SMax,Valve opens above activation temperatureSLeak,Valve closes above activation temperature
- *SMax* 是 **最大开度面积** 参数的值。
- *SLeak* 是 **泄漏面积** 参数的值。
- *TRange* 是 **温度调节范围** 参数的值。
- *TActivation* 是 **激活温度** 参数的值
- *TSensor* 是传感器温度读数。

  - 当 **温度传感** 为 `Valve inlet temperature` 时，*TSensor* 是阀门内部的平均温度。
  - 当 **温度传感** 为 `Thermal liquid sensing port` 时，*TSensor* 是 thermal liquid 网络在连接到端口 **T** 处的温度。
  - 当 **温度传感** 为 `Thermal sensing port` 时，*TSensor* 是 thermal 网络在连接到端口 **T** 处的温度。

阀门模型通过以下微分方程考虑所测量阀门温度中的一阶滞后

ddt(TSensor)=TAvg−TSensorτ,

其中：

- *TAvg* 是阀门端口温度的算术平均值，

  TAvg=TA+TB2,

  其中 *TA* 和 *TB* 是端口 **A** 和 **B** 处的温度。
- *τ* 是 **传感器时间常数** 参数的值。

当阀门处于接近打开或接近关闭位置时，可以通过调整 **平滑因子** 参数来保持仿真中的数值稳健性。如果 **平滑因子** 参数非零，模块会将阀门面积平滑地饱和在 *SLeak* 和 *SMax* 之间。有关详细信息，请参阅 Numerical Smoothing。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
