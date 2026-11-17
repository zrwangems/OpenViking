---
type: simulink-block
title: 'Variable-Displacement Motor (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pumps & Motors'
documentation_page: 'variabledisplacementmotortl'
documentation_source_path: 'ref/variabledisplacementmotortl.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Motor (TL)

## 端口
```yaml
ports:
- name: D
  summary: 排量，cm^3/rev 物理信号
  direction: input
- name: EV
  summary: 容积效率，无量纲 物理信号
  direction: input
- name: EM
  summary: 机械效率，无量纲 物理信号
  direction: input
- name: LV
  summary: 容积损失，m^3/s 物理信号
  direction: input
- name: LM
  summary: 机械损失，N*m 物理信号
  direction: input
- name: A
  summary: 马达入口热液体
  direction: input
- name: B
  summary: 马达出口热液体
  direction: input
- name: C
  summary: 马达壳体机械旋转
  direction: input
- name: R
  summary: 马达轴机械旋转
  direction: input
```

### 输入

### **D** — 排量，cm^3/rev 物理信号

每转排出的流体体积的物理信号输入端口。平滑函数可缓和正负输入值之间的过渡。

### **EV** — 容积效率，无量纲 物理信号

容积效率系数的物理信号输入端口。输入信号的上限为 **Maximum volumetric efficiency** 参数值，下限为 **Minimum volumetric efficiency** 参数值。

#### 依赖关系

仅当模块变体设置为 `Input efficiencies` 时，此端口才会显示。

### **EM** — 机械效率，无量纲 物理信号

机械效率系数的物理信号输入端口。输入信号的上限为 **Maximum mechanical efficiency** 参数值，下限为 **Minimum mechanical efficiency** 参数值。

#### 依赖关系

仅当模块变体设置为 `Input efficiencies` 时，此端口才会显示。

### **LV** — 容积损失，`m^3/s` 物理信号

容积损失的物理信号输入端口，定义为马达入口之间的内部泄漏流量。

#### 依赖关系

仅当模块变体设置为 `Input losses` 时，此端口才会显示。

### **LM** — 机械损失，`N*m` 物理信号

机械损失的物理信号输入端口，定义为旋转马达轴上的摩擦扭矩。

#### 依赖关系

仅当模块变体设置为 `Input losses` 时，此端口才会显示。
### 守恒

### **A** — 马达入口热液体

表示马达入口的热液体守恒端口。

### **B** — 马达出口热液体

表示马达出口的热液体守恒端口。

### **C** — 马达壳体机械旋转

表示马达壳体的机械旋转守恒端口。

### **R** — 马达轴机械旋转

表示旋转马达轴的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Leakage and friction parameterization
  summary: 泄漏流量和摩擦扭矩的参数化 Analytical（默认）| Tabulated data - volumetric and mechanical efficiencies | Tabulated data - volumetric
    and mechanical losses | Input signal - volumetric and mechanical efficiencies | Input signal - volumetric and mechanical
    losses
  group: ''
- name: Nominal displacement
  summary: 指定容积效率时的排量 30 cm^3/rev（默认）| 正标量
  group: ''
- name: Nominal shaft angular velocity
  summary: 给定容积效率下的轴角速度 1800 rpm（默认）| 标量
  group: ''
- name: Nominal pressure drop
  summary: 对应容积效率的压降 10 MPa（默认）| 标量
  group: ''
- name: Nominal dynamic viscosity
  summary: 指定容积效率时的动力粘度 0.9 cP（默认）| 标量
  group: ''
- name: Volumetric efficiency at nominal conditions
  summary: 指定标称条件下的容积效率 0.92（默认）| 范围 (0,1) 内的标量
  group: ''
- name: Mechanical efficiency at nominal conditions
  summary: 实际机械功率与理想机械功率之比 0.88（默认）| 正标量
  group: ''
- name: No-load torque
  summary: 引起轴旋转所需的最小扭矩 0 N*m（默认）| 标量
  group: ''
- name: Pressure drop vector, dp
  summary: 给定容积效率和机械效率下的压降 [.1, 1, 2] MPa（默认）| 向量
  group: ''
- name: Shaft angular velocity vector, w
  summary: 指定容积效率和机械效率时的角速度 [250, 500, 1000, 2000, 3000, 4000] rpm | 向量
  group: ''
- name: Displacement vector, D
  summary: 用于指定容积效率和机械效率的排量 [-30, -19, 19, 30] cm^3/rev（默认值）
  group: ''
- name: Volumetric efficiency table, e_v(dp,w,D)
  summary: 给定压降、角速度和排量下的容积效率 repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78,
    .892, .893, .91], 1, 1, 4) | 矩阵
  group: ''
- name: Mechanical efficiency table, e_m(dp,w,D)
  summary: 给定压降、角速度和排量下的机械效率 repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982,
    .982, .983, .984], 1, 1, 4) | 矩阵
  group: ''
- name: Pressure drop vector, dp
  summary: 对应损失下的压降 [.1, 1, 2] MPa（默认值）
  group: ''
- name: Displacement vector, D
  summary: 用于指定容积损失和机械损失的排量 [-30, -19, 19, 30] cm^3/rev（默认值）
  group: ''
- name: Volumetric loss table, q_loss(dp,w,D)
  summary: 对应压降、角速度和排量下的内部泄漏流量 repmat([.0282, .0253, .0241, .0235, .0291, .0325; .2596, .1271, .1017, .0917, .1216, .1142;
    .7874, .1901, .141, .1211, .1797, .1978] * 1e-3, 1, 1, 4) m^3/s
  group: ''
- name: Mechanical loss table, torque_loss(dp,w,D)
  summary: 对应压降、角速度和排量下的摩擦力矩 repmat([.002, .002, .002, .002, .002, .002; .06, .055, .055, .055, .055, .05; .19, .19, .18,
    .18, .17, .16], 1, 1, 4) N*m
  group: ''
- name: Minimum volumetric efficiency
  summary: 容积效率输入信号的下饱和边界 1e-3（默认值）| 范围 (0,1) 内的标量
  group: ''
- name: Maximum volumetric efficiency
  summary: 容积效率输入信号的上饱和边界 1（默认值）| 范围 (0,1) 内的标量
  group: ''
- name: Minimum mechanical efficiency
  summary: 容积效率输入信号的下饱和边界 1e-3（默认值）| 范围 (0,1) 内的标量
  group: ''
- name: Maximum mechanical efficiency
  summary: 容积效率输入信号 1（默认值）| (0,1) 范围内的标量 的上饱和边界
  group: ''
- name: Pressure drop threshold for motor-pump transition
  summary: 启动马达与泵模式之间平滑过渡时的压降 1e-3 MPa（默认值）| 标量
  group: ''
- name: Angular velocity threshold for motor-pump transition
  summary: 启动泵与马达模式之间平滑过渡时的角速度 100 rpm（默认值）| 标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 组件入口和出口处的流通面积 0.01 m^2（默认值）| 正标量
  group: ''
- name: Check if operating beyond the range of supplied tabulated data
  summary: 工作条件超出表格数据范围时的仿真警告模式 None（默认值）| Warning
  group: ''
- name: Check if operating outside of motor mode
  summary: 工作条件超出马达模式时的仿真警告模式 None（默认值）| Warning
  group: ''
```

### **Leakage and friction parameterization** — 泄漏流量和摩擦扭矩的参数化 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

计算由内部泄漏和摩擦引起的流量和扭矩损失的方法。当您选择 `Analytical` 时，模块参数通常可从组件数据表中获得。当您选择 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 时，模块使用查找表将压降、角速度和排量映射到组件效率或损失。

当您选择 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses` 时，模块分别执行与 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses` 设置相同的泄漏流量和摩擦扭矩计算。当您选择 `Input signal - volumetric and mechanical efficiencies` 时，模块启用物理信号端口 **EV** 和 **EM**。您可以使用这些端口指定容积效率和机械效率。当您选择 `Input signal - volumetric and mechanical losses` 时，模块启用物理信号端口 **LV** 和 **LM**。您可以使用这些端口指定容积损失和机械损失。

### **Nominal displacement** — 指定容积效率时的排量 `30` `cm^3/rev`（默认）| 正标量

给定容积效率下的流体排量。这些值通常可在制造商数据表的标准操作条件下获得。模块使用此参数计算泄漏流量和摩擦扭矩。

### **Nominal shaft angular velocity** — 给定容积效率下的轴角速度 `1800` `rpm`（默认）| 标量

与给定容积效率对应的旋转轴角速度。这些值通常可在制造商数据表的标准操作条件下获得。模块使用此参数计算泄漏流量和摩擦扭矩。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 对应容积效率的压降 `10` `MPa`（默认）| 标量

与给定容积效率对应的压降。这些值通常可在制造商数据表的标准操作条件下获得。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal dynamic viscosity** — 指定容积效率时的动力粘度 `0.9` `cP`（默认）| 标量

给定容积效率下液压流体的动力粘度。这些值通常可在制造商数据表的标准操作条件下获得。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 指定标称条件下的容积效率 `0.92`（默认）| 范围 (0,1) 内的标量

给定条件下的容积效率。模块将容积效率定义为实际体积流量与理想体积流量之比。这些值通常可在制造商数据表的标准操作条件下获得。模块使用此参数计算内部泄漏流量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际机械功率与理想机械功率之比 `0.88`（默认）| 正标量

标称条件下实际机械功率与理想机械功率之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 引起轴旋转所需的最小扭矩 `0` `N*m`（默认）| 标量

克服密封摩擦并引起机械轴旋转所需的扭矩。此扭矩是总摩擦扭矩中与负载无关的分量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 给定容积效率和机械效率下的压降 `[.1, 1, 2]` `MPa`（默认）| 向量

对应表格效率数据的压降。该向量必须至少包含两个严格递增顺序的元素。

您可以指定单个八分圆 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分圆对应的操作模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Shaft angular velocity vector, w** — 指定容积效率和机械效率时的角速度 `[250, 500, 1000, 2000, 3000, 4000]` `rpm` | 向量

对应表格效率数据的轴角速度。该向量必须至少包含两个严格递增顺序的元素。

您可以指定单个八分圆 (*ɷ*, *Δp*,*D*) 的数据。有关各种八分圆对应的操作模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 或 `Tabulated data - volumetric and mechanical losses`。

### **Displacement vector, D** — 用于指定容积效率和机械效率的排量 `[-30, -19, 19, 30]` `cm^3/rev`（默认值）

用于指定效率表格数据的排量。该向量必须至少包含两个元素，且按严格递增顺序排列。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric efficiency table, e\_v(dp,w,D)** — 给定压降、角速度和排量下的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)` | 矩阵

在指定的流体压降、轴角速度和排量下的容积效率。效率必须在 `0`–`1` 范围内。*M*、*N* 和 *L* 是指定的查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *L* 是 **Displacement vector, D** 参数中向量元素的数量。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w,D)** — 给定压降、角速度和排量下的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)` | 矩阵

对应于指定流体压降、轴角速度和排量的机械效率。效率必须在 `0`–`1` 范围内。*M*、*N* 和 *L* 是指定的查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *L* 是 **Displacement vector, D** 参数中向量元素的数量。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Pressure drop vector, dp** — 对应损失下的压降 `[.1, 1, 2]` `MPa`（默认值）

对应于表格损失数据的压降。该向量必须至少包含两个元素，且按严格递增顺序排列。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Displacement vector, D** — 用于指定容积损失和机械损失的排量 `[-30, -19, 19, 30]` `cm^3/rev`（默认值）

用于指定损失表格数据的排量。该向量必须至少包含两个元素，且按严格递增顺序排列。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Volumetric loss table, q\_loss(dp,w,D)** — 对应压降、角速度和排量下的内部泄漏流量 `repmat([.0282, .0253, .0241, .0235, .0291, .0325; .2596, .1271, .1017, .0917, .1216, .1142; .7874, .1901, .141, .1211, .1797, .1978] * 1e-3, 1, 1, 4)` `m^3/s`

在指定的流体压降、轴角速度和排量下的容积损失。该模块将容积损失定义为端口 **A** 和端口 **B** 之间的内部泄漏体积流量。*M* 和 *N* 是指定的查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *L* 是 **Displacement vector, D** 参数中向量元素的数量。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w,D)** — 对应压降、角速度和排量下的摩擦力矩 `repmat([.002, .002, .002, .002, .002, .002; .06, .055, .055, .055, .055, .05; .19, .19, .18, .18, .17, .16], 1, 1, 4)` `N*m`

在给定压降、轴角速度和排量下的机械损失。该模块将机械损失定义为由于密封件和内部组件引起的摩擦力矩。*M* 和 *N* 是指定的查找表向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *L* 是 **Displacement vector, D** 参数中向量元素的数量。

您可以指定单个八分仪 (*ɷ*, *Δp*, *D*) 的数据。有关各种八分仪对应的运行模式，请参阅模块描述。机械损失的表格数据必须遵循图中的约定，即在正角速度下为正值，在负角速度下为负值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Minimum volumetric efficiency** — 容积效率输入信号的下饱和边界 `1e-3`（默认值）| 范围 (0,1) 内的标量

容积效率允许的最小值。来自物理信号端口 **EV** 的输入会将低于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率输入信号的上饱和边界 `1`（默认值）| 范围 (0,1) 内的标量

容积效率允许的最大值。来自物理信号端口 **EV** 的输入会将高于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 容积效率输入信号的下饱和边界 `1e-3`（默认值）| 范围 (0,1) 内的标量

机械效率允许的最小值。来自物理信号端口 **EM** 的输入会将低于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 容积效率输入信号 `1`（默认值）| (0,1) 范围内的标量 的上饱和边界

机械效率的最大允许值。来自物理信号端口 **EM** 的输入会将高于此值的输入饱和。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure drop threshold for motor-pump transition** — 启动马达与泵模式之间平滑过渡时的压降 `1e-3` `MPa`（默认值）| 标量

从入口到出口的压降，低于该值时模块开始在马达和泵模式之间过渡。模块使用双曲正切函数来平滑泄漏流量和摩擦力矩。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **Angular velocity threshold for motor-pump transition** — 启动泵与马达模式之间平滑过渡时的角速度 `100` `rpm`（默认值）| 标量

轴角速度，低于该值时模块开始在泵和马达模式之间过渡。模块使用双曲正切函数来平滑泄漏流量和摩擦力矩。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical losses`。

### **Cross-sectional area at ports A and B** — 组件入口和出口处的流通面积 `0.01` `m^2`（默认值）| 正标量

组件入口和出口处的流通面积。假定这些面积相等。

### **Check if operating beyond the range of supplied tabulated data** — 工作条件超出表格数据范围时的仿真警告模式 `None`（默认值）| `Warning`

工作条件超出表格数据范围时的仿真警告模式。选择 `Warning` 可在流体压降、轴角速度或瞬时排量超出指定的表格数据时收到通知。该警告不会导致仿真停止。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Check if operating outside of motor mode** — 工作条件超出马达模式时的仿真警告模式 `None`（默认值）| `Warning`

工作条件超出马达模式时的仿真警告模式。如果马达过渡到泵模式，模块会生成警告。选择 `Warning` 可在发生此过渡时收到通知。该警告不会导致仿真停止。
## 所属库

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the octants of supplied tabulated data** 参数已重命名为 **Check if operating beyond the range of supplied tabulated data**。您可以启用 **Check if operating beyond the range of supplied tabulated data** 参数来检查模块是否在模块参数指定的数据范围之外运行，即模块已扩展数据的区域中运行。

## 描述

可变排量双向热液体马达

Variable-Displacement Motor 模块表示一种从热液体网络提取功率并将其传递给机械旋转网络的设备。马达排量在仿真期间根据端口 **D** 处指定的物理信号输入而变化。

端口 **A** 和 **B** 表示马达入口。端口 **R** 和 **C** 表示马达驱动轴和壳体。在正常运行期间，从端口 **A** 到端口 **B** 的压降会导致从端口 **A** 到端口 **B** 的正流量，以及马达轴相对于马达壳体的正旋转。此运行模式在此称为*正向马达*。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益，*Δp = p*A – *p*B；角速度，*ω = ω*R – *ω*C；以及端口 **D** 处的流体容积排量。上图将这些模式映射到 *Δp*-*ω*-*D* 图的八个卦限：

- 模式 1，*正向马达*：从端口 **A** 到端口 **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 2，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 到端口 **A** 的流动。
- 模式 3，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 4，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 到 **B** 的流动。
- 模式 5，*反向泵*：正轴角速度导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 到 **A** 的流动。
- 模式 6，*正向马达*：从端口 **A** 到端口 **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 7，*正向泵*：负轴角速度导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 到 **B** 的流动。
- 模式 8，*反向马达*：从 **B** 到 **A** 的流动导致从 **B** 到 **A** 的压力降低以及正轴角速度。

与系统响应时间相比，马达的响应时间被认为可以忽略不计。假定马达几乎瞬时达到稳态，并将其视为准稳态组件。

### 流量和驱动力矩

马达处生成的质量流量为

m˙=m˙Ideal+m˙Leak，

其中：

- m˙ 是实际质量流量。
- m˙Ideal 是理想质量流量。
- m˙Leak 是内部泄漏质量流量。

马达处生成的力矩为

τ=τIdeal−τFriction，

其中：

- *τ* 是实际力矩。
- *τ*Ideal 是理想力矩。
- *τ*Friction 是摩擦力矩。

**理想流量和理想力矩**

理想质量流量为

m˙Ideal=ρDω，

理想生成力矩为

τIdeal=DΔp，

其中：

- *ρ* 是热液体端口 **A** 和 **B** 处流体密度的平均值。
- *D* 是物理信号端口 **D** 处指定的排量。
- *ω* 是轴角速度。
- *Δp* 是从入口到出口的压降。

### 泄漏与摩擦参数化

您可以通过解析方式、使用表格化的效率或损失，或者通过输入效率或输入损失来参数化泄漏与摩擦。

**解析方式**

当您将 **Leakage and friction parameterization** 设置为 `Analytical` 时，泄漏流量为

m˙Leak=KHPρAvgΔpμAvg，

摩擦力矩为

τFriction=(τ0+KTP|Δp||D|DNomtanh4ω(5e−5)ωNom)，

其中：

- *K*HP 是层流管道流的 Hagen-Poiseuille 系数。该系数由指定的标称参数计算得出。
- *μ* 是热液体的动力粘度，此处取其热液体端口处值的平均值。
- *k* 是标称排量下的摩擦力矩与压力增益系数，由 **Mechanical efficiency at nominal conditions**、*ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 是标称条件下的摩擦力矩：

  τfr,nom=(1−ηm,nom)DnomΔpnom。
- *D*Nom 是 **Nominal Displacement** 模块参数的指定值。
- *τ*0 是 **No-load torque** 模块参数的指定值。
- *ω*Nom 是 **Nominal shaft angular velocity** 模块参数的指定值。
- *Δp*Nom 是 **Nominal pressure drop** 模块参数的指定值。这是指定标称容积效率时的压降。

Hagen-Poiseuille 系数由标称流体和组件参数通过以下方程确定

KHP=DNomωNomμNom(1ηv,Nom−1)ΔpNom，

其中：

- *ω*Nom 是 **Nominal shaft angular velocity** 参数的指定值。这是指定标称容积效率时的角速度。
- *μ*Nom 是 **Nominal Dynamic viscosity** 模块参数的指定值。这是指定标称容积效率时的动力粘度。
- *η*v,Nom 是 **Volumetric efficiency at nominal conditions** 模块参数的指定值。这是对应于指定标称条件的容积效率。

**表格化效率**

当您将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies` 时，泄漏流量为

m˙Leak=m˙Leak,Pump(1+α)2+m˙Leak,Motor(1−α)2，

摩擦力矩为

τFriction=τFriction,Pump1+α2+τFriction,Motor1−α2，

其中：

- *α* 是用于泵-马达过渡的数值平滑参数。
- m˙Leak,Motor 是马达模式下的泄漏流量。
- m˙Leak,Pump 是泵模式下的泄漏流量。
- *τ*Friction,Motor 是马达模式下的摩擦力矩。
- *τ*Friction,Pump 是泵模式下的摩擦力矩。

平滑参数 *α* 由双曲正切函数给出

α=tanh(4ΔpΔpThreshold)·tanh(4ωωThreshold)·tanh(4DDThreshold)，

其中：

- *Δp*Threshold 是 **Pressure gain threshold for pump-motor transition** 模块参数的指定值。
- *ω*Threshold 是 **Angular velocity threshold for pump-motor transition** 模块参数的指定值。
- *D*Threshold 是 **Angular velocity threshold for motor-pump transition** 模块参数的指定值。

泄漏流量由容积效率计算得出，该量通过 **Volumetric efficiency table** 模块参数以表格形式在 *Δp*–*ɷ*–*D* 域上指定。当在泵模式下运行（Operation Modes 图中所示 *Δp*–*ɷ*–*D* 图的八分圆 **1** 和 **3**）时，泄漏流量为：

m˙Leak,Pump=(1−ηv)m˙Ideal，

其中 *η*v 是容积效率，通过表格数据的插值或外推获得。类似地，当在马达模式下运行（*Δp*–*ɷ*–*D* 图的八分圆 **2** 和 **4**）时，泄漏流量为：

m˙Leak,Motor=−(1−ηv)m˙。

摩擦力矩类似地由机械效率计算得出，该量通过 **Mechanical efficiency table** 模块参数以表格形式在 *Δp*–*ɷ*–*D* 域上指定。当在泵模式下运行（*Δp*–*ɷ*–*D* 图的八分圆 **1** 和 **3**）时：

τFriction,Pump=(1−ηm)τ，

其中 *η*m 是机械效率，通过表格数据的插值或外推获得。类似地，当在马达模式下运行（*Δp*–*ɷ*–*D* 图的八分圆 **2** 和 **4**）时：

τFriction,Motor=−(1−ηm)τIdeal。

**表格化损失**

当您将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses` 时，泄漏（容积）流量直接以表格形式在 *Δp*–*ɷ*–*D* 域上指定：

qLeak=qLeak(Δp,ω,D)。

由泄漏引起的质量流量由容积流量计算得出：

m˙Leak=ρqLeak。

摩擦力矩类似地以表格形式指定：

τFriction=τFriction(Δp,ω,D)，

其中 *q*Leak(*Δp*,*ω*,*D*) 和 *τ*Friction(*Δp*,*ω*,*D*) 是通过 **Volumetric loss table** 和 **Mechanical loss table** 模块参数指定的表格数据的插值或外推获得的容积损失和机械损失。

**输入效率**

当您将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦力矩的计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。容积效率和机械效率查找表被替换为您通过端口 **EV** 和 **EM** 指定的物理信号输入。

效率是正值量，值介于 `0` 和 `1` 之间。超出这些范围的输入值被设置为最接近的边界值（对于小于 `0` 的输入为 `0`，对于大于 `1` 的输入为 `1`）。效率信号在 **Minimum volumetric efficiency** 或 **Minimum mechanical efficiency** 以及 **Maximum volumetric efficiency** 或 **Maximum mechanical efficiency** 处饱和。

**输入损失**

当您将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies` 时，泄漏流量和摩擦力矩的计算与 `Tabulated data - volumetric and mechanical efficiencies` 设置相同。容积损失和机械损失查找表被替换为您通过端口 **LV** 和 **LM** 指定的物理信号输入。

该模块期望输入为正值。它根据仿真期间建立的工作条件自动设置符号——更准确地说，根据组件恰好运行的 *Δp*–*ɷ* 象限来确定。

### 能量平衡

马达所做的机械功与能量交换相关。控制能量平衡方程为：

ϕA+ϕB−Phydro=0，

其中：

- *Φ*A 和 *Φ*B 分别是端口 **A** 和 **B** 处的能量流率。
- *P*hydro 是马达端口之间压力差的函数：Phydro=Δpm˙ρ。

马达机械功率由转矩 *τ* 和角速度 *ω* 产生：

Pmech=τω。

### 假设

- 流体可压缩性可忽略不计。
- 由于惯性、摩擦和弹簧力作用在马达轴上的载荷可忽略不计。
