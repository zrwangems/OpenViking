---
type: simulink-block
title: 'Synchronous Machine GENTPJ'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Synchronous'
documentation_page: 'synchronousmachinegentpj'
documentation_source_path: 'ref/synchronousmachinegentpj.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine GENTPJ

## 端口

### 输入

### **Efd** — 标幺励磁电压物理

与标幺励磁电压关联的物理信号端口。

### 输出

### **pu** — 电机标幺测量物理

与电机标幺测量值关联的物理信号向量端口。向量元素为：

- 励磁电压（励磁回路基准，Efd），*pu\_fd\_Efd*
- 励磁电流（励磁回路基准，Ifd），*pu\_fd\_Ifd*
- 电气转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 d 轴电压，*pu\_ed*
- 定子 q 轴电压，*pu\_eq*
- 定子零序电压，*pu\_e0*
- 定子 d 轴电流，*pu\_id*
- 定子 q 轴电流，*pu\_iq*
- 定子零序电流，*pu\_i0*
- 转子电角度，*electrical\_angle\_out*

要连接到此端口，请使用 Synchronous Machine Measurement 模块。

### 守恒

### **R** — 电机转子机械

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳关联的机械旋转守恒端口。

### **~** — 定子绕组电气

与定子绕组关联的可扩展三相电气守恒端口。有关详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否使用复合三相端口或展开三相端口。

### **额定视在功率** — 额定视在功率 `555e6` `A*V`（默认）

额定视在功率。

### **额定电压** — 额定线电压均方根值 `24e3` `V`（默认）

额定线电压的均方根 (RMS) 值。

### **额定电气频率** — 标称电气频率 `60` `Hz`（默认）

模块据以给出额定视在功率的标称电气频率。

### **极对数** — 电机极对数 `1`（默认）

电机的极对数。

### **转子角定义** — 转子角测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角测量的参考点。

当您选择默认值时，当转子角为零时，转子 *d* 轴和定子 *a* 相磁轴对齐。

您可以为该参数选择的另一个值是 `Angle between the a-phase magnetic axis and the q-axis`。当您选择该值时，当转子角为零时，转子 *q* 轴和定子 *a* 相磁轴对齐。

### 阻抗

### **定子电阻, Ra** — 定子电阻 `0.003`（默认）| 正标量

定子电阻。

### **定子漏抗, Xl** — 定子漏抗 `0.15`（默认）| 正标量

定子漏抗。

### **d 轴同步电抗, Xd** — *d* 轴同步电抗 `1.81`（默认）| 正标量

*d* 轴同步电抗。

### **q 轴同步电抗, Xq** — *q* 轴同步电抗 `1.76`（默认）| 正标量

*q* 轴同步电抗。

### **d 轴暂态电抗, Xd'** — *d* 轴暂态电抗 `0.3`（默认）| 正标量

*d* 轴暂态电抗。

### **q 轴暂态电抗, Xq'** — *q* 轴暂态电抗 `0.65`（默认）| 正标量

*q* 轴暂态电抗。

### **d 轴次暂态电抗, Xd''** — *d* 轴次暂态电抗 `0.23`（默认）| 正标量

*d* 轴次暂态电抗。

### **q 轴次暂态电抗, Xq''** — *q* 轴次暂态电抗 `0.25`（默认）| 正标量

*q* 轴次暂态电抗。

### 时间常数

### **d 轴暂态开路, Td0'** — *d* 轴暂态开路 `8` `s`（默认）| 正标量

*d* 轴暂态开路时间常数。此参数值必须：

- 大于 0
- 大于 **d 轴次暂态开路, Td0''**

### **d 轴次暂态开路, Td0''** — *d* 轴次暂态开路 `0.03` `s`（默认）| 正标量

*d* 轴次暂态开路时间常数。

### **q 轴暂态开路, Tq0'** — *q* 轴暂态开路 `1` `s`（默认）| 正标量

*q* 轴暂态开路时间常数。此参数值必须：

- 大于 0
- 大于 **q 轴次暂态开路, Tq0''**

### **q 轴次暂态开路, Tq0''** — *q* 轴次暂态开路 `0.07` `s`（默认）| 正标量

*q* 轴次暂态开路时间常数。

### 饱和

### **磁饱和表示** — 磁饱和表示 `None`（默认）| `Quadratic` | `Scaled quadratic` | `Exponential` | `Open-circuit lookup table`

用于表示模块磁饱和的选项：

- `None` — 模块不对磁饱和建模。
- `Quadratic` — 模块使用二次函数对磁饱和建模。
- `Scaled quadratic` — 模块使用缩放函数对磁饱和建模。
- `Exponential` — 模块使用指数函数对磁饱和建模。
- `Open-circuit lookup table` — 模块使用标幺非互易励磁电流和标幺气隙电压饱和数据对磁饱和建模。

### **饱和因子, S10** — 饱和因子, S10 `0.005`（默认）| 正标量

对应于 1.0 标幺端电压的饱和因子。

#### 依赖关系

要启用此参数，请将 **磁饱和表示** 设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`。

### **饱和因子, S12** — 饱和因子, S12 `0.08`（默认）| 正标量

对应于 1.2 标幺端电压的饱和因子。此参数的值必须大于 **饱和因子, S10** 参数的值。

#### 依赖关系

要启用此参数，请将 **磁饱和表示** 设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`。

### **非互易标幺励磁电流饱和数据, ifd** — 标幺励磁电流饱和数据 `[0, .8, 1.26, 2.29, 2.97]`（默认）| 非负值向量

用于填充气隙电压 *Vag* 对励磁电流 *ifd* 查找表的非互易励磁电流 *ifd* 数据。此参数值必须包含至少五个元素的向量。

#### 依赖关系

要启用此参数，请将 **磁饱和表示** 设置为 `Open-circuit lookup table`。

### **标幺气隙电压饱和数据, Vag** — 标幺气隙电压饱和数据 `[0, .8, 1.08, 1.31, 1.4]`（默认）| 非负值向量

用于填充气隙电压 *Vag* 对励磁电流 *ifd* 查找表的气隙电压 *Vag* 数据。此参数值必须包含至少五个元素的向量。

#### 依赖关系

要启用此参数，请将 **磁饱和表示** 设置为 `Open-circuit lookup table`。

### **Kis** — 定子电流对饱和的影响 `0.05`（默认）| 非负标量

定子电流对饱和的影响。模块使用此参数的值计算 *d* 轴和 *q* 轴饱和因子。

### 初始条件

### **初始化选项** — 用于指定仿真开始时值的选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于指定仿真开始时某些参数和变量的值的选项：

- `Set real power, reactive power, terminal voltage, and terminal phase` — 无论连接的网络如何，设置运行点。
- `Set targets for rotor angle and Park's transform variables` — 在仿真前使用 **变量** 设置指定模块变量的优先级和初始目标值。有关详细信息，请参阅设置模块变量的优先级和初始目标。
- `Set targets for load flow variables` — 选择母线类型，并在 **初始条件** 设置中指定潮流分析的相关参数。

### **源类型** — 电压源模型 `Swing bus`（默认）| `PV bus` | `PQ bus`

模块建模的电压源类型。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set targets for load flow variables`。

### **端电压幅值** — 端电压幅值 `24e3` `V`（默认）| 正标量

端电压幅值。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `Swing bus` 或 `PV bus`。

### **端电压相角** — 端电压相角 `0` `deg`（默认）| 标量

端电压相角。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `Swing bus`。

### **发出的有功功率** — 发出的有功功率 `500e6` `V*A`（默认）| 标量

电机发出的有功功率。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `PV bus` 或 `PQ bus`。

### **发出的无功功率** — 发出的无功功率 `0` `V*A`（默认）| 标量

电机发出的无功功率。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `PQ bus`。

### **最小端电压幅值 (pu)** — 最小端电压幅值 `0.95`（默认）| 正标量

标幺最小稳态电压幅值。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `PQ bus`。

### **端子处的相角搜索范围** — 端子处的相角搜索范围 `[-inf, inf]` `deg`（默认）| 两元素向量

定义端子处相角搜索范围的向量。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set targets for load flow variables`，并将 **源类型** 设置为 `PV bus` 或 `PQ bus`。

### **对电气参考的寄生电导** — 对电气参考的寄生电导 `1e-6` `S`（默认）| 正标量

对电气参考的寄生电导。

#### 依赖关系

要启用此参数，请将 **初始化选项** 设置为 `Set targets for load flow variables`。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

GENTPJ 同步电机

Synchronous Machine GENTPJ 模块对 GENTPJ 同步发电机模型进行建模。GENTPJ 同步发电机模型广泛用于发电厂模型验证和电力系统暂态稳定性研究。

### 使用潮流目标值初始化同步电机

如果模块所在的网络与频率-时间仿真模式兼容，则可以在该网络上执行潮流分析。潮流分析提供稳态值，您可以使用这些值来初始化电机。

有关详细信息，请参阅使用 Simscape Electrical 和频率与时间仿真模式执行潮流分析。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅使用潮流初始化同步电机。

### 方程

同步电机方程基于旋转参考坐标系表示，

θe(t)=Nθr(t),

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。此方程定义 Park 变换：

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

该模块使用 Park 变换定义标幺同步电机方程。这些方程定义 *d* 轴和 *q* 轴定子电压：

vd=ed''ωr−Raid+(Xq''−Xl1+Sq+Xl)iqvq=eq''ωr−Raiq−(Xd''−Xl1+Sd+Xl)id

在这些方程中：

- *e''d* 是次暂态电抗后的 *d* 轴电压。
- *Ra* 是定子电阻。
- *id* 是 *d* 轴定子电流。
- *X''q* 是 *q* 轴次暂态电抗。
- *Xl* 是定子漏电抗。
- *Sq* 是 *q* 轴饱和因子。
- *iq* 是 *q* 轴定子电流。
- *e''q* 是次暂态电抗后的 *q* 轴电压。
- *X''d* 是 *d* 轴次暂态电抗。
- *Sd* 是 *d* 轴饱和因子。

这些方程定义暂态电抗后的电压：

de″ddt=1T″q0[(1+Sq)(e′d−e″d)+iq(X′q−X″q)]de″qdt=1T″d0[(1+Sd)(e′q−e″q)−id(X′d−X″d)]de′ddt=1+SqT′q0(e″dXq−X′qX′q−X″q−e′dXq−X″qX′q−X″q)de′qdt=EfdT′d0+1+SdT′d0(e″qXd−X′dX′d−X″d−e′qXd−X″dX′d−X″d)

在这些方程中：

- *e'd* 是暂态电抗后的 *d* 轴电压。
- *e'q* 是暂态电抗后的 *q* 轴电压。
- *T'd0* 是 *d* 轴暂态开路时间常数。
- *T'q0* 是 *q* 轴暂态开路时间常数。
- *T''d0* 是 *d* 轴次暂态开路时间常数。
- *T''q0* 是 *q* 轴次暂态开路时间常数。
- *X'd* 是 *d* 轴暂态电抗。
- *X'q* 是 *q* 轴暂态电抗。
- *Efd* 是标幺励磁电压。

这些方程定义电机饱和，

ψad=vq+Raiq+Xlidψaq=vd+Raid−Xliqψat=ψad2+ψaq2Sd=f(ψat+Kisid2+iq2)Sq=XqXdf(ψat+Kisid2+iq2)

其中：

- *ψad* 是 *d* 轴气隙磁链。
- *ψaq* 是 *q* 轴气隙磁链。
- *ψat* 是气隙磁链。
- *Kis* 表示定子电流对饱和的影响。
- *Sd* 和 *Sq* 分别是 *d* 轴和 *q* 轴饱和因子。如果将 **Magnetic saturation representation** 参数设置为 `None`，则 *Sd* 和 *Sq* 等于零。如果将 **Magnetic saturation representation** 参数设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`，则模块根据 **Saturation factor, S10** 和 **Saturation factor, S12** 参数的值计算饱和因子函数 *f*。如果将 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table`，则模块根据标幺励磁电流和气隙电压饱和数据计算饱和因子函数 *f*。

此方程定义非互易标幺值系统中的标幺励磁电流：

Ifd=(1+Sd)(e′qXd−X″dX′d−X″d−e″qXd−X′dX′d−X″d).

此方程定义转子转矩：

Te=e″did+e″qiq−(X″d−Xl1+Sd−X″q−Xl1+Sq)idiq.

### 绘图和显示选项

可以使用模块上下文菜单上的 **Electrical** 菜单执行绘图和显示操作。

右键点击该模块。从 **Electrical** 菜单中，选择一个选项：

- **Display Base Values** — 在 MATLAB® 命令窗口中显示电机标幺基准值。
- **Display Associated Initial Conditions** — 在 MATLAB 命令窗口中显示关联的初始条件。
- **Plot Open-Circuit Saturation (pu)** — 在 MATLAB 图窗中绘制气隙电压 *Vag* 与励磁电流 *ifd* 的关系，二者均以标幺值计量。图中包含两条迹线：

  - 未饱和 — 你指定的 **Stator d-axis mutual inductance (unsaturated), Ladu**
  - 饱和 — 你指定的 **Per-unit open-circuit lookup table (Vag versus ifd)**
- **Plot Saturation Factor (pu)** — 使用电机参数在 MATLAB 图窗中绘制饱和因子 *f* 与磁链 *ψat* 的关系，二者均以标幺值计量。如果将 **Magnetic saturation representation** 参数设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`，则模块根据 **Saturation factor, S10** 和 **Saturation factor, S12** 参数的值推导饱和因子函数。

  如果将 **Magnetic saturation representation** 设置为 `Open-circuit lookup table`，则模块根据 **Non-reciprocal per-unit field current saturation data, ifd** 和 **Per-unit air-gap voltage saturation data, Vag** 参数的值推导饱和因子函数。
- **Plot Power Capability Curves** — 在 MATLAB 图窗中绘制有功功率 P 与无功功率 Q 的关系，二者均以标幺值计量。图中可以包含多条迹线。每条迹线对应一个以标幺值（非互易标幺值系统）计量的最大励磁电路电压。图中显示发电机在滞后功率因数下运行时产生的最大无功功率，以及在超前功率因数下运行时吸收的最小无功功率。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当在 **Initial Conditions** 部分将 **Initialization option** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
