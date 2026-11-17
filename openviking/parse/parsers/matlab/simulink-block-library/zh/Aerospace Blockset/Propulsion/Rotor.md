---
type: simulink-block
title: 'Rotor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'rotor'
documentation_source_path: 'rotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotor

## 端口
```yaml
ports:
- name: Ω (rad/sec)
  summary: 旋翼转速标量
  direction: input
  data_types: double
- name: ρ
  summary: 空气密度正标量
  direction: input
  data_types: double
- name: Vb
  summary: 旋翼机体速度 3×1 向量 | 1×3 向量
  direction: input
  data_types: double
- name: ωb
  summary: 角速度 3×1 向量 | 1×3 向量
  direction: input
  data_types: double
- name: θ0
  summary: 总距桨距角标量
  direction: input
  data_types: double
- name: θc
  summary: 横向周期变距桨距角标量
  direction: input
  data_types: double
- name: θs
  summary: 纵向周期变距桨距角标量
  direction: input
  data_types: double
- name: CT
  summary: 输入推力系数非零正标量
  direction: input
  data_types: double
- name: CQ
  summary: 输入扭矩系数非零正标量
  direction: input
  data_types: double
- name: Fxyz(N)
  summary: 总力三元素向量
  direction: output
  data_types: double
- name: Mxyz(Nm)
  summary: 净力矩三元素向量
  direction: output
  data_types: double
- name: CT
  summary: 计算得到的推力系数正标量
  direction: output
  data_types: double
- name: CQ
  summary: 计算得到的扭矩系数正标量
  direction: output
  data_types: double
```

### 输入

### **Ω (rad/sec)** — 旋翼转速标量

旋翼转速，指定为机体坐标系下以 rad/sec 为单位的标量。

**数据类型：** `double`

### **ρ** — 空气密度正标量

空气密度，指定为以指定单位表示的正标量。

**数据类型：** `double`

### **Vb** — 旋翼机体速度 3×1 向量 | 1×3 向量

旋翼速度，指定为机体坐标系下的 3×1 或 1×3 向量。要执行多系统分析，请考虑将 State-Space 或 Integrator 模块的输出连接到此端口。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

速度的单位取决于 `Units` 参数的值。

**数据类型：** `double`

### **ωb** — 角速度 3×1 向量 | 1×3 向量

整个飞行器的角速度，指定为机体坐标系下以 rad/s 为单位的 3×1 或 1×3 向量。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

**数据类型：** `double`

### **θ0** — 总距桨距角标量

总距桨距角，指定为以弧度为单位的标量。

#### 依赖关系

要启用此输入端口，请选中 **Include pitch angle inputs** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **θc** — 横向周期变距桨距角标量

横向周期变距桨距角，指定为以弧度为单位的标量。

#### 依赖关系

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **θs** — 纵向周期变距桨距角标量

纵向周期变距桨距角，指定为以弧度为单位的标量。

#### 依赖关系

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **CT** — 输入推力系数非零正标量

输入推力系数，指定为非零正标量。

#### 依赖关系

要启用此输入端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### **CQ** — 输入扭矩系数非零正标量

输入扭矩系数，指定为非零正标量。

#### 依赖关系

要启用此输出端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`
### 输出

### **Fxyz(N)** — 总力三元素向量

总力，以机体坐标系下的三元素向量形式返回。单位取决于 **Units** 参数。

**数据类型：** `double`

### **Mxyz(Nm)** — 净力矩三元素向量

沿 *x*-*y*-*z* 方向的净力矩，以机体坐标系下的三元素向量形式返回。单位取决于 **Units** 参数。

**数据类型：** `double`

### **CT** — 计算得到的推力系数正标量

计算得到的推力系数，以正标量形式返回。

#### 依赖关系

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **CQ** — 计算得到的扭矩系数正标量

计算得到的扭矩系数，以正标量形式返回。

#### 依赖关系

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Modeling
  summary: 旋翼推力计算方法 Without flap effects（默认）| With flap effects
  group: ''
  block_parameter: modelMode
  type: character vector
  values: '''Without flap effects'' | ''With flap effects'''
  default: '''Without flap effects'''
- name: Include pitch angle inputs
  summary: 启用桨距角输入 off（默认）| on
  group: ''
  block_parameter: controlInput
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: CT and CQ Source
  summary: 用于选择推力和扭矩系数值来源的下拉菜单 'Dialog'（默认）| 'Compute using BEMT' | 'Ports'
  group: ''
  block_parameter: CTCQMode
  type: character vector
  values: '''Dialog'' | ''Compute using BEMT'''
  default: '''Dialog'''
- name: Thrust coefficient (CT)
  summary: 推力系数 0.0107（默认）| 非零正标量
  group: ''
  block_parameter: CT
  type: character vector
  values: '''0.0107'' | nonzero positive scalar'
  default: '''0.0107'''
- name: Torque coefficient (CQ)
  summary: 扭矩系数 7.8263e-4（默认）| 非零正标量
  group: ''
  block_parameter: CQ
  type: character vector
  values: '''7.8263e-4'' | nonzero positive scalar'
  default: '''7.8263e-4'''
- name: Number of blades
  summary: 每个旋翼的桨叶数 2（默认）| 非零正标量
  group: ''
  block_parameter: Nb
  type: character vector
  values: '''2'' | nonzero positive scalar'
  default: '''2'''
- name: Output computed CT and CQ
  summary: 输出计算得到的推力系数和扭矩系数 off（默认）| on
  group: ''
  block_parameter: CTout
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Radius (m)
  summary: 旋翼半径 0.0330（默认）| 非零正标量
  group: ''
  block_parameter: radius
  type: character vector
  values: '''0.0330'' | nonzero positive scalar'
  default: '''0.0330'''
- name: Chord (m)
  summary: 桨叶弦长 0.0080（默认）| 非零正标量
  group: ''
  block_parameter: chord
  type: character vector
  values: '''0.0080'' | nonzero positive scalar'
  default: '''0.0080'''
- name: Hinge offset (m)
  summary: 铰链偏移 0（默认）| 正标量
  group: ''
  block_parameter: hingeOffset
  type: character vector
  values: '''0'' | positive scalar'
  default: '''0'''
- name: Lift curve slope (per rad)
  summary: 升力曲线斜率 5.5（默认）| 非零正标量
  group: ''
  block_parameter: clalpha
  type: character vector
  values: '''5.5'' | nonzero positive scalar'
  default: '''5.5'''
- name: Mean drag coefficient
  summary: 平均阻力系数 0（默认）| 正标量
  group: ''
  block_parameter: cd0
  type: character vector
  values: '''0'' | positive scalar'
  default: '''0'''
- name: Lock number
  summary: 洛克数 0.6051（默认）| 非零正标量
  group: ''
  block_parameter: gamma
  type: character vector
  values: '''0.6051'' | nonzero positive scalar'
  default: '''0.6051'''
- name: Twist distribution
  summary: 旋翼桨叶扭转分布 Linear（默认）| Ideal
  group: ''
  block_parameter: twistType
  type: character vector
  values: '''Linear'' | ''Ideal'''
  default: '''Linear'''
- name: Blade root angle (rad)
  summary: 桨叶根部桨距角 0.2548（默认）| 实标量
  group: ''
  block_parameter: thetaRoot
  type: real scalar
  values: '''0.2548'' | nonzero positive scalar'
  default: '''0.2548'''
- name: Blade twist angle (rad)
  summary: 桨叶扭转角 -0.1361（默认）| 实标量
  group: ''
  block_parameter: thetaTwist
  type: real scalar
  values: '''0.1018'' | positive scalar'
  default: '''0.1018'''
- name: Blade tip angle (rad)
  summary: 桨叶尖部桨距角 0.1018（默认）| 实标量
  group: ''
  block_parameter: thetaTip
  type: real scalar
  values: '''0.06'' | nonzero positive scalar'
  default: '''0.06'''
```

#### 主

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

| 单位 | 速度 | 密度 | 力 | 力矩 | 半径 | 弦长 | 铰链偏移 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | 米每秒 | kg/m3 | 牛顿 | 牛顿-米 | 米 | 米 | 米 |
| `English (Velocity in ft/s)` | 英尺每秒 | slug/ft3 | 磅力 | 磅力-英尺 | 英尺 | 英尺 | 英尺 |
| `English (Velocity in kts)` | 节 | slug/ft3 | 磅力 | 磅力-英尺 | 英尺 | 英尺 | 英尺 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Modeling** — 旋翼推力计算方法 `Without flap effects`（默认）| `With flap effects`

旋翼推力计算方法，指定为：

- `Without flap effects` — 使用力和力矩计算来建模旋翼推力。有关详细信息，请参阅 Force and Moment。
- `With flap effects` — 包含前飞时由于挥舞运动导致的旋翼桨盘倾斜效应。稳态横向和纵向挥舞角使用 [1] 中的方程计算，并用于力和力矩的计算 [2]。有关详细信息，请参阅 Force and Moment。

#### 编程使用

|  |
| --- |
| **模块参数**：`modelMode` |
| **类型**：character vector |
| **值**：`'Without flap effects'` | `'With flap effects'` |
| **默认值**：`'Without flap effects'` |

### **Include pitch angle inputs** — 启用桨距角输入 `off`（默认）| `on`

选中此复选框以启用桨距角（斜盘）输入端口。

#### 依赖关系

要启用此复选框

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`controlInput` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### 旋翼

### **CT and CQ Source** — 用于选择推力和扭矩系数值来源的下拉菜单 `'Dialog'`（默认）| `'Compute using BEMT'` | `'Ports'`

选择推力系数和扭矩系数值的来源，指定为字符向量值 `'Dialog'`、`'Compute using BEMT'` 或 `'Ports'`。该模块假定气动和结构参数为常数。

- 选择 `'Dialog'` 以手动输入推力和扭矩系数值。
- 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。
- 选择 `'Ports'` 以将推力和扭矩系数值作为输入接受。

#### 编程使用

|  |
| --- |
| **模块参数**：`CTCQMode` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Compute using BEMT'` |
| **默认值**：`'Dialog'` |

### **Thrust coefficient (CT)** — 推力系数 `0.0107`（默认）| 非零正标量

推力系数，指定为非零正标量。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`CT` |
| **类型**：character vector |
| **值**：`'0.0107'` | nonzero positive scalar |
| **默认值**：`'0.0107'` |

### **Torque coefficient (CQ)** — 扭矩系数 `7.8263e-4`（默认）| 非零正标量

扭矩系数，指定为非零正标量。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`CQ` |
| **类型**：character vector |
| **值**：`'7.8263e-4'` | nonzero positive scalar |
| **默认值**：`'7.8263e-4'` |

### **Number of blades** — 每个旋翼的桨叶数 `2`（默认）| 非零正标量

桨叶数，指定为非零正标量。

#### 依赖关系

要启用此参数，

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`Nb` |
| **类型**：character vector |
| **值**：`'2'` | nonzero positive scalar |
| **默认值**：`'2'` |

### **Output computed CT and CQ** — 输出计算得到的推力系数和扭矩系数 off（默认）| on

选中此复选框以将计算得到的推力系数和扭矩系数输出到 **CT** 和 **CQ** 输出端口。有关这些计算的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。该模块假定气动和结构参数为常数。

否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`CTout` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### 桨叶

### **Radius (m)** — 旋翼半径 `0.0330`（默认）| 非零正标量

旋翼半径，指定为非零正标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`radius` |
| **类型**：character vector |
| **值**：`'0.0330'` | nonzero positive scalar |
| **默认值**：`'0.0330'` |

### **Chord (m)** — 桨叶弦长 `0.0080`（默认）| 非零正标量

桨叶弦长，指定为非零正标量。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`chord` |
| **类型**：character vector |
| **值**：`'0.0080'` | nonzero positive scalar |
| **默认值**：`'0.0080'` |

### **Hinge offset (m)** — 铰链偏移 `0`（默认）| 正标量

铰链偏移，指定为正标量。对于螺旋桨，此值通常为 `0`。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`hingeOffset` |
| **类型**：character vector |
| **值**：`'0'` | positive scalar |
| **默认值**：`'0'` |

### **Lift curve slope (per rad)** — 升力曲线斜率 `5.5`（默认）| 非零正标量

升力曲线斜率，指定为非零正标量。该模块假定气动和结构参数为常数。该模块不考虑随迎角的变化。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`clalpha` |
| **类型**：character vector |
| **值**：`'5.5'` | nonzero positive scalar |
| **默认值**：`'5.5'` |

### **Mean drag coefficient** — 平均阻力系数 0（默认）| 正标量

平均阻力系数，指定为正标量。该模块不考虑随迎角的变化。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 编程使用

|  |
| --- |
| **模块参数**：`cd0` |
| **类型**：character vector |
| **值**：`'0'` | positive scalar |
| **默认值**：`'0'` |

### **Lock number** — 洛克数 `0.6051`（默认）| 非零正标量

洛克数，即气动力与惯性力之比，指定为非零正标量。

#### 依赖关系

要启用此参数，请将 **Modeling** 设置为 `With flap effects`。

#### 编程使用

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：character vector |
| **值**：`'0.6051'` | nonzero positive scalar |
| **默认值**：`'0.6051'` |

### **Twist distribution** — 旋翼桨叶扭转分布 `Linear`（默认）| `Ideal`

旋翼桨叶扭转分布，指定为：

- `Linear` — 桨叶扭转分布的近似。

  θ(r)=θroot+θtwistr
- `Ideal` — 桨叶扭转分布的最优近似。

  θ(r)=θtipr

其中 *r* 是沿桨叶的无量纲径向位置。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程使用

|  |
| --- |
| **模块参数**：`twistType` |
| **类型**：character vector |
| **值**：`'Linear'` | `'Ideal'` |
| **默认值**：`'Linear'` |

### **Blade root angle (rad)** — 桨叶根部桨距角 `0.2548`（默认）| 实标量

桨叶根部桨距角 θroot，指定为实标量。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 编程使用

|  |
| --- |
| **模块参数**：`thetaRoot` |
| **类型**：real scalar |
| **值**：`'0.2548'` | nonzero positive scalar |
| **默认值**：`'0.2548'` |

### **Blade twist angle (rad)** — 桨叶扭转角 `-0.1361`（默认）| 实标量

桨叶扭转角 θtwist，指定为实标量。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 编程使用

|  |
| --- |
| **模块参数**：`thetaTwist` |
| **类型**：real scalar |
| **值**：`'0.1018'` | positive scalar |
| **默认值**：`'0.1018'` |

### **Blade tip angle (rad)** — 桨叶尖部桨距角 `0.1018`（默认）| 实标量

用于理想扭转分布的桨叶尖部桨距角 θtip，指定为实标量。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Ideal`。

#### 编程使用

|  |
| --- |
| **模块参数**：`thetaTip` |
| **类型**：real scalar |
| **值**：`'0.06'` | nonzero positive scalar |
| **默认值**：`'0.06'` |
## 所属库

Aerospace Blockset / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2025a：Rotor 模块现在包含推力和扭矩系数作为输入

从 R2025a 开始，当您将 **CT and CQ Source** 下拉菜单设置为 `'Ports'` 时，可以将 `CT` 和 `CQ` 作为 Rotor 模块的可选输入端口。

### R2024b：Rotor 模块现在包含斜盘作为输入

- 从 R2024b 开始，Rotor 模块已更新以支持斜盘输入。此新增功能允许通过新的可选输入端口在力和力矩的计算中包含总距和周期变距桨距角。
- 旋翼转速 Ω 现在也接受负输入。
- 从 R2024b 开始，Rotor 模块已更新，包含具有两个选项的 **CT and CQ Source** 下拉菜单：`'Dialog'` 和 `'Compute using BEMT'`。

  - 选择 `'Dialog'` 以手动输入推力和扭矩系数值。
  - 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。此选项等效于以前版本中的 **Compute CT and CQ** 复选框。

## 描述

计算气动力和力矩

Rotor 模块计算旋转螺旋桨或旋翼在所有三个维度上产生的气动力和力矩。该模块允许您包含前飞时由于挥舞运动导致的旋翼桨盘倾斜对所产生的力和力矩的影响。Rotor 模块考虑通过旋翼桨盘的轴向和横向流动的影响，这是旋翼飞行器系统分析所需的。
