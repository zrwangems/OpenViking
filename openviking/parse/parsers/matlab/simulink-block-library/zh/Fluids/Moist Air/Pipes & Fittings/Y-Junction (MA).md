---
type: simulink-block
title: 'Y-Junction (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'yjunctionma'
documentation_source_path: 'ref/yjunctionma.html'
language: zh-CN
chinese_source: worker-translation
---

# Y-Junction (MA)

## 端口

### 守恒端口

### **A** — 湿空气端口 moist air

与连接处液体入口或出口相关联的湿空气守恒端口。

### **B** — 湿空气端口 moist air

与连接处液体入口或出口相关联的湿空气守恒端口。

### **C** — 湿空气端口 moist air

与连接处液体入口或出口相关联的湿空气守恒端口。

## 参数

### **Main branch area (A-B)** — 端口 A 和 B 之间的横截面积 `0.01 m^2`（默认）| 正标量

端口 **A** 和 **B** 之间连接管的面积。

### **Side branch area (C)** — 侧支路的横截面积 `0.004` `m^2`（默认）| 正标量

端口 **C** 与主管路之间连接管的面积。

### **Loss coefficient model** — 损失系数类型 `Idel'chik correlation`（默认）| `Custom`

连接处损失系数模型。将此参数设置为 `Custom`，以为每个流路段指定单独的分流和汇流损失系数。

### **Loss coefficient configuration change time constant** — 平滑函数的时间尺度 `0.0001 s`（默认）| 正标量

平滑函数的时间尺度。使用此参数，通过调整流量反转期间的模块动态行为来确保平滑过渡。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换的压力比 `0.999`（默认）| 正标量

湿空气流动在层流和湍流状态之间转换时的压力比。

### **Zero-flow threshold pressure ratio** — 对应于停滞流动的压力比 `0.999999`（默认）| 正标量

模块用于计算流动停滞阈值的压力比。模块使用此阈值来减少仿真期间的数值抖动。

### **Junction angle between (A-C)** — 侧支路的偏置角度 `45` `deg`（默认）| 介于 15 和 60 之间的正标量

侧支路相对于主管路的偏置角度。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Minimum valid flow ratio for coefficient calculation** — 系数计算的流量比限制 `0.2`（默认）| 正标量

模块用于计算损失系数的任何流量比的最小值。如果流量比低于此限制，则饱和于此值。模块使用此参数来限制支路之间流量大小差异的影响，并在某一支路的流量显著小于其他支路时提高数值稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 介于 0 和 1 之间的标量

连续平滑因子，当流动响应接近 **Minimum valid flow ratio for coefficient calculation** 参数指定的限制时，引入一层渐变。将此参数设置为小于 1 的非零值以提高仿真的稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Fluid inertia** — 用于对流体惯性建模的选项 `off`（默认）| `on`

是否对流体惯性建模，这可降低流量反转期间模块出现数值问题的风险。除非数值上必要，否则避免对流体惯性建模，因为这会增加计算成本。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Report when flow configuration is invalid** — 无效流动配置的仿真警告模式 `None`（默认）| `Warning` | `Error`

工作条件超出有效流动配置时的仿真警告模式。如果选择 `Warning`，模块会为超出有效流动配置的条件生成警告。该警告不会导致仿真停止。如果选择 `Error`，仿真将在条件超出有效流动配置时停止。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Idel'chik correlation`。

### **Main branch converging loss coefficient** — A 和 B 之间的汇流损失系数 `1.12`（默认）| 正标量

端口 **A** 和 **B** 之间汇流的压力损失计算用损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Main branch diverging loss coefficient** — A 和 B 之间的分流损失系数 `1.12`（默认）| 正标量

端口 **A** 和 **B** 之间分流的压力损失计算用损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Side branch converging loss coefficient** — C 与主管路之间的汇流损失系数 `1.12`（默认）| 正标量

端口 **C** 与主管路之间汇流的压力损失计算用损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Side branch diverging loss coefficient** — C 与主管路之间的分流损失系数 `1.12`（默认）| 正标量

端口 **C** 与主管路之间分流的压力损失计算用损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过连接处的层流的上限雷诺数。

## 所属库

Simscape / Fluids / Moist Air / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

湿空气网络中的 Y 形连接处

Y-Junction (MA) 模块对湿空气网络中由主管路和侧支路组成的 Y 形连接处进行建模。端口 **A** 和 **B** 之间的路径为主管路。端口 **A** 和 **C** 之间或端口 **B** 和 **C** 之间的路径为侧支路。侧支路以 **Junction angle between (A-C)** 参数值指定的角度从主管路延伸。

### 流动方向

当通过端口 **C** 的流动汇入主流时，流动为*汇流*。当支路流动从主流分流时，流动为*分流*。

模块使用模式图来确定给定流动配置下的每个损失系数。此表描述了当 **Loss coefficient model** 参数为 `Custom` 时的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| 停滞 | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |
| 从节点 A 分流 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *Kmain,div* | *Kside,div* |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| 汇流至节点 A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *Kmain,conv* | *Kside,conv* |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| 汇流至节点 C（支路） | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | (*Kmain,conv* + *Kside,conv*)/2 | (*Kmain,conv* + *Kside,conv*)/2 | 0 |
| 从节点 C（支路）分流 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | (*Kmain,div* + *Kside,div*)/2 | (*Kmain,div* + *Kside,div*)/2 | 0 |

此表描述了当 **Loss coefficient model** 参数为 `Idel'chik correlation` 时的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| 停滞 | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |
| 从节点 A 分流 — 无效 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | 1 | 1 |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| 汇流至节点 A — 无效 | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | 1 | 1 |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| 汇流至节点 C（支路）— 无效 | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | 1 | 1 | 0 |
| 从节点 C（支路）分流 — 无效 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | 1 | 1 | 0 |

在停滞流动中，质量流量条件不匹配任何已定义的流动场景。停滞流动允许在仿真开始时出现，但模块在达到其他模式后不会恢复到停滞流动。质量流量阈值（即管道中流动开始反向的点）为

m˙thresh=Recυρ¯π4Amin，

其中：

- *Re*c 是 **Critical Reynolds number** 参数，超过该值即开始过渡流态。
- *ν* 是流体粘度。
- ρ¯ 是平均流体密度。
- *Amin* 是管道连接处中最小的横截面积。

### Idel'chik 关联式系数模型

当将 **Loss coefficient model** 参数设置为 `Idel'chik correlation` 时，模块根据 [2] 计算管道损失系数。

**流动配置**

模块支持端口 **A** 和 **B** 之间的主管路与端口 **C** 的侧支路之间的两种流动配置。侧支路以角度 *α* 从主管路偏置，该角度为 **Junction angle between (A-C)** 参数的值。

在汇流中，流动从端口 **A** 和 **C** 进入，从端口 **B** 流出。

在分流中，流动从端口 **B** 进入，从端口 **A** 和 **C** 流出。

您可以使用 **Report when flow configuration is invalid** 参数来控制禁止流动配置下的模块行为。如果 **Report when flow configuration is invalid** 参数设置为 `None` 或 `Warning`，模型将继续在禁止的流动配置下运行，但结果可能不正确。

**汇流**

对于汇流，模块使用 Idel'chik 的简化版本计算端口 **C** 和 **B** 之间侧支路的损失系数，该版本假设主管路的面积恒定。侧支路的损失系数为

Kside,conv=[1+(m˙Cm˙BABAC)2−2(ABAA)(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][m˙Cm˙BACAB]−2，

其中：

- m˙A,m˙B,m˙C 分别是端口 **A**、**B** 和 **C** 的质量流量。
- *AA*、*AB*、*AC* 分别是端口 **A**、**B** 和 **C** 的拟合系数。

模块使用 Idel'chik 的简化版本计算端口 **A** 和 **B** 之间主管路的损失系数，该版本假设主管路面积恒定且 QC=QB+QS，其中 *Q* 是通过指定端口的体积流量。主管路的损失系数为

Kmain,conv=[1−(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][1−(m˙Cm˙B)2]−1。

**分流**

对于分流，模块计算端口 **C** 和 **B** 之间侧支路的损失系数为

Kside,div=A′[1+(m˙Cm˙BABAC)2−2∗cosα∗m˙Cm˙BABAC][m˙Cm˙BACAB]−2，

其中

A'=12[1+tanh(4(RA′−0.8)0.8)]+0.92[1−tanh(4(RA′−0.8)0.8)]

以及

RA′=m˙C2+m˙thresh2m˙B2+m˙thresh2。

模块计算端口 **A** 和 **B** 之间主管路的损失系数为

Kmain,div=0.4(1−m˙Am˙BABAA)2(m˙Am˙B)−2。

### 自定义 Y 形连接处

当将 **Loss coefficient model** 参数设置为 `Custom` 时，模块根据用户定义的汇流和分流损失参数以及每个端口处的质量流量，计算每个端口处的管道损失系数 *K*。您必须分别将 *Kmain,conv*、*Kmain,div*、*Kside,conv* 和 *Kside,div* 指定为 **Main branch converging loss coefficient**、**Main branch diverging loss coefficient**、**Side branch converging loss coefficient** 和 **Side branch diverging loss coefficient** 参数。Y 形连接处的自定义损失系数模型行为与自定义 T 形连接处相同。

### 质量和动量平衡

模块在连接处守恒质量，使得

m˙A+m˙B+m˙C=0m˙wA+m˙wB+m˙wC=0m˙gA+m˙gB+m˙gC=0m˙dA+m˙dB+m˙dC=0

- *ṁi* 是给定端口 *i* 的混合物质量流量。
- m˙*wi* 是给定端口 *i* 的水蒸气质量流量。
- m˙*gi* 是给定端口 *i* 的示踪气体质量流量。
- m˙*di* 是给定端口 *i* 的水滴质量流量。

通过管道连接处的流动遵循端口 **A**、**B** 和 **C** 之间的动量守恒方程：

pA−pI=IA+KA2ρ¯Amain2m˙Am˙A2+m˙thresh2pB−pI=IB+KB2ρ¯Amain2m˙Bm˙B2+m˙thresh2pC−pI=IC+KC2ρ¯Aside2m˙Cm˙C2+m˙thresh2

其中 *I* 表示流体惯性，且

IA=m¨Aπ⋅AsideAmainIB=m¨Bπ⋅AsideAmainIC=m¨Cπ⋅AmainAside

*Amain* 是 **Main branch area (A-B)** 参数，*Aside* 是 **Side branch area (C)** 参数。

### 能量平衡

模块平衡能量，使得

ϕA+ϕB+ϕC=0，

其中：

- *ϕA* 是端口 **A** 的能量流量。
- *ϕB* 是端口 **B** 的能量流量。
- *ϕC* 是端口 **C** 的能量流量。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
