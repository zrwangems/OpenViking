---
type: simulink-block
title: 'Y-Junction (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'yjunctionil'
documentation_source_path: 'ref/yjunctionil.html'
language: zh-CN
chinese_source: worker-translation
---

# Y-Junction (IL)

## 端口

### 守恒

### **A** — 液体端口 等温液体

与连接处的液体入口或出口关联的等温液体守恒端口。

### **B** — 液体端口 等温液体

与连接处的液体入口或出口关联的等温液体守恒端口。

### **C** — 液体端口 等温液体

与连接处的液体入口或出口关联的等温液体守恒端口。

## 参数

### **主管路面积 (A-B)** — 端口 A 和 B 之间的横截面积 `0.01 m^2` (default) | positive scalar

端口 **A** 和 **B** 之间连接管的面积。

### **侧支路面积 (C)** — 侧支路的横截面积 `0.004` `m^2` (default) | positive scalar

端口 **C** 与主管路之间连接管的面积。

### **损失系数模型** — 损失系数类型 `Idel'chik correlation` (default) | `Custom`

连接处损失系数模型。将此参数设置为 `Custom`，以指定每个流动路径段各自的分流和汇流损失系数。

### **损失系数配置变化时间常数** — 平滑函数的时间尺度 `0.0001 s` (default) | positive scalar

平滑函数的时间尺度。使用此参数可在流动反向期间调整模块动态行为，以确保平滑过渡。

### **临界 Reynolds 数** — 层流的 Reynolds 数上限 `150` (default) | positive scalar

通过连接处的层流的 Reynolds 数上限。

### **零流量阈值 Reynolds 数** — 对应于停滞流动的 Reynolds 数 `10` (default) | positive scalar

模块用于计算流动停滞阈值的 Reynolds 数。模块使用此阈值来减少仿真期间的数值抖动。此参数没有物理意义，但必须相对于预期质量流量值足够小。

### **连接处夹角 (A-C)** — 侧支路的偏移角 `45` `deg` (default) | scalar between 15 and 60

侧支路相对于主管路的偏移角。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Idel'chik correlation`。

### **用于系数计算的最小有效流量比** — 用于系数计算的流量比限制 `0.2` (default) | positive scalar

模块用于计算损失系数的任何流量比的最小值。如果流量比低于此限制，则饱和于此值。模块使用此参数来限制支路之间流量大小差异的影响，并在某一支路的流量显著小于其他支路时提高数值稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Idel'chik correlation`。

### **平滑因子** — 数值平滑因子 `0.01` (default) | scalar between 0 and 1

连续平滑因子，当流动响应接近 **用于系数计算的最小有效流量比** 参数指定的限制时，引入一层逐渐变化。将此参数设置为小于 1 的非零值，以提高仿真稳定性。

仅当模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Idel'chik correlation`。

### **流体惯性** — 对流体惯性建模的选项 `off` (default) | `on`

是否对流体惯性建模，这会在流动反向期间降低模块数值问题的风险。除非数值上必要，否则避免对流体惯性建模，因为这会增加计算成本。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Idel'chik correlation`。

### **当流动配置无效时报告** — 无效流动配置的仿真警告模式 `None` (default) | `Warning` | `Error`

有效流动配置之外运行工况的仿真警告模式。如果选择 `Warning`，模块会为有效流动配置之外的情况生成警告。该警告不会导致仿真停止。如果选择 `Error`，则对于有效流动配置之外的情况，仿真将停止。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Idel'chik correlation`。

### **主管路汇流损失系数** — A 和 B 之间的汇流损失系数 `1.12` (default) | positive scalar

用于端口 **A** 和 **B** 之间汇流压力损失计算的损失系数。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom`。

### **主管路分流损失系数** — A 和 B 之间的分流损失系数 `1.12` (default) | positive scalar

用于端口 **A** 和 **B** 之间分流压力损失计算的损失系数。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom`。

### **侧支路汇流损失系数** — C 与主管路之间的汇流损失系数 `1.12` (default) | positive scalar

用于端口 **C** 与主管路之间汇流压力损失计算的损失系数。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom`。

### **侧支路分流损失系数** — C 与主管路之间的分流损失系数 `1.12` (default) | positive scalar

用于端口 **C** 与主管路之间分流压力损失计算的损失系数。

#### 依赖关系

要启用此参数，请将 **损失系数模型** 设置为 `Custom`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：稳健性改进使模块能够更平滑地在 mode chart 状态之间切换

Y-Junction (IL) 模块新增了参数和功能，使该模块能够更平滑地在 mode chart 中的状态之间切换。调整 **损失系数配置变化时间常数** 参数以控制平滑函数的时间尺度。使用 **零流量阈值 Reynold 数** 参数为停滞流动计算非零质量流量阈值。现在还可以选择对流体惯性建模，这会在流动反向期间降低模块数值问题的风险。

流动反向期间的结果可能与之前的版本不同。稳态条件下的行为没有变化。

## 描述

等温液体系统中的 Y 型接头

Y-Junction (IL) 模块在等温液体网络中建模由主管路和侧支路组成的 Y 型接头。端口 **A** 和 **B** 之间的路径是主管路。端口 **A** 和 **C** 之间或端口 **B** 和 **C** 之间的路径是侧支路。

### 流动方向

当通过端口 **C** 的流动汇入主流时，流动为*汇流*。当支路流动从主流分流时，流动为*分流*。

模块使用 mode chart 确定为给定流动配置的每个损失系数。此表描述了当 **损失系数模型** 参数为 `Custom` 时的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| 停滞 | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |
| 从节点 A 分流 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *Kmain,div* | *Kside,div* |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| 汇流至节点 A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *Kmain,conv* | *Kside,conv* |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| 汇流至节点 C（支路） | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | (*Kmain,conv* + *Kside,conv*)/2 | (*Kmain,conv* + *Kside,conv*)/2 | 0 |
| 从节点 C（支路）分流 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | (*Kmain,div* + *Kside,div*)/2 | (*Kmain,div* + *Kside,div*)/2 | 0 |

此表描述了当 **损失系数模型** 参数为 `Idel'chik correlation` 时的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| 停滞 | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |
| 从节点 A 分流 — 无效 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | 1 | 1 |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| 汇流至节点 A — 无效 | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | 1 | 1 |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| 汇流至节点 C（支路）— 无效 | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | 1 | 1 | 0 |
| 从节点 C（支路）分流 — 无效 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | 1 | 1 | 0 |

在停滞流动中，质量流量条件不匹配任何已定义的流动场景。允许在仿真开始时出现停滞流动，但模块在达到另一模式后不会恢复到停滞流动。质量流量阈值（即管道中的流动开始反向的点）为

m˙thresh=Recυρ¯π4Amin,

其中：

- *Re*c 是 **临界 Reynolds 数** 参数，超过该值后开始过渡流态。
- *ν* 是流体黏度。
- ρ¯ 是平均流体密度。
- *Amin* 是管道连接处中的最小横截面积。

### Idel'chik 关联式系数模型

当将 **损失系数模型** 参数设置为 `Idel'chik correlation` 时，模块根据 [1] 计算管道损失系数。

**流动配置**

模块支持从端口 **A** 和 **B** 的主管路与从端口 **C** 的侧支路之间的两种流动配置。侧支路相对于主管路偏移一个角度 *α*，即 **连接处夹角 (A-C)** 参数的值。

在汇流中，流动从端口 **A** 和 **C** 进入，并从端口 **B** 流出。

在分流中，流动从端口 **B** 进入，并从端口 **A** 和 **C** 流出。

您可以使用 **当流动配置无效时报告** 参数控制模块在禁止的流动配置中的行为。如果将 **当流动配置无效时报告** 参数设置为 `None` 或 `Warning`，模型会在禁止的流动配置中继续运行，但结果可能不正确。

**汇流**

对于汇流，模块使用假设主管路面积恒定的简化 Idel'chik 版本，计算端口 **C** 和 **B** 之间侧支路的损失系数。侧支路的损失系数为

Kside,conv=[1+(m˙Cm˙BABAC)2−2(ABAA)(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][m˙Cm˙BACAB]−2,

其中：

- m˙A,m˙B,m˙C 分别是端口 **A**、**B** 和 **C** 的质量流量。
- *AA*、*AB*、*AC* 分别是端口 **A**、**B** 和 **C** 的拟合系数。

模块使用假设主管路面积恒定且 QC=QB+QS 的简化 Idel'chik 版本，计算端口 **A** 和 **B** 之间主管路的损失系数，其中 *Q* 是通过指定端口的体积流量。主管路的损失系数为

Kmain,conv=[1−(1−m˙Cm˙B)2−2∗cosα∗ABAC(m˙Cm˙B)2][1−(m˙Cm˙B)2]−1.

**分流**

对于分流，模块将端口 **C** 和 **B** 之间侧支路的损失系数计算为

Kside,div=A′[1+(m˙Cm˙BABAC)2−2∗cosα∗m˙Cm˙BABAC][m˙Cm˙BACAB]−2,

其中

A'=12[1+tanh(4(RA′−0.8)0.8)]+0.92[1−tanh(4(RA′−0.8)0.8)]

以及

RA′=m˙C2+m˙thresh2m˙B2+m˙thresh2.

模块将端口 **A** 和 **B** 之间主管路的损失系数计算为

Kmain,div=0.4(1−m˙Am˙BABAA)2(m˙Am˙B)−2.

### 自定义 Y-Junction

当将 **损失系数模型** 参数设置为 `Custom` 时，模块根据用户定义的汇流和分流损失参数以及每个端口处的质量流量，计算每个端口处的管道损失系数 *K*。您必须分别将 *Kmain,conv*、*Kmain,div*、*Kside,conv* 和 *Kside,div* 指定为 **主管路汇流损失系数**、**主管路分流损失系数**、**侧支路汇流损失系数** 和 **侧支路分流损失系数** 参数。Y 型接头的自定义损失系数模型行为与自定义 T 型接头相同。

### 质量和动量平衡

模块在连接处守恒质量，使得

m˙A+m˙B+m˙C=0.

通过管道连接处的流动遵循端口 **A**、**B** 和 **C** 之间的动量守恒方程：

pA−pI=IA+KA2ρ¯Amain2m˙Am˙A2+m˙thresh2pB−pI=IB+KB2ρ¯Amain2m˙Bm˙B2+m˙thresh2pC−pI=IC+KC2ρ¯Aside2m˙Cm˙C2+m˙thresh2

其中 *I* 表示流体惯性，并且

IA=m¨Aπ⋅AsideAmainIB=m¨Bπ⋅AsideAmainIC=m¨Cπ⋅AmainAside

*Amain* 是 **主管路面积 (A-B)** 参数，*Aside* 是 **侧支路面积 (C)** 参数。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
