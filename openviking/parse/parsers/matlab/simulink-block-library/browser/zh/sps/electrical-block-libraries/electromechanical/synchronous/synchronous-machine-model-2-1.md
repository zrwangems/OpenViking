---
type: simulink-block
title: 'Synchronous Machine Model 2.1'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachinemodel21'
documentation_source_path: 'ref/synchronousmachinemodel21.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine Model 2.1

## 端口

### 输出

### **pu** — 电机标幺值测量（物理）

物理信号矢量端口，与电机标幺值测量相关联。矢量元素为：

- 励磁电压（励磁电路基值，Efd），
  *pu\_fd\_Efd*
- 励磁电流（励磁电路基值，Ifd），
  *pu\_fd\_Ifd*
- 电气转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 d 轴电压，*pu\_ed*
- 定子 q 轴电压，*pu\_eq*
- 定子零序电压，*pu\_e0*
  — 提供此端口是为了保持与其他电机模型的兼容接口。其值始终为零。
- 定子 d 轴电流，*pu\_id*
- 定子 q 轴电流，*pu\_iq*
- 定子零序电流，*pu\_i0*
  — 提供此端口是为了保持与其他电机模型的兼容接口。其值始终为零。
- 转子电角度，
  *electrical\_angle\_out*

要将此端口连接，请使用 Synchronous Machine Measurement 模块。

### 守恒

### **fd+** — 励磁绕组正极端子（电气）

与励磁绕组正极端子关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子（电气）

与励磁绕组负极端子关联的电气守恒端口。

### **R** — 电机转子（机械）

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳（机械）

与电机机壳关联的机械旋转守恒端口。

### **~** — 定子绕组（电气）

与定子绕组关联的可扩展三相端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **n** — 中性相（电气）

与星形绕组配置的中性点关联的电气守恒端口。提供此端口是为了保持对现有电机模型的兼容接口。此端口上的电压和电流被忽略。

### **a** — *a* 相（电气）

与 *a* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相（电气）

与 *b* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相（电气）

与 *c* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **HA** — *a* 相端子热端口（热）

与定子绕组 *a* 关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口（热）

与定子绕组 *b* 关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口（热）

与定子绕组 *c* 关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

### **HR** — 转子热端口（热）

与转子关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 用于启用热端口的选项 `No thermal port`（默认） | `Show thermal port`

用于启用模块热端口并对生成热量和电机温度的影响进行建模的选项。

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否使用复合三相端口或扩展三相端口。

### **额定视在功率** — 额定视在功率 `555e6` `V*A`（默认）

额定视在功率。

### **额定电压** — RMS 额定线电压 `24e3` `V`（默认）

RMS 额定线电压。

### **额定电气频率** — 标称电气频率 `60` `Hz`（默认）

给出额定视在功率时的标称电气频率。

### **极对数** — 极对数 `1`（默认）

电机极对数。

### **通过以下方式指定参数化** — 模块参数化 `Fundamental parameters`（默认） | `Standard parameters`

模块参数化方法。选项为：

- `Fundamental parameters` — 基本参数在 **阻抗** 设置中可见，而 **时间常数** 设置不可见。
- `Standard parameters` — 标准参数在 **阻抗** 设置中可见，且 **时间常数** 设置可见。

此参数会影响 **时间常数** 设置和 **阻抗** 设置中参数的可见性。

### **通过以下项指定空载时产生额定端子电压所需的励磁电路输入** — 通过以下项指定空载时产生额定端子电压所需的励磁电路输入 `Field circuit current`（默认） | `Field circuit voltage`

励磁电路参数化方法。选项为：

- `Field circuit voltage` — 以电压形式指定励磁电路。
- `Field circuit current` — 以电流形式指定励磁电路。此方法是默认的励磁电路参数化方法。

此参数会影响 **励磁电路电压** 和 **励磁电路电流** 参数的可见性。

### **励磁电路电压** — 励磁电路电压 `92.95` `V`（默认）

在电机端子上产生额定电压时，励磁电路两端的电压。

#### 依赖项

仅当 **通过以下项指定空载时产生额定端子电压所需的励磁电路输入** 参数设置为 `Field circuit voltage` 时，此参数才可见。

### **励磁电路电流** — 励磁电路电流 `1300` `A`（默认）

在电机端子上产生额定电压时，励磁电路中的电流。

#### 依赖项

仅当 **通过以下项指定空载时产生额定端子电压所需的励磁电路输入** 参数设置为 `Field circuit current` 时，此参数才可见。

### **转子角定义** — 转子角测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认） | `Angle between the a-phase magnetic axis and the q-axis`

转子角测量的参考点。

当选择默认值时，转子 *d* 轴与定子 *a* 相磁轴在转子角为零时对齐。

此参数可选择的另一个值是 `Angle between the a-phase magnetic axis and the q-axis`。当选择此值时，转子 *q* 轴与定子 *a* 相磁轴在转子角为零时对齐。

### 阻抗

### **定子 d 轴互电感（未饱和），Ladu** — 定子 d 轴互电感（未饱和） `1.66`（默认） | 正标量

未饱和定子 *d* 轴互电感。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子 q 轴互电感（未饱和），Laqu** — 定子 q 轴互电感（未饱和） `1.61`（默认） | 正标量

未饱和定子 *q* 轴互电感。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子漏电感，Ll** — 定子漏电感 `0.15`（默认） | 正标量

定子漏电感。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子电阻，Ra** — 定子电阻 `0.003`（默认） | 正标量

定子电阻。此参数必须大于 0。

### **转子励磁电路电感，Lfd** — 转子励磁电路电感 `0.165`（默认） | 正标量

转子励磁电路电感。此参数必须大于 0。

### **转子励磁电路电阻，Rfd** — 转子励磁电路电阻 `0.0006`（默认） | 正标量

转子励磁电路电阻。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 d 轴阻尼绕组 1 电感，L1d** — 转子 d 轴阻尼绕组 1 电感 `0.1713`（默认） | 正标量

转子 *d* 轴阻尼绕组 1 电感。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 d 轴阻尼绕组 1 电阻，R1d** — 转子 d 轴阻尼绕组 1 电阻 `0.0284`（默认） | 正标量

转子 *d* 轴阻尼绕组 1 电阻。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 q 轴阻尼绕组 1 电感，L1q** — 转子 q 轴阻尼绕组 1 电感 `0.1066`（默认） | 正标量

转子 *q* 轴阻尼绕组 1 电感。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **转子 q 轴阻尼绕组 1 电阻，R1q** — 转子 q 轴阻尼绕组 1 电阻 `0.0650`（默认） | 正标量

转子 *q* 轴阻尼绕组 1 电阻。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Fundamental parameters` 时，此参数才可见。

### **定子漏电抗，Xl** — 定子漏电抗 `0.15`（默认） | 正标量

定子漏电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d 轴同步电抗，Xd** — d 轴同步电抗 `1.81`（默认） | 正标量

*d* 轴同步电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q 轴同步电抗，Xq** — q 轴同步电抗 `1.76`（默认） | 正标量

*q* 轴同步电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d 轴瞬态电抗，Xd'** — d 轴瞬态电抗 `0.3`（默认） | 正标量

*d* 轴瞬态电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### **d 轴次暂态电抗，Xd''** — d 轴次暂态电抗 `0.23`（默认） | 正标量

*d* 轴次暂态电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### **q 轴次暂态电抗，Xq''** — q 轴次暂态电抗 `0.25`（默认） | 正标量

*q* 轴次暂态电抗。此参数必须大于 0。

#### 依赖项

仅当 **通过以下方式指定参数化** 参数设置为 `Standard parameters` 时，此参数才可见。

### 时间常数

### **指定 d 轴时间常数** — 指定 d 轴时间常数 `Open circuit`（默认） | `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置会影响 *d* 轴时间常数参数的可见性。

### **d 轴瞬态开路，Td0'** — d 轴瞬态开路 `8` `s`（默认） | 正标量

*d* 轴瞬态开路时间常数。此参数必须：

- 大于 0。
- 大于 **d 轴次暂态开路，Td0''**。

#### 依赖项

仅当 **指定 d 轴瞬态时间常数** 参数设置为 `Open circuit` 时，此参数才可见。

### **d 轴瞬态短路，Td'** — d 轴瞬态短路 `1.3260` `s`（默认） | 正标量

*d* 轴瞬态短路时间常数。此参数必须：

- 大于 0。
- 大于 **d 轴次暂态短路，Td''**。

#### 依赖项

仅当 **指定 d 轴瞬态时间常数** 参数设置为 `Short circuit` 时，此参数才可见。

### **d 轴次暂态开路，Td0''** — d 轴次暂态开路 `0.03` `s`（默认） | 正标量

*d* 轴次暂态开路时间常数。此参数必须大于 0。

#### 依赖项

仅当 **指定 d 轴瞬态时间常数** 参数设置为 `Open circuit` 时，此参数才可见。

### **d 轴次暂态短路，Td''** — d 轴次暂态短路 `0.0230` `s`（默认） | 正标量

*d* 轴次暂态短路时间常数。此参数必须大于 0。

#### 依赖项

仅当 **指定 d 轴瞬态时间常数** 参数设置为 `Short circuit` 时，此参数才可见。

### **指定 q 轴时间常数** — 指定 q 轴时间常数 `Open circuit`（默认） | `Short circuit`

在 `Open circuit` 和 `Short circuit` 之间选择。

此参数的设置会影响 *q* 轴时间常数参数的可见性。

### **q 轴次暂态开路，Tq0''** — q 轴次暂态开路 `0.07` `s`（默认） | 正标量

*q* 轴次暂态开路时间常数。此参数必须大于 0。

#### 依赖项

仅当 **指定 q 轴瞬态时间常数** 参数设置为 `Open circuit` 时，此参数才可见。

### **q 轴次暂态短路，Tq''** — q 轴次暂态短路 `0.0269` `s`（默认） | 正标量

*q* 轴次暂态短路时间常数。此参数必须大于 0。

#### 依赖项

仅当 **指定 q 轴瞬态时间常数** 参数设置为 `Short circuit` 时，此参数才可见。

### 初始条件

### **初始化选项** — 初始化选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认） | `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于在仿真开始时为某些参数和变量指定值的模型。若要：

与所连接网络无关地设置运行点，请选择 `Set real power, reactive power, terminal voltage and terminal phase`。

- 使用 **变量** 设置在仿真前指定模块变量的优先级和初始目标值，请选择 `Set targets for rotor angle and Park's transform variables`。有关更多信息，请参阅为模块变量设置优先级和初始目标。
- 选择母线类型并在 **初始条件** 设置中指定潮流分析的相关参数，请选择 `Set targets for load flow variables`。

#### 依赖项

如果将此参数设置为：

- `Set targets for rotor angle and Park's transform variables` — **变量** 设置变为可见。
- `Set real power, reactive power, terminal voltage, and terminal phase` — 相关参数变为可见。
- `Set targets for load flow variables` — 相关参数变为可见。

### **源类型** — 电压源模型 `Swing bus`（默认） | `Voltage source with series impedance` | `PV bus` | `PQ bus`

该模块所建模的电压源类型。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set targets for load flow variables`，且 **源类型** 参数设置为 `Swing bus` 或 `PV bus` 时，此参数可见。

**终端电压幅值**、**终端电压相角**、**生成有功功率**、**生成无功功率**、**最小终端电压幅值 (pu**、**终端相角搜索范围** 和 **终端相角搜索范围** 的可见性取决于您为此参数选择的值。

### **终端电压幅值** — 终端电压幅值 `24e3` `V`（默认）

终端电压幅值。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `Swing bus` 或 `PV bus` 时，此参数可见。

### **终端电压相角** — 终端电压相角 `0` `deg`（默认）

终端电压相角。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `Swing bus` 时，此参数可见。

### **生成有功功率** — 生成有功功率 `500e6` `V*A`（默认）

生成有功功率。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `PV bus` 或 `PQ bus` 时，此参数可见。

### **生成无功功率** — 生成无功功率 `0` `V*A`（默认）

生成无功功率。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `PQ bus` 时，此参数可见。

### **最小终端电压幅值 (pu)** — 最小终端电压幅值 `0.95`（默认）

标幺最小稳态电压幅值。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `PQ bus` 时，此参数可见。

### **终端相角搜索范围** — 终端相角搜索范围 `[-inf, inf]` `deg`（默认）

定义相角搜索范围的向量。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set targets for load flow variables` 且 **源类型** 参数设置为 `PV bus` 或 `PQ bus` 时，此参数可见。

### **到电气参考的寄生电导** — 到电气参考的寄生电导 `1e-6` `S`（默认）

到电气参考的寄生电导。

#### 依赖项

仅当 **初始化选项** 参数设置为 `Set targets for load flow variables` 时，此参数可见。

### 热

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

### **测量温度** — 额定温度 `298.15` `k`（默认） | real scalar

用于给出电机参数的温度。

### **电阻温度系数** — 温度系数 `3.93e-3` `1/K`（默认） | positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **每个定子绕组的热质量** — 绕组热质量 `100` `J/K`（默认） | positive scalar

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **转子热质量** — 转子热质量 `200` `J/K`（默认） | positive scalar

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在以前版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

具有简化变换、简化表示以及基本或标准参数化的同步电机

Synchronous Machine Model 2.1 模块对同步电机建模，该电机在 *d* 轴上有一个励磁绕组和一个阻尼器，在 *q* 轴上有一个阻尼器。您使用基本或标准参数来定义电机特性。此模块包含 *d**q* Park 变换，因此仅用于平衡运行。

### 使用潮流目标值进行同步电机初始化

如果该模块位于与频率-时间仿真模式兼容的网络中，您可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关更多信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅 Synchronous Machine Initialization with Loadflow。

### 方程

同步电机方程相对于旋转参考系表示，旋转参考系定义为

θe(t)=Nθr(t),

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考系。Park 变换定义为

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)].

Park 变换用于定义标幺值同步电机方程。定子电压方程定义为

ed=ed"−Raid+xq"iq

和

eq=eq"−xd"id−Raiq,

其中：

- *e”d* 和 *e”q* 是次暂态电抗后的 *d* 轴和 *q* 轴电压。
- *Ra* 是定子电阻。
- *id* 和 *iq* 是 *d* 轴和 *q* 轴定子电流，定义为

  [idiq]=Ps[iaibic].

  *ia*、*ib* 和 *ic* 是从端口 ~ 流向端口 n 的定子电流。
- *x”d* 和 *x”q* 是 *d* 轴和 *q* 轴次暂态电抗。

- *ed* 和 *eq* 是 *d* 轴和 *q* 轴定子电压，定义为

  [edeq]=Ps[vavbvc].

  *va*、*vb* 和 *vc* 是从端口 ~ 到中性端口 n 测得的定子电压。

转子电压方程定义为

efd=Rfd⋅ifd,

其中：

- *Rfd* 是转子励磁电路电阻。
- *ifd* 是使用同步电机模型倒数标幺值系统的标幺励磁电流。
- *efd* 是使用同步电机模型倒数标幺值系统的标幺励磁电压。

暂态电抗后电压方程定义为

ded"dt=(xq−xq")iq−ed"Tq0",

deq'dt=Efd−(xd−xd')id−eq'Td0',

和

deq"dt=eq'−(xd'−xd")id−eq"Td0",

其中：

- *xd* 和 *xq* 是 *d* 轴和 *q* 轴同步电抗。
- *T”d0* 和 *T”q0* 是 *d* 轴和 *q* 轴次暂态开路时间常数。
- *Efd* 是使用励磁机模型非倒数标幺值系统的标幺励磁电压。
- *x’d* 是 *d* 轴暂态电抗。
- *e’q* 是暂态电抗后的 *q* 轴电压。
- *T’d0* 是 *d* 轴暂态开路时间常数。

转子转矩定义为

Te=ed"id+eq"iq−(xd"−xq")idiq.

这些定义方程不描述您可以在对话框中设置的参数。要查看它们与方程系数的关系，请参阅 P. Kundur 关于理解、建模、分析和缓解电力系统稳定性与控制问题的书 [1]。

### 显示选项

您可以使用模块上下文菜单上的 **Electrical** 菜单执行显示操作。

右键单击该模块，然后从 **Electrical** 菜单选择一个选项：

- **Display Base Values** 在 MATLAB® Command Window 中显示机器标幺基准值。
- **Display Associated Base Values** 在 MATLAB Command Window 中显示关联的标幺基准值。
- **Display Associated Initial Conditions** 在 MATLAB Command Window 中显示关联的初始条件。

### 对热效应建模

您可以公开热端口，以对生成热量和机器温度的影响建模。要公开热端口，请将 **建模选项** 参数设置为以下任一值：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含多个热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当您在 **Initial Conditions** 部分将 **初始化选项** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。
