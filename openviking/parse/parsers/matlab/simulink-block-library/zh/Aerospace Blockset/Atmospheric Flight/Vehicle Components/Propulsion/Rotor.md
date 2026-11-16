---
type: simulink-block
title: 'Rotor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Vehicle Components / Propulsion'
documentation_page: 'rotor'
documentation_source_path: 'rotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotor

## 端口

### 输入

### **Ω (rad/sec)** — 转子速度标量

转子速度，指定为机体坐标系中的标量，单位为 rad/sec。

**数据类型：** `double`

### **ρ** — 空气密度 positive scalar

空气密度，指定为按指定单位表示的 positive scalar。

**数据类型：** `double`

### **Vb** — 机体速度 3×1 向量 | 1×3 向量

转子速度，指定为机体坐标系中的 3×1 或 1×3 向量。要进行多系统分析，可考虑将 State-Space 或 Integrator 模块的输出连接到此端口。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

速度单位取决于 `Units` 参数的值。

**数据类型：** `double`

### **ωb** — 角速度 3×1 向量 | 1×3 向量

整个飞行器的角速度，指定为机体坐标系中的 3×1 或 1×3 向量，单位为 rad/s。

#### 依赖关系

要启用此输入，请将 `Modeling` 设置为 `With flap effects`。

**数据类型：** `double`

### **θ0** — 总距桨叶桨距角标量

总距桨叶桨距角，指定为弧度标量。

#### 依赖关系

要启用此输入端口，请选中 **Include pitch angle inputs** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **θc** — 横向周期变距桨距角标量

横向周期变距桨距角，指定为弧度标量。

#### 依赖关系

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **θs** — 纵向周期变距桨距角标量

纵向周期变距桨距角，指定为弧度标量。

#### 依赖关系

要启用此输入端口，

- 选中 **Include pitch angle inputs** 复选框。
- 将 **Modeling** 设置为 `With flap effects`。

**数据类型：** `double`

### **CT** — 输入推力系数 nonzero positive scalar

输入推力系数，指定为 nonzero positive scalar。

#### 依赖关系

要启用此输入端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### **CQ** — 输入扭矩系数 nonzero positive scalar

输入扭矩系数，指定为 nonzero positive scalar。

#### 依赖关系

要启用此输出端口，请将 **CT and CQ Source** 下拉菜单设置为 `'Ports'`。

**数据类型：** `double`

### 输出

### **Fxyz(N)** — 总力三元素向量

总力，返回为机体坐标系中的三元素向量。单位取决于 **Units** 参数。

**数据类型：** `double`

### **Mxyz(Nm)** — 净力矩三元素向量

*x*-*y*-*z* 方向上的净力矩，返回为机体坐标系中的三元素向量。单位取决于 **Units** 参数。

**数据类型：** `double`

### **CT** — 计算的推力系数 positive scalar

计算的推力系数，返回为 positive scalar。

#### 依赖关系

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

### **CQ** — 计算的扭矩系数 positive scalar

计算的扭矩系数，返回为 positive scalar。

#### 依赖关系

要启用此输出端口，请选中 **Output computed CT and CQ** 复选框，并将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`。

**数据类型：** `double`

## 参数

#### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

| 单位 | 速度 | 密度 | 力 | 力矩 | 半径 | 弦长 | 铰链偏移 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters per second | kg/m3 | Newtons | Newton-meter | Meters | Meters | Meters |
| `English (Velocity in ft/s)` | Feet per second | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet |
| `English (Velocity in kts)` | Knots | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **取值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Modeling** — 转子推力计算方法 `Without flap effects`（默认） | `With flap effects`

转子推力计算方法，指定为：

- `Without flap effects` — 使用力和力矩计算来模拟转子推力。有关详细信息，请参阅 Force and Moment。
- `With flap effects` — 包含前飞时由于挥舞运动引起的旋翼桨盘倾斜效应。稳态横向和纵向挥舞角使用 [1] 中的方程计算，并用于力和力矩的计算 [2]。有关详细信息，请参阅 Force and Moment。

#### 编程用法

|  |
| --- |
| **模块参数**：`modelMode` |
| **类型**：character vector |
| **取值**：`'Without flap effects'` | `'With flap effects'` |
| **默认值**：`'Without flap effects'` |

### **Include pitch angle inputs** — 启用桨距角输入 `off`（默认） | `on`

选中此复选框以启用桨距角（斜盘）输入端口。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`controlInput` |
| **类型**：character vector |
| **取值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### 转子

### **CT and CQ Source** — 用于选择推力系数和扭矩系数值来源的下拉菜单 `'Dialog'`（默认） | `'Compute using BEMT'` | `'Ports'`

选择推力系数和扭矩系数值的来源，指定为值 `'Dialog'`、`'Compute using BEMT'` 或 `'Ports'` 的字符向量。该模块假定气动和结构参数为常量。

- 选择 `'Dialog'` 以手动输入推力系数和扭矩系数值。
- 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。
- 选择 `'Ports'` 以接受推力系数和扭矩系数值作为输入。

#### 编程用法

|  |
| --- |
| **模块参数**：`CTCQMode` |
| **类型**：character vector |
| **取值**：`'Dialog'` | `'Compute using BEMT'` |
| **默认值**：`'Dialog'` |

### **Thrust coefficient (CT)** — 推力系数 `0.0107`（默认） | nonzero positive scalar

推力系数，指定为 nonzero positive scalar。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 编程用法

|  |
| --- |
| **模块参数**：`CT` |
| **类型**：character vector |
| **取值**：`'0.0107'` | nonzero positive scalar |
| **默认值**：`'0.0107'` |

### **Torque coefficient (CQ)** — 扭矩系数 `7.8263e-4`（默认） | nonzero positive scalar

扭矩系数，指定为 nonzero positive scalar。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Dialog'`。

#### 编程用法

|  |
| --- |
| **模块参数**：`CQ` |
| **类型**：character vector |
| **取值**：`'7.8263e-4'` | nonzero positive scalar |
| **默认值**：`'7.8263e-4'` |

### **Number of blades** — 每个转子的桨叶数量 `2`（默认） | nonzero positive scalar

桨叶数量，指定为 nonzero positive scalar。

#### 依赖关系

要启用此参数，

- 将 **CT and CQ Source** 下拉菜单设置为 `Compute using BEMT`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`Nb` |
| **类型**：character vector |
| **取值**：`'2'` | nonzero positive scalar |
| **默认值**：`'2'` |

### **Output computed CT and CQ** — 输出计算的推力系数和扭矩系数 off（默认） | on

选中此复选框以将计算的推力系数和扭矩系数输出到 **CT** 和 **CQ** 输出端口。有关这些计算的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。该模块假定气动和结构参数为常量。

否则，清除此复选框。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 编程用法

|  |
| --- |
| **模块参数**：`CTout` |
| **类型**：character vector |
| **取值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

#### 桨叶

### **Radius (m)** — 转子半径 `0.0330`（默认） | nonzero positive scalar

转子半径，指定为 nonzero positive scalar。

#### 编程用法

|  |
| --- |
| **模块参数**：`radius` |
| **类型**：character vector |
| **取值**：`'0.0330'` | nonzero positive scalar |
| **默认值**：`'0.0330'` |

### **Chord (m)** — 桨叶弦长 `0.0080`（默认） | nonzero positive scalar

桨叶弦长，指定为 nonzero positive scalar。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`chord` |
| **类型**：character vector |
| **取值**：`'0.0080'` | nonzero positive scalar |
| **默认值**：`'0.0080'` |

### **Hinge offset (m)** — 铰链偏移 `0`（默认） | positive scalar

铰链偏移，指定为 positive scalar。对于螺旋桨，该值通常为 `0`。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`hingeOffset` |
| **类型**：character vector |
| **取值**：`'0'` | positive scalar |
| **默认值**：`'0'` |

### **Lift curve slope (per rad)** — 升力曲线斜率 `5.5`（默认） | nonzero positive scalar

升力曲线斜率，指定为 nonzero positive scalar。该模块假定气动和结构参数为常量。该模块不考虑随迎角的变化。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`clalpha` |
| **类型**：character vector |
| **取值**：`'5.5'` | nonzero positive scalar |
| **默认值**：`'5.5'` |

### **Mean drag coefficient** — 平均阻力系数 0（默认） | positive scalar

平均阻力系数，指定为 positive scalar。该模块不考虑随迎角的变化。

#### 依赖关系

要启用此参数，请将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

#### 编程用法

|  |
| --- |
| **模块参数**：`cd0` |
| **类型**：character vector |
| **取值**：`'0'` | positive scalar |
| **默认值**：`'0'` |

### **Lock number** — 洛克数 `0.6051`（默认） | nonzero positive scalar

洛克数，即气动力与惯性力之比，指定为 nonzero positive scalar。

#### 依赖关系

要启用此参数，请将 **Modeling** 设置为 `With flap effects`。

#### 编程用法

|  |
| --- |
| **模块参数**：`gamma` |
| **类型**：character vector |
| **取值**：`'0.6051'` | nonzero positive scalar |
| **默认值**：`'0.6051'` |

### **Twist distribution** — 转子桨叶扭转分布 `Linear`（默认） | `Ideal`

转子桨叶扭转分布，指定为：

- `Linear` — 桨叶扭转分布的近似。

  θ(r)=θroot+θtwistr
- `Ideal` — 桨叶扭转分布的最佳近似。

  θ(r)=θtipr

其中 *r* 是沿桨叶的无量纲径向位置。

#### 依赖关系

要启用此复选框，

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

#### 编程用法

|  |
| --- |
| **模块参数**：`twistType` |
| **类型**：character vector |
| **取值**：`'Linear'` | `'Ideal'` |
| **默认值**：`'Linear'` |

### **Blade root angle (rad)** — 桨叶根部桨距角 `0.2548`（默认） | real scalar

桨叶根部桨距角 θroot，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 编程用法

|  |
| --- |
| **模块参数**：`thetaRoot` |
| **类型**：real scalar |
| **取值**：`'0.2548'` | nonzero positive scalar |
| **默认值**：`'0.2548'` |

### **Blade twist angle (rad)** — 桨叶扭转角 `-0.1361`（默认） | real scalar

桨叶扭转角 θtwist，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Linear`。

#### 编程用法

|  |
| --- |
| **模块参数**：`thetaTwist` |
| **类型**：real scalar |
| **取值**：`'0.1018'` | positive scalar |
| **默认值**：`'0.1018'` |

### **Blade tip angle (rad)** — 桨叶尖部桨距角 `0.1018`（默认） | real scalar

理想扭转分布的桨叶尖部桨距角 θtip，指定为 real scalar。

#### 依赖关系

要启用此参数：

- 将 **CT and CQ Source** 下拉菜单设置为 `'Compute using BEMT'`。

和/或

- 将 **Modeling** 设置为 `'With flap effects'`

- 将 **Twist distribution** 设置为 `Ideal`。

#### 编程用法

|  |
| --- |
| **模块参数**：`thetaTip` |
| **类型**：real scalar |
| **取值**：`'0.06'` | nonzero positive scalar |
| **默认值**：`'0.06'` |

## 所属库

Aerospace Blockset / Propulsion

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2025a：Rotor 模块现在包含推力系数和扭矩系数作为输入

从 R2025a 开始，当您将 **CT and CQ Source** 下拉菜单设置为 `'Ports'` 时，可以将 `CT` 和 `CQ` 作为 Rotor 模块的可选输入端口包含在内。

### R2024b：Rotor 模块现在包含斜盘作为输入

- 从 R2024b 开始，Rotor 模块已更新以支持斜盘输入。此新增功能允许通过新的可选输入端口在力和力矩计算中包含总距和周期变距桨叶桨距角。
- 转子速度 Ω 现在也接受负输入。
- 从 R2024b 开始，Rotor 模块已更新为包含下拉菜单 **CT and CQ Source**，其中有两个选项：`'Dialog'` 和 `'Compute using BEMT'`。

  - 选择 `'Dialog'` 以手动输入推力系数和扭矩系数值。
  - 选择 `'Compute using BEMT'` 以使用叶素动量理论 (BEMT) 计算这些值。有关 BEMT 的详细信息，请参阅 Thrust Coefficient and Torque Coefficient Calculations。此选项等效于之前版本中的 **Compute CT and CQ** 复选框。

## 描述

计算气动力和力矩

Rotor 模块计算旋转螺旋桨或旋翼在所有三个维度上产生的气动力和力矩。该模块允许您包含前飞时由于挥舞运动引起的旋翼桨盘倾斜对所产生的力和力矩的影响。Rotor 模块考虑通过旋翼桨盘的轴向流以及横向流的影响，这是旋翼飞行器系统分析所需的。
