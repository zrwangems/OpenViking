---
type: simulink-block
title: 'Nonlinear Translational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlineartranslationalspring'
documentation_source_path: 'ref/nonlineartranslationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Translational Spring

## 端口
```yaml
ports:
- name: C
  summary: 从动端口 机械旋转
  direction: unspecified
- name: R
  summary: 基座端口 机械旋转
  direction: unspecified
```

### 守恒

### **C** — 从动端口 机械旋转

与从动端关联的机械旋转守恒端口。

### **R** — 基座端口 机械旋转

与基座端关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Parameterization
  summary: 表征弹簧行为的方法 By polynomial（默认）| By table lookup
  group: ''
- name: Symmetry
  summary: 相对于零变形位置的弹簧行为 Symmetric（默认）| Two-sided
  group: ''
- name: Vector of spring coefficients
  summary: 对称变形多项式系数 [100, 0, 10, 0, 1] N/m（默认）| 向量
  group: ''
- name: Vector of spring tension coefficients
  summary: 正向双侧变形多项式系数 [100, 0, 10, 0, 1] N/m（默认）
  group: ''
- name: Vector of spring compression coefficients
  summary: 负向双侧变形多项式系数 [1000, -10, 100, 0, 0] N/m（默认）
  group: ''
- name: Deformation vector
  summary: 力查找表条目对应的变形 [-1, -.5, -.3, -.1, .1, .3, .5, 1]（默认）
  group: ''
- name: Force vector
  summary: 查找表条目对应的施加力 [-1000, -400, -200, -50, 50, 200, 400, 1000]（默认）
  group: ''
- name: Interpolation method
  summary: 断点值之间的插值方法 Smooth（默认）| Linear
  group: ''
- name: Extrapolation method
  summary: 处理超出断点数据集范围的输入值的方法 Linear（默认）| Nearest | Error
  group: ''
```

### **Parameterization** — 表征弹簧行为的方法 `By polynomial`（默认）| `By table lookup`

弹簧行为选择。您可以选择通过多项式或查找表进行参数化。

### **Symmetry** — 相对于零变形位置的弹簧行为 `Symmetric`（默认）| `Two-sided`

弹簧行为关于零变形点的对称性。当您选择 `Symmetric` 时，模块关于零变形点对称地应用一个多项式。当您选择 `Two-sided` 时，模块对拉伸和压缩应用不同的多项式。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`。

### **Vector of spring coefficients** — 对称变形多项式系数 `[100, 0, 10, 0, 1]` `N/m`（默认）| 向量

多项式弹簧刚度系数。最高非零阶元素必须为正。物理单位表示第一个系数，模块会为您选择适当的高阶单位。此向量的长度必须为 5。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Symmetric`。

### **Vector of spring tension coefficients** — 正向双侧变形多项式系数 `[100, 0, 10, 0, 1]` `N/m`（默认）

弹簧拉伸的多项式系数。物理单位表示第一个系数，模块会为您选择适当的高阶单位。此向量的长度必须为 5。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Two-sided`。

### **Vector of spring compression coefficients** — 负向双侧变形多项式系数 `[1000, -10, 100, 0, 0]` `N/m`（默认）

弹簧压缩的多项式系数。物理单位表示第一个系数，模块会为您选择适当的高阶单位。此向量的长度必须为 5。

### **Deformation vector** — 力查找表条目对应的变形 `[-1, -.5, -.3, -.1, .1, .3, .5, 1]`（默认）

相对于零变形位置的相对位移值，对应于 **Force vector** 参数中的相应元素。此参数的长度必须与 **Force vector** 参数相同。最小向量长度取决于插值方法：`Linear` 为两个，`Smooth` 为三个。如果向量中未包含原点，模块会自动在原点变形-力坐标处添加一个点。

### **Force vector** — 查找表条目对应的施加力 `[-1000, -400, -200, -50, 50, 200, 400, 1000]`（默认）

对应于 **Deformation vector** 参数中相应元素的力值。此参数的长度必须与 **Deformation vector** 参数相同。最小向量长度为：`Linear` 为两个，`Smooth` 为三个。如果您未指定原点变形-力坐标，模块会自动添加一个点。

### **Interpolation method** — 断点值之间的插值方法 `Smooth`（默认）| `Linear`

查找表断点插值。模块使用 `tablelookup` 函数，通过向量数据将输入值映射到输出值来建模非线性：

- `Linear` — 选择此选项可获得最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

查找表断点外推。此方法确定当输入值超出参数列表中指定的范围时的输出值。模块使用 `tablelookup` 函数，通过向量数据将输入值映射到输出值来建模非线性：

- `Linear` — 选择此选项可生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点也不低于数据中最低点的外推。
- `Error` — 当您希望数据在表范围内时，选择此选项可避免外推。如果输入信号超出表的范围，仿真将停止并生成错误。

有关详细信息，请参阅 `tablelookup`。
## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

基于多项式或查找表参数化的平移弹簧

Nonlinear Translational Spring 模块表示具有非线性力-位移曲线的平移弹簧。弹簧力的大小是位移的一般函数，不一定需要满足胡克定律。您可以使用多项式或查找表来参数化力-位移关系。弹簧力可以关于零变形对称或不对称。

对称多项式参数化根据以下表达式定义弹簧力

F=k1x+sign(x)⋅k2x2+k3x3+sign(x)⋅k4x4+k5x5,

其中：

- *F* 是弹簧力。
- *k*1、*k*2、...、*k*5 是弹簧系数。
- *x* 是端口 **R** 和 **C** 之间的相对位移。
- *x*init 是初始相对位移。

在仿真开始时，*x* 等于 *x*init。

为避免减慢仿真的零穿越，请通过指定奇多项式（*b*2、*b*4 = 0）来消除多项式表达式中的符号函数。

非对称多项式参数化根据以下表达式定义弹簧力：

F={k1tx+k2tx2+k3tx3+k4tx4+k5tx5,x≥0k1cx+k2cx2+k3cx3+k4cx4+k5cx5,x<0,

其中：

- *k*1、*k*2、...、*k*5 是弹簧拉伸系数。
- *k*1、*k*2、...、*k*5 是弹簧压缩系数。

两种多项式参数化均使用五阶多项式表达式。要使用低阶多项式，请将不需要的高阶系数设置为零。要使用高阶多项式，请拟合为低阶多项式或使用查找表参数化。

将 **Parameterization** 设置为 `By table lookup` 会根据一组扭矩和角速度向量定义阻尼扭矩。如果您未输入原点的数据点，模块会自动添加一个（零角速度和零扭矩）。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期大小的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
