---
type: simulink-block
title: 'MTPA Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'mtpacontrolreference'
documentation_source_path: 'ref/mtpacontrolreference.html'
language: zh-CN
chinese_source: worker-translation
---

# MTPA Control Reference

## 端口

### 输入

### **Tref** — 参考转矩值标量

模块为其计算参考电流的参考转矩输入值。
此端口的单位取决于 **Input units** 参数值。
如果将此参数设置为 `SI Units`，则该端口接受
以 Nm 为单位的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 机械速度标量

模块为其计算参考电流的参考机械速度值。此端口的单位取决于 **Input units**
参数值。如果将此参数设置为 `SI Units`，则该
端口接受以机械弧度/秒为单位的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 直流母线电压标量

可变直流母线电压。此端口的单位取决于 **Input
units** 参数值。如果将此参数设置为 `SI
Units`，则该端口接受以伏特为单位的输入信号。

#### 依赖关系

要启用此端口，请将 **Type of motor** 设置为
`Interior PMSM`，并将 **Vdc input method**
设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Idref** — 参考 *d* 轴电流标量

能够高效生成输入转矩和速度值的参考 *d* 轴相电流。

此端口的单位取决于由 **Input units** 参数定义的模块输入单位。如果将此参数设置为
`SI Units`，则该端口输出以安培为单位的信号。

**数据类型：** `single` | `double` | `fixed point`

### **Iqref** — 参考 *q* 轴电流标量

能够高效生成输入转矩和速度值的参考 *q* 轴相电流。

此端口的单位取决于由 **Input units** 参数定义的模块输入单位。如果将此参数设置为
`SI Units`，则该端口输出以安培为单位的信号。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Type of motor** — PMSM 类型 `Interior PMSM`（默认）| `Surface PMSM`

基于永磁体位置的 PMSM 类型。

### **Number of pole pairs** — 可用极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Stator resistance per phase (Ohm)** — 定子相绕组电阻（欧姆） `0.36`（默认）| 标量

定子相绕组的电阻（以欧姆为单位）。

#### 依赖关系

要启用此参数，请将 **Type of motor** 设置为
`Interior PMSM`。

### **Stator d-axis inductance (H)** — *d* 轴定子绕组电感 `0.2e-3`（默认）| 标量

沿旋转 *dq* 参考坐标系 *d* 轴的定子绕组电感（以亨利为单位）。

### **Stator q-axis inductance (H)** — *q* 轴定子绕组电感 `0.4e-3`（默认）| 标量

沿旋转 *dq* 参考坐标系 *q* 轴的定子绕组电感（以亨利为单位）。

#### 依赖关系

要启用此参数，请将 **Type of motor** 设置为
`Interior PMSM`。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `6.4e-3`（默认）| 标量

定子绕组与转子上的永磁体之间的磁链（以韦伯为单位）（韦伯）。

### **Max current (A)** — 电机最大相电流限值（安培） `7.1`（默认）| 标量

电机的最大相电流限值（以安培为单位）。

### **Vdc input method** — Vdc 输入方法 `Specify via dialog`（默认）| `Input port`

使用以下方法之一来指定 *Vdc* 输入。

- `Specify via dialog` — 使用参数 **DC voltage
  (V)** 指定固定参考电压 *Vdc*。
- `Input port` — 使用输入端口 `Vdc` 指定可变参考电压
  *Vdc*。

  **注意**

  如果为 *Vdc* 选择 `Input port` 输入方法，请确保在 **Input Units** 选项卡中配置 **Base voltage
  (V)** 参数。

#### 依赖关系

要启用此参数，请将 **Type of motor** 设置为
`Interior PMSM`。

### **DC voltage (V)** — 直流母线电压（伏特） `24`（默认）| 标量

直流母线电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **Type of motor** 设置为
`Interior PMSM`，并将 **Vdc input method**
设置为 `Specify via dialog`。

### Input Units

### **Input signal units** — 模块输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

模块输入值的单位。

### **Base speed (rpm)** — 电机基准转速（rpm） `4107`（默认）| 标量

在额定电压和额定电流下、弱磁区域之外的电机转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Input signal units** 设置为
`Per-Unit (PU)`。

### **Base current (A)** — 用于标幺值转换的基准电流（安培） `19.3`（默认）| 标量

对应于 1 标幺值的电流（单位：安培）。建议您使用模数转换器 (ADC) 检测到的最大电流作为基准电流。

#### 依赖关系

要启用此参数，请将 **Input signal units** 设置为
`Per-Unit (PU)`。

### **Base torque (Nm)** — 用于标幺值转换的基准转矩（Nm） `0.74112`（默认）| 标量

对应于 1 标幺值的转矩（单位：Nm）。有关更多详细信息，请参阅 Per-Unit System 页面。

您无法指定此值。该模块使用其他参数在内部计算此值。

#### 依赖关系

要显示此参数，请将 **Input signal units** 设置为
`Per-Unit (PU)`。

### **Base voltage (V)** — 用于标幺值转换的基准电压（伏特） `24/sqrt(3)`（默认）| 标量

对应于 1 标幺值的电压（单位：伏特）。有关更多详细信息，请参阅 Per-Unit System 页面。

您无法指定此值。该模块使用其他参数在内部计算此值。

#### 依赖关系

要显示此参数，请将 **Input signal units** 设置为
`Per-Unit (PU)`。

### Implementation

### **Prioritise execution time** — 缩减计算以缩短算法执行时间 `on`（默认）| `off`

如果选择此参数，该模块将采用计算近似来优先缩短并减少算法执行时间。清除此字段可在不使用近似的情况下迭代运行模块算法。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### Fixed-Point Conversion 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算最大转矩每安培 (MTPA) 和弱磁操作的参考电流

MTPA Control Reference 模块计算最大转矩每安培 (MTPA) 和弱磁操作的 *d* 轴和
*q* 轴参考电流值。计算得到的参考电流值可为永磁同步电机 (PMSM) 带来高效输出。

您可以指定参考转矩和反馈机械转速，该模块将输出用于 MTPA 和弱磁操作的相应 *d* 轴和 *q* 轴参考电流值。对于给定的机械转速，除了尽可能高的转矩值外，该模块还支持小于 PMSM 额定转矩的参考转矩值。

该模块通过求解数学关系来计算参考电流值。

此外，您可以使用 **Vdc input method** 参数将该模块配置为通过 **DC voltage
(V)** 参数接受固定参考直流电压，或通过单独的输入端口 **Vdc** 接受可变参考直流电压。

以下方程描述了该模块对参考 *d* 轴和 *q* 轴电流值的计算：

### 永磁同步电机的数学模型

这些模型方程描述了永磁同步电机在转子磁链参考坐标系下的动态特性：

vd=idRs+ dλddt − ωeLqiq

vq=iqRs+ dλqdt + ωeLdid+ ωeλpm

λd=Ldid+ λpm

λq=Lqiq

Te= 32p(λpmiq+(Ld− Lq)idiq)

Te− TL=Jdωmdt +Bωm

其中：

- vd 是 *d* 轴电压（伏特）。
- vq 是 *q* 轴电压（伏特）。
- id 是 *d* 轴电流（安培）。
- iq 是 *q* 轴电流（安培）。
- Rs 是定子相绕组电阻（欧姆）。
- λpm 是永磁体磁链（韦伯）。
- λd 是 *d* 轴磁链（韦伯）。
- λq 是 *q* 轴磁链（韦伯）。
- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- ωm 是转子机械速度（弧度/秒）。
- Ld 是 *d* 轴绕组电感（亨利）。
- Lq 是 *q* 轴绕组电感（亨利）。
- Te 是永磁同步电机产生的电磁转矩（牛·米）。
- TL 是负载转矩（牛·米）。
- p 是电机极对数。
- J 是惯性系数（千克·平方米）。
- B 是摩擦系数（千克·平方米/秒）。

### 基速

基速是电机在额定电压和额定负载下、弱磁区域之外的最大转速。以下方程描述了电机基速的计算。

逆变器电压约束通过计算 *d* 轴和 *q* 轴电压来定义：

vdo=− ωeLqiq

vqo=ωe(Ldid+ λpm)

vmax= vdc 3 −Rsimax ≥ vdo2+ vqo2

电流限制圆定义了电流约束，可表示为：

imax2= id 2+ iq2

在上述方程中，对于表贴式永磁同步电机，id 为零。对于内置式永磁同步电机，该模块考虑对应于 MTPA 的 id 和 iq 值。

利用这些方程，我们可以计算基速为：

ωbase= 1p⋅ vmax(Lqiq)2+(Ldid+ λpm)2

其中：

- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- ωbase 是电机的机械基速（弧度/秒）。
- id 是 *d* 轴电流（安培）。
- iq 是 *q* 轴电流（安培）。
- vdo 是 id 为零时的 *d* 轴电压（伏特）。
- vqo 是 iq 为零时的 *q* 轴电压（伏特）。
- Ld 是 *d* 轴绕组电感（亨利）。
- Lq 是 *q* 轴绕组电感（亨利）。
- Rs 是定子相绕组电阻（欧姆）。
- λpm 是永磁体磁链（韦伯）。
- vd 是 *d* 轴电压（伏特）。
- vq 是 *q* 轴电压（伏特）。
- vmax 是提供给电机的最大基波线电压到中性点电压（峰值）（伏特）。
- vdc 是提供给逆变器的直流电压（伏特）。
- imax 是电机的最大相电流（峰值）（安培）。
- p 是电机极对数。

### Surface PMSM

对于表贴式永磁同步电机，当电机运行在基速以下时，可以通过使用零 *d* 轴电流来实现最大转矩。对于弱磁运行，该模块使用恒压恒功率控制（CVCP）算法计算参考 *d* 轴电流，该算法由以下方程定义：

如果 ωm≤ ωbase：

- id\_mtpa= 0
- iq\_mtpa= Tref32⋅p⋅λpm
- id\_sat= id\_mtpa= 0
- iq\_sat=sat(iq\_mtpa,  imax)

如果 ωm> ωbase：

- id\_fw= (ωe\_base− ωe)λpmωeLd
- id\_sat=max(id\_fw,  −imax)
- iq\_fw= Tref32⋅p⋅λpm
- iq\_lim= imax2− id\_sat2
- iq\_sat=sat(iq\_fw,  iq\_lim)

用于计算 iq\_sat 的饱和函数为：

如果 iq\_fw< −iq\_lim，

iq\_sat= −iq\_lim

如果 iq\_fw>iq\_lim，

iq\_sat= iq\_lim

如果  −iq\_lim≤iq\_fw≥iq\_lim，

iq\_sat= iq\_fw

该模块输出以下值：

Idref=id\_sat

Iqref=iq\_sat

其中：

- ωe 是对应于定子电压频率的电气速度（弧度/秒）。
- ωm 是转子机械速度（弧度/秒）。
- ωbase 是电机的机械基速（弧度/秒）。
- ωe\_base 是电机的电气基速（弧度/秒）。
- id\_mtpa 是对应于 MTPA 的 *d* 轴相电流（安培）。
- iq\_mtpa 是对应于 MTPA 的 *q* 轴相电流（安培）。
- Tref 是参考转矩（Nm）。
- p 是电机极对数。
- λpm 是永磁磁链（韦伯）。
- id\_fw 是 *d* 轴弱磁电流（安培）。
- iq\_fw 是 *q* 轴弱磁电流（安培）。
- Ld 是 *d* 轴绕组电感（亨利）。
- imax 是电机的最大相电流（峰值）（安培）。
- id\_sat 是 *d* 轴饱和电流（安培）。
- iq\_sat 是 *q* 轴饱和电流（安培）。
- Idref 是对应于参考转矩和参考速度的 *d* 轴电流（安培）。
- Iqref 是对应于参考转矩和参考速度的 *q* 轴电流（安培）。

### Interior PMSM

对于内置式 PMSM，您可以通过从转矩方程计算 *d* 轴和 *q* 轴参考电流来实现最大转矩。对于弱磁操作，该模块使用电压和电流受限最大转矩控制 (VCLMT) 算法计算参考 *d* 轴电流。

MTPA 和弱磁操作的参考电流由以下方程定义：

im\_ref= 2⋅Tref3⋅p⋅λpm

im=min(im\_ref,  imax)

id\_mtpa=λpm4(Lq−Ld)−λpm216(Lq−Ld)2+im22

iq\_mtpa=im2−(id\_mtpa)2

vdo=−ωeLqiq

vqo=ωe(Ldid+ λpm)

vdo2+vqo2=vmax2

(Lqiq)2+(Ldid+ λpm)2≤ vmax2ωe2

iq= imax2− id2

(Ld2− Lq2)id2+2λpmLdid+ λpm2+ Lq2imax2−vmax2ωe2=0

这两个方程描述了对应于给定转速值的最大可能转矩的弱磁电流的计算：

id\_fw= −λpmLd+ (λpmLd)2− (Ld2− Lq2)(λpm2+  Lq2imax2− vmax2ωe2  )(Ld2− Lq2)

iq\_fw= imax2− id\_fw2

这两个方程描述了给定转速和转矩值的弱磁电流的计算。

9p2(Ld−Lq)2Lq2ωe2iq\_fw4+(9p2λpm2Lq2ωe2−9p2(Ld−Lq)2vmax2)iq\_fw2−12TrefpλpmLdLqωe2iq\_fw+4(Tref)2Ld2ωe2=0

id\_fw=−λpmLd+1Ldvmax2ωe2−(Lqiq\_fw)2

为了减少计算时间，该模块使用近似方法来求解上述多项式。

如果 ωm≤ ωbase，

Idref= id\_mtpa

Iqref= iq\_mtpa

如果 ωm> ωbase，

Idref=max(id\_fw,−imax)

iq\_fw= imax2− id\_fw2

如果 iq\_fw<im，

Iqref=iq\_fw

如果 iq\_fw≥im，

Iqref=im

对于负参考转矩值，该模块更新 im 和 Iqref 的符号并相应地修改方程。

其中：

- im\_ref 是产生参考转矩的估计最大电流（安培）。
- im 是估计最大电流的饱和值（安培）。
- id\_max 是最大 *d* 轴相电流（峰值）（安培）。
- iq\_max 是最大 *q* 轴相电流（峰值）（安培）。
- Tref 是参考转矩 (Nm)。
- Idref 是对应于参考转矩和参考转速的 *d* 轴电流分量（安培）。
- Iqref 是对应于参考转矩和参考转速的 *q* 轴电流分量（安培）。
- p 是电机极对数。
- λpm 是永磁体磁链（韦伯）。
- id\_mtpa 是对应于 MTPA 的 *d* 轴相电流（安培）。
- iq\_mtpa 是对应于 MTPA 的 *q* 轴相电流（安培）。
- Ld 是 *d* 轴绕组电感（亨利）。
- Lq 是 *q* 轴绕组电感（亨利）。
- imax 是电机的最大相电流（峰值）（安培）。
- vmax 是提供给电机的最大基波线电压到中性点电压（峰值）（伏特）。
- vdo 是当 id 为零时的 *d* 轴电压（伏特）。
- vqo 是当 iq 为零时的 *q* 轴电压（伏特）。
- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- id 是 *d* 轴电流（安培）。
- iq 是 *q* 轴电流（安培）。
- id\_fw 是 *d* 轴弱磁电流（安培）。
- iq\_fw 是 *q* 轴弱磁电流（安培）。
- ωbase 是电机的机械基速（弧度/秒）。
