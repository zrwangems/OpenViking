---
type: simulink-block
title: 'Pressure Compensator Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Pressure Control Valves'
documentation_page: 'pressurecompensatorvalveil'
documentation_source_path: 'ref/pressurecompensatorvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Compensator Valve (IL)

## 端口

### 守恒

### **A** — 液体端口 等温液体

与阀的 A 侧相关联的等温液体守恒端口。

### **B** — 液体端口 等温液体

与阀的 B 侧相关联的等温液体守恒端口。

### **X** — 压力参考 等温液体

与感测 X 点压力 *Px* 相关联的等温液体守恒端口。

### **Y** — 压力参考 等温液体

与感测 Y 点压力 *P*y 相关联的等温液体守恒端口。

### 输入

### **Ps** — 受控压差，Pa 物理信号

用于受控阀运行的压差，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **压力控制设置** 设置为 `Controlled`。

## 参数

### 参数

### **阀规格** — 阀偏置 `Normally open`（默认） | `Normally closed`

压力补偿阀的正常工作状态。对于减压阀，选择 `Normally open` 阀。对于溢流阀，选择 `Normally closed` 阀。

### **压力控制设置** — 恒定或受控的阀运行 `Constant`（默认） | `Controlled`

阀运行方法。将此参数设置为：

- `Controlled` 并将压力信号连接到端口 **Ps** 时，模块保持压力调节范围恒定。当 *Pcontrol* 大于端口 **Ps** 处的信号值且小于 *Pmax* 时，阀调节压力。
- `Constant` 时，**设定压差** 参数定义恒定的设定压力。

### **开启参数化** — 开启参数化 `Linear`（默认） | `Tabulated`

阀开启动作的参数化方法。

### **设定压差** — 超出此范围时触发恒定阀运行 `0` `MPa`（默认） | scalar

触发压力补偿的压差幅值。

#### 依赖关系

要启用此参数，请将 **压力控制设置** 设置为 `Constant`。

### **压力调节范围** — 阀的工作压力范围 `0.1` `MPa`（默认） | scalar

阀的工作压力范围。压力调节范围定义了 **设定压差** 参数与阀最大工作压力之间的差值。

#### 依赖关系

要启用此参数，请将 **开启参数化** 设置为 `Linear`。

### **最大开口面积** — 阀全开时的面积 `1e-4` `m^2`（默认） | positive scalar

阀处于全开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **开启参数化** 设置为 `Linear`。

### **泄漏面积** — 处于全闭位置时的间隙面积 `1e-10` `m^2`（默认） | positive scalar

阀处于全闭位置时所有间隙面积之和。任何小于此值的面积都会饱和为指定的泄漏面积。该值通过保持流量的连续性来提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **开启参数化** 设置为 `Linear`。

### **压差向量** — 用于表格参数化的压差值 `[0.2 : 0.2 : 1.2]` `MPa`（默认） | 1-by*n* vector

用于开口面积表格参数化的压差值向量。向量元素必须与 **开口面积向量** 参数中的值一一对应。压力必须按升序排列。

#### 依赖关系

要启用此参数，请将 **开启参数化** 设置为 `Tabulated`。

### **Opening area vector** — 用于表格化参数化的阀开口面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2`（默认值） | 1×*n* 向量

开口面积值的向量，用于开口面积的表格化参数化。该向量的元素必须与 **Pressure differential vector** 参数中的值一一对应。对于常开阀，按降序排列元素。对于常闭阀，按升序排列元素。

开口面积向量的元素数必须与 **Pressure differential vector** 相同。模块在表数据点之间使用线性插值。

#### 依存关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated`。

### **Cross-sectional area at ports A and B** — 阀入口或出口处的面积 `inf` `m^2`（默认值） | 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在用于确定通过阀的质量流量的压力-流量方程中使用此面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认值） | 正标量

用于考虑理论流动中流量损失的修正系数。

### **Critical Reynolds number** — 层流的雷诺数上限 `150`（默认值） | 正标量

通过阀的层流流动的雷诺数上限。

### **Pressure recovery** — 包含压力恢复的选项 `Off`（默认值） | `On`

是否考虑流体从横截面积较小的区域流向横截面积较大的区域时发生的压力升高。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认值） | [0,1] 范围内的正标量

连续平滑因子，当阀处于接近打开或接近关闭的位置时，在流动响应中引入一个渐变层。将此值设置为小于 1 的非零值，以提高仿真在这些工况下的稳定性。

#### 依存关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Opening dynamics** — 模拟阀切换时流动响应的选项 `off`（默认值） | `on`

是否考虑阀打开引起的流体系统瞬态影响。选择 **Opening dynamics** 后，模块通过在流动响应中引入一阶滞后来近似阀的打开过程。

### **Opening time constant** — 阀打开时间常数 `0.1` `s`（默认值） | 正标量

用于计算打开动态中滞后效应的时间常数。

#### 依存关系

要启用此参数，请选择 **Opening dynamics**。

### 故障

### **Pressure Compensator Valve Area fault** — 对阀面积故障建模的选项 `Add fault`

用于在模块中对阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障后，模块根据 **Opening area when faulted** 参数指定的值设置阀面积。

### **Opening area when faulted** — 故障时的阀位置 `Closed`（默认值） | `Open` | `Maintain last value`

故障时的开口面积。您可以选择让阀在故障后卡滞在打开位置、关闭位置，或保持原开口面积。

#### 依存关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

未在 R2025b 中提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中推出**

### R2024a：使用 Simscape 故障接口对故障建模

Pressure Compensator Valve (IL) 模块现在支持 Simscape 故障接口。要了解详细信息，请参阅《Simscape 故障简介》。

## 描述

等温液体网络中的压力补偿器阀

Pressure Compensator Valve (IL) 模块表示等温液体网络中的压力补偿器，例如溢流阀或减压阀。使用此阀可根据系统其他部分的信号来维持阀处的压力。

端口 **X** 和 **Y** 之间的压差为控制压力 *Pcontrol*。当该值达到或超过设定压力时，阀口会根据 **Valve specification** 参数打开或关闭。压力调节范围始于设定压力 *Pset*。您可以选择恒定设定压力调节或受控设定压力调节。端口 **Ps** 处的物理信号提供可变的设定压力。

### 压力控制

当 *Pcontrol* 超过 *Pset* 时，模块调节压力。模块会持续调节压力，直到达到 *Pmax*，即 *Pset* 与压力调节范围之和。模块支持两种调节模式：

- 当您将 **Set pressure control** 设置为
  `Controlled` 并将压力信号连接到端口 **Ps** 时，模块会保持压力调节范围不变。当 *Pcontrol* 大于端口 **Ps** 处信号的值且小于 *Pmax* 时，阀会调节压力。
- 当您将 **Set pressure control** 设置为
  `Constant` 时，**Set pressure differential** 参数定义恒定的设定压力。

### 质量守恒

模块遵循质量守恒，满足：

m˙A+m˙B=0.

模块按以下公式计算通过阀的质量流量：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 为 **Discharge coefficient** 参数。
- *Avalve* 为阀的瞬时开口面积。
- *Aport* 为 **Cross-sectional area at ports A and B** 参数。
- ρ¯ 为平均流体密度。
- *Δp* 为阀两端的压差 *pA* – *pB*。

临界压差 *Δpcrit* 是由 **Critical Reynolds number** 参数 *Recrit* 确定的压差。该参数表示层流与湍流之间的流态转变点。模块按以下公式计算临界压差：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

压力损失 *PRloss* 描述由于面积减小而导致的阀内压力降低。模块按以下公式计算压力损失：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

压力恢复描述由于面积增大而导致的阀内正向压力变化。当您将 **Pressure recovery** 设置为 `Off` 时，模块将 *PRloss* 设置为 1。

模块使用开口参数化和阀开启动力学来计算 *Avalve*。

### 阀门开度参数化

将 **开口参数化** 设置为 `Linear` 时，常开阀的阀口面积为

Avalve=p^(Aleak−Amax)+Amax.

下图展示了模块如何采用线性参数化控制常开阀的开口面积。

采用线性参数化时，常开阀的端口 X 和 Y 之间的压差与开口面积的关系

对于常闭阀，模块使用

Avalve=p^(Amax−Aleak)+Aleak.

下图展示了模块如何采用线性参数化控制常闭阀的开口面积。

采用线性参数化时，常闭阀的端口 X 和 Y 之间的压差与开口面积的关系

归一化压力 p^ 为

p^=pcontrol−psetpmax−pset.

在线性参数化中，当阀门处于接近开启或接近关闭的位置时，可以通过调整 **平滑因子** 参数来保持仿真的数值鲁棒性。如果 **平滑因子** 参数非零，模块会在 *pset* 和 *pmax* 之间对控制压力进行平滑饱和处理。有关详细信息，请参阅数值平滑。

将 **开口参数化** 设置为 `Tabulated` 时，*Aleak* 和 *Amax* 分别为 **开口面积向量** 参数中的第一个和最后一个参数。模块将开口面积计算为

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol* 是控制压力，即端口 **X** 和 **Y** 之间的压差。
- *pcontrol,TLU,ref*
  = *pTLU* +
  *poffset*。
- *pTLU* 是 **压差向量** 参数。
- *poffset* 是内部压力偏移量，使阀门在 *pcontrol,TLU,ref* =
  *pset* 时开始关闭。
- *ATLU* 是 **开口面积向量** 参数。

下图展示了模块如何采用表格参数化控制常开阀的开口面积。

采用表格参数化时，常开阀的端口 X 和 Y 之间的压差与开口面积的关系

下图展示了模块如何采用表格参数化控制常闭阀的开口面积。

采用表格参数化时，常闭阀的端口 X 和 Y 之间的压差与开口面积的关系

### 开启动态特性

将 **开启动态特性** 设置为 `On` 时，模块会引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。模块根据 **开启时间常数** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，模块不对 **开启动态特性** 建模。对于线性参数化，当节流孔处于接近关闭或接近开启的位置时，**平滑因子** 参数的非零值可提供额外的数值稳定性。

模块根据 **开口参数化** 参数计算稳态动态特性，该计算基于控制压力 *pcontrol*。

### 故障

要对故障进行建模，请在 **故障** 部分中，点击要建模的故障旁边的 **添加故障** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Simscape 故障简介。

您可以将 **故障时的开口面积** 参数设置为：

- `Closed` — 阀口面积停止变化并保持在其最小值，具体取决于 **开口参数化** 参数的设置：

  - `Linear` — 阀口面积停止变化并保持在 **泄漏面积** 参数的值。
  - `Tabulated` — 阀口面积停止变化并保持在 **开口面积向量** 参数的最小元素。
- `Open` — 阀口面积停止变化并保持在其最大值，具体取决于 **开口参数化** 参数的设置：

  - `Linear` — 阀口面积停止变化并保持在 **最大开口面积** 参数的值。
  - `Tabulated` — 阀口面积停止变化并保持在 **开口面积向量** 参数的最大元素。
- `Maintain last value` — 阀口面积停止变化并保持在触发发生时的阀开口面积。

由于阀口面积在极值处采用数值平滑，模块使用的最小面积大于泄漏面积，最大面积小于 **最大孔口面积** 参数的值。此影响与您应用的平滑程度成正比。

故障触发后，阀口面积在剩余的仿真过程中保持为故障状态下的面积。
