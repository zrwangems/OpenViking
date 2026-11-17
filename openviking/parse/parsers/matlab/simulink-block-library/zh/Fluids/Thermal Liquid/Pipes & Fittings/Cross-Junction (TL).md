---
type: simulink-block
title: 'Cross-Junction (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'crossjunctiontl'
documentation_source_path: 'ref/crossjunctiontl.html'
language: zh-CN
chinese_source: worker-translation
---

# Cross-Junction (TL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口（热液体）
  direction: conserving
- name: B
  summary: 液体端口（热液体）
  direction: conserving
- name: C
  summary: 液体端口（热液体）
  direction: conserving
- name: D
  summary: 液体端口（热液体）
  direction: conserving
```

### 守恒端口

### **A** — 液体端口（热液体）

与液体端口关联的热液体守恒端口。

### **B** — 液体端口（热液体）

与液体端口关联的热液体守恒端口。

### **C** — 液体端口（热液体）

与液体端口关联的热液体守恒端口。

### **D** — 液体端口（热液体）

与液体端口关联的热液体守恒端口。
## 参数
```yaml
parameters:
- name: Main line area (A,C)
  summary: 主管路面积 0.01 m^2（默认）| 正标量
  group: 接头属性
- name: Branch line area (B,D)
  summary: 支管路面积 0.01 m^2（默认）| 正标量
  group: 接头属性
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 接头属性
- name: Zero-flow threshold Reynolds number
  summary: 对应滞止流的雷诺数 10（默认）| 正标量
  group: 接头属性
- name: Loss coefficient configuration change time constant
  summary: 平滑函数的时间尺度 0.0001 s（默认）| 正标量
  group: 接头属性
- name: Minimum valid flow ratio for coefficient calculation
  summary: 系数计算的流量比限值 0.2（默认）| 正标量
  group: 接头属性
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 0 到 1 之间的标量
  group: 接头属性
- name: Fluid inertia
  summary: 用于对流体惯性建模的选项 off（默认）| on
  group: 接头属性
- name: Loss coefficient model
  summary: 损失系数类型 Idel'chik correlation（默认）| Custom
  group: 接头属性
- name: Report when flow configuration is invalid
  summary: 无效流动配置的仿真警告模式 None（默认）| Warning | Error
  group: 接头属性
- name: Diverging flow loss coefficients
  summary: 用于指定分流损失系数的选项 on（默认）| off
  group: 接头属性
- name: Converging flow loss coefficients
  summary: 用于指定汇流损失系数的选项 on（默认）| off
  group: 接头属性
- name: Perpendicular flow loss coefficients
  summary: 用于指定垂直流动损失系数的选项 off（默认）| on
  group: 接头属性
- name: Colliding flow loss coefficients
  summary: 用于指定碰撞流动损失系数的选项 off（默认）| on
  group: 接头属性
- name: Diverging flow straight loss coefficient
  summary: 分流直通损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 分流系数
- name: Diverging flow turning loss coefficient
  summary: 分流转向损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 分流系数
- name: Converging flow straight loss coefficient
  summary: 汇流直通损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 汇流系数
- name: Converging flow turning loss coefficient
  summary: 汇流转向损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 汇流系数
- name: 垂直流直通损失系数
  summary: 垂直流直通损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 垂直流动系数
- name: 垂直流转向流入损失系数
  summary: 垂直流转向流入损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 垂直流动系数
- name: 垂直流转向流出损失系数
  summary: 垂直流转向流出损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 垂直流动系数
- name: 碰撞流直通损失系数
  summary: 碰撞流直通损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 碰撞流系数
- name: 碰撞流转向损失系数
  summary: 碰撞流转向损失系数 [1.12, 1.12]（默认）| 正标量或向量
  group: 碰撞流系数
```

### 接头属性

### **Main line area (A,C)** — 主管路面积 `0.01` `m^2`（默认）| 正标量

从端口 **A** 到端口 **C** 的主流动路径的横截面积。

### **Branch line area (B,D)** — 支管路面积 `0.01` `m^2`（默认）| 正标量

从端口 **B** 到端口 **D** 的支路流动路径的横截面积。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过接头的层流的上限雷诺数。

### **Zero-flow threshold Reynolds number** — 对应滞止流的雷诺数 `10`（默认）| 正标量

模块用于计算流动滞止阈值的雷诺数。模块使用此阈值来减少仿真期间的数值抖动。此参数没有物理意义，但相对于预期的质量流量值必须很小。

### **Loss coefficient configuration change time constant** — 平滑函数的时间尺度 `0.0001 s`（默认）| 正标量

平滑函数的时间尺度。使用此参数通过在流动反向期间调节模块动态行为来确保平滑过渡。

### **Minimum valid flow ratio for coefficient calculation** — 系数计算的流量比限值 `0.2`（默认）| 正标量

模块用于计算损失系数的任何流量比的最小值。如果流量比低于此限值，则饱和于此值。模块使用此参数来限制支路之间流量大小差异的影响，并在某一支路的流量显著小于其他支路时提高数值稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 0 到 1 之间的标量

连续平滑因子，当流动响应接近 **Minimum valid flow ratio for coefficient calculation** 参数指定的限值时，引入一层渐变。将此参数设置为小于 1 的非零值以提高仿真稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Fluid inertia** — 用于对流体惯性建模的选项 `off`（默认）| `on`

是否对流体惯性建模，这可降低流动反向期间模块出现数值问题的风险。除非数值上必要，否则避免对流体惯性建模，因为这会增加计算成本。

### **Loss coefficient model** — 损失系数类型 `Idel'chik correlation`（默认）| `Custom`

接头损失系数模型。将此参数设置为 `Custom` 以指定每个流动路径段的单独分流和汇流损失系数。

### **Report when flow configuration is invalid** — 无效流动配置的仿真警告模式 `None`（默认）| `Warning` | `Error`

有效流动配置之外工况的仿真警告模式。如果选择 `Warning`，模块会为有效流动配置之外的工况生成警告。该警告不会导致仿真停止。如果选择 `Error`，仿真将在有效流动配置之外的工况下停止。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Diverging flow loss coefficients** — 用于指定分流损失系数的选项 `on`（默认）| `off`

是否指定分流损失系数。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Converging flow loss coefficients** — 用于指定汇流损失系数的选项 `on`（默认）| `off`

是否指定汇流损失系数。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Perpendicular flow loss coefficients** — 用于指定垂直流动损失系数的选项 `off`（默认）| `on`

是否指定垂直流动损失系数。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Colliding flow loss coefficients** — 用于指定碰撞流动损失系数的选项 `off`（默认）| `on`

是否指定碰撞流动损失系数。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### 分流系数

### **Diverging flow straight loss coefficient** — 分流直通损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

分流直通部分的损失系数。当将此参数指定为向量时，第一个元素表示端口 **A** 或 **C** 与节点 1 对齐时的损失系数。第二个元素表示端口 **B** 或 **D** 与节点 1 对齐时的情况。当使用标量时，模块在所有方向下行为相同。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom` 并选择 **Diverging flow loss coefficients**。

### **Diverging flow turning loss coefficient** — 分流转向损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

分流转向部分的损失系数。当将此参数指定为向量时，第一个元素表示端口 **A** 或 **C** 与节点 1 对齐时的损失系数。第二个元素表示端口 **B** 或 **D** 与节点 1 对齐时的情况。当使用标量时，模块在所有方向下行为相同。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom` 并选择 **Diverging flow loss coefficients**。

### 汇流系数

### **Converging flow straight loss coefficient** — 汇流直通损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

汇流直通部分的损失系数。当将此参数指定为向量时，第一个元素表示端口 **A** 或 **C** 与节点 1 对齐时的损失系数。第二个元素表示端口 **B** 或 **D** 与节点 1 对齐时的情况。当使用标量时，模块在所有方向下行为相同。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom` 并选择 **Converging flow loss coefficients**。

### **Converging flow turning loss coefficient** — 汇流转向损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

汇流转向部分的损失系数。当将此参数指定为向量时，第一个元素表示端口 **A** 或 **C** 与节点 1 对齐时的损失系数。第二个元素表示端口 **B** 或 **D** 与节点 1 对齐时的情况。当使用标量时，模块在所有方向下行为相同。

#### 依赖

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom` 并选择 **Converging flow loss coefficients**。

### 垂直流动系数

### **垂直流直通损失系数** — 垂直流直通损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

垂直流直通部分的损失系数。
当您将此参数指定为向量时，第一个元素
表示端口 **A** 或
**C** 与节点 1 对齐时的损失系数。第二个元素
表示端口 **B** 或 **D**
与节点 1 对齐时的情况。当您使用标量时，该模块在所有方向上的行为相同。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom` 并选择
**垂直流损失
系数**。

### **垂直流转向流入损失系数** — 垂直流转向流入损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

垂直流中流向转为流入的损失系数。当您
将此参数指定为向量时，第一个元素表示
端口 **A** 或
**C** 与节点 1 对齐时的损失系数。第二个元素
表示端口 **B** 或 **D**
与节点 1 对齐时的情况。当您使用标量时，该模块在所有方向上的行为相同。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom` 并选择
**垂直流损失
系数**。

### **垂直流转向流出损失系数** — 垂直流转向流出损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

垂直流中流向转为流出的损失系数。当您
将此参数指定为向量时，第一个元素表示
端口 **A** 或
**C** 与节点 1 对齐时的损失系数。第二个元素
表示端口 **B** 或 **D**
与节点 1 对齐时的情况。当您使用标量时，该模块在所有方向上的行为相同。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom` 并选择
**垂直流损失
系数**。

### 碰撞流系数

### **碰撞流直通损失系数** — 碰撞流直通损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

碰撞流直通部分的损失系数。当您
将此参数指定为向量时，第一个元素表示
端口 **A** 或
**C** 与节点 1 对齐时的损失系数。第二个元素
表示端口 **B** 或 **D**
与节点 1 对齐时的情况。当您使用标量时，该模块在所有方向上的行为相同。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom` 并选择
**碰撞流损失系数**。

### **碰撞流转向损失系数** — 碰撞流转向损失系数 `[1.12, 1.12]`（默认）| 正标量或向量

碰撞流转向部分的损失系数。当您将此
参数指定为向量时，第一个元素表示损失系数
当端口 **A** 或 **C** 与
节点 1 对齐时。第二个元素表示当端口 **B**
或 **D** 与节点 1 对齐时的情况。当您使用标量时，该模块
在所有方向上的行为相同。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom` 并选择
**碰撞流损失系数**。
## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2024b：鲁棒性改进使模块能够在模式图状态之间更平滑地切换

Cross-Junction (TL) 模块具有新的参数和
功能，使模块能够在模式图中更平滑地在状态之间切换。
调整 **损失系数配置变化时间常数**
参数以控制平滑函数的时间尺度。使用 **零流量
阈值雷诺数** 参数来计算停滞流的非零质量流量
阈值。您现在还可以选择性地对流体惯性进行建模，这降低了
在流动反转期间出现模块数值问题的风险。

流动反转期间的结果可能与之前的版本不同。稳态
条件下的行为没有改变。

### R2023b：新的损失系数模型

使用 **损失系数模型** 参数来控制接头损失
系数模型。将 **损失系数模型** 设置为
`Idel'chik correlation` 以使用新的解析损失
系数模型。要使用与之前版本相同的模块行为，请将
**损失系数模型** 设置为
`Custom`。

## 描述

热液网络中的十字接头

Cross-Junction (TL) 模块表示热液网络中的四通
接头。该模块根据每个端口处的流动方向抽象流体相互作用，
其中端口 **A** 和
**C** 是主管线，端口 **B** 和
**D** 是支管线。

### 质量、动量和能量平衡

该模块守恒质量，使得

m˙A+m˙B+m˙C+m˙D=0，

其中 *ṁi* 是给定端口 *i* 的质量
流量。

该模块确定使用哪个系数和向量元素，然后计算
压力差以守恒动量，使得

pi−p1=Ii+ki2m˙im˙i2+m˙threshold2ρ¯Ai2，

其中：

- ρ¯ 是平均流体密度。
- *pi* 是给定端口 *i* 的
  压力。
- *p1* 是节点
  1 处的压力。
- *ki* 是该模块分配给给定端口 *i* 的流量系数。
  **损失系数模型** 参数指定
  用于计算 *ki* 的模块方法。
- *Ii* 是给定端口 *i* 的流体惯性。

该模块计算每个端口的惯性为

IA=m¨AπAsideAmainIB=m¨BπAmainAsideIC=m¨CπAsideAmainID=m¨DπAmainAside

其中 *Amain* 是
**主管线面积 (A,C)** 参数的值，
*Aside* 是
**支管线面积 (B,D)** 参数的值。

该模块守恒能量，使得

φA+φB+φC+φD=0。

### Idel'chik Correlation Coefficient Model

当您将 **Loss coefficient model** 参数设置为
`Idel'chik correlation` 时，模块根据 [1] 计算管道
损失系数。
Idel'chik 模型仅支持流向端口 **C** 的汇流或
从端口 **C** 流出的分流。为获得预期结果，请根据模型流体
网络的预期流动配置正确调整模块方向。

模块将接头视为关于水平和垂直平面均对称，因此 *AA* =
*AC* 是 **Main line area (A,C)**
参数的值，*AB* =
*AD* 是 **Branch line area (B,D)**
参数的值，其中 *AA,B,C,D* 是对应端口
的面积。

两种 Idel'chik 流动配置示意图：分流和汇流

在禁止的流动几何情况下，您可以通过
**Report when flow configuration is invalid** 参数控制模块行为。
如果 **Report when flow configuration is invalid** 参数为
`None` 或 `Warning`，模型
会在禁止的流动配置下继续运行，但结果可能不
正确。

**流向端口 C 的汇流**

当流动汇流至端口 **C** 时，端口 **A** 和 **C** 的损失
系数为

kA=(1+(m˙Am˙C)2−(m˙Am˙C)21+m˙Am˙C(0.75+0.25m˙Am˙C)2)(m˙Am˙CACAA)−2kC=0

端口 **B** 和
**D** 的汇流损失系数为

kB=(1+(m˙Bm˙CACAB)2−8(m˙Bm˙C)2[m˙Cm˙B−(1+m˙Dm˙B)]24−(1+m˙Dm˙B)m˙Bm˙C)(m˙Bm˙CACAB)−2kD=(1+(m˙Dm˙CACAD)2−8(m˙Dm˙C)2[m˙Cm˙D−(1+m˙Bm˙D)]24−(1+m˙Bm˙D)m˙Dm˙C)(m˙Dm˙CACAD)−2

**从端口 C 流出的分流**

当流动从端口 **C** 分流时，端口 **A** 和 **C** 的损失
系数为

kA=0.4(m˙Cm˙A−1)2kC=0

端口 **B** 和
**D** 的分流损失系数为

kB=A'(m˙Cm˙BABAC+1)2kD=A'(m˙Cm˙DADAC+1)2

其中当 m˙Bm˙CACAB≤0.8 或 m˙Dm˙CACAD≤0.8 时，*A'=1*；当 m˙Bm˙CACAB>0.8 或 m˙Dm˙CACAD>0.8 时，*A'≈0.9*。模块使用双曲正切
函数平滑 *A' =
1* 和 *A' = 0.9* 之间的过渡。

根据 [1]，这些损失系数仅适用于分流
流动，且侧支管直径与主管直径之比
小于或等于 `2/3`。然而，当比值高于 `2/3` 时，预期误差通常足够低，因此模块
继续使用上述损失系数。

### Custom Cross-Junction

当您将 **Loss coefficient model** 参数设置为 `Custom` 时，模块使用用户定义的损失参数来描述每个端口处的管道损失系数。

对于自定义十字交叉接头，模块允许四种配置：分流、汇流、垂直流和碰撞流：

- 分流 — 流体从节点 1 进入，从节点 2、3 和 4 流出。
- 汇流 — 流体从节点 1、2 和 4 进入，从节点 3 流出。
- 垂直流 — 流体从节点 1 和 2 进入，从节点 3 和 4 流出。
- 碰撞流 — 流体从节点 1 和 3 进入，从节点 2 和 4 流出。

此图展示了这些配置。

四种流动配置示意图：分流、汇流、垂直流和碰撞流

模块将接头视为关于水平和垂直平面均对称，使得 *A1* = *A3* 且 *A2* = *A4*，其中 *A1,2,3,4* 是图中对应端口的面积。利用这种对称性，模块假设在分流、汇流和碰撞流期间，从 1 到 2 和从 1 到 4 的损失系数相同。

在仿真期间，模块持续检查每个端口处的流动方向，并将结果与四种可能的流动配置进行比较。当模块确定流动配置后，它会调整每个端口对应的节点。例如，当模块经历分流时，流体从端口 **A** 进入并从端口 **B**、**C** 和 **D** 流出，它将节点 1 分配给端口 **A**，如图中第一个面板所示。其他面板显示了从 **A** 以外的端口进入的分流所分配的节点。

分流的四种可能方向，其中入口点为参考节点，可以发生在任何端口。

对于自定义十字交叉接头，所有四种流动配置可以在仿真期间在同一模块中发生。您只需为模块经历的每种工况提供参数。如果您使用双元素向量来指定流动系数，模块将根据节点 1 是与主管线还是支管线对齐来使用第一个或第二个元素。第一个元素对应于节点 1 在端口 **A** 或 **C** 处，第二个元素对应于节点 1 在端口 **B** 或 **D** 处。

此表描述了用于确定损失系数的每种运行模式的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *ṁD* | *kA* | *kB* | *kC* | *kD* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 从节点 A 分流 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *kdiv,turning,main* | *kdiv,straight,main* | *kdiv,turning,main* |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | *kdiv,turning,side* | 0 | *kdiv,turning,side* | *kdiv,straight,side* |
| 从节点 C 分流 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kdiv,straight,main* | *kdiv,turning,main* | 0 | *kdiv,turning,main* |
| 从节点 D 分流 | <*-ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kdiv,turning,side* | *kdiv,straight,side* | *kdiv,turning,side* | 0 |
| 汇流至节点 A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *kconv,turning,main* | *kconv,straight,main* | *kconv,turning,main* |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | *kconv,turing,side* | 0 | *kconv,turing,side* | *kconv,straight,side* |
| 汇流至节点 C | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kconv,straight,main* | *kconv,turning,main* | 0 | *kconv,turning,main* |
| 汇流至节点 D | >*ṁthresh* | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kconv,turing,side* | *kconv,straight,side* | *kconv,turing,side* | 0 |
| 主管入口 A 的垂直流 | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *kperp,turning in,main* | *kperp,straight,main* | *kperp,turning out,main* |
| 主管入口 B 的垂直流 | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *kperp,turning out,side* | 0 | *kperp,turning in,side* | *kperp,turning straight,side* |
| 主管入口 C 的垂直流 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | *kperp,straight,main* | *kperp,turning out,main* | 0 | *kperp,turning in,main* |
| 主管入口 D 的垂直流 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kperp,turning in,side* | *kperp,turning straight,side* | *kperp,turning out,side* | 0 |
| 从主管到支管的碰撞流 | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | 0 | *kcoll,turning,main* | *kcoll,straight,main* | *kcoll,turning,main* |
| 从支管到主管的碰撞流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *kcoll,turning,side* | 0 | *kcoll,turning,side* | *kcoll,straight,side* |
| 停滞 | – | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |

当质量流量条件不匹配任何已定义的流动场景时，流动为停滞。模块使用以下参数来计算流动系数：

- *kdiv,straight,main* 和 *kdiv,straight,side* 分别是 **Diverging flow straight loss coefficient** 参数的第一个和第二个元素。
- *kdiv,turning,main* 和 *kdiv,turning,side* 分别是 **Diverging flow turning loss coefficient** 参数的第一个和第二个元素。
- *kconv,straight,main* 和 *kconv,straight,side* 分别是 **Converging flow straight loss coefficient** 参数的第一个和第二个元素。
- *kconv,turning,main* 和 *kconv,turning,side* 分别是 **Converging flow turning loss coefficient** 参数的第一个和第二个元素。
- *kperp,straight,main* 和 *kperp,straight,side* 分别是 **Perpendicular flow straight loss coefficient** 参数的第一个和第二个元素。
- *kperp,turning in,main* 和 *kperp,turning in,side* 分别是 **Perpendicular flow straight loss coefficient** 参数的第一个和第二个元素。
- *kperp,turning out,main* 和 *kperp,turning out,side* 分别是 **Perpendicular flow straight loss coefficient** 参数的第一个和第二个元素。
- *kcoll,straight,main* 和 *kcoll,straight,side* 分别是 **Colliding flow straight loss coefficient** 参数的第一个和第二个元素。
- *kcoll,turning,main* 和 *kcoll,turning,side* 分别是 **Colliding flow turning loss coefficient** 参数的第一个和第二个元素。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
