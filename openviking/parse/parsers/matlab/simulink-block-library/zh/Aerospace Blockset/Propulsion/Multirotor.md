---
type: simulink-block
title: 'Multirotor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'multirotor'
documentation_source_path: 'multirotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Multirotor

## 端口
```yaml
ports:
- name: Ω (rad/sec)
  summary: 旋翼转速 *N* 元向量
  direction: input
  data_types: double
- name: ρ
  summary: 空气密度 正标量
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
  summary: 总距桨距角 N×1 向量 | 1×N 向量
  direction: input
  data_types: double
- name: θc
  summary: 横向周期变距桨距角 N×1 向量 | 1×N 向量
  direction: input
  data_types: double
- name: θs
  summary: 纵向周期变距桨距角 N×1 向量 | 1×N 向量
  direction: input
  data_types: double
- name: CT
  summary: 输入推力系数 非零正标量 | N×1 向量
  direction: input
  data_types: double
- name: CQ
  summary: 输入扭矩系数 非零正标量 | N×1 向量
  direction: input
  data_types: double
- name: Fxyz(N)
  summary: 总力 三元向量
  direction: output
  data_types: double
- name: Mxyz(Nm)
  summary: 净力矩 三元向量
  direction: output
  data_types: double
- name: CT
  summary: 计算的推力系数 正向量
  direction: output
- name: CQ
  summary: 计算的扭矩系数 正向量
  direction: output
```

### 输入

### **Ω (rad/sec)** — 旋翼转速 *N* 元向量

旋翼转速，指定为机体坐标系下以 rad/sec 为单位的 *N* 元向量。模块中考虑的两种四旋翼配置（*N* = 4）的旋翼顺序如臂计算中所示。

**数据类型：** `double`

### **ρ** — 空气密度 正标量

空气密度，指定为以指定单位表示的正标量。

**数据类型：** `double`

### **Vb** — 旋翼机体速度 3×1 向量 | 1×3 向量

旋翼速度，指定为机体坐标系下的 3×1 或 1×3 向量。要进行多系统分析，请考虑将 State-Space 或 Integrator 模块的输出连接到此端口。

#### 依赖

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

速度的单位取决于 `Units` 参数的值。

**数据类型：** `double`

### **ωb** — 角速度 3×1 向量 | 1×3 向量

整个飞行器的角速度，指定为机体坐标系下以 rad/s 为单位的 3×1 或 1×3 向量。

#### 依赖

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

**数据类型：** `double`

### **θ0** — 总距桨距角 N×1 向量 | 1×N 向量

总距桨距角，指定为 *N* 元向量。

#### 依赖

要启用此输入端口，请选中 **Include pitch angle inputs** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **θc** — 横向周期变距桨距角 N×1 向量 | 1×N 向量

横向周期变距桨距角，指定为 *N* 元向量。

#### 依赖

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **θs** — 纵向周期变距桨距角 N×1 向量 | 1×N 向量

纵向周期变距桨距角，指定为 *N* 元向量。

#### 依赖

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **CT** — 输入推力系数 非零正标量 | N×1 向量

输入推力系数，指定为非零正标量或 M×1 向量。

如果为标量，则假定所有旋翼具有相同的 `CT` 值。

#### 依赖

要启用此输入端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### **CQ** — 输入扭矩系数 非零正标量 | N×1 向量

输入扭矩系数，指定为非零正标量或 N×1 向量。

如果为标量，则假定所有旋翼具有相同的 `CQ` 值。

#### 依赖

要启用此输出端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`
### 输出

### **Fxyz(N)** — 总力 三元向量

总力，以机体坐标系下的三元向量返回。单位取决于 **Units** 参数。

**数据类型：** `double`

### **Mxyz(Nm)** — 净力矩 三元向量

沿 *x*-*y*-*z* 方向的净力矩，以机体坐标系下的三元向量返回。单位取决于 **Units** 参数。

**数据类型：** `double`

### **CT** — 计算的推力系数 正向量

计算的推力系数，以 *N* 元正向量返回。

#### 依赖

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

### **CQ** — 计算的扭矩系数 正向量

计算的扭矩系数，以 *N* 元正向量返回。

#### 依赖

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: 主要
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Modeling
  summary: 旋翼推力计算方法 Without flap effects（默认）| With flap effects
  group: 主要
  block_parameter: modelMode
  type: 字符向量
  values: '''Without flap effects'' | ''With flap effects'''
  default: '''Without flap effects'''
- name: Include pitch angle inputs
  summary: 启用桨距角输入 off（默认）| on
  group: 主要
  block_parameter: controlInput
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Configuration
  summary: 飞行器配置 Quadcopter X（默认）| Quadcopter +
  group: 飞行器
  block_parameter: config
  type: 字符向量
  values: '''Quadcopter X'' | ''Quadcopter +'''
  default: '''Quadcopter X'''
- name: Arm length (m)
  summary: 飞行器臂长 0.0624（默认）| 非零正标量
  group: 飞行器
  block_parameter: armLength
  type: 字符向量
  values: '''0.0624'' | 非零正标量'
  default: '''0.0624'''
- name: Height (m)
  summary: 距飞行器重心的垂直偏移 -0.0159（默认）| 非零标量
  group: 飞行器
  block_parameter: rotorHeight
  type: 字符向量
  values: '''-0.0159'' | 非零正标量'
  default: '''-0.0159'''
- name: CT and CQ Source
  summary: 用于选择推力和扭矩系数值来源的下拉菜单 'Dialog'（默认）| 'Compute using BEMT' | 'Ports'
  group: 旋翼
  block_parameter: CTCQMode
  type: 字符向量
  values: '''Dialog'' | ''Compute using BEMT'''
  default: '''Dialog'''
- name: Thrust coefficient (CT)
  summary: 推力系数 0.0107（默认）| 非零正标量 | 非零正 N×1 向量
  group: 旋翼
  block_parameter: CT
  type: 字符向量
  values: '''0.0107'' | 非零正标量'
  default: '''0.0107'''
- name: Torque coefficient (CQ)
  summary: 扭矩系数 7.8263e-4（默认）| 非零正标量 | 非零正 N×1 向量
  group: 旋翼
  block_parameter: CQ
  type: 字符向量
  values: '''7.8263e-4'' | 非零正标量'
  default: '''7.8263e-4'''
- name: Number of blades
  summary: 每个旋翼的桨叶数 2（默认）| 非零正标量
  group: 旋翼
  block_parameter: Nb
  type: 字符向量
  values: '''2'' | 非零正标量'
  default: '''2'''
- name: Output computed CT and CQ
  summary: 输出计算的推力系数和扭矩系数 off（默认）| on
  group: 旋翼
  block_parameter: CTout
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Radius (m)
  summary: 旋翼半径 0.0330（默认）| 非零正标量
  group: 旋翼
  block_parameter: radius
  type: 字符向量
  values: '''0.0330'' | 非零正标量'
  default: '''0.0330'''
- name: Chord (m)
  summary: 桨叶弦长 0.0080（默认）| 非零正标量
  group: 旋翼
  block_parameter: chord
  type: 字符向量
  values: '''0.0080'' | 非零正标量'
  default: '''0.0080'''
- name: Hinge offset (m)
  summary: 铰链偏移 0（默认）| 正标量
  group: 旋翼
  block_parameter: hingeOffset
  type: 字符向量
  values: '''0'' | 正标量'
  default: '''0'''
- name: Lift curve slope (per rad)
  summary: 升力曲线斜率 5.5（默认）| 非零正标量
  group: 旋翼
  block_parameter: clalpha
  type: 字符向量
  values: '''5.5'' | 非零正标量'
  default: '''5.5'''
- name: Mean drag coefficient
  summary: 平均阻力系数 0（默认）| 正标量
  group: 旋翼
  block_parameter: cd0
  type: 字符向量
  values: '''0'' | 正标量'
  default: '''0'''
- name: Lock number
  summary: 洛克数 0.6051（默认）| 非零正标量
  group: 旋翼
  block_parameter: gamma
  type: 字符向量
  values: '''0.6051'' | 非零正标量'
  default: '''0.6051'''
- name: Twist distribution
  summary: 旋翼桨叶扭转分布 Linear（默认）| Ideal
  group: 旋翼
  block_parameter: twistType
  type: 字符向量
  values: '''Linear'' | ''Ideal'''
  default: '''Linear'''
- name: Blade root angle (rad)
  summary: 桨叶根部桨距角 0.2548（默认）| 实标量
  group: 旋翼
  block_parameter: thetaRoot
  type: 实标量
  values: '''0.2548'' | 非零正标量'
  default: '''0.2548'''
- name: Blade twist angle (rad)
  summary: 桨叶扭转角 -0.1361（默认）| 实标量
  group: 旋翼
  block_parameter: thetaTwist
  type: 实标量
  values: '''0.1018'' | 正标量'
  default: '''0.1018'''
- name: Blade tip angle (rad)
  summary: 桨叶尖部桨距角 0.1018（默认）| 实标量
  group: 旋翼
  block_parameter: thetaTip
  type: 实标量
  values: '''0.06'' | 非零正标量'
  default: '''0.06'''
```

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

| 单位 | 速度 | 密度 | 力 | 力矩 | 臂长 | 高度 | 半径 | 弦长 | 铰链偏移 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | 米每秒 | kg/m3 | 牛顿 | 牛顿-米 | 米 | 米 | 米 | 米 | 米 |
| `English (Velocity in ft/s)` | 英尺每秒 | slug/ft3 | 磅力 | 磅力-英尺 | 英尺 | 英尺 | 英尺 | 英尺 | 英尺 |
| `English (Velocity in kts)` | 节 | slug/ft3 | 磅力 | 磅力-英尺 | 英尺 | 英尺 | 英尺 | 英尺 | 英尺 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Modeling** — 旋翼推力计算方法 `Without flap effects`（默认）| `With flap effects`

旋翼推力计算方法，指定为：

- `Without flap effects` — 使用力和力矩计算来建模旋翼推力。有关详细信息，请参阅力和力矩。
- `With flap effects` — 包含前飞时由于挥舞运动引起的旋翼桨盘倾斜效应。稳态横向和纵向挥舞角使用文献 [1] 中的方程计算，并用于力和力矩的计算 [2]。有关详细信息，请参阅力和力矩。

#### 程序化使用

|  |
| --- |
| **模块参数**：`modelMode` |
| **类型**：字符向量 |
| **值**：`'Without flap effects'` | `'With flap effects'` |
| **默认值**：`'Without flap effects'` |

### **Include pitch angle inputs** — 启用桨距角输入 `off`（默认）| `on`

选中此复选框以启用桨距角（斜盘）输入端口。

#### 依赖

要启用此复选框

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`controlInput` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 飞行器

### **Configuration** — 飞行器配置 `Quadcopter X`（默认）| `Quadcopter +`

四旋翼配置，指定为：

- `Quadcopter X` — 螺旋桨配置为 `X` 形，被认为比 `Quadcopter +` 配置更稳定。
- `Quadcopter +` — 螺旋桨配置为 `+` 形。

有关详细信息，请参阅臂计算。

#### 程序化使用

|  |
| --- |
| **模块参数**：`config` |
| **类型**：字符向量 |
| **值**：`'Quadcopter X'` | `'Quadcopter +'` |
| **默认值**：`'Quadcopter X'` |

### **Arm length (m)** — 飞行器臂长 `0.0624`（默认）| 非零正标量

飞行器臂长，指定为非零正标量。该长度为旋翼相对于飞行器质心的位移。有关臂长的详细信息，请参阅算法。

#### 程序化使用

|  |
| --- |
| **模块参数**：`armLength` |
| **类型**：字符向量 |
| **值**：`'0.0624'` | 非零正标量 |
| **默认值**：`'0.0624'` |

### **Height (m)** — 距飞行器重心的垂直偏移 `-0.0159`（默认）| 非零标量

距飞行器重心的垂直偏移，指定为非零标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`rotorHeight` |
| **类型**：字符向量 |
| **值**：`'-0.0159'` | 非零正标量 |
| **默认值**：`'-0.0159'` |

### 旋翼

### **CT and CQ Source** — 用于选择推力和扭矩系数值来源的下拉菜单 `'Dialog'`（默认）| `'Compute using BEMT'` | `'Ports'`

选择推力系数和扭矩系数值的来源，指定为值为 `'Dialog'`、`'Compute using BEMT'` 或 `'Ports'` 的字符向量。模块假定气动和结构参数为常数。

- 选择 `'Dialog'` 以手动输入推力和扭矩系数值。
- 选择 `'Compute using BEMT'` 以使用叶素动量理论（BEMT）计算值。有关 BEMT 的详细信息，请参阅推力系数和扭矩系数计算。
- 选择 `'Ports'` 以接受推力和扭矩系数值作为输入。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CTCQMode` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Compute using BEMT'` |
| **默认值**：`'Dialog'` |

### **Thrust coefficient (CT)** — 推力系数 `0.0107`（默认）| 非零正标量 | 非零正 N×1 向量

推力系数，指定为非零正标量或 N×1 向量。

如果将 `Thrust coefficient (CT)` 定义为标量，则假定所有旋翼具有相同的 *CT* 值。如果为向量，则旋翼顺序如臂计算中所示。

#### 依赖

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CT` |
| **类型**：字符向量 |
| **值**：`'0.0107'` | 非零正标量 |
| **默认值**：`'0.0107'` |

### **Torque coefficient (CQ)** — 扭矩系数 `7.8263e-4`（默认）| 非零正标量 | 非零正 N×1 向量

扭矩系数，指定为非零正标量或 N×1 元向量。

如果将 `Torque coefficient (CQ)` 定义为标量，则假定所有旋翼具有相同的 *CQ* 值。如果为向量，则旋翼顺序如臂计算中所示。

#### 依赖

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CQ` |
| **类型**：字符向量 |
| **值**：`'7.8263e-4'` | 非零正标量 |
| **默认值**：`'7.8263e-4'` |

### **Number of blades** — 每个旋翼的桨叶数 `2`（默认）| 非零正标量

每个旋翼的桨叶数，指定为非零正标量。

#### 依赖

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nb` |
| **类型**：字符向量 |
| **值**：`'2'` | 非零正标量 |
| **默认值**：`'2'` |

### **Output computed CT and CQ** — 输出计算的推力系数和扭矩系数 off（默认）| on

选中此复选框以将计算的推力系数和扭矩系数输出到 **CT** 和 **CQ** 输出端口。有关这些计算的详细信息，请参阅推力系数和扭矩系数计算。模块假定气动和结构参数为常数。

否则，清除此复选框。

#### 依赖

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CTout` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### 桨叶

### **Radius (m)** — 旋翼半径 `0.0330`（默认）| 非零正标量

旋翼半径，指定为非零正标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`radius` |
| **类型**：字符向量 |
| **值**：`'0.0330'` | 非零正标量 |
| **默认值**：`'0.0330'` |

### **Chord (m)** — 桨叶弦长 `0.0080`（默认）| 非零正标量

桨叶弦长，指定为非零正标量。

#### 依赖

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`chord` |
| **类型**：字符向量 |
| **值**：`'0.0080'` | 非零正标量 |
| **默认值**：`'0.0080'` |

### **Hinge offset (m)** — 铰链偏移 `0`（默认）| 正标量

铰链偏移，指定为正标量。对于螺旋桨，该值通常为 `0`。

#### 依赖

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`hingeOffset` |
| **类型**：字符向量 |
| **值**：`'0'` | 正标量 |
| **默认值**：`'0'` |

### **Lift curve slope (per rad)** — 升力曲线斜率 `5.5`（默认）| 非零正标量

升力曲线斜率，指定为非零正标量。模块假定气动和结构参数为常数。模块不考虑随攻角的变化。

#### 依赖

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`clalpha` |
| **类型**：字符向量 |
| **值**：`'5.5'` | 非零正标量 |
| **默认值**：`'5.5'` |

### **Mean drag coefficient** — 平均阻力系数 0（默认）| 正标量

平均阻力系数，指定为正标量。模块不考虑随攻角的变化。

#### 依赖

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`cd0` |
| **类型**：字符向量 |
| **值**：`'0'` | 正标量 |
| **默认值**：`'0'` |

### **Lock number** — 洛克数 `0.6051`（默认）| 非零正标量

洛克数，即气动力与惯性力之比，指定为非零正标量。

#### 依赖

要启用此参数，请将 **Modeling** 设置为 `With flap effects`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：字符向量 |
| **值**：`'0.6051'` | 非零正标量 |
| **默认值**：`'0.6051'` |

### **Twist distribution** — 旋翼桨叶扭转分布 `Linear`（默认）| `Ideal`

旋翼桨叶扭转分布，指定为：

- `Linear` — 桨叶扭转分布的近似。

  θ(r)=θroot+θtwistr
- `Ideal` — 桨叶扭转分布的最优近似。

  θ(r)=θtipr

其中 *r* 是沿桨叶的无量纲径向位置。

#### 依赖

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`twistType` |
| **类型**：字符向量 |
| **值**：`'Linear'` | `'Ideal'` |
| **默认值**：`'Linear'` |

### **Blade root angle (rad)** — 桨叶根部桨距角 `0.2548`（默认）| 实标量

桨叶根部桨距角 θroot，指定为实标量。

#### 依赖

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`thetaRoot` |
| **类型**：实标量 |
| **值**：`'0.2548'` | 非零正标量 |
| **默认值**：`'0.2548'` |

### **Blade twist angle (rad)** — 桨叶扭转角 `-0.1361`（默认）| 实标量

桨叶扭转角 θtwist，指定为实标量。

#### 依赖

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`thetaTwist` |
| **类型**：实标量 |
| **值**：`'0.1018'` | 正标量 |
| **默认值**：`'0.1018'` |

### **Blade tip angle (rad)** — 桨叶尖部桨距角 `0.1018`（默认）| 实标量

理想扭转分布的桨叶尖部桨距角 θtip，指定为实标量。

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
| **类型**：实标量 |
| **值**：`'0.06'` | 非零正标量 |
| **默认值**：`'0.06'` |
## 所属库

Aerospace Blockset / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2025a：Multirotor 模块现在包含推力和扭矩系数作为输入

从 R2025a 开始，当您将 **CT and CQ Source** 下拉菜单设置为 `'Ports'` 时，可以将 `CT` 和 `CQ` 作为 Multirotor 模块的可选输入端口。

### R2024b：Multirotor 模块现在包含斜盘作为输入

- Multirotor 模块已更新以支持斜盘输入。此新增功能允许通过新的可选输入端口在力和力矩的计算中包含总距和周期变距桨距角。
- `Thrust coefficient (CT)` 和 `Torque coefficient (CQ)` 参数现在也接受 N 元素向量作为输入。
- 从 R2024b 开始，Multirotor 模块已更新，包含 **CT and CQ Source** 下拉菜单，具有两个选项：`'Dialog'` 和 `'Compute using BEMT'`。

  - 选择 `'Dialog'` 以手动输入推力和扭矩系数值。
  - 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的更多信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。此选项等同于之前版本中的 **Compute CT and CQ** 复选框。

## 描述

计算空气动力和力矩

Multirotor 模块计算由多个旋转螺旋桨或旋翼（例如四旋翼飞行器）在所有三个维度中产生的空气动力和力矩。您还可以包含简化的挥舞（或稳态）空气动力学。
