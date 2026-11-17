---
type: simulink-block
title: 'PMLSM'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Permanent Magnet'
documentation_page: 'pmlsm'
documentation_source_path: 'ref/pmlsm.html'
language: zh-CN
chinese_source: worker-translation
---

# PMLSM

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口电气
  direction: conserving
- name: a
  summary: '*a* 相电气'
  direction: conserving
- name: b
  summary: '*b* 相电气'
  direction: conserving
- name: c
  summary: '*c* 相电气'
  direction: conserving
- name: ~1
  summary: 定子正端连接电气
  direction: conserving
- name: ~2
  summary: 定子负端连接电气
  direction: conserving
- name: a1
  summary: '*a* 正端连接电气'
  direction: conserving
- name: b1
  summary: '*b* 正端连接电气'
  direction: conserving
- name: c1
  summary: '*c* 正端连接电气'
  direction: conserving
- name: a2
  summary: '*a* 负端连接电气'
  direction: conserving
- name: b2
  summary: '*b* 负端连接电气'
  direction: conserving
- name: c2
  summary: '*c* 负端连接电气'
  direction: conserving
- name: n
  summary: 中性相电气
  direction: conserving
- name: R
  summary: 电机动子机械
  direction: conserving
- name: C
  summary: 电机外壳机械
  direction: conserving
- name: HA
  summary: 绕组 A 热端口热
  direction: conserving
- name: HB
  summary: 绕组 B 热端口热
  direction: conserving
- name: HC
  summary: 绕组 C 热端口热
  direction: conserving
- name: HR
  summary: 转子热端口热
  direction: conserving
```

### 守恒端口

### **~** — 三相端口电气

可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **a** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **b** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **c** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Wye-wound` 或 `Delta-wound`。

### **~1** — 定子正端连接电气

*自 R2024a 起*

与定子正端连接相关的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **~2** — 定子负端连接电气

*自 R2024a 起*

与定子负端连接相关的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a1** — *a* 正端连接电气

*自 R2024a 起*

与 *a* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b1** — *b* 正端连接电气

*自 R2024a 起*

与 *b* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c1** — *c* 正端连接电气

*自 R2024a 起*

与 *c* 正端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **a2** — *a* 负端连接电气

*自 R2024a 起*

与 *a* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **b2** — *b* 负端连接电气

*自 R2024a 起*

与 *b* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **c2** — *c* 负端连接电气

*自 R2024a 起*

与 *c* 负端连接相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`，并将 **Winding type** 设置为 `Open-end`。

### **n** — 中性相电气

与中性相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding Type** 设置为 `Wye-wound`，并将 **Zero sequence** 设置为 `Include`。

### **R** — 电机动子机械

与电机动子相关的机械平移守恒端口。

### **C** — 电机外壳机械

与电机外壳相关的机械平移守恒端口。

### **HA** — 绕组 A 热端口热

与绕组 A 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 绕组 B 热端口热

与绕组 B 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HC** — 绕组 C 热端口热

与绕组 C 相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口热

与转子相关的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主
- name: Winding type
  summary: 绕组配置 Wye-wound（默认）| Delta-wound | Open-end
  group: 主
- name: Modeling fidelity
  summary: 建模保真度 Constant Ld, Lq and PM（默认）| Tabulated Ld, Lq and PM
  group: 主
- name: Polar pitch
  summary: 极距 0.03 m（默认）| 标量
  group: 主
- name: Permanent magnet flux linkage parameterization
  summary: 永磁磁链参数化 Specify flux linkage（默认）| Specify force constant | Specify back EMF constant
  group: 主
- name: Permanent magnet flux linkage
  summary: 永磁磁链 0.03 Wb（默认）| 标量
  group: 主
- name: Force constant
  summary: 力常数 0.18 N/A（默认）| 标量
  group: 主
- name: Back EMF constant
  summary: 反电动势常数 0.18 s*V/m（默认）| 标量
  group: 主
- name: Stator parameterization
  summary: 定子参数化 Specify Ld, Lq, and L0（默认）| Specify Ls, Lm, and Ms
  group: 主
- name: Stator d-axis inductance, Ld
  summary: 定子 d 轴电感 0.00019 H（默认）| 标量
  group: 主
- name: Stator q-axis inductance, Lq
  summary: 定子 q 轴电感 0.00025 H（默认）| 标量
  group: 主
- name: Stator zero-sequence inductance, L0
  summary: 定子零序电感 0.00016 H（默认）| 标量
  group: 主
- name: Direct-axis current vector, iD
  summary: 直轴电流向量 [-200, 0, 200] A（默认）| 向量
  group: 主
- name: Quadrature-axis current vector, iQ
  summary: 交轴电流向量 [-200, 0, 200] A（默认）| 向量
  group: 主
- name: Ld matrix, Ld(id,iq)
  summary: Ld 矩阵 0.00019 * ones(3, 3) H（默认）| 矩阵
  group: 主
- name: Lq matrix, Lq(id,iq)
  summary: Lq 矩阵 0.00025 * ones(3, 3) H（默认）| 矩阵
  group: 主
- name: Permanent magnet flux linkage, PM(id,iq)
  summary: 永磁磁链 0.03 * ones(3, 3) Wb（默认）
  group: 主
- name: Force constant matrix, kf(iD,iQ)
  summary: 力常数矩阵 0.18 * ones(3, 3) N/A（默认）| 矩阵
  group: 主
- name: Back EMF constant matrix, ke(iD,iQ)
  summary: 反电动势常数矩阵 0.18 * ones(3, 3) s*V/m（默认）| 矩阵
  group: 主
- name: Stator self-inductance per phase, Ls
  summary: 每相定子自感 0.0002 H（默认）| 标量
  group: 主
- name: Stator inductance fluctuation, Lm
  summary: 定子电感波动 -0.00002 H（默认）| 标量
  group: 主
- name: Stator mutual inductance, Ms
  summary: 定子互感 0.00002 H（默认）| 标量
  group: 主
- name: Stator resistance per phase, Rs
  summary: 每相定子电阻 0.013 Ohm（默认）| 标量
  group: 主
- name: Zero sequence
  summary: 零序选项 Include（默认）| Exclude
  group: 主
- name: Angle definition
  summary: 角度测量的参考点 Angle between the a-phase magnetic axis and the d-axis（默认）| Angle between the a-phase magnetic axis and
    the q-axis
  group: 主
- name: Mass of the mover
  summary: 动子质量 0.01 kg（默认）
  group: 机械
- name: Linear damping
  summary: 线性阻尼 0 N/(m/s)（默认）
  group: 机械
- name: Measurement temperature
  summary: 测量温度 298.15 K（默认）
  group: 热
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认）
  group: 热
- name: Permanent magnet flux temperature coefficient
  summary: 永磁磁通温度系数 -0.001 1/K（默认）
  group: 热
- name: Thermal mass for each stator winding
  summary: 每个定子绕组的热质量 100 J/K（默认）
  group: 热
- name: Rotor thermal mass
  summary: 转子热质量 200 J/K（默认）
  group: 热
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对生成的热效应和电机温度进行建模。

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

使用复合三相端口还是扩展三相端口。

### **Winding type** — 绕组配置 `Wye-wound`（默认）| `Delta-wound` | `Open-end`

绕组配置：

- `Wye-wound` — 绕组为星形连接。
- `Delta-wound` — 绕组为三角形连接。*a* 相连接在端口 **a** 和 **b** 之间，*b* 相连接在端口 **b** 和 **c** 之间，*c* 相连接在端口 **c** 和 **a** 之间。
- `Open-end` — 绕组为开放式配置。模块将绕组的每一端作为电气连接暴露出来。

### **Modeling fidelity** — 建模保真度 `Constant Ld, Lq and PM`（默认）| `Tabulated Ld, Lq and PM`

建模保真度：

- `Constant Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值为常数，由各自的参数定义。
- `Tabulated Ld, Lq and PM` — *Ld*、*Lq* 和 *PM* 值根据 DQ 电流查找表在线计算，如下所示：

  Ld=f1(id,iq)

  Ld=f2(id,iq)

  λPM=f2(id,iq)

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Polar pitch** — 极距 `0.03` `m`（默认）| 标量

极距。

### **Permanent magnet flux linkage parameterization** — 永磁磁链参数化 `Specify flux linkage`（默认）| `Specify force constant` | `Specify back EMF constant`

永磁磁链，指定为 `Specify flux linkage`、`Specify force constant` 或 `Specify back EMF constant`。

### **Permanent magnet flux linkage** — 永磁磁链 `0.03` `Wb`（默认）| 标量

与任一 stator 绕组交链的峰值永磁磁链。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify flux linkage`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Force constant** — 力常数 `0.18` `N/A`（默认）| 标量

任一 stator 绕组的力常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify force constant`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Back EMF constant** — 反电动势常数 `0.18` `s*V/m`（默认）| 标量

任一 stator 绕组的反电动势常数。

#### 依赖关系

要启用此参数，请将 **Permanent magnet flux linkage parameterization** 设置为 `Specify back EMF constant`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator parameterization** — 定子参数化 `Specify Ld, Lq, and L0`（默认）| `Specify Ls, Lm, and Ms`

定子参数化，指定为 `Specify Ld, Lq, and L0` 或 `Specify Ls, Lm, and Ms`。

### **Stator d-axis inductance, Ld** — 定子 `d` 轴电感 `0.00019` `H`（默认）| 标量

`d` 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator q-axis inductance, Lq** — 定子 q 轴电感 `0.00025` `H`（默认）| 标量

`q` 轴电感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Constant Ld, Lq and PM`。

### **Stator zero-sequence inductance, L0** — 定子零序电感 `0.00016` `H`（默认）| 标量

零序电感。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Winding Type** 设置为 `Wye-wound`，将 **Zero sequence** 设置为 `Include`，并将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。
- 将 **Winding Type** 设置为 `Delta-wound`，并将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`。

### **Direct-axis current vector, iD** — 直轴电流向量 `[-200, 0, 200]` `A`（默认）| 向量

直轴电流向量，iD。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Quadrature-axis current vector, iQ** — 交轴电流向量 `[-200, 0, 200]` `A`（默认）| 向量

交轴电流向量，iQ。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Ld matrix, Ld(id,iq)** — Ld 矩阵 `0.00019 * ones(3, 3)` `H`（默认）| 矩阵

Ld 矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Lq matrix, Lq(id,iq)** — Lq 矩阵 `0.00025 * ones(3, 3)` `H`（默认）| 矩阵

Lq 矩阵。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ld, Lq, and L0`，并将 **Modeling fidelity** 设置为 `Tabulated Ld, Lq and PM`。

### **Permanent magnet flux linkage, PM(id,iq)** — 永磁磁链 `0.03 * ones(3, 3)` `Wb`（默认）

永磁磁链。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify flux linkage`

### **Force constant matrix, kf(iD,iQ)** — 力常数矩阵 `0.18 * ones(3, 3)` `N/A`（默认）| 矩阵

力常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify force constant`

### **Back EMF constant matrix, ke(iD,iQ)** — 反电动势常数矩阵 `0.18 * ones(3, 3)` `s*V/m`（默认）| 矩阵

反电动势常数矩阵。

#### 依赖关系

要启用此参数，请设置：

- **Stator parameterization** 为 `Specify Ld, Lq, and L0`
- **Modeling fidelity** 为 `Tabulated Ld, Lq and PM`
- **Permanent magnet flux linkage parameterization** 为 `Specify back EMF constant`

### **Stator self-inductance per phase, Ls** — 每相定子自感 `0.0002` `H`（默认）| 标量

五个定子绕组中每个绕组的平均自感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator inductance fluctuation, Lm** — 定子电感波动 `-0.00002` `H`（默认）| 标量

定子绕组的自感和互感随角度的波动。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator mutual inductance, Ms** — 定子互感 `0.00002` `H`（默认）| 标量

定子绕组之间的平均互感。

#### 依赖关系

要启用此参数，请将 **Stator parameterization** 设置为 `Specify Ls, Lm, and Ms`。

### **Stator resistance per phase, Rs** — 每相定子电阻 `0.013` `Ohm`（默认）| 标量

每个定子绕组的电阻。

### **Zero sequence** — 零序选项 `Include`（默认）| `Exclude`

包含或排除零序项的选项。

- `Include` — 包含零序项。要优先考虑模型保真度，请使用此默认设置。使用此选项：

  - 对于使用 Partitioning 求解器的仿真会导致错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
  - 会暴露一个零序参数。
- `Exclude` — 排除零序项。要优先考虑桌面仿真或实时部署的仿真速度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **Winding Type** 设置为 `Wye-wound`。

### **Angle definition** — 角度测量的参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认）| `Angle between the a-phase magnetic axis and the q-axis`

角度测量的参考点。默认值为 `Angle between the a-phase magnetic axis and the d-axis`。此定义显示在 Motor Construction 图中。当您选择此值时，动子角度为零时动子和 *a* 相磁通对齐。

此参数可选择的另一个值为 `Angle between the a-phase magnetic axis and the q-axis`。当您选择此值时，动子角度为零时 *a* 相电流产生最大力。

### 机械

### **Mass of the mover** — 动子质量 `0.01` `kg`（默认）

电机动子的质量。

### **Linear damping** — 线性阻尼 `0` `N/(m/s)`（默认）

线性阻尼。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Measurement temperature** — 测量温度 `298.15` `K`（默认）

电机参数的标称温度。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值为铜的值。

### **Permanent magnet flux temperature coefficient** — 永磁磁通温度系数 `-0.001` `1/K`（默认）

永磁磁通密度随温度的分数变化率。使用此参数可在温度升高时线性降低转矩和感应反电动势。

### **Thermal mass for each stator winding** — 每个定子绕组的热质量 `100` `J/K`（默认）

A、B 和 C 绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）

转子的热质量，即使转子温度升高一度所需的能量。
## 所属库

Simscape / Electrical / Electromechanical / Permanent Magnet

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：定子绕组的开放式配置

要以开放式配置对电机的定子绕组进行建模，请将 **Winding type** 参数设置为 `Open-end`。然后，PMLSM 模块通过启用相应的电气守恒端口来暴露绕组的每一端。

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有正弦磁通分布的水磁直线同步电机

PMLSM 模块对具有三相星形绕组定子的永磁直线同步电机（PMLSM）进行建模。使用此模块对直线同步电机（LSM）和直线伺服电机进行建模。下图显示了定子绕组的等效电路。

您也可以通过将 **Winding type** 设置为 `Delta-wound` 来对三角形绕组配置的永磁直线同步电机进行建模。

### 电机结构

下图显示了电机结构。

### 方程

定子绕组两端的电压定义为：

[vavbvc]=[Rs000Rs000Rs][iaibic]+[dψadtdψbdtdψcdt],

其中：

- *va*、*vb* 和 *vc* 是定子绕组各相的相电压。
- *Rs* 是每个定子绕组的等效电阻。
- *ia*、*ib* 和 *ic* 是流过定子绕组的电流。
- dψadt、dψbdt 和 dψcdt 是每个定子绕组中磁通的变化率。

永磁体和三个绕组共同贡献了链接每个绕组的总磁通。总磁通定义为：

[ψaψbψc]=[LaaLabLacLbaLbbLbcLcaLcbLcc][iaibic]+[ψamψbmψcm],

其中：

- *ψa*、*ψb* 和 *ψc* 是链接每个定子绕组的总磁通。
- *Laa*、*Lbb* 和 *Lcc* 是定子绕组的自感。
- *Lab*、*Lac*、*Lba*、*Lbc*、*Lca* 和 *Lcb* 是定子绕组的互感。
- *ψam*、*ψbm* 和 *ψcm* 是链接定子绕组的永磁体磁通。

定子绕组中的电感是电角度的函数，定义为：

θe=Npx+rotor offset,

Laa=Ls+Lmcos(2θe)

Lbb=Ls+Lmcos(2(θe−2π/3))

Lcc=Ls+Lmcos(2(θe+2π/3))

Lab=Lba=−Ms−Lmcos(2(θe+π/6))

Lbc=Lcb=−Ms−Lmcos(2(θe+π/6−2π/3))

以及

Lca=Lac=−Ms−Lmcos(2(θe+π/6+2π/3))

其中：

- *θe* 是电角度。
- *rotor offset* 如果您相对于 d 轴定义转子电角度，则为 `0`；如果您相对于 q 轴定义转子电角度，则为 `-pi/2`。
- Np=πτ，*τ* 是极距。
- *x* 是距离。
- *Ls* 是每相定子自感。该值是每个定子绕组的平均自感。
- *Lm* 是定子电感波动。该值是自感和互感随角度变化的波动量。
- *Ms* 是定子互感。该值是定子绕组之间的平均互感。

当 *θe* = 0° 时，链接绕组 *a* 的永磁体磁通最大；当 *θe* = 90° 时为零。因此，链接的电机磁通定义为：

[ψamψbmψcm]=[ψmcosθeψmcos(θe−2π/3)ψmcos(θe+2π/3)]

其中 *ψm* 是永磁体磁链。

### 简化电气方程

对电气方程应用 Park 变换可得到与角度无关的力表达式。

Park 变换定义为：

P=2/3[cosθecos(θe−2π/3)cos(θe+2π/3)−sinθe−sin(θe−2π/3)−sin(θe+2π/3)0.50.50.5]

其中 *θe* 是定义为 *Npx* 的电角度。

对定子绕组电压和电流使用 Park 变换将其转换到 dq0 坐标系，该坐标系与角度无关：

[vdvqv0]=P[vavbvc]

以及

[idiqi0]=P[iaibic]

对前两个电气方程应用 Park 变换可得到以下定义模块行为的方程：

vd=Rsid+Lddiddt−NpviqLq,

vq=Rsiq+Lqdiqdt+Npv(idLd+ψm),

v0=Rsi0+L0di0dt

以及

F=32Np(iq(idLd+ψm)−idiqLq),

Mdvdt=F−FL−Bmv,

其中：

- *Ld* = *Ls* + *Ms* + 3/2 *Lm*。*Ld* 是定子 *d* 轴电感。
- *Lq* = *Ls* + *Ms* − 3/2 *Lm*。*Lq* 是定子 *q* 轴电感。
- *L0* = *Ls* – 2*Ms*。*L0* 是定子零序电感。
- *Rs* 是每相定子电阻。
- *v* 是线速度。
- *Np* 是极距因子。
- *M* 是动子的质量。
- *Bm* 是阻尼。
- *FL* 是负载力。

PMLSM 模块使用 Park 变换的原始非正交实现。如果您尝试应用替代实现，会得到不同的 dq0 电压和电流结果。

力常数 *kf*、反电动势常数 *ke* 和永磁体磁链之间的关系定义如下：

ke=kf=Npψm。

### 建模热效应

您可以暴露热端口来对产生的热量和电机温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块包含与定子绕组相关的扩展电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组相关的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
