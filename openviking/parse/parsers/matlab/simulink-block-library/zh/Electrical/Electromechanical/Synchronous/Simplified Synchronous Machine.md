---
type: simulink-block
title: 'Simplified Synchronous Machine'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'simplifiedsynchronousmachine'
documentation_source_path: 'ref/simplifiedsynchronousmachine.html'
language: zh-CN
chinese_source: worker-translation
---

# Simplified Synchronous Machine

## 端口
```yaml
ports:
- name: E_si
  summary: 内部生成电压（相电压）幅值，物理信号向量
  direction: input
- name: E_pu
  summary: 内部生成电压幅值，标幺值，物理信号向量
  direction: input
- name: o
  summary: 电机标幺值测量值，物理信号向量
  direction: output
- name: R
  summary: 电机转子机械旋转
  direction: output
- name: C
  summary: 电机机壳机械旋转
  direction: output
- name: '~'
  summary: 定子绕组电气
  direction: output
- name: n
  summary: 中性相电气
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
- name: HA
  summary: '*a* 相端子热端口，热'
  direction: output
- name: HB
  summary: '*b* 相端子热端口，热'
  direction: output
- name: HC
  summary: '*c* 相端子热端口，热'
  direction: output
- name: HR
  summary: 转子热端口，热
  direction: output
```

### 输入

### **E\_si** — 内部生成电压（相电压）幅值，物理信号向量

与内部生成电压（相电压）幅值关联的物理信号端口，指定为物理信号向量。

#### 依赖关系

要启用此端口，请将 **Parameterization unit** 设置为 `SI`。

### **E\_pu** — 内部生成电压幅值，标幺值，物理信号向量

与内部生成电压的标幺值幅值关联的物理信号端口，指定为物理信号向量。

#### 依赖关系

要启用此端口，请将 **Parameterization unit** 设置为 `Per unit`。
### 输出

### **o** — 电机标幺值测量值，物理信号向量

与电机标幺值测量值关联的物理信号端口，以物理信号向量形式返回。向量元素为：

- 与 a 相相关的电动势，*pu\_EMF(1)*
- 与 b 相相关的电动势，*pu\_EMF(2)*
- 与 c 相相关的电动势，*pu\_EMF(3)*
- 电磁转矩，*pu\_torque*
- 转子速度，*pu\_velocity*
- 定子 `d` 轴电压，*pu\_vd*
- 定子 `q` 轴电压，*pu\_vq*
- 定子零序电压，*pu\_e0*
- 定子 `d` 轴电流，*pu\_id*
- 定子 `q` 轴电流，*pu\_iq*
- 定子零序电流，*pu\_i0*
- 转子电角度，*electrical\_angle\_out*

要连接到此端口，请使用 Synchronous Machine Measurement 模块。
### 守恒

### **R** — 电机转子机械旋转

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳机械旋转

与电机机壳关联的机械旋转守恒端口。

### **~** — 定子绕组电气

与定子绕组关联的可扩展三相电气端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **n** — 中性相电气

与星形绕组配置的中性点关联的电气守恒端口。

### **a** — *a* 相电气

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **HA** — *a* 相端子热端口，热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — *b* 相端子热端口，热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — *c* 相端子热端口，热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口，热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 启用热端口的选项 No thermal port（默认）| Show thermal port
  group: ''
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主要
- name: Rated apparent power
  summary: 额定视在功率 555e6 V*A（默认）| 标量
  group: 主要
- name: Rated voltage
  summary: 额定线电压均方根值 24e3 V（默认）| 标量
  group: 主要
- name: Rated electrical frequency
  summary: 标称电气频率 60 Hz（默认）| 标量
  group: 主要
- name: Number of pole pairs
  summary: 极对数 2（默认）| 标量
  group: 主要
- name: Parameterization unit
  summary: 模块参数化 SI（默认）| Per unit
  group: 主要
- name: Internal resistance (pu)
  summary: 内部标幺值电阻 0.05（默认）| 标量
  group: 主要
- name: Internal inductance (pu)
  summary: 内部标幺值电感 0.3（默认）| 标量
  group: 主要
- name: Internal resistance
  summary: 内部电阻 0.0519 Ohm（默认）| 标量
  group: 主要
- name: Internal inductance
  summary: 内部电感 8.2589e-04 H（默认）| 标量
  group: 主要
- name: Initialization option
  summary: 初始化选项 Set real power, reactive power, terminal voltage, and terminal phase（默认）| Set targets for rotor angle and
    Park's transform variables | Set targets for load flow variables
  group: 初始条件
- name: Source type
  summary: 电压源模型 Swing bus（默认）| PV bus | PQ bus
  group: 初始条件
- name: Terminal voltage magnitude
  summary: 端子电压幅值 24e3 V（默认）
  group: 初始条件
- name: Terminal voltage angle
  summary: 端子电压角度 0 deg（默认）
  group: 初始条件
- name: Active power generated
  summary: 生成的有功功率 500e6 V*A（默认）
  group: 初始条件
- name: Reactive power generated
  summary: 生成的无功功率 0 V*A（默认）
  group: 初始条件
- name: Minimum terminal voltage magnitude (pu)
  summary: 最小端子电压幅值 0.95（默认）
  group: 初始条件
- name: Phase search range at terminals
  summary: 端子处的相位搜索范围 [-inf, inf] deg（默认）
  group: 初始条件
- name: Parasitic conductance to electrical reference
  summary: 到电气参考的寄生电导 1e-6 S（默认）
  group: 初始条件
- name: Measurement temperature
  summary: 额定温度 298.15 k（默认）| 实数标量
  group: 热
- name: Resistance temperature coefficient
  summary: 温度系数 3.93e-3 1/K（默认）| 正标量
  group: 热
- name: Thermal mass for each stator winding
  summary: 绕组热质量 100 J/K（默认）| 正标量
  group: 热
- name: Rotor thermal mass
  summary: 转子热质量 200 J/K（默认）| 正标量
  group: 热
```

### **Modeling option** — 启用热端口的选项 `No thermal port`（默认）| `Show thermal port`

启用模块热端口并对生成热量和电机温度效应进行建模的选项。

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Rated apparent power** — 额定视在功率 `555e6` `V*A`（默认）| 标量

额定视在功率。

### **Rated voltage** — 额定线电压均方根值 `24e3` `V`（默认）| 标量

额定线电压均方根值。

### **Rated electrical frequency** — 标称电气频率 `60` `Hz`（默认）| 标量

额定视在功率对应的标称电气频率。

### **Number of pole pairs** — 极对数 `2`（默认）| 标量

电机极对数。

### **Parameterization unit** — 模块参数化 `SI`（默认）| `Per unit`

模块参数化方法。选项为：

- `SI`
- `Per unit`

### **Internal resistance (pu)** — 内部标幺值电阻 `0.05`（默认）| 标量

内部标幺值电阻。

#### 依赖关系

要启用此参数，请将 **Parameterization unit** 设置为 `Per unit`。

### **Internal inductance (pu)** — 内部标幺值电感 `0.3`（默认）| 标量

内部标幺值电感。

#### 依赖关系

要启用此参数，请将 **Parameterization unit** 设置为 `Per unit`。

### **Internal resistance** — 内部电阻 `0.0519` `Ohm`（默认）| 标量

内部电阻。

#### 依赖关系

要启用此参数，请将 **Parameterization unit** 设置为 `SI`。

### **Internal inductance** — 内部电感 `8.2589e-04` `H`（默认）| 标量

内部电感。

#### 依赖关系

要启用此参数，请将 **Parameterization unit** 设置为 `SI`。

### 初始条件

### **Initialization option** — 初始化选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认）| `Set targets for rotor angle and Park's transform variables` | `Set targets for load flow variables`

用于指定仿真开始时某些参数和变量值的模型。要：

- 无论连接的网络如何都设置工作点，请选择 `Set real power, reactive power, terminal voltage and terminal phase`。
- 在仿真前使用 **Variables** 设置指定模块变量的优先级和初始目标值，请选择 `Set targets for rotor angle and Park's transform variables`。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
- 选择母线类型并在 **Initial Conditions** 设置中指定潮流分析的相关参数，请选择 `Set targets for load flow variables`。

#### 依赖关系

如果将此参数设置为：

- `Set targets for rotor angle and Park's transform variables` — **Variables** 设置将变为可见。
- `Set real power, reactive power, terminal voltage, and terminal phase` — 相关参数将变为可见。
- `Set targets for load flow variables` — 相关参数将变为可见。

### **Source type** — 电压源模型 `Swing bus`（默认）| `PV bus` | `PQ bus`

模块建模的电压源类型。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `Swing bus` 或 `PV bus`。

### **Terminal voltage magnitude** — 端子电压幅值 `24e3` `V`（默认）

端子电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或将 **Initialization option** 设置为 `Set targets for load flow variables` 并将 **Source type** 设置为 `Swing bus` 或 `PV bus`。

### **Terminal voltage angle** — 端子电压角度 `0` `deg`（默认）

端子电压角度。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或将 **Initialization option** 设置为 `Set targets for load flow variables` 并将 **Source type** 设置为 `Swing bus`。

### **Active power generated** — 生成的有功功率 `500e6` `V*A`（默认）

生成的有功功率。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或将 **Initialization option** 设置为 `Set targets for load flow variables` 并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Reactive power generated** — 生成的无功功率 `0` `V*A`（默认）

生成的无功功率。

#### 依赖关系

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set real power, reactive power, terminal voltage, and terminal phase`，或将 **Initialization option** 设置为 `Set targets for load flow variables` 并将 **Source type** 设置为 `PQ bus`。

### **Minimum terminal voltage magnitude (pu)** — 最小端子电压幅值 `0.95`（默认）

标幺值最小稳态电压幅值。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PQ bus`。

### **Phase search range at terminals** — 端子处的相位搜索范围 `[-inf, inf]` `deg`（默认）

定义相位角搜索范围的向量。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`，并将 **Source type** 设置为 `PV bus` 或 `PQ bus`。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）

到电气参考的寄生电导。

#### 依赖关系

要启用此参数，请将 **Initialization option** 设置为 `Set targets for load flow variables`。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认）| 实数标量

电机参数的标称温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。
## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。此外，`Composite three-phase ports` 和 `Expanded three-phase ports` 的 simlog 格式相同。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

## 描述

带电动势的简化同步电机

Simplified Synchronous Machine 模块对带有表示电动势 (EMF) 的电压源的简化同步电机进行建模。您可以使用标幺值或 SI 参数指定内部电阻和电感。

简化同步电机在直轴、交轴和零序下的等效电路为：

### 方程

简化同步电机方程是相对于旋转参考坐标系表示的，该坐标系定义为：

θe(t)=Nθr(t)，

其中：

- *θe* 是电角度。
- *N* 是极对数。
- *θr* 是转子角度。

Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。Park 变换定义为：

Ps=23[−cosθe−cos(θe−2π3)−cos(θe+2π3)sinθesin(θe−2π3)sin(θe+2π3)121212]。

Park 变换用于定义标幺值简化同步电机方程。电压方程定义为：

ed=1ωbasedψddt−Ψqωr+Rid+vd

eq=1ωbasedψqdt+Ψdωr+Riq+vq

e0=1ωbasedΨ0dt+Ri0+v0

其中：

- *ed*、*eq* 和 *e0* 是 *d* 轴、*q* 轴和零序电压，定义为：

  [edeqe0]=Ps[eaebec]。

  *ea*、*eb* 和 *ec* 是标幺值内部电压源，定义为：

  ea=Epusinθeeb=Epusin(θe−120°)ec=Epusin(θe+120°)

  *epu* 是内部生成电压的标幺值幅值。
- *vd*、*vq* 和 *v0* 定义为：

  [vdvqv0]=Ps[vavbvc]。

  *va*、*vb* 和 *vc* 是从端口 **~** 到中性端口 **n** 测量的定子电压。
- *ωbase* 是标幺值基准电气速度。
- *ψd*、*ψq* 和 *ψ0* 是 *d* 轴、*q* 轴和零序磁链。
- *ωr* 是标幺值转子旋转速度。
- *R* 是定子电阻。
- *id*、*iq* 和 *i0* 是 *d* 轴、*q* 轴和零序定子电流，定义为：

  [idiqi0]=Ps[iaibic]。

  *ia*、*ib* 和 *ic* 是从端口 **~** 流出的定子电流。

定子磁链方程定义为

ψd=L⋅idψq=L⋅iqψ0=L⋅i0

其中 *L* 是定子漏电感。

简化同步电机的标幺值功率方程定义为：

P=edid+eqiq。

### 绘图和显示选项

您可以使用模块上下文菜单上的 **Electrical** 菜单执行绘图和显示操作。

右键单击模块，然后从 **Electrical** 菜单中选择以下选项之一：

- **Display Base Values** — 在 MATLAB® 命令窗口中显示电机标幺值基准值。
- **Display Associated Initial Conditions** — 在 MATLAB 命令窗口中显示关联的初始条件。

### 热效应建模

您可以暴露热端口，以对生成热量和电机温度的效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

对于此模块，仅当在 **Initial Conditions** 部分中将 **Initialization option** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**Initial Targets** 设置才可见。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
