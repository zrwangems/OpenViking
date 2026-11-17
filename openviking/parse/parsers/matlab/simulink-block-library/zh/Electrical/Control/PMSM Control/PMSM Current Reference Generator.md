---
type: simulink-block
title: 'PMSM Current Reference Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmcurrentreferencegenerator'
documentation_source_path: 'ref/pmsmcurrentreferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Current Reference Generator

## 端口

### 输入

### **TqRef** — 参考转矩，N\*m 标量

PMSM 产生的期望机械转矩，单位为 N\*m。

**数据类型：** `single` | `double`

### **wMechanical** — 转子机械转速，rad/s 标量

转子的机械角速度，通过 PMSM 的直接测量获得，单位为 rad/s。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压，V 标量

变换器的直流母线电压，单位为 V。对于 ZDAC 方法，该值用于限制输出参考转矩和转矩限值。对于查找表方法，该值用作查找表的输入。

**数据类型：** `single` | `double`
### 输出

### **idqRef** — 参考电流，A 向量

作为 PMSM 电流控制器输入的参考 *d* 轴和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **TqRefSat** — 参考转矩，N\*m 标量

经计算得到的转矩限值 **TqLim** 饱和后的参考转矩，单位为 N\*m。

**数据类型：** `single` | `double`

### **TqLim** — 转矩限值，N\*m 标量

由系统电气和机械约束共同施加的转矩限值，单位为 N\*m。

**数据类型：** `single` | `double`

## 参数

#### 通用参数

### **Nominal dc-link voltage (V)** — 额定直流电压 `300``V`（默认）| 正数

电源的额定直流母线电压。

### **Maximum power (W)** — 额定功率 `30000``W`（默认）| 正数

PMSM 的最大允许功率。

### **Maximum torque (N\*m)** — 额定转矩 `250``N*m`（默认）| 正数

PMSM 的最大允许转矩。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| -1 或正数

模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 -1。如果在连续变步长模型中使用此模块，可以显式指定采样时间。

#### 参考生成策略

### **Current references** — 电流参考策略 `Zero d-axis control`（默认）| `Lookup-table based` | `Automatically generated lookup-table`

选择确定电流参考的策略。

### **Mechanical speed vector, wMechanical (rpm)** — 转子转速查找向量 `[0, 3000]``rpm`（默认）| 正单调递增向量

用于确定电流参考的查找表中的转速向量。

### **Torque reference vector, TqRef (N\*m)** — 转矩参考查找向量 `[-100, 0, 100]``N*m`（默认）| 正单调递增向量

用于确定电流参考的查找表中的转矩向量。

### **DC-link voltage vector, Vdc (V)** — 直流母线电压查找向量 `[300, 350]``V`（默认）| 正单调递增向量

用于确定电流参考的查找表中的直流母线电压向量。

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — 参考 d 轴电流值 `zeros(2,3,2)``A`（默认）| 实数矩阵

直轴电流参考查找数据。

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — 参考 q 轴电流值 `zeros(2,3,2)``A`（默认）| 实数矩阵

交轴电流参考查找数据。

### **PWM method** — 脉宽调制方法 `SVM: space vector modulation`（默认）| `SPWM: sinusoidal PWM`

指定波形技术。

#### 依赖关系

仅当 **Current references** 设置为 `Automatically generated lookup-table` 时，此参数可见。

### **Modulation factor** — 调制系数 `1`（默认）| 正标量

用于计算电流参考生成所允许的最大相电压的安全系数。

#### 依赖关系

仅当 **Current references** 设置为 `Automatically generated lookup-table` 时，此参数可见。

### **Number of pole pairs** — 极对数 `8`（默认）| 正整数

转子上永磁体的极对数。

### **Permanent magnet flux linkage (Wb)** — 永磁磁链 `0.04``Wb`（默认）| 正标量

峰值永磁磁链。

### **D-axis inductance (H)** — d 轴电感 `0.00024`（默认）| 正标量

直轴电感。

### **Q-axis inductance (H)** — q 轴电感 `0.00029`（默认）| 正标量

交轴电感。

### **Stator resistance (Ohm)** — 定子电阻 `0.01`（默认）| 正标量

每相定子电阻。

## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

永磁同步电机电流参考生成器

PMSM Current Reference Generator 模块为永磁同步电机（PMSM）在转子 *d*-*q* 参考坐标系下的电流控制实现了一个电流参考生成器。

通常将此模块用于构成控制结构的一系列模块中。

- 通过将此模块放置在 PMSM Current Controller 或 PMSM Current Controller with Pre-Control 模块之前，可以在 d-q 坐标系中生成电压参考。
- 通过将此模块放置在 Velocity Controller 模块之后，可以实现速度控制。

有关从电机测量到电机输入的完整控制结构示例，请参阅 PMSM Field-Oriented Control 模块。

### 方程

PMSM Current Reference Generator 模块使用以下方法之一获得电流参考：

- 零 *d* 轴控制（ZDAC）
- 用户定义的查找表
- 自动生成的查找表

对于 ZDAC 方法，模块将 *d* 轴电流参考 idref 设置为零，并使用转矩方程确定 *q* 轴电流参考 iqref：

idref=0，

以及

iqref= 2Tref3pψm，

其中：

- *Tref* 是参考转矩输入。
- *p* 是极对数。
- *ψm* 是永磁磁链。

对于同步电机基速以下的运行，ZDAC 是一种合适的方法。在基速以上，生成器需要弱磁控制器来调整 *d* 轴参考。

为了离线预生成多个工作点的最优电流参考，使用用户定义查找表方法定义两个查找表：

idref=f(nm,Tref,vdc)，

以及

iqref= g(nm,Tref,vdc)，

其中：

- *nm* 是转子角速度。
- *vdc* 是变换器的直流母线电压。

要让模块创建查找表，请选择自动生成的查找表方法。模块使用两种策略生成查找表：

- 最大转矩每安培
- 弱磁

两种策略之间的选择取决于调制系数。以下方程计算调制系数，

M=VskVph\_max，

其中 *Vs* 是定子电压幅值，*k* 是调制系数，*Vph\_max* 是最大允许相电压。如果调制系数大于 1，模块使用弱磁过程生成电流参考。否则，模块使用最大转矩每安培过程计算电流参考。

### 最大转矩每安培

可以使用最大转矩每安培（MTPA）策略在恒转矩区域（出现在额定转速以下）生成电流参考。

以下方程以角度和幅值的形式定义了定子电流的直轴和交轴分量，

id=−Issinβ

iq= Iscosβ

其中：

- *β* 是定子电流矢量的角度。
- *Is* 是定子电流幅值。

使用 d-q 电流的角度-幅值变体，以下方程计算 PMSM 转矩方程，

Te=3p2ψmIscosβ+3p4(Lq−Ld)Is2sin2β，

其中 *Ld* 和 *Lq* 分别是直轴和交轴电感。

为了获得快速瞬态响应并以尽可能小的定子电流幅值最大化转矩，MTPA 对转矩方程施加 (*dTe*)/*dβ* = 0，由此得到

−3p2ψmIssinβ+3p2(Lq−Ld)Is2(cos2β−sin2β)=0。

通过将 d-q 电流从其角度和幅值变体代回，MTPA *d* 轴电流 *id\_mtpa* 用 *q* 轴分量 *iq\_mtpa* 表示为：

id\_mtpa=ψm2(Lq−Ld)−ψm24(Lq−Ld)2+iq\_mtpa2。

最后，通过将前述方程代入 PMSM 转矩方程的 d-q 变体，模块得到以下多项式：

9p2(Lq−Ld)2iq\_mtpa4+6Trefpψmiq\_mtpa−4Tref2=0。

*q* 轴分量是该多项式的解。

### 弱磁

可以使用弱磁（FW）策略在额定转速以上的区域生成电流参考。

在额定转速以上，定子电压受功率变换器和可用直流母线电压的限制。最大定子电压为

Vs=vd2+vq2≤Vph\_max，

其中 *Vph\_max* 是最大可用定子相电压。

PMSM 的稳态电压方程为

vd=Rsid−ωeLqiq ，

以及

vq=Rsiq+ωe(Ldid+ψm)，

其中 *ωe* 是转子电角速度，单位为 rad/s。

对于额定转速以上的转子转速，定子电阻可忽略不计，弱磁 *d* 轴电流分量 *id\_fw* 由 *vq* 稳态方程用 *q* 轴分量 *iq\_fw* 表示为：

id\_fw=−ψmLd+1LdVph\_max2ωe2−(Lqiq\_fw)2，

最后，通过将 *id\_fw* 方程代入 PMSM 转矩方程，模块得到以下多项式：

9p2(Ld−Lq)2Lq2ωe2iq\_fw4+(9p2ψm2Lq2ωe2−9p2(Ld−Lq)2Vph\_max2)iq\_fw2−12TrefpψmLdLqωe2iqfw+4Tref2Ld2ωe2=0

*q* 轴分量是该多项式的解。

### 假设

电机参数为常数。

### 限制

自动生成的电流参考会在预仿真阶段引入延迟。对于中等功率 PMSM 驱动，延迟约为 300 ms。
