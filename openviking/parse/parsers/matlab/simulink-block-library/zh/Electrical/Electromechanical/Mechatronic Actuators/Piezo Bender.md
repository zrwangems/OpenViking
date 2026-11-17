---
type: simulink-block
title: 'Piezo Bender'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'piezobender'
documentation_source_path: 'ref/piezobender.html'
language: zh-CN
chinese_source: worker-translation
---

# Piezo Bender

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: unspecified
- name: '-'
  summary: 负极端子电气
  direction: unspecified
- name: Ctr
  summary: 平移壳体机械
  direction: unspecified
- name: Cro
  summary: 旋转壳体机械
  direction: unspecified
- name: Rtr
  summary: 平移转子机械
  direction: unspecified
- name: Rro
  summary: 旋转转子机械
  direction: unspecified
```

### 守恒

### **+** — 正极端子电气

与压电弯曲器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与压电弯曲器负极端子关联的电气守恒端口。

### **Ctr** — 平移壳体机械

与壳体关联的机械平移守恒端口。

### **Cro** — 旋转壳体机械

与壳体关联的机械旋转守恒端口。

### **Rtr** — 平移转子机械

与转子关联的机械平移守恒端口。

### **Rro** — 旋转转子机械

与转子关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Number of elements
  summary: 单元数量 1（默认）| 大于或等于 1 的正整数
  group: 尺寸
- name: Total beam length
  summary: 梁总长度 3.175E-2 m（默认）| 正标量
  group: 尺寸
- name: Beam width
  summary: 梁宽度 1.27E-2 m（默认）| 正标量
  group: 尺寸
- name: Beam thickness
  summary: 梁厚度 5.08E-4 m（默认）| 正标量
  group: 尺寸
- name: Parameterization
  summary: 稳态参数化 Specify from a datasheet for clamped-free configuration（默认）| Specify from material properties
  group: 稳态
- name: Capacitance
  summary: 压电弯曲器电容 15 nF（默认）| 正标量
  group: 稳态
- name: Rated drive voltage, Vrated
  summary: 额定驱动电压 180 V（默认）| 正标量
  group: 稳态
- name: Free deflection at Vrated
  summary: Vrated 下的自由偏转 +0.233 mm（默认）| 非零值
  group: 稳态
- name: Blocking force at Vrated
  summary: Vrated 下的阻塞力 -0.414 N（默认）| 标量
  group: 稳态
- name: Young modulus, E
  summary: 杨氏模量 1.36628e11 N/m^2（默认）| 正标量
  group: 稳态
- name: Piezoelectric stress coefficient, e31
  summary: 压电应力系数 7.5459 C/m^2（默认）| 非零标量
  group: 稳态
- name: Dielectric constant
  summary: 介电常数 1.38965e-08 F/m（默认）| 正标量
  group: 稳态
- name: Inertial effects
  summary: 惯性效应建模选项 On（默认）| Off
  group: 动力学
- name: Parameterization
  summary: 惯性参数化 Specify from a datasheet for clamped-free configuration（默认）| Specify from material properties
  group: 动力学
- name: Beam mass
  summary: 梁质量 1.6 g（默认）| 正标量
  group: 动力学
- name: First natural frequency
  summary: 第一阶固有频率 391 Hz（默认）| 正标量
  group: 动力学
- name: Rayleigh damping constant proportional to stiffness
  summary: 与刚度成比例的 Rayleigh 阻尼常数 1e-5 s（默认）| 非负标量
  group: 动力学
- name: Rayleigh damping constant proportional to mass
  summary: 与质量成比例的 Rayleigh 阻尼常数 0 1/s（默认）| 非负标量
  group: 动力学
```

### 尺寸

### **Number of elements** — 单元数量 `1`（默认）| 大于或等于 1 的正整数

压电弯曲器梁使用 Euler-Bernoulli 有限元方程离散化的单元数量。

### **Total beam length** — 梁总长度 `3.175E-2` `m`（默认）| 正标量

梁的总长度。

### **Beam width** — 梁宽度 `1.27E-2` `m`（默认）| 正标量

梁的宽度。

### **Beam thickness** — 梁厚度 `5.08E-4` `m`（默认）| 正标量

梁的厚度。

### 稳态

### **Parameterization** — 稳态参数化 `Specify from a datasheet for clamped-free configuration`（默认）| `Specify from material properties`

是从数据手册还是从材料属性来参数化稳态参数。

### **Capacitance** — 压电弯曲器电容 `15` `nF`（默认）| 正标量

压电弯曲器的电容。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet for clamped-free configuration`。

### **Rated drive voltage, Vrated** — 额定驱动电压 `180` `V`（默认）| 正标量

额定驱动电压。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet for clamped-free configuration`。

### **Free deflection at Vrated** — Vrated 下的自由偏转 `+0.233` `mm`（默认）| 非零值

未施加力时的尖端偏转。此参数的符号必须与 **Blocking force at Vrated** 参数的符号不同。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet for clamped-free configuration`。

### **Blocking force at Vrated** — Vrated 下的阻塞力 `-0.414` `N`（默认）| 标量

使尖端偏转归零的力。此参数的符号必须与 **Free deflection at Vrated** 参数的符号不同。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet for clamped-free configuration`。

### **Young modulus, E** — 杨氏模量 `1.36628e11` `N/m^2`（默认）| 正标量

杨氏模量，即拉伸弹性模量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from material properties`。

### **Piezoelectric stress coefficient, e31** — 压电应力系数 `7.5459` `C/m^2`（默认）| 非零标量

(3,1) 压电应力-电荷耦合系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from material properties`。

### **Dielectric constant** — 介电常数 `1.38965e-08` `F/m`（默认）| 正标量

表示材料相对介电常数的介电常数。此参数必须大于真空介电常数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from material properties`。

### 动力学

### **Inertial effects** — 惯性效应建模选项 `On`（默认）| `Off`

是否对惯性效应建模。

### **Parameterization** — 惯性参数化 `Specify from a datasheet for clamped-free configuration`（默认）| `Specify from material properties`

是从数据手册还是从材料属性来参数化惯性参数。

#### 依赖关系

要启用此参数，请将 **Inertial effects** 设置为 `On`。

### **Beam mass** — 梁质量 `1.6` `g`（默认）| 正标量

梁的质量。

#### 依赖关系

要启用此参数，请将 **Inertial effects** 设置为 `On`，并将 **Parameterization** 设置为 `Specify from material properties`。

### **First natural frequency** — 第一阶固有频率 `391` `Hz`（默认）| 正标量

第一阶固有频率。

#### 依赖关系

要启用此参数，请将 **Inertial effects** 设置为 `On`，并将 **Parameterization** 设置为 `Specify from a datasheet for clamped-free configuration`。

### **Rayleigh damping constant proportional to stiffness** — 与刚度成比例的 Rayleigh 阻尼常数 `1e-5` `s`（默认）| 非负标量

用于 Rayleigh 阻尼的与刚度成比例的阻尼系数。

### **Rayleigh damping constant proportional to mass** — 与质量成比例的 Rayleigh 阻尼常数 `0` `1/s`（默认）| 非负标量

用于 Rayleigh 阻尼的与质量成比例的阻尼系数。

#### 依赖关系

要启用此参数，请将 **Inertial effects** 设置为 `On`。
## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

矩形截面的压电双压电晶片梁

Piezo Bender 模块对矩形截面的压电双压电晶片梁进行建模。

压电弯曲器是一种压电设备，当在其极板之间施加电势时会发生弯曲。相反，当压电弯曲器弯曲时，会产生电势。

压电弯曲器由不同的矩形压电材料层组成，其极化方向垂直于叠层方向。每一层中的极化方向交替变化。

### 方程

此图显示了笛卡尔参考坐标系

其中：

- *L* 是梁的长度。
- *w* 是梁的宽度。
- *d* 是梁的厚度。

以下是应力-电荷公式下压电材料的本构方程，

|  |  |
| --- | --- |
| T=[c]S−[e]TE | **(1)** |

|  |  |
| --- | --- |
| D=[e]S−[ϵS]E | **(2)** |

其中：

- *T* 是应力场。
- *[c]* 是柔度张量。
- *S* 是应变场。
- *[e]* 是压电应力系数张量。
- *E* 是电场。
- *D* 是电位移场。
- *[ϵS]* 是恒定应变或零应变下的介电常数张量。

为了对柔度进行建模，该模块使用 Euler-Bernoulli 有限元梁方程。每个梁横截面随 *x* 轴的平移和旋转决定了梁的运动学。

此模块仅考虑沿 *y* 方向施加的力，并且压电材料被极化为仅在 *x-y* 平面内弯曲。因此，为了描述运动学，您只需指定每个横截面重心沿 *y* 方向的垂直位移 *y(x)*，以及每个横截面绕 *z* 轴的旋转 *φz(x)*。

根据上述假设，Euler-Bernoulli 梁在弯曲作用下的应变场等于：

|  |  |
| --- | --- |
| Sxx(x,y)=−ydφzdx(x). | **(3)** |

由于正极板和负极板之间的电场是恒定的，Ey=vd，该模块将方程 3 代入方程 1：

Txx(x,y)=−Eydφzdx(x)−e31vd.

在此方程中，*E = c11* 是材料的杨氏模量，*e31* 是 (3,1) 压电应力-电荷耦合系数，σxx=−e31Ey。

此方程根据应力场定义弯矩：

Mz(x)=−∬yTxx(x,y) dS=∬Ey2dφzdx(x)+e31vdy dS.

由于材料在 y=[−d2,0] 范围内的极化方向与 y=[0,d2] 范围内的极化方向相反，(3,1) 压电应力-电荷耦合系数改变符号，弯矩定义为

Mz(x)=E12w d3dφzdx(x)+w d e31v=EIdφzdx(x)+w d e31v,

其中 I=112wd3 是矩形横截面的面积二次矩。

在此方程中，第一项是梁受弯曲作用的经典方程，第二项是由于压电材料两端存在电压而产生的机电耦合。此电压产生沿梁加载的均匀电弯矩。

然后该模块将方程 3 代入方程 2：

Dy(x,y)=−e31ydφzdx(x)+ϵvd.

体积内的电荷等于电位移的高斯积分：

dq(x)=∯Dy dS=e31dw dxdφzdx=e31dw dφz.

然后，此方程定义了由于压电效应而在梁的两个截面之间累积的电荷：

q=e31dw(φz(x2)−φz(x1)).

最后，从机械角度来看，您可以将压电弯曲器建模为承受与电压成比例的均匀扭矩的 Euler-Bernoulli 梁：

Mz(x)=EIdφzdx(x)+w d e31v

从电气角度来看，您可以将压电弯曲器建模为具有与弯曲角度成比例的电荷源的电容器：

q=e31d w(φzR−φzC)+ϵwldv.

### 有限元公式

为了使用压电耦合对 Euler-Bernoulli 方程进行离散化和求解，Piezo Bender 模块使用有限元方法。

该模块将压电弯曲器梁沿长度方向离散为若干具有相同宽度 *w* 和厚度 *d* 的切片。每个单元的长度等于梁的总长度除以单元数量，l=LNelements。

Euler-Bernoulli 梁有限单元的刚度矩阵定义了梁单元每一端的垂直位移和旋转角度与梁弹性引起的相应力和力矩之间的关系：

[FCTCFRTR]=[12EIl36EIl2−12EIl36EIl26EIl24EIl−6EIl22EIl−12EIl3−6EIl212EIl3−6EIl26EIl22EIl−6EIl24EIl][yCφCyRφR].

然后，为了获得压电弯曲器梁单元的方程，添加耦合项和惯性的质量矩阵：

ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2][d2yCdt2d2φCdt2d2yRdt2d2φRdt20]+[12EIl36EIl2−12EIl36EIl206EIl24EIl−6EIl22EIle31wd−12EIl3−6EIl212EIl3−6EIl206EIl22EIl−6EIl24EIl−e31wd0−e31wd0e31wdϵwld][yCφCyRφRv]=[FCTCFRTRq].

最后，这是带阻尼的压电弯曲器梁单元的方程：

ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2][d2yCdt2d2φCdt2d2yRdt2d2φRdt20]+[[B]⋯0⋮⋱⋮0⋯0][dyCdtdφCdtdyRdtdφRdt0]+[12EIl36EIl2−12EIl36EIl206EIl24EIl−6EIl22EIle31wd−12EIl3−6EIl212EIl3−6EIl206EIl22EIl−6EIl24EIl−e31wd0−e31wd0e31wdϵwld][yCφCyRφRv]=[FCTCFRTRq]

其中：

- *l* 是单元长度。
- *w* 是单元宽度。
- *d* 是单元厚度。
- I=112wt3 是面积二次矩。
- *E* 是杨氏模量。
- *m = ρlwd* 是单元质量，其中 *ρ* 是质量密度。
- *e31* 是 (3,1) 压电应力-电荷耦合系数，σxx=−e31Ey。
- *ε* 是介电常数。
- B=bkK+bmM 是阻尼矩阵。
- *bm* 是与质量成比例的 Rayleigh 阻尼系数。
- *bk* 是与刚度成比例的 Rayleigh 阻尼系数。
- K=[12EIl36EIl2−12EIl36EIl26EIl24EIl−6EIl22EIl−12EIl3−6EIl212EIl3−6EIl26EIl22EIl−6EIl24EIl] 是刚度有限元矩阵。
- M=ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2] 是质量矩阵。
- *yC* 是单元左端沿 *y* 轴的偏转。
- *yR* 是单元右端沿 *y* 轴的偏转。
- *φC* 是单元左端绕 *z* 轴的旋转。
- *φR* 是单元右端绕 *z* 轴的旋转。
- *FC* 是单元左端沿 *y* 轴的力。
- *FR* 是单元右端沿 *y* 轴的力。
- *TC* 是单元左端绕 *z* 轴的扭矩。
- *TR* 是单元右端绕 *z* 轴的扭矩。
- *v* 是顶部和底部电极之间的电压。
- *q* 是电极与压电材料之间累积的电荷。

### 数据手册参数化

压电弯曲器的数据手册通常提供以下数据：

- 尺寸（*l*、*w*、*d*）
- 质量，*m*
- 额定电压，*vrated*
- 额定电压下的自由偏转，*yfree*
- 额定电压下的阻塞力，*Fblock*
- 电容，*Cpiezo*
- 第一阶谐振频率，*f1*

可以使用数据手册参数来计算压电弯曲器的基本材料参数。

首先，该模块根据未施加扭矩且为 clamped-free 配置的稳态方程求解电压-力-偏转关系：

[12EIl3−6EIl20−6EIl24EIl−e31w d0e31w dε wld][yRφRv]=[FR0q].

这些方程定义了尖端偏转、电压和尖端力之间的关系：

yR=l2(4FR l+6 d w e31 v)12EI=l2 (4FR l+6 d w e31 v)E w d3=FR4l3Ewd3+v6 e31l2E d2yfree=6l2 d w e31 vrated12EI=6 e31l2 vratedE d2Fblock=−3 d w e31 vrated2l

该模块通过假设施加的力为零来计算电容：

Cpiezo=εl wd+e312l d2w2EI=εl wd+e31212l wEd=(ε+12e312E)l wd.

最后，此方程显示了密度与质量之间的关系：

m=ρ lwd.

一旦定义了基本参数与数据手册参数之间的所有关系，就可以使用以下方程计算基本参数：

e31=−2 l Fblock3 d w vratedE=−4 Fblockl3yfreed3wε=dl w(Cpiezo+4Fblockyfreevrated2)

然后将这些方程代入本构方程：

vvrated=FRFblock+yRyfreeq=Cpiezov+yfreevratedFR

**动力学数据手册参数化**

可以使用以下方程计算均匀横截面 clamped-free 梁的第一阶谐振频率：

2πf0=1.8552EIm l3.

然后，该模块通过指定所需的固有频率直接参数化动力学。

### 边界条件

梁在其左端和右端具有不同的边界条件：

- 自由 — 位移和旋转均等于任意值。
- 简支 — 位移等于 `0`。
- 固支 — 位移和旋转均等于 `0`。

此表显示了压电弯曲器梁可能的边界配置。

| **配置** | 模型 |
| --- | --- |
| Clamped-free |  |
| Supported-supported |  |
| Clamped-clamped |  |
