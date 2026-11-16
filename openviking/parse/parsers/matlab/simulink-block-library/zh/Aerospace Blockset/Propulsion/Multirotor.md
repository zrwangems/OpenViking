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

### 输入

### **Ω (rad/sec)** — 转子速度 *N* 元素向量

转子速度，指定为机体坐标系中单位为 rad/sec 的 *N* 元素向量。该模块中考虑的两种四旋翼配置（*N* = 4）的转子排序如臂计算所示。

**数据类型：** `double`

### **ρ** — 空气密度正标量

空气密度，指定为指定单位下的正标量。

**数据类型：** `double`

### **Vb** — 转子的机体速度 3×1 向量 | 1×3 向量

转子速度，指定为机体坐标系中的 3×1 或 1×3 向量。要进行多系统分析，可考虑将 State-Space 或 Integrator 模块的输出连接到此端口。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

速度单位取决于 `Units` 参数的值。

**数据类型：** `double`

### **ωb** — 角速度 3×1 向量 | 1×3 向量

整个飞行器的角速度，指定为机体坐标系中单位为 rad/s 的 3×1 或 1×3 向量。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

**数据类型：** `double`

### **θ0** — 总距桨叶桨距角 N×1 向量 | 1×N 向量

总距桨叶桨距角，指定为 *N* 元素向量。

#### 依赖关系

要启用此输入端口，请选中 **包括桨距角输入** 复选框，并将 **CT 和 CQ 来源** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **θc** — 横向周期变距桨距角 N×1 向量 | 1×N 向量

横向周期变距桨距角，指定为 *N* 元素向量。

#### 依赖关系

要启用此输入端口，

- 选中 **包括桨距角输入** 复选框。
- 将 **建模** 设置为 `With flap effects`。

**数据类型：** `double`

### **θs** — 纵向周期变距桨距角 N×1 向量 | 1×N 向量

纵向周期变距桨距角，指定为 *N* 元素向量。

#### 依赖关系

要启用此输入端口，

- 选中 **包括桨距角输入** 复选框。
- 将 **建模** 设置为 `With flap effects`。

**数据类型：** `double`

### **CT** — 输入推力系数 非零正标量 | N×1 向量

输入推力系数，指定为非零正标量或 M×1 向量。

如果为标量，则假定所有转子具有相同的 `CT` 值。

#### 依赖关系

要启用此输入端口，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### **CQ** — 输入扭矩系数 非零正标量 | N×1 向量

输入扭矩系数，指定为非零正标量或 N×1 向量。

如果为标量，则假定所有转子具有相同的 `CQ` 值。

#### 依赖关系

要启用此输出端口，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### 输出

### **Fxyz(N)** — 总力 三元素向量

总力，以机体坐标系中的三元素向量形式返回。单位取决于 **单位** 参数。

**数据类型：** `double`

### **Mxyz(Nm)** — 净力矩 三元素向量

沿 *x*-*y*-*z* 方向的净力矩，以机体坐标系中的三元素向量形式返回。单位取决于 **单位** 参数。

**数据类型：** `double`

### **CT** — 计算得到的推力系数 正向量

计算得到的推力系数，以 *N* 个元素的正向量形式返回。

#### 依赖关系

要启用此输出端口，请选中 **输出计算得到的 CT 和 CQ** 复选框，并将 **CT 和 CQ 来源** 下拉菜单设置为 `Compute using BEMT`。

### **CQ** — 计算得到的扭矩系数 正向量

计算得到的扭矩系数，以 *N* 个元素的正向量形式返回。

#### 依赖关系

要启用此输出端口，请选中 **输出计算得到的 CT 和 CQ** 复选框，并将 **CT 和 CQ 来源** 下拉菜单设置为 `Compute using BEMT`。

## 参数

### 主

### **单位** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

| 单位 | 速度 | 密度 | 力 | 力矩 | 臂长 | 高度 | 半径 | 弦长 | 铰链偏移 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters per second | kg/m3 | Newtons | Newton-meter | Meters | Meters | Meters | Meters | Meters |
| `English (Velocity in ft/s)` | Feet per second | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet | Feet | Feet |
| `English (Velocity in kts)` | Knots | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet | Feet | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认**：`'Metric (MKS)'` |

### **建模** — 转子推力计算方法 `Without flap effects`（默认）| `With flap effects`

转子推力计算方法，指定为：

- `Without flap effects` — 使用力和力矩计算对转子推力进行建模。有关详细信息，请参阅力和力矩。
- `With flap effects` — 包含前飞时由于挥舞运动导致的旋翼桨盘倾斜效应。稳态横向和纵向挥舞角使用 [1] 中的方程计算，并用于力和力矩的计算 [2]。有关详细信息，请参阅力和力矩。

#### 程序化使用

|  |
| --- |
| **模块参数**：`modelMode` |
| **类型**：character vector |
| **值**：`'Without flap effects'` | `'With flap effects'` |
| **默认**：`'Without flap effects'` |

### **包括桨距角输入** — 启用桨距角输入 `off`（默认）| `on`

选中此复选框以启用桨距角（斜盘）输入端口。

#### 依赖关系

要启用此复选框

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`controlInput` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

### 载具

### **配置** — 载具配置 `Quadcopter X`（默认）| `Quadcopter +`

四旋翼配置，指定为：

- `Quadcopter X` — 螺旋桨按 `X` 形配置，被认为比 `Quadcopter +` 配置更稳定。
- `Quadcopter +` — 螺旋桨按 `+` 形配置。

有关详细信息，请参阅臂计算。

#### 程序化使用

|  |
| --- |
| **模块参数**：`config` |
| **类型**：character vector |
| **值**：`'Quadcopter X'` | `'Quadcopter +'` |
| **默认**：`'Quadcopter X'` |

### **臂长 (m)** — 载具臂长 `0.0624`（默认）| 非零正标量

载具臂长，指定为非零正标量。此长度是转子相对于载具质心的位移。有关臂长的详细信息，请参阅算法。

#### 程序化使用

|  |
| --- |
| **模块参数**：`armLength` |
| **类型**：character vector |
| **值**：`'0.0624'` | 非零正标量 |
| **默认**：`'0.0624'` |

### **高度 (m)** — 相对于载具重心的垂直偏移 `-0.0159`（默认）| 非零标量

相对于载具重心的垂直偏移，指定为非零标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`rotorHeight` |
| **类型**：character vector |
| **值**：`'-0.0159'` | 非零正标量 |
| **默认**：`'-0.0159'` |

### 转子

### **CT 和 CQ 来源** — 用于选择推力系数和扭矩系数值来源的下拉菜单 `'Dialog'`（默认）| `'Compute using BEMT'` | `'Ports'`

选择推力系数和扭矩系数值的来源，指定为值为 `'Dialog'`、`'Compute using BEMT'` 或 `'Ports'` 的字符向量。该模块假定空气动力学和结构参数为常量。

- 选择 `'Dialog'` 以手动输入推力系数和扭矩系数值。
- 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅推力系数和扭矩系数计算。
- 选择 `'Ports'` 以将推力系数和扭矩系数值作为输入接受。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CTCQMode` |
| **类型**：character vector |
| **值**：`'Dialog'` | `'Compute using BEMT'` |
| **默认**：`'Dialog'` |

### **推力系数 (CT)** — 推力系数 `0.0107`（默认）| 非零正标量 | 非零正 N×1 向量

推力系数，指定为非零正标量或 N×1 向量。

如果将 `Thrust coefficient (CT)` 定义为标量，则假定所有转子具有相同的 *CT* 值。如果为向量，则转子的排序如臂计算所示。

#### 依赖关系

要启用此参数，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Dialog'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CT` |
| **类型**：character vector |
| **值**：`'0.0107'` | 非零正标量 |
| **默认**：`'0.0107'` |

### **扭矩系数 (CQ)** — 扭矩系数 `7.8263e-4`（默认）| 非零正标量 | 非零正 N×1 向量

扭矩系数，指定为非零正标量或 N×1 元素向量。

如果将 `Torque coefficient (CQ)` 定义为标量，则假定所有转子具有相同的 *CQ* 值。如果为向量，则转子的排序如臂计算所示。

#### 依赖关系

要启用此参数，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Dialog'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CQ` |
| **类型**：character vector |
| **值**：`'7.8263e-4'` | 非零正标量 |
| **默认**：`'7.8263e-4'` |

### **桨叶数量** — 每个转子的桨叶数量 `2`（默认）| 非零正标量

每个转子的桨叶数量，指定为非零正标量。

#### 依赖关系

要启用此复选框，

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`Nb` |
| **类型**：character vector |
| **值**：`'2'` | 非零正标量 |
| **默认**：`'2'` |

### **输出计算得到的 CT 和 CQ** — 输出计算得到的推力系数和扭矩系数 off（默认）| on

选中此复选框以将计算得到的推力系数和扭矩系数输出到 **CT** 和 **CQ** 输出端口。有关这些计算的详细信息，请参阅推力系数和扭矩系数计算。该模块假定空气动力学和结构参数为常量。

否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`CTout` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'off'` |

#### 桨叶

### **半径 (m)** — 转子半径 `0.0330`（默认）| 非零正标量

转子半径，指定为非零正标量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`radius` |
| **类型**：character vector |
| **值**：`'0.0330'` | 非零正标量 |
| **默认**：`'0.0330'` |

### **弦长 (m)** — 桨叶弦长 `0.0080`（默认）| 非零正标量

桨叶弦长，指定为非零正标量。

#### 依赖关系

要启用此复选框，

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`chord` |
| **类型**：character vector |
| **值**：`'0.0080'` | 非零正标量 |
| **默认**：`'0.0080'` |

### **铰链偏移 (m)** — 铰链偏移 `0`（默认）| 正标量

铰链偏移，指定为正标量。对于螺旋桨，此值通常为 `0`。

#### 依赖关系

要启用此复选框，

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`hingeOffset` |
| **类型**：character vector |
| **值**：`'0'` | 正标量 |
| **默认**：`'0'` |

### **升力曲线斜率 (per rad)** — 升力曲线斜率 `5.5`（默认）| 非零正标量

升力曲线斜率，指定为非零正标量。该模块假定空气动力学和结构参数为常量。该模块不考虑随攻角的变化。

#### 依赖关系

要启用此复选框，

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`clalpha` |
| **类型**：character vector |
| **值**：`'5.5'` | 非零正标量 |
| **默认**：`'5.5'` |

### **平均阻力系数** — 平均阻力系数 0（默认）| 正标量

平均阻力系数，指定为正标量。该模块不考虑随攻角的变化。

#### 依赖关系

要启用此参数，请将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`cd0` |
| **类型**：character vector |
| **值**：`'0'` | 正标量 |
| **默认**：`'0'` |

### **洛克数** — 洛克数 `0.6051`（默认）| 非零正标量

洛克数，即空气动力与惯性力之比，指定为非零正标量。

#### 依赖关系

要启用此参数，请将 **建模** 设置为 `With flap effects`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：character vector |
| **值**：`'0.6051'` | 非零正标量 |
| **默认**：`'0.6051'` |

### **扭转分布** — 旋翼桨叶扭转分布 `Linear`（默认）| `Ideal`

旋翼桨叶扭转分布，指定为：

- `Linear` — 桨叶扭转分布的近似。

  θ(r)=θroot+θtwistr
- `Ideal` — 桨叶扭转分布的最优近似。

  θ(r)=θtipr

其中 *r* 是沿桨叶的无量纲径向位置。

#### 依赖关系

要启用此复选框，

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

#### 程序化使用

|  |
| --- |
| **模块参数**：`twistType` |
| **类型**：character vector |
| **值**：`'Linear'` | `'Ideal'` |
| **默认**：`'Linear'` |

### **桨叶根部角 (rad)** — 桨叶根部桨距角 `0.2548`（默认）| real scalar

桨叶根部桨距角 θroot，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

- 将 **扭转分布** 设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`thetaRoot` |
| **类型**：real scalar |
| **值**：`'0.2548'` | 非零正标量 |
| **默认**：`'0.2548'` |

### **桨叶扭转角 (rad)** — 桨叶扭转角 `-0.1361`（默认）| real scalar

桨叶扭转角 θtwist，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

- 将 **扭转分布** 设置为 `Linear`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`thetaTwist` |
| **类型**：real scalar |
| **值**：`'0.1018'` | 正标量 |
| **默认**：`'0.1018'` |

### **桨叶尖端角 (rad)** — 桨叶尖端桨距角 `0.1018`（默认）| real scalar

用于 `Ideal` 扭转分布的桨叶尖端桨距角 θtip，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT 和 CQ 来源** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **建模** 设置为 `'With flap effects'`

- 将 **扭转分布** 设置为 `Ideal`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`thetaTip` |
| **类型**：real scalar |
| **值**：`'0.06'` | 非零正标量 |
| **默认**：`'0.06'` |

## 所属库

Aerospace Blockset / Propulsion

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023a 中引入**

### R2025a：Multirotor 模块现在包含推力系数和扭矩系数作为输入

从 R2025a 开始，当您将 **CT 和 CQ 来源** 下拉菜单设置为 `'Ports'` 时，可以将 `CT` 和 `CQ` 作为 Multirotor 模块的可选输入端口。

### R2024b：Multirotor 模块现在包含斜盘作为输入

- Multirotor 模块已更新以支持斜盘输入。此新增功能允许通过新的可选输入端口，在力和力矩的计算中包含总距和周期变距桨叶桨距角。
- `Thrust coefficient (CT)` 和 `Torque coefficient (CQ)` 参数现在也接受 N 元素向量作为输入。
- 从 R2024b 开始，Multirotor 模块已更新，包含带有两个选项的下拉菜单 **CT 和 CQ 来源**：`'Dialog'` 和 `'Compute using BEMT'`。

  - 选择 `'Dialog'` 以手动输入推力系数和扭矩系数值。
  - 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅推力系数和扭矩系数计算。此选项等效于以前版本中的 **计算 CT 和 CQ** 复选框。

## 描述

计算空气动力力和力矩

Multirotor 模块可计算多个旋转螺旋桨或旋翼（例如四旋翼）在三个维度上产生的空气动力力和力矩。您还可以包括简化的挥舞（或稳态）空气动力学。
