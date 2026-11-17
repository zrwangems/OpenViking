---
type: simulink-block
title: 'Tank (G-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'tankgil'
documentation_source_path: 'ref/tankgil.html'
language: zh-CN
chinese_source: worker-translation
---

# Tank (G-IL)

## 端口
```yaml
ports:
- name: V
  summary: 等温液体体积，m^3 物理信号
  direction: output
- name: L
  summary: 等温液体液位，m 物理信号
  direction: output
- name: A1
  summary: 气体入口 气体
  direction: output
- name: B1
  summary: 气体入口 气体
  direction: output
- name: A2
  summary: 等温液体入口 等温液体
  direction: output
- name: B2
  summary: 等温液体入口 等温液体
  direction: output
- name: C2
  summary: 等温液体入口 等温液体
  direction: output
- name: D2
  summary: 等温液体入口 等温液体
  direction: output
- name: E2
  summary: 等温液体入口 等温液体
  direction: output
- name: F2
  summary: 等温液体入口 等温液体
  direction: output
- name: H1
  summary: 传热 热
  direction: output
```

### 输出

### **V** — 等温液体体积，`m^3` 物理信号

物理信号输出端口，报告储罐中等温液体的体积，单位为 m3。

### **L** — 等温液体液位，`m` 物理信号

物理信号输出端口，报告等温液体体积相对于储罐底部的高度，单位为 m。
### 守恒

### **A1** — 气体入口 气体

气体守恒端口，与气体流入或流出储罐的开口相关联。

### **B1** — 气体入口 气体

气体守恒端口，与气体流入或流出储罐的开口相关联。

### **A2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

### **B2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **C2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`3`、`4`、
`5` 或
`6`。

### **D2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`4`、`5` 或
`6`。

### **E2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`5` 或
`6`。

### **F2** — 等温液体入口 等温液体

等温液体守恒端口，与等温液体流入或流出储罐的开口相关联。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为
`6`。

### **H1** — 传热 热

热守恒端口，与气体体积在储罐壁处的传热相关联。
## 参数
```yaml
parameters:
- name: Number of inlets
  summary: 等温液体端口数量 1（默认）| 2 | 3 | 4 | 5 | 6
  group: ''
- name: Total tank volume
  summary: 气体和等温液体的合计体积 10 m^3（默认）| 正标量
  group: ''
- name: Tank volume parameterization
  summary: 等温液体体积的参数化方式 Constant cross-sectional area（默认）| Tabulated data — volume vs. level
  group: ''
- name: Tank cross-sectional area
  summary: 恒定储罐横截面的面积 1 m^2（默认）| 正标量
  group: ''
- name: Liquid level vector
  summary: 用于指定等温液体体积的等温液体液位 [0, 3, 5] m（默认）| 向量
  group: ''
- name: Liquid volume vector
  summary: 指定等温液体液位处的等温液体体积 [0, 4, 6] m^3（默认）| 向量
  group: ''
- name: Cross-sectional area vector for inlets A1 and B1
  summary: 气体入口的流通面积 [.01, .01] m^2（默认）| 向量
  group: ''
- name: Inlet height at port A2
  summary: 等温液体入口的高度 0.1 m（默认）| 正标量
  group: ''
- name: Cross-sectional area at port A2
  summary: 等温液体入口的流通面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Height vector for inlets A2 and B2
  summary: 端口高度向量 [.1, .1] m（默认）| 1×*n* 向量
  group: ''
- name: Cross-sectional area vector for inlets A2 and B2
  summary: 端口入口面积向量 [.01, .01] m^2（默认）| 1×*n* 向量
  group: ''
- name: Liquid volume above max capacity
  summary: 是否在储罐体积过高时收到通知 None（默认）| Warning | Error
  group: ''
- name: Maximum tank liquid capacity
  summary: 储罐的填充限值 10 m^3（默认）| 正标量
  group: ''
- name: Gravitational acceleration
  summary: 重力加速度常数 9.81 m/s^2（默认）| 正标量
  group: ''
```

### **Number of inlets** — 等温液体端口数量 `1`（默认）| `2` | `3` | `4` | `5` | `6`

模块的等温液体端口数量。

### **Total tank volume** — 气体和等温液体的合计体积 `10 m^3`（默认）| 正标量

储罐中气体和等温液体部分的总容积。

### **Tank volume parameterization** — 等温液体体积的参数化方式 `Constant cross-sectional area`（默认）| `Tabulated data — volume vs. level`

等温液体体积的参数化方式选择。选择
`Constant cross-sectional area` 以指定恒定的储罐横截面积。选择 `Tabulated data
— volume vs. level` 以通过表格数据的插值或外推来计算等温液体体积。

### **Tank cross-sectional area** — 恒定储罐横截面的面积 `1` m^2（默认）| 正标量

储罐横截面的面积。模块假定该值在允许的液位范围内恒定。模块使用此参数计算储罐内等温液体的体积。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Constant cross-sectional
area`。

### **Liquid level vector** — 用于指定等温液体体积的等温液体液位 `[0, 3, 5]` m（默认）| 向量

用于指定储罐中等温液体体积的等温液体液位向量。模块使用此向量构建等温液体体积作为等温液体液位函数的单向查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Liquid volume vector** — 指定等温液体液位处的等温液体体积 `[0, 4, 6]` m^3（默认）| 向量

与 **Liquid level vector** 参数元素对应的等温液体体积向量。模块使用此向量构建等温液体体积作为等温液体液位函数的单向查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume
parameterization** 设置为 `Tabulated data - volume
vs. level`。

### **Cross-sectional area vector for inlets A1 and B1** — 气体入口的流通面积 `[.01, .01] m^2`（默认）| 向量

指定气体入口流通面积的双元素向量。

### **Inlet height at port A2** — 等温液体入口的高度 `0.1 m`（默认）| 正标量

等温液体入口的高度。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`1`。

### **Cross-sectional area at port A2** — 等温液体入口的流通面积 `0.01 m^2`（默认）| 正标量

等温液体入口的流通面积。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`1`。

### **Height vector for inlets A2 and B2** — 端口高度向量 `[.1, .1]` m（默认）| 1×*n* 向量

多个已启用端口的高度向量。参数名称和向量长度取决于 **Number of
inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.1 m`。此向量的每个元素必须大于或等于 0。

例如，如果 **Number of inlets** 为
`4`，则此参数的名称为
**Height vector for inlets A2, B2, C2, and D2**，默认值为 `0.1 * ones(1, 4)` m。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Cross-sectional area vector for inlets A2 and B2** — 端口入口面积向量 `[.01, .01] m^2`（默认）| 1×*n* 向量

多个已启用端口的横截面积向量。参数名称和向量长度取决于 **Number of
inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.01 m`。此向量的每个元素必须大于 0。

例如，如果 **Number of inlets** 为
`4`，则此参数的名称为
**入口 A2、B2、C2 和
D2**，默认值为 `0.01 * ones(1,
4)` m2。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为
`2`、`3`、
`4`、`5` 或
`6`。

### **Liquid volume above max capacity** — 是否在储罐体积过高时收到通知 `None`（默认）| `Warning` | `Error`

是否在仿真期间储罐流体体积超过 **Total tank volume** 参数值时收到通知。将此参数设置为 `Warning` 以在仿真期间发生此情况时收到警告。将此参数设置为
`Error` 以在发生此情况时停止仿真。

### **Maximum tank liquid capacity** — 储罐的填充限值 `10 m^3`（默认）| 正标量

储罐的填充限值。

#### 依赖关系

要启用此参数，请将 **Liquid volume above max
capacity** 设置为 `Warning` 或
`Error`。

### **Gravitational acceleration** — 重力加速度常数 `9.81` m/s^2（默认）| 正标量

储罐所在高度处的重力加速度值。模块假定该值在储罐高度范围内恒定。
## 所属库

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

具有可变气体和等温液体体积的加压储罐

Tank (G-IL) 模块对具有独立气体和等温液体体积的腔室中的质量和能量积聚进行建模。总流体体积是固定的，但各个气体和等温液体体积可以变化。两个气体端口允许气体流动，可变数量的等温液体端口（从一到六）允许等温液体流动。等温液体端口可以位于不同的高度。

图示：储罐中等温液体高度为 y，包含端口 A2、B2 和 C2。储罐顶部包含气体和端口 A1 和 B1。

储罐是加压的，但加压压力不是固定的。它在仿真过程中根据气体体积中的压力而变化。当气体体积的压力升高时，压力上升；当气体体积的压力降低时，压力下降。该模块假设等温液体体积与气体体积处于平衡状态，且其压力与气体压力相同。两种流体体积之间不交换能量，但可以通过气体端口与其他组件进行能量交换。

### 等温液体端口

您可以使用 **Number of inlets** 参数指定等温液体端口的数量：

| Number of inlets | 暴露的等温液体端口 |
| --- | --- |
| `1` | 端口 **A2** |
| `2` | 端口 **A2** 和 **B2** |
| `3` | 端口 **A2**、**B2** 和 **C2** |
| `4` | 端口 **A2**、**B2**、**C2** 和 **D2** |
| `5` | 端口 **A2**、**B2**、**C2**、**D2** 和 **E2** |
| `6` | 端口 **A2**、**B2**、**C2**、**D2**、**E2** 和 **F2** |

### 流体体积

储罐的总体积是其包含的气体和等温液体体积之和，

VT=VL+VG，

其中 *V* 是体积，*T*、*L* 和 *G* 分别代表总体、液体和气体。由于总体积是固定的，气体体积的时间变化率必须与等温液体体积的时间变化率相反，

V˙G=−V˙L。

该模块通过对表达式

ML=ρLVL

进行微分来计算等温液体体积的时间变化率，其中 *M* 是质量，*ρ* 是密度。微分得到进入等温液体体积的质量流量，

M˙L=VLρ˙L+V˙LρL。

等温液体体积的变化率以及由此推得的气体体积变化率为

V˙G=−V˙L≈VLp˙LρLdρLdp|−M˙LρL，

其中 *p* 是压力。

### 质量平衡

每个流体体积中的质量积聚率等于进入该流体体积的净质量流量。在等温液体体积中

M˙L=∑i=A2,B2,...F2m˙i，

其中 *ML* 是等温液体体积中的质量积聚率，m˙i 是通过等温液体端口 **A2**、**B2**、**C2**、**D2**、**E2** 或 **F2** 进入该体积的各个质量流量。

在气体体积中

M˙G=∑i=A1, B1m˙i，

*MG* 是气体体积中的质量积聚率，m˙i 是通过气体端口 **A1** 和 **B1** 进入该体积的各个质量流量。气体体积的质量积聚率包含来自压力、温度和体积变化的贡献，

M˙G=dMdp|Gp˙G+dMdT|GT˙G+V˙GρG，

其中 *T* 是温度，压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。Translational Mechanical Converter (G) 页面的 equations 部分定义了这些导数。气体体积的质量平衡方程为

p˙GdMdp|G+T˙GdMdT|G+p˙GρGρLVLdρLdp|=∑i=A1, B1m˙i+ρGρL∑i=A2, B2,...F2m˙i，

### 能量平衡

气体体积中的能量积聚率为

p˙GdUdp|G+T˙GdUdT|G+p˙GρGρLhGVLdρLdp|=QH1+∑i=A1, B1ϕi+ρGρLhG∑i=A2, B2,...F2m˙i

其中：

- *U* 是流体体积的总能量。
- *h* 是流体焓。
- *Q* 是通过热端口的热流量。
- *ϕi* 是通过流体入口的能量流量。

压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。有关定义，请参见 Translational Mechanical Converter (G) 页面的 equations 部分。

### 动量平衡

该模块忽略两种流体体积中由摩擦或其他原因引起的流动阻力。该模块还忽略高度对入口压力的影响，但仅在气体侧。气体入口压力彼此相等，且等于气体体积的内部压力：

pA1=pB1=pG。

等温液体入口压力分别是入口深度的函数。等温液体体积的内部压力等于气体体积压力，*pL* = *pG*。该模块通过以下方程将入口处的动压 *p*i*,dyn* 纳入考虑

pi+pi,dyn=pG+ρL(y−yi)g，

其中 *y* 是等温液体表面的高度，*y*i 是等温液体入口的高度，*g* 是重力常数。项 *y* - *yi* 给出等温液体入口相对于气体-等温液体边界的深度。每个等温液体入口处的动压取决于该入口处的流动方向

pi,dyn={12ρivi2,if m˙i<00,if m˙i≥0

其中 *vi* 是流速。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Gas Volume。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见 Modify Nominal Values for a Block Variable。

### 假设和限制

- 由于突然膨胀进入储罐体积，流体动量在储罐入口处损失。
