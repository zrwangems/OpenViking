---
type: simulink-block
title: 'T-Junction (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'tjunctionma'
documentation_source_path: 'ref/tjunctionma.html'
language: zh-CN
chinese_source: worker-translation
---

# T-Junction (MA)

## 端口

### 守恒端口

### **A** — 液体端口湿空气

与交汇处液体入口或出口相关联的湿空气守恒端口。

### **B** — 湿空气端口湿空气

与交汇处液体入口或出口相关联的湿空气守恒端口。

### **C** — 湿空气端口湿空气

与交汇处液体入口或出口相关联的湿空气守恒端口。

## 参数

### **Main branch area (A-B)** — 端口 A 和 B 之间的横截面积 `0.01 m^2`（默认）| 正标量

端口 **A** 和 **B** 之间连接管的面积。

### **Side branch area (A-C, B-C)** — 侧支路的横截面积 `0.01 m^2`（默认）| 正标量

端口 **A** 和 **C** 之间以及端口 **B** 和 **C** 之间连接管的面积。

### **Loss coefficient model** — 损失系数类型 `Crane correlation`（默认）| `Rennels correlation` | `Custom` | `Constant Coefficients`

交汇处损失系数模型。将此参数设置为 `Custom`，以指定每个流动路径段的单独分流和汇流损失系数。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间过渡时的压力比 `0.999`（默认）| 正标量

湿空气流动在层流和湍流状态之间过渡时的压力比。

### **Zero-flow threshold pressure ratio** — 对应于停滞流动的压力比 `0.999999`（默认）| 正标量

模块用于计算流动停滞阈值的压力比。模块使用此阈值来减少仿真期间的数值振荡。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Crane correlation`、`Rennels correlation` 或 `Custom`。

### **Loss coefficient configuration change time constant** — 平滑函数的时间尺度 `0.0001 s`（默认）| 正标量

平滑函数的时间尺度。使用此参数通过在流动反向期间调整模块动态行为来确保平滑过渡。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Crane correlation`、`Rennels correlation` 或 `Custom`。

### **Junction radius of curvature** — 交汇处的曲率半径 `0.001 m`（默认）| 正标量

当 **Loss coefficient model** 设置为 `Rennels correlation` 时，用于计算损失系数的交汇处曲率半径。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Rennels correlation`。

### **Minimum valid flow ratio for coefficient calculation** — 系数计算的流量比限制 `0.2`（默认）| 正标量

模块用于计算损失系数的任何流量比的最小值。如果流量比低于此限制，则在此值处饱和。模块使用此参数来限制支路之间流量大小差异的影响，并在一个支路的流量显著小于其他支路时提高数值稳定性。

仅在模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Rennels correlation`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 0 到 1 之间的标量

连续平滑因子，当流动响应接近 **Minimum valid flow ratio for coefficient calculation** 参数指定的限制时，引入一层渐变变化。将此参数设置为小于 1 的非零值以提高仿真的稳定性。

仅在模型存在数值稳定性问题时才调整此设置。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Rennels correlation`。

### **Fluid inertia** — 模拟流体惯性的选项 `off`（默认）| `on`

是否模拟流体惯性，这可降低流动反向期间模块出现数值问题的风险。除非数值上必要，否则避免模拟流体惯性，因为它会增加计算成本。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Rennels correlation`。

### **Main branch converging loss coefficient** — A 和 B 之间的汇流损失系数 `1.12`（默认）| 正标量

端口 **A** 和 **B** 之间汇流的压力损失计算损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Main branch diverging loss coefficient** — A 和 B 之间的分流损失系数 `1.12`（默认）| 正标量

端口 **A** 和 **B** 之间分流的压力损失计算损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Side branch converging loss coefficient** — C 和主管线之间的汇流损失系数 `1.12`（默认）| 正标量

端口 **C** 和主管线之间汇流的压力损失计算损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Side branch diverging loss coefficient** — C 和主管线之间的分流损失系数 `1.12`（默认）| 正标量

端口 **C** 和主管线之间分流的压力损失计算损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Custom`。

### **Loss coefficient A** — 支路 A 的损失系数 `1`（默认）| 正标量

沿支路 A 流动的损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Constant Coefficients`。

### **Loss coefficient B** — 支路 B 的损失系数 `1`（默认）| 正标量

沿支路 B 流动的损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Constant Coefficients`。

### **Loss coefficient C** — 支路 C 的损失系数 `1`（默认）| 正标量

沿支路 C 流动的损失系数。

#### 依赖关系

要启用此参数，请将 **Loss coefficient model** 设置为 `Constant Coefficients`。

## 所属库

Simscape / Fluids / Moist Air / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

湿空气网络中的三通接头

T-Junction (MA) 模块表示一个三通管接头，其支路在端口 **C** 处以 90° 角连接到端口 **A** 和 **B** 之间的主管线。您可以指定自定义接头，或使用 Rennels 关联式或 Crane 关联式损失系数的接头。当 **Loss coefficient model** 设置为 `Custom` 时，您可以指定每个管段在汇流和分流流动时的损失系数。

### 流动方向

当 **Loss coefficient model** 参数为 `Crane correlation`、`Rennels correlation` 或 `Custom` 时，模块根据流动配置确定每个损失系数。当通过端口 **C** 的流动汇入主流时，流动为*汇流*。当支路流动从主流分流时，流动为*分流*。**A** 与 **I**（支路与主管线相交的点）之间以及 **B** 与 **I** 之间的流动方向必须一致，才能应用所有损失系数。如果不一致，如下图所示的后两个图所示，交汇处的损失将用汇流或分流的主流损失系数来近似。

T-Junction 模块可能的流动场景示意图。在汇流中，2 个垂直支路流动在中心节点汇合。在分流中，一个流动进入中心节点并分成另外两个垂直流动。对于流动损失，两个平行流动汇合或分流

模块使用模式图来确定给定流动配置的每个损失系数。下表描述了每种运行模式的条件和系数。

| 流动场景 | *ṁA* | *ṁB* | *ṁC* | *KA* | *KB* | *KC* |
| --- | --- | --- | --- | --- | --- | --- |
| 停滞 | – | – | – | 1 或最后有效值 | 1 或最后有效值 | 1 或最后有效值 |
| 从节点 A 分流 | >*ṁthresh* | <*-ṁthresh* | <*-ṁthresh* | 0 | *Kmain,div* | *Kside,div* |
| 从节点 B 分流 | <*-ṁthresh* | >*ṁthresh* | <*-ṁthresh* | *Kmain,div* | 0 | *Kside,div* |
| 汇流至节点 A | <*-ṁthresh* | >*ṁthresh* | >*ṁthresh* | 0 | *Kmain,conv* | *Kside,conv* |
| 汇流至节点 B | >*ṁthresh* | <*-ṁthresh* | >*ṁthresh* | *Kmain,conv* | 0 | *Kside,conv* |
| 汇流至节点 C（支路），当 **Loss coefficient model** 参数为 `Crane correlation` 或 `Custom` 时 | >*ṁthresh* | >*ṁthresh* | <*-ṁthresh* | (*Kmain,conv* + *Kside,conv*)/2 | (*Kmain,conv* + *Kside,conv*)/2 | 0 |
| 从节点 C（支路）分流，当 **Loss coefficient model** 参数为 `Crane correlation` 或 `Custom` 时 | <*-ṁthresh* | <*-ṁthresh* | >*ṁthresh* | (*Kmain,div* + *Kside,div*)/2 | (*Kmain,div* + *Kside,div*)/2 | 0 |

当 **Loss coefficient model** 参数为 `Rennels correlation` 时，汇流至节点 C（支路）和从节点 C（支路）分流的值为直接计算。

当质量流量条件不匹配任何已定义的流动场景时，流动为停滞。停滞流动允许在仿真开始时出现，但模块在达到其他模式后不会恢复到停滞流动。质量流量阈值，即管道中流动开始反向的点，为

m˙thresh=Recυρ¯π4Amin,

其中：

- *Re*c 是 **Critical Reynolds number**，超过该值即开始过渡流态。
- *ν* 是流体粘度。
- ρ¯ 是平均流体密度。
- *Amin* 是管道交汇处的最小横截面积。

### Crane 关联式系数模型

当您将 **Loss coefficient model** 参数设置为 `Crane correlation` 时，管道损失系数 *Kmain* 和 *Kside* 以及管道摩擦因子 *f*T 根据 Crane [1] 计算：

Kmain,div=Kmain,conv=20fT,main,

Kside,div=Kside,conv=60fT,side.

与自定义接头类型不同，标准接头损失系数对于汇流和分流流动是相同的。然后 *K*A、*K*B 和 *K*C 以与自定义接头相同的方式计算。

| 公称尺寸 (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 摩擦因子，*fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

### Rennels 关联式系数模型

当您将 **Loss coefficient model** 参数设置为 `Rennels correlation` 时，模块根据 [2] 计算管道损失系数。

**主管线上的分流**

主流分流损失系数为

Kmain,div=0.62−0.98m˙1m˙2+0.36(m˙1m˙2)2+0.03(m˙2m˙1)6,

其中：

- m˙1 是主流入口处的质量流量。
- m˙2 是主流出口处的质量流量。

当 m˙2/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kmain,div* 的值饱和。

侧支路分流损失系数为

Kside,div=(0.81−1.13m˙1m˙3+(m˙1m˙3)2)(d3d1)4+1.12d3d1−1.08(d3d1)3+K\*,

其中

- m˙3 是侧支路出口处的质量流量。
- *d1* 是主管线的直径。
- *d3* 是侧支路的直径。
- K\*=0.57−1.07(rd3)1/2−2.13rd3+8.24(rd3)3/2−8.48(rd3)2+2.90(rd3)5/2。
- *r* 是 **Junction radius of curvature** 参数的值。

当 m˙3/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kside,div* 的值饱和。

**主管线上的汇流**

主流汇流损失系数为

Kmain,conv=(m˙1m˙2)2−0.95−2CxC(m˙1m˙2−1)−2CM((m˙1m˙2)2−m˙1m˙2),

其中

CM=0.23+1.46(rd3)−2.75(rd3)2+1.65(rd3)3CxC=0.08+0.56(rd3)−1.75(rd3)2+1.83(rd3)3

当 m˙2/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kmain,conv* 的值饱和。

侧支路汇流损失系数为

Kside,conv=(2CyC−1)+(d3d1)4[2(CxC−1)+2(2−CxC−CM)m˙1m˙3−0.92(m˙1m˙3)2],

其中：

CyC=1−0.25(d3d1)1.3−[0.11rd3−0.65(rd3)+0.83(rd3)3](d3d1)2.

当 m˙3/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kside,conv* 的值饱和。

**从侧支路汇流或分流**

流动汇流至侧支路时的损失系数为

Kconvtoside=(0.81−1.16rd+0.5rd)(m˙1m˙2)2−(0.95−1.65rd)m˙1m˙2+1.34−1.69rd,

其中 *d* 是侧支路的直径。当 m˙2/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kconv to side* 的值饱和。

流动从侧支路分流时的损失系数为

Kdivfromside=0.59(m˙1m˙2)2+(1.18−1.84rd+1.16rd)m˙1m˙2−0.68+1.04rd−1.16rd.

当 m˙2/m˙1 等于 **Minimum valid flow ratio for coefficient calculation** 参数的值时，*Kdiv from side* 的值饱和。

### 自定义 T 型接头

当您将 **Loss coefficient model** 参数设置为 `Custom` 时，模块根据用户定义的汇流和分流损失参数以及每个端口处的质量流量，计算每个端口处的管道损失系数 *K*。您必须分别将 *Kmain,conv*、*Kmain,div*、*Kside,conv* 和 *Kside,div* 指定为 **Main branch converging loss coefficient**、**Main branch diverging loss coefficient**、**Side branch converging loss coefficient** 和 **Side branch diverging loss coefficient** 参数。

### 常数系数 T 型接头

当您将 **Loss coefficient model** 参数设置为 `Constant Coefficients` 时，模块将交汇处建模为三个 Local Resistance (MA) 模块在中心节点连接而成的复合组件。当模块使用此设置时，它不使用模式图。如果您的模型在标称条件下运行且不需要高保真度，请使用此选项。

### 质量和动量平衡

模块在交汇处守恒质量，使得

m˙A+m˙B+m˙C=0m˙wA+m˙wB+m˙wC=0m˙gA+m˙gB+m˙gC=0m˙dA+m˙dB+m˙dC=0

- *ṁi* 是给定端口 *i* 的混合物质量流量。
- m˙*wi* 是给定端口 *i* 的水蒸气质量流量。
- m˙*gi* 是给定端口 *i* 的示踪气体质量流量。
- m˙*di* 是给定端口 *i* 的水滴质量流量。

模块使用端口 **A**、**B** 和 **C** 之间的动量守恒方程计算通过管道交汇处的流动：

pA−pI=IA+KA2ρ¯Amain2m˙Am˙A2+m˙thresh2pB−pI=IB+KB2ρ¯Amain2m˙Bm˙B2+m˙thresh2pC−pI=IC+KC2ρ¯Aside2m˙Cm˙C2+m˙thresh2

其中 *I* 表示流体惯性，且

IA=m¨Aπ⋅AsideAmainIB=m¨Bπ⋅AsideAmainIC=m¨Cπ⋅AmainAside

*Amain* 是 **Main branch area (A-B)** 参数，*Aside* 是 **Side branch area (A-C, B-C)** 参数。

### 能量平衡

模块平衡能量，使得

ϕA+ϕB+ϕC=0,

其中：

- *ϕA* 是端口 **A** 处的能量流量。
- *ϕB* 是端口 **B** 处的能量流量。
- *ϕC* 是端口 **C** 处的能量流量。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
