---
type: simulink-block
title: 'Pressure Compensator Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurecompensatorvalvetl'
documentation_source_path: 'ref/pressurecompensatorvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Compensator Valve (TL)

## 端口

### 守恒端口

### **A** — 液体端口（热液体）

与阀的 A 侧相关联的热液体守恒端口。

### **B** — 液体端口（热液体）

与阀的 B 侧相关联的热液体守恒端口。

### **X** — 压力参考（热液体）

与点 X 处压力 *Px* 相关联的热液体守恒端口。

### **Y** — 压力参考（热液体）

与点 Y 处压力 *P*y 相关联的热液体守恒端口。

### 输入

### **Ps** — 受控压差，Pa（物理信号）

用于受控阀操作的压差，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### 参数

### **Valve specification** — 阀偏置 `Normally open`（默认）| `Normally closed`

压力补偿阀的正常工作状态。对于减压阀，选择 `Normally open` 阀。对于溢流阀，选择 `Normally closed`。

### **Set pressure control** — 恒定或受控阀操作 `Constant`（默认）| `Controlled`

阀操作方法。当您将此参数设置为：

- `Controlled` 并将压力信号连接到端口 **Ps** 时，模块保持压力调节范围恒定。当 *Pcontrol* 大于端口 **Ps** 处信号的值且小于 *Pmax* 时，阀调节压力。
- `Constant` 时，**Set pressure differential** 参数定义恒定的设定压力。

### **Opening parameterization** — 开度参数化 `Linear`（默认）| `Tabulated`

用于参数化阀开度动作的方法。

### **Set pressure differential** — 触发压力补偿的压差 `0` `MPa`（默认）| 标量

触发压力补偿的压差大小。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀工作压力范围 `0.1` `MPa`（默认）| 标量

阀的工作压力范围。压力调节范围定义 **Set pressure differential** 参数与阀最大工作压力之间的差值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Maximum opening area** — 阀全开时的面积 `1e-4` `m^2`（默认）| 正标量

阀在全开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Leakage area** — 全关位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于全关位置时所有间隙的总和。小于此值的面积会饱和到指定的泄漏面积。此值通过保持流量连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure differential vector** — 表格化参数化的压差值 `[0.2 : 0.2 : 1.2]` `MPa`（默认）| 1×*n* 向量

用于开度面积表格化参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的值一一对应。压力必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated`。

### **Opening area vector** — 表格化参数化的阀开度面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2`（默认）| 1×*n* 向量

用于开度面积表格化参数化的开度面积值向量。向量元素必须与 **Pressure differential vector** 参数中的值一一对应。对于常开阀，按降序列出元素。对于常闭阀，按升序列出元素。

开度面积向量必须与 **Pressure differential vector** 参数具有相同数量的元素。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated`。

### **Cross-sectional area at ports A and B** — 阀入口或出口处的面积 `0.01` `m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在确定通过阀的质量流量的压力-流量方程中使用此面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

模块用于考虑理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

模块用于在阀处于接近打开或接近关闭位置时对流量响应引入渐变层的连续平滑因子。将此参数设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure recovery** — 包含压力恢复的选项 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Opening dynamics** — 模拟阀过渡流量响应的选项 `off`（默认）| `on`

是否考虑阀打开对流体系统的瞬态效应。当您选择此参数时，模块通过在流量响应中引入一阶滞后来近似开度条件。

### **Opening time constant** — 阀打开时间常数 `0.1` `s`（默认）| 正标量

用于计算开度动态滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 故障

### **Pressure Compensator Valve Area fault** — 模拟阀面积故障的选项 `Add fault`

用于在模块中模拟阀面积故障的选项。要添加故障，请单击 **Add fault** 超链接。故障发生后，模块根据 **Opening area when faulted** 参数中指定的值设置阀面积。

### **Opening area when faulted** — 故障时的阀位置 `Closed`（默认）| `Open` | `Maintain last value`

故障时的开度面积。您可以选择阀在打开、关闭或故障后面积处卡住。

#### 依赖关系

要启用此参数，请通过单击 **Add fault** 超链接为模块启用故障。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：使用输入端口控制压差

当 **Set pressure control** 参数为 `Controlled` 时，您现在可以使用端口 **Ps** 处的信号来指定压差。要保持与先前版本相同的行为，请将 **Set pressure control** 设置为 `Constant`。

### R2024b：使用 Simscape 故障接口模拟故障

Pressure Compensator Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

热液体网络中的压力补偿阀

Pressure Compensator Valve (TL) 模块表示热液体网络中的压力补偿器，例如压力溢流阀或减压阀。使用此模块可根据系统其他部分的信号维持阀处的压力。

端口 **X** 和 **Y** 之间的压差为控制压力 *Pcontrol*。当此值达到或超过设定压力时，阀面积根据 **Valve specification** 参数打开或关闭。压力调节范围从设定压力 *Pset* 开始。

### 压力控制

当 *Pcontrol* 超过 *Pset* 时，模块调节压力。模块持续调节压力直至 *Pmax*，即 *Pset* 与压力调节范围之和。模块支持两种调节模式：

- 当您将 **Set pressure control** 设置为 `Controlled` 并将压力信号连接到端口 **Ps** 时，模块保持压力调节范围恒定。当 *Pcontrol* 大于端口 **Ps** 处信号的值且小于 *Pmax* 时，阀调节压力。
- 当您将 **Set pressure control** 设置为 `Constant` 时，**Set pressure differential** 参数定义恒定的设定压力。

### 质量守恒

模块守恒质量，使得

m˙A+m˙B=0。

模块计算通过阀的质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是瞬时阀开度面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差 *pA* – *pB*。

临界压差 *Δpcrit* 是由 **Critical Reynolds number** 参数 *Recrit* 指定的压差。此参数表示层流和湍流之间的流态转变点。模块按如下方式计算临界压差：

Δpcrit=π8Avalveρ¯(μRecritCd)2，

其中 *μ* 是热液体的动力粘度。

压力损失 *PRloss* 描述由于面积减小而导致的阀中压力降低。模块按如下方式计算压力损失：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

压力恢复描述由于面积增加而导致的阀中正压力变化。当您清除 **Pressure recovery** 复选框时，模块将 *PRloss* 设置为 1。

模块使用开度参数化和阀开度动态计算 *Avalve*。

### 阀开度参数化

当您将 **Opening parameterization** 设置为 `Linear` 时，常开阀的阀面积为

Avalve=p^(Aleak−Amax)+Amax，

其中 *Aleak* 是 **Leakage Area** 参数的值，*Amax* 是 **Maximum opening area** 参数的值。下图显示了模块如何使用线性参数化控制常开阀的开度面积。

使用线性参数化的常开阀，端口 X 和 Y 之间的压差与开度面积的关系

对于常闭阀，模块使用

Avalve=p^(Amax−Aleak)+Aleak。

下图显示了模块如何使用线性参数化控制常闭阀的开度面积。

使用线性参数化的常闭阀，端口 X 和 Y 之间的压差与开度面积的关系

归一化压力 p^ 为

p^=pcontrol−psetpmax−pset。

当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关更多信息，请参阅 Numerical Smoothing。

当您将 **Opening parameterization** 设置为 `Tabulated` 时，*Aleak* 和 *Amax* 分别是 **Opening area vector** 参数的第一个和最后一个参数。模块按如下方式计算开度面积：

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest)，

其中：

- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector** 参数。
- *poffset* 是内部压力偏移，使阀在 *pcontrol,TLU,ref* = *pset* 时开始关闭。
- *ATLU* 是 **Opening area vector** 参数。

下图演示了模块如何使用表格化数据参数化控制常开阀的开度面积。

使用表格化参数化的常开阀，端口 X 和 Y 之间的压差与开度面积的关系

下图演示了模块如何使用表格化数据参数化控制常闭阀的开度面积。

使用表格化参数化的常闭阀，端口 X 和 Y 之间的压差与开度面积的关系

### 开度动态

当您选择 **Opening dynamics** 时，模块引入控制压力滞后，其中 *pcontrol* 变为动态控制压力 *pdyn*。模块根据 **Opening time constant** 参数 *τ* 计算动态控制压力的瞬时变化：

p˙dyn=pcontrol−pdynτ。

默认情况下，模块清除 **Opening dynamics** 复选框。当 **Opening parameterization** 为 `Linear` 时，**Smoothing factor** 参数的非零值在节流口处于接近关闭或接近打开位置时提供额外的数值稳定性。

模块根据控制压力 *pcontrol* 按照 **Opening parameterization** 参数计算稳态动态。

### 能量平衡

阀中的能量守恒方程为

ϕA+ϕB=0，

其中：

- *ϕA* 是通过端口 **A** 进入阀的能量流率。
- *ϕB* 是通过端口 **B** 进入阀的能量流率。

### 故障

要模拟故障，请在 **Faults** 部分中，单击要模拟的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

您可以将 **Opening area when faulted** 参数设置为：

- `Closed` — 阀面积停止在其最小值处，具体取决于 **Opening parameterization** 参数设置：

  - `Linear` — 阀面积停止在 **Leakage area** 参数的值处。
  - `Tabulated` — 阀面积停止在 **Opening area vector** 参数的最小元素处。
- `Open` — 阀停止在其最大值处，具体取决于 **Opening parameterization** 参数设置：

  - `Linear` — 阀面积停止在 **Maximum opening area** 参数的值处。
  - `Tabulated` — 阀面积停止在 **Opening area vector** 参数的最大元素处。
- `Maintain last value` — 阀面积在触发发生时停止在阀开度面积处。

由于阀面积极值处的数值平滑，模块使用的最小面积大于泄漏面积，最大值小于 **Maximum orifice area** 参数的值。此效应与您应用的平滑量成比例。

故障触发后，阀在仿真的剩余时间内保持在故障面积处。
