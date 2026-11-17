---
type: simulink-block
title: 'Synchronous Machine GENTPJ'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinegentpj'
documentation_source_path: 'ref/synchronousmachinegentpj.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine GENTPJ

## 端口
```yaml
ports:
- name: Efd
  summary: 标幺励磁电压物理信号
  direction: input
- name: pu
  summary: 电机标幺测量物理信号
  direction: output
- name: R
  summary: 电机转子机械
  direction: output
- name: C
  summary: 电机机壳机械
  direction: output
- name: '~'
  summary: 定子绕组电气
  direction: output
- name: a
  summary: '*a* 相电气'
  direction: output
- name: b
  summary: '*b* 相电气'
  direction: output
- name: c
  summary: '*c* 相电气'
  direction: output
```

### 输入

### **Efd** — 标幺励磁电压物理信号

与标幺励磁电压相关联的物理信号端口。
### 输出

### **pu** — 电机标幺测量物理信号

与电机标幺测量值相关联的物理信号矢量端口。矢量元素为：

- 励磁电压（励磁回路基准值，Efd），*pu\_fd\_Efd*
- 励磁电流（励磁回路基准值，Ifd），*pu\_fd\_Ifd*
- 电磁转矩，*pu\_torque*
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

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳相关联的机械旋转守恒端口。

### **~** — 定子绕组电气

与定子绕组相关联的可扩展三相电气守恒端口。有关详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主
- name: Rated apparent power
  summary: 额定视在功率 555e6 A*V（默认）
  group: 主
- name: Rated voltage
  summary: 额定线电压均方根值 24e3 V（默认）
  group: 主
- name: Rated electrical frequency
  summary: 额定电气频率 60 Hz（默认）
  group: 主
- name: Number of pole pairs
  summary: 电机极对数 1（默认）
  group: 主
- name: Rotor angle definition
  summary: 转子角度测量的参考点 Angle between the a-phase magnetic axis and the d-axis（默认）| Angle between the a-phase magnetic axis
    and the q-axis
  group: 主
- name: Stator resistance, Ra
  summary: 定子电阻 0.003（默认）| 正标量
  group: 阻抗
- name: Stator leakage reactance, Xl
  summary: 定子漏电抗 0.15（默认）| 正标量
  group: 阻抗
- name: d-axis synchronous reactance, Xd
  summary: '*d* 轴同步电抗 1.81（默认）| 正标量'
  group: 阻抗
- name: q-axis synchronous reactance, Xq
  summary: '*q* 轴同步电抗 1.76（默认）| 正标量'
  group: 阻抗
- name: d-axis transient reactance, Xd'
  summary: '*d* 轴瞬态电抗 0.3（默认）| 正标量'
  group: 阻抗
- name: q-axis transient reactance, Xq'
  summary: '*q* 轴瞬态电抗 0.65（默认）| 正标量'
  group: 阻抗
- name: d-axis subtransient reactance, Xd''
  summary: '*d* 轴次瞬态电抗 0.23（默认）| 正标量'
  group: 阻抗
- name: q-axis subtransient reactance, Xq''
  summary: '*q* 轴次瞬态电抗 0.25（默认）| 正标量'
  group: 阻抗
- name: d-axis transient open-circuit, Td0'
  summary: '*d* 轴瞬态开路 8 s（默认）| 正标量'
  group: 时间常数
- name: d-axis subtransient open-circuit, Td0''
  summary: '*d* 轴次瞬态开路 0.03 s（默认）| 正标量'
  group: 时间常数
- name: q-axis transient open-circuit, Tq0'
  summary: '*q* 轴瞬态开路 1 s（默认）| 正标量'
  group: 时间常数
- name: q-axis subtransient open-circuit, Tq0''
  summary: '*q* 轴次瞬态开路 0.07 s（默认）| 正标量'
  group: 时间常数
- name: Magnetic saturation representation
  summary: 磁饱和表示 None（默认）| Quadratic | Scaled quadratic | Exponential | Open-circuit lookup table
  group: 饱和
- name: Saturation factor, S10
  summary: 饱和系数，S10 0.005（默认）| 正标量
  group: 饱和
- name: Saturation factor, S12
  summary: 饱和系数，S12 0.08（默认）| 正标量
  group: 饱和
- name: Non-reciprocal per-unit field current saturation data, ifd
  summary: 标幺励磁电流饱和数据 [0, .8, 1.26, 2.29, 2.97]（默认）| 非负值矢量
  group: 饱和
- name: Per-unit air-gap voltage saturation data, Vag
  summary: 标幺气隙电压饱和数据 [0, .8, 1.08, 1.31, 1.4]（默认）| 非负值矢量
  group: 饱和
- name: Kis
  summary: 定子电流对饱和的影响 0.05（默认）| 非负标量
  group: 饱和
- name: Initialization option
  summary: 用于指定仿真开始时值的选项 Set real power, reactive power, terminal voltage, and terminal phase（默认）| Set targets for rotor angle
    and Park's transform variables | Set targets for load flow variables
  group: 初始条件
- name: Source type
  summary: 电压源模型 Swing bus（默认）| PV bus | PQ bus
  group: 初始条件
- name: Terminal voltage magnitude
  summary: 端电压幅值 24e3 V（默认）| 正标量
  group: 初始条件
- name: Terminal voltage angle
  summary: 端电压角度 0 deg（默认）| 标量
  group: 初始条件
- name: Active power generated
  summary: 发出的有功功率 500e6 V*A（默认）| 标量
  group: 初始条件
- name: Reactive power generated
  summary: 发出的无功功率 0 V*A（默认）| 标量
  group: 初始条件
- name: Minimum terminal voltage magnitude (pu)
  summary: 最小端电压幅值 0.95（默认）| 正标量
  group: 初始条件
- name: Phase search range at terminals
  summary: 端子处的相位搜索范围 [-inf, inf] deg（默认）| 两个元素的矢量
  group: 初始条件
- name: Parasitic conductance to electrical reference
  summary: 到电气参考的寄生电导 1e-6 S（默认）| 正标量
  group: 初始条件
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Rated apparent power** — 额定视在功率 `555e6` `A*V`（默认）

额定视在功率。

### **Rated voltage** — 额定线电压均方根值 `24e3` `V`（默认）

额定线电压的均方根（RMS）值。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）

模块据此引用额定视在功率的额定电气频率。

### **Number of pole pairs** — 电机极对数 `1`（默认）

电机的极对数。

### **Rotor angle definition** — 转子角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。

当您选择默认值时，转子 *d* 轴与定子 *a* 相磁轴在转子角度为零时对齐。

此参数可选的另一个值为 `Angle between the a-phase magnetic axis and the q-axis`。当您选择此值时，转子 *q* 轴与定子 *a* 相磁轴在转子角度为零时对齐。

### 阻抗

### **Stator resistance, Ra** — 定子电阻 `0.003`（默认）| 正标量

定子的电阻。

### **Stator leakage reactance, Xl** — 定子漏电抗 `0.15`（默认）| 正标量

定子的漏电抗。

### **d-axis synchronous reactance, Xd** — *d* 轴同步电抗 `1.81`（默认）| 正标量

*d* 轴同步电抗。

### **q-axis synchronous reactance, Xq** — *q* 轴同步电抗 `1.76`（默认）| 正标量

*q* 轴同步电抗。

### **d-axis transient reactance, Xd'** — *d* 轴瞬态电抗 `0.3`（默认）| 正标量

*d* 轴瞬态电抗。

### **q-axis transient reactance, Xq'** — *q* 轴瞬态电抗 `0.65`（默认）| 正标量

*q* 轴瞬态电抗。

### **d-axis subtransient reactance, Xd''** — *d* 轴次瞬态电抗 `0.23`（默认）| 正标量

*d* 轴次瞬态电抗。

### **q-axis subtransient reactance, Xq''** — *q* 轴次瞬态电抗 `0.25`（默认）| 正标量

*q* 轴次瞬态电抗。

### 时间常数

### **d-axis transient open-circuit, Td0'** — *d* 轴瞬态开路 `8` `s`（默认）| 正标量

*d* 轴瞬态开路时间常数。此参数值必须：

- 大于 0
- 大于 **d-axis subtransient open-circuit, Td0''**

### **d-axis subtransient open-circuit, Td0''** — *d* 轴次瞬态开路 `0.03` `s`（默认）| 正标量

*d* 轴次瞬态开路时间常数。

### **q-axis transient open-circuit, Tq0'** — *q* 轴瞬态开路 `1` `s`（默认）| 正标量

*q* 轴瞬态开路时间常数。此参数值必须：

- 大于 0
- 大于 **q-axis subtransient open-circuit, Tq0''**

### **q-axis subtransient open-circuit, Tq0''** — *q* 轴次瞬态开路 `0.07` `s`（默认）| 正标量

*q* 轴次瞬态开路时间常数。

### 饱和

### **Magnetic saturation representation** — 磁饱和表示 `None`（默认）| `Quadratic` | `Scaled quadratic` | `Exponential` | `Open-circuit lookup table`

用于表示模块磁饱和的选项：

- `None` — 模块不对磁饱和进行建模。
- `Quadratic` — 模块使用二次函数对磁饱和进行建模。
- `Scaled quadratic` — 模块使用缩放函数对磁饱和进行建模。
- `Exponential` — 模块使用指数函数对磁饱和进行建模。
- `Open-circuit lookup table` — 模块使用标幺非互易励磁电流和标幺气隙电压饱和数据对磁饱和进行建模。

### **Saturation factor, S10** — 饱和系数，S10 `0.005`（默认）| 正标量

对应于 1.0 标幺端电压的饱和系数。

#### 依赖关系

要启用此参数，请将 **Magnetic saturation representation** 设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`。

### **Saturation factor, S12** — 饱和系数，S12 `0.08`（默认）| 正标量

对应于 1.2 标幺端电压的饱和系数。此参数的值必须大于 **Saturation factor, S10** 参数的值。

#### 依赖关系

要启用此参数，请将 **Magnetic saturation representation** 设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`。

### **Non-reciprocal per-unit field current saturation data, ifd** — 标幺励磁电流饱和数据 `[0, .8, 1.26, 2.29, 2.97]`（默认）| 非负值矢量

非互易励磁电流 *ifd* 数据，用于填充气隙电压 *Vag* 对励磁电流 *ifd* 的查找表。此参数值必须包含至少五个元素的矢量。

#### 依赖关系

要启用此参数，请将 **Magnetic saturation representation** 设置为 `Open-circuit lookup table`。

### **Per-unit air-gap voltage saturation data, Vag** — 标幺气隙电压饱和数据 `[0, .8, 1.08, 1.31, 1.4]`（默认）| 非负值矢量

气隙电压 *Vag* 数据，用于填充气隙电压 *Vag* 对励磁电流 *ifd* 的查找表。此参数值必须包含至少五个元素的矢量。

#### 依赖关系

要启用此参数，请将 **Magnetic saturation representation** 设置为 `Open-circuit lookup table`。

### **Kis** — 定子电流对饱和的影响 `0.05`（默认）| 非负标量

定子电流对饱和的影响。模块使用此参数的值来计算 *d* 轴和 *q* 轴饱和系数。

### 初始条件

### **Initialization option** — 用于指定仿真开始时值的选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于指定仿真开始时某些参数和变量值的选项：

- `Set real power, reactive power, terminal voltage, and terminal phase` — 无论所连接网络如何，均设置运行点。
- `Set targets for rotor angle and Park's transform variables` — 在仿真前使用 **Variables** 设置指定模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
- `Set targets for load flow variables` — 在 **Initial Conditions** 设置中选择母线类型并指定潮流分析的相关参数。

### **Source type** — 电压源模型 `Swing bus`（默认）| `PV bus` | `PQ bus`

模块所建模的电压源类型。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`。

### **Terminal voltage magnitude** — 端电压幅值 `24e3` `V`（默认）| 正标量

端电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `Swing bus` 或 `PV bus`。

### **Terminal voltage angle** — 端电压角度 `0` `deg`（默认）| 标量

端电压角度。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `Swing bus`。

### **Active power generated** — 发出的有功功率 `500e6` `V*A`（默认）| 标量

电机发出的有功功率。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Reactive power generated** — 发出的无功功率 `0` `V*A`（默认）| 标量

电机发出的无功功率。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`。或者，将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PQ bus`。

### **Minimum terminal voltage magnitude (pu)** — 最小端电压幅值 `0.95`（默认）| 正标量

标幺最小稳态电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PQ bus`。

### **Phase search range at terminals** — 端子处的相位搜索范围 `[-inf, inf]` `deg`（默认）| 两个元素的矢量

定义端子处相位角搜索范围的矢量。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）| 正标量

到电气参考的寄生电导。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`。
## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

GENTPJ 同步电机

Synchronous Machine GENTPJ 模块对 GENTPJ 同步发电机模型进行建模。GENTPJ 同步发电机模型广泛用于发电厂模型验证和电力系统暂态稳定性研究。

### 使用潮流目标值进行同步电机初始化

如果模块所在的网络与频率-时间仿真模式兼容，您可以对网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。有关展示如何使用潮流分析数据初始化同步电机的示例，请参阅 Synchronous Machine Initialization with Loadflow。

### 方程

同步电机方程基于旋转参考坐标系表示，

θe(t)=Nθr(t)，

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。此方程定义了 Park 变换：

Ps=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212]。

该模块使用 Park 变换来定义标幺值同步电机方程。这些方程定义了 *d* 轴和 *q* 轴定子电压：

vd=ed''ωr−Raid+(Xq''−Xl1+Sq+Xl)iqvq=eq''ωr−Raiq−(Xd''−Xl1+Sd+Xl)id

在这些方程中：

- *e''d* 是次暂态电抗后的 *d* 轴电压。
- *Ra* 是定子电阻。
- *id* 是 *d* 轴定子电流。
- *X''q* 是 *q* 轴次暂态电抗。
- *Xl* 是定子漏电抗。
- *Sq* 是 *q* 轴饱和系数。
- *iq* 是 *q* 轴定子电流。
- *e''q* 是次暂态电抗后的 *q* 轴电压。
- *X''d* 是 *d* 轴次暂态电抗。
- *Sd* 是 *d* 轴饱和系数。

这些方程定义了暂态电抗后的电压：

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
- *Efd* 是标幺值励磁电压。

这些方程定义了电机饱和，

ψad=vq+Raiq+Xlidψaq=vd+Raid−Xliqψat=ψad2+ψaq2Sd=f(ψat+Kisid2+iq2)Sq=XqXdf(ψat+Kisid2+iq2)

其中：

- *ψad* 是 *d* 轴气隙磁链。
- *ψaq* 是 *q* 轴气隙磁链。
- *ψat* 是气隙磁链。
- *Kis* 表示定子电流对饱和的影响。
- *Sd* 和 *Sq* 分别是 *d* 轴和 *q* 轴饱和系数。如果将 **Magnetic saturation representation** 参数设置为 `None`，则 *Sd* 和 *Sq* 等于零。如果将 **Magnetic saturation representation** 参数设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`，则该模块根据 **Saturation factor, S10** 和 **Saturation factor, S12** 参数的值计算饱和系数函数 *f*。如果将 **Magnetic saturation representation** 参数设置为 `Open-circuit lookup table`，则该模块根据标幺值励磁电流和气隙电压饱和数据计算饱和系数函数 *f*。

此方程定义了非互易标幺值系统中的标幺值励磁电流：

Ifd=(1+Sd)(e′qXd−X″dX′d−X″d−e″qXd−X′dX′d−X″d)。

此方程定义了转子转矩：

Te=e″did+e″qiq−(X″d−Xl1+Sd−X″q−Xl1+Sq)idiq。

### 绘图和显示选项

您可以使用模块上下文菜单上的 **Electrical** 菜单执行绘图和显示操作。

右键单击该模块。从 **Electrical** 菜单中，选择一个选项：

- **Display Base Values** — 在 MATLAB® 命令窗口中显示电机标幺值基准值。
- **Display Associated Initial Conditions** — 在 MATLAB 命令窗口中显示关联的初始条件。
- **Plot Open-Circuit Saturation (pu)** — 在 MATLAB 图窗中绘制气隙电压 *Vag* 与励磁电流 *ifd* 的关系，两者均以标幺值测量。该图包含两条迹线：

  - Unsaturated — 您指定的 **Stator d-axis mutual inductance (unsaturated), Ladu**
  - Saturated — 您指定的 **Per-unit open-circuit lookup table (Vag versus ifd)**
- **Plot Saturation Factor (pu)** — 使用电机参数在 MATLAB 图窗中绘制饱和系数 *f* 与磁链 *ψat* 的关系，两者均以标幺值测量。如果将 **Magnetic saturation representation** 参数设置为 `Quadratic`、`Scaled quadratic` 或 `Exponential`，则该模块根据 **Saturation factor, S10** 和 **Saturation factor, S12** 参数的值推导饱和系数函数。

  如果将 **Magnetic saturation representation** 设置为 `Open-circuit lookup table`，则该模块根据 **Non-reciprocal per-unit field current saturation data, ifd** 和 **Per-unit air-gap voltage saturation data, Vag** 参数的值推导饱和系数函数。
- **Plot Power Capability Curves** — 在 MATLAB 图窗中绘制有功功率 P 与无功功率 Q 的关系，两者均以标幺值测量。该图可以包含多条迹线。每条迹线对应于以标幺值（非互易标幺值系统）测量的最大励磁电路电压。该图显示了发电机在滞后功率因数下运行时所发出的最大无功功率，以及发电机在超前功率因数下运行时所吸收的最小无功功率。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当在 **Initial Conditions** 部分中将 **Initialization option** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
