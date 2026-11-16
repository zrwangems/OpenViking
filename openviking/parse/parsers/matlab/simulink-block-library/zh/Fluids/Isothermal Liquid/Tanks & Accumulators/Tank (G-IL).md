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

### 输出

### **V** — 等温液体体积，`m^3` physical signal

物理信号输出端口，用于报告储罐中等温液体的体积，单位为 m3。

### **L** — 等温液体液位，`m` physical signal

物理信号输出端口，用于报告等温液体体积相对于储罐底部的高度，单位为 m。

### 守恒

### **A1** — 气体入口 gas

与气体流入或流出储罐的开口关联的气体守恒端口。

### **B1** — 气体入口 gas

与气体流入或流出储罐的开口关联的气体守恒端口。

### **A2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

### **B2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **C2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `3`、`4`、`5` 或 `6`。

### **D2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `4`、`5` 或 `6`。

### **E2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `5` 或 `6`。

### **F2** — 等温液体入口 isothermal liquid

与等温液体流入或流出储罐的开口关联的等温液体守恒端口。

#### 依赖关系

要启用此端口，请将 **Number of inlets** 设置为 `6`。

### **H1** — 热传递 thermal

与气体体积的储罐壁处热传递关联的热守恒端口。

## 参数

### **Number of inlets** — 等温液体端口数量 `1`（默认） | `2` | `3` | `4` | `5` | `6`

用于模块的等温液体端口数量。

### **Total tank volume** — 气体和等温液体合计体积 `10 m^3`（默认） | 正标量

储罐中气体和等温液体部分的总容积。

### **Tank volume parameterization** — 等温液体体积的参数化方式 `Constant cross-sectional area`（默认） | `Tabulated data — volume vs. level`

等温液体体积的参数化选择。选择 `Constant cross-sectional area` 以指定恒定的储罐横截面积。选择 `Tabulated data — volume vs. level` 以通过表列数据的插值或外推来计算等温液体体积。

### **Tank cross-sectional area** — 恒定储罐横截面的面积 `1` m^2（默认） | 正标量

储罐横截面的面积。模块假定该值在允许的液位范围内恒定。模块使用此参数计算储罐内等温液体的体积。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Constant cross-sectional area`。

### **Liquid level vector** — 指定等温液体体积所用的等温液体液位 `[0, 3, 5]` m（默认） | 向量

用于指定储罐中等温液体体积的等温液体液位向量。模块使用此向量构造等温液体体积作为等温液体液位函数的一维查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Tabulated data - volume vs. level`。

### **Liquid volume vector** — 指定等温液体液位处的等温液体体积 `[0, 4, 6]` m^3（默认） | 向量

与 **Liquid level vector** 参数元素对应的等温液体体积向量。模块使用此向量构造等温液体体积作为等温液体液位函数的一维查找表。

#### 依赖关系

要启用此参数，请将 **Tank volume parameterization** 设置为 `Tabulated data - volume vs. level`。

### **Cross-sectional area vector for inlets A1 and B1** — 气体入口的流通面积 `[.01, .01] m^2`（默认） | 向量

指定气体入口流通面积的二元素向量。

### **Inlet height at port A2** — 等温液体入口高度 `0.1 m`（默认） | 正标量

等温液体入口的高度。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `1`。

### **Cross-sectional area at port A2** — 等温液体入口的流通面积 `0.01 m^2`（默认） | 正标量

等温液体入口的流通面积。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `1`。

### **Height vector for inlets A2 and B2** — 端口的端口高度向量 `[.1, .1]` m（默认） | 1×*n* 向量

多个已启用端口的端口高度向量。参数名称和向量长度取决于 **Number of inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.1 m`。此向量的每个元素必须大于或等于 0。

例如，如果 **Number of inlets** 为 `4`，则此参数的名称为 **Height vector for inlets A2, B2, C2, and D2**，默认值为 `0.1 * ones(1, 4)` m。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **Cross-sectional area vector for inlets A2 and B2** — 端口的入口面积向量 `[.01, .01] m^2`（默认） | 1×*n* 向量

多个已启用端口的横截面积向量。参数名称和向量长度取决于 **Number of inlets** 参数的值。向量的每个元素对应一个入口端口，从端口 **A2** 开始。每个入口的默认高度为 `.01 m`。此向量的每个元素必须大于 0。

例如，如果 **Number of inlets** 为 `4`，则此参数的名称为 **Cross-sectional area vector for inlets A2, B2, C2, and D2**，默认值为 `0.01 * ones(1, 4)` m2。

#### 依赖关系

要启用此参数，请将 **Number of inlets** 设置为 `2`、`3`、`4`、`5` 或 `6`。

### **Liquid volume above max capacity** — 是否通知储罐体积过高 `None`（默认） | `Warning` | `Error`

是否在仿真期间储罐流体体积超过 **Total tank volume** 参数值时收到通知。将此参数设置为 `Warning`，以在仿真期间发生此情况时收到警告。将此参数设置为 `Error`，以在发生此情况时停止仿真。

### **Maximum tank liquid capacity** — 储罐的填充上限 `10 m^3`（默认） | 正标量

储罐的填充上限。

#### 依赖关系

要启用此参数，请将 **Liquid volume above max capacity** 设置为 `Warning` 或 `Error`。

### **Gravitational acceleration** — 重力加速度常数 `9.81` m/s^2（默认） | 正标量

储罐所在高度处的重力加速度值。模块假定该值在储罐高度上恒定。

## 所属库

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

具有可变气体和等温液体体积的加压储罐

Tank (G-IL) 模块对具有独立气体和等温液体体积的腔室中的质量和能量积累进行建模。总流体体积固定，但各自的气体和等温液体体积可以变化。两个气体端口允许气体流动，一个可变数量的等温液体端口（从一到六）允许等温液体流动。等温液体端口可以处于不同的高度。

图示：储罐中等温液体达到高度 y，并包含端口 A2、B2 和 C2。储罐顶部包含气体以及端口 A1 和 B1。

储罐是加压的，但压力不是固定的。它会在仿真期间根据气体体积中的压力而变化。当气体体积的压力升高时压力升高，当气体体积的压力降低时压力降低。模块假定等温液体体积与气体体积处于平衡状态，并且其压力与气体压力相同。这两个流体体积彼此不交换能量，但可以通过气体端口与其他组件发生能量交换。

### 等温液体端口

可以使用 **Number of inlets** 参数指定等温液体端口的数量：

| Number of inlets | 暴露的等温液体端口 |
| --- | --- |
| `1` | 端口 **A2** |
| `2` | 端口 **A2** 和 **B2** |
| `3` | 端口 **A2**、**B2** 和 **C2** |
| `4` | 端口 **A2**、**B2**、**C2** 和 **D2** |
| `5` | 端口 **A2**、**B2**、**C2**、**D2** 和 **E2** |
| `6` | 端口 **A2**、**B2**、**C2**、**D2**、**E2** 和 **F2** |

### 流体体积

储罐的总体积是其所含气体和等温液体体积之和，

VT=VL+VG,

其中 *V* 是体积，*T*、*L* 和 *G* 分别代表总体、液体和气体。由于总体积固定，气体体积的时间变化率必须与等温液体体积的时间变化率相反，

V˙G=−V˙L.

模块通过对表达式求导来计算等温液体体积的时间变化率

ML=ρLVL,

其中 *M* 是质量，*ρ* 是密度。求导得到进入等温液体体积的质量流量，

M˙L=VLρ˙L+V˙LρL.

等温液体体积的变化率，进而气体体积的变化率为

V˙G=−V˙L≈VLp˙LρLdρLdp|−M˙LρL,

其中 *p* 是压力。

### 质量平衡

每个流体体积中的质量积累率等于进入该流体体积的净质量流量。在等温液体体积中

M˙L=∑i=A2,B2,...F2m˙i,

其中 *ML* 是等温液体体积中的质量积累率，m˙i 是通过等温液体端口 **A2**、**B2**、**C2**、**D2**、**E2** 或 **F2** 进入该体积的各质量流量。

在气体体积中

M˙G=∑i=A1, B1m˙i,

*MG* 是气体体积中的质量积累率，m˙i 是通过气体端口 **A1** 和 **B1** 进入该体积的各质量流量。气体体积的质量积累率包含来自压力、温度和体积变化的贡献，

M˙G=dMdp|Gp˙G+dMdT|GT˙G+V˙GρG,

其中 *T* 是温度，压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。Translational Mechanical Converter (G) 页面的方程章节定义了这些导数。气体体积的质量平衡方程为

p˙GdMdp|G+T˙GdMdT|G+p˙GρGρLVLdρLdp|=∑i=A1, B1m˙i+ρGρL∑i=A2, B2,...F2m˙i,

### 能量平衡

气体体积中的能量积累率为

p˙GdUdp|G+T˙GdUdT|G+p˙GρGρLhGVLdρLdp|=QH1+∑i=A1, B1ϕi+ρGρLhG∑i=A2, B2,...F2m˙i

其中：

- *U* 是流体体积的总能量。
- *h* 是流体焓。
- *Q* 是通过热端口的热流率。
- *ϕi* 是通过流体入口的能量流率。

压力和温度导数取决于 Gas Properties (G) 模块中指定的气体类型。有关定义，请参见 Translational Mechanical Converter (G) 页面的方程章节。

### 动量平衡

模块忽略两个流体体积中因摩擦或其他原因造成的流动阻力。模块还忽略高度对入口压力的影响，但仅在气体侧如此。气体入口压力彼此相等，并且等于气体体积的内部压力：

pA1=pB1=pG.

等温液体入口压力各自是入口深度的函数。等温液体体积的内部压力等于气体体积压力，*pL* = *pG*。模块使用以下方程在入口处包含动态压力 *p*i*,dyn*：

pi+pi,dyn=pG+ρL(y−yi)g,

其中 *y* 是等温液体表面的高度，*y*i 是等温液体入口的高度，*g* 是重力常数。项 *y* - *yi* 给出等温液体入口相对于气体-等温液体边界的深度。每个等温液体入口处的动态压力取决于该入口处的流动方向

pi,dyn={12ρivi2,if m˙i<00,if m˙i≥0

其中 *vi* 是流速。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅《为模块变量设置优先级和初始目标》和《具有有限气体体积的模块的初始条件》。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅《修改模块变量的标称值》。

### 假设和限制

- 由于突然膨胀进入储罐体积，流体动量在储罐入口处损失。
