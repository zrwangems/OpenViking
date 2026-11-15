---
type: simulink-block
title: 'Simple Variable Mass 6DOF Wind (Wind Angles)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofwindwindangles'
documentation_source_path: 'simplevariablemass6dofwindwindangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 6DOF Wind (Wind Angles)

## 端口

### 输入

### **Fxyz(N)** — 施加力 three-element vector

施加的力，指定为 three-element vector。

**数据类型：** `double`

### **Mxyz(N-m)** — 施加力矩 three-element vector

施加的力矩，指定为 three-element vector。

**数据类型：** `double`

### **dm/dt (kg/s)** — 质量变化率 scalar

一个或多个质量变化率（如果质量积聚则为正，如果质量消融则为负），指定为 scalar。

**数据类型：** `double`

### **Vre** — 相对速度 three-element vector

一个或多个相对速度，指定为 three-element vector，表示在体轴系中质量附着到机体或从机体消融时的速度。

#### 依赖关系

要启用此端口，请选择 **包含质量流相对速度**。

**数据类型：** `double`

### 输出

### **Ve** — 平地参考系中的速度 three-element vector

平地参考系中的速度，以 three-element vector 形式返回。

**数据类型：** `double`

### **Xe** — 平地参考系中的位置 three-element vector

平地参考系中的位置，以 three-element vector 形式返回。

**数据类型：** `double`

### **μ γ x (rad)** — 风旋转角 three-element vector

风旋转角 [滚转, 航迹, 航向]，以 three-element vector 形式返回，单位为 radians。

**数据类型：** `double`

### **DCMwe** — 坐标变换 3-by-3 matrix

从平地轴系到风固连轴系的坐标变换，以 3-by-3 matrix 形式返回。

**数据类型：** `double`

### **Vw** — 风固连坐标系中的速度 three-element vector

风固连坐标系中的速度，以 three-element vector 形式返回。

**数据类型：** `double`

### **α β (rad)** — 迎角和侧滑角 two-element vector

迎角和侧滑角，以 two-element vector 形式返回，单位为 radians。

**数据类型：** `double`

### **dα/dt dβ/dt** — 迎角变化率和侧滑角变化率 two-element vector

迎角变化率和侧滑角变化率，以 two-element vector 形式返回，单位为 radians per second。

**数据类型：** `double`

### **ωb (rad/s)** — 体轴系中的角速率 three-element vector

体轴系中的角速率，以 three-element vector 形式返回。

**数据类型：** `double`

### **dωb/dt** — 体轴系中的角加速度 three-element vector

体轴系中的角加速度，以 three-element vector 形式返回，单位为 radians per second squared。

**数据类型：** `double`

### **Abb** — 体轴系中的加速度 three-element vector

相对于体坐标系的体轴系中的加速度，以 three-element vector 形式返回。

**数据类型：** `double`

### **Fuel** — 燃料箱状态 scalar

燃料箱状态，返回为：

- `1` — 燃料箱已满。
- `0` — 燃料箱既未满也未空。
- `-1` — 燃料箱为空。

**数据类型：** `double`

### **Abe** — 相对于惯性系的加速度 three-element vector

相对于惯性系（平地）的体轴系加速度，以 three-element vector 形式返回。通常将此信号连接到加速度计。

#### 依赖关系

仅当选中 **包含惯性加速度** 复选框时，此端口才会出现。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 编程使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **质量类型** — 质量类型 `Simple Variable` (默认) | `Fixed` | `Custom Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 在整个仿真过程中质量恒定（请参阅 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯性变化可自定义（请参阅 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Simple Variable` 选择符合前面描述的运动方程。

#### 编程使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认值：** `'Simple Variable'` |

### **表示形式** — 运动方程表示形式 `Wind Angles` (默认) | `Quaternion`

运动方程表示形式，根据下表指定。

| 表示形式 | 描述 |
| --- | --- |
| `Wind Angles` | 在运动方程中使用风角。 |
| `Quaternion` | 在运动方程中使用四元数。 |

`Quaternion` 选择符合算法中的运动方程。

#### 编程使用

|  |
| --- |
| **模块参数：** `rep` |
| **类型：** character vector |
| **值：** `Wind Angles` | `Quaternion` |
| **默认值：** `'Wind Angles'` |

### **惯性轴中的初始位置 [Xe,Ye,Ze]** — 惯性轴中的位置 `[0 0 0]` (默认) | three-element vector

机体在平地参考系中的初始位置，指定为 three-element vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `xme_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始空速、迎角和侧滑角 [V,alpha,beta]** — 初始空速、迎角和侧滑角 `[0 0 0]` (默认) | three-element vector

初始空速、迎角和侧滑角，指定为 three-element vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始风姿态 [滚转角,航迹角,航向角]** — 初始风姿态 `[0 0 0]` (默认) | three-element vector

初始风角 [滚转、航迹和航向]，指定为 three-element vector，单位为 radians。

#### 编程使用

|  |
| --- |
| **模块参数：** `wind_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始体旋转速率 [p,q,r]** — 初始体旋转 `[0 0 0]` (默认) | three-element vector

相对于 NED 坐标系的初始体轴系角速率，指定为 three-element vector，单位为 radians per second。

#### 编程使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | three-element vector |
| **默认值：** `'[0 0 0]'` |

### **初始质量** — 初始质量 `1.0` (默认) | scalar

刚体的初始质量，指定为 double scalar。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double scalar |
| **默认值：** `'1.0'` |

### **空载质量** — 空载质量 `0.5` (默认) | scalar

机体的空载质量，指定为 double scalar。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** character vector |
| **值：** double scalar |
| **默认值：** `'0.5'` |

### **满载质量** — 机体满载质量 `2.0` (默认) | scalar

机体的满载质量，指定为 double scalar。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** character vector |
| **值：** double scalar |
| **默认值：** `'2.0'` |

### **体轴中的空载惯性矩阵** — 空载惯性的惯性张量矩阵 `eye(3)` (默认) | 3-by-3 matrix

机体空载惯性的惯性张量矩阵，指定为 3-by-3 matrix，位于体轴系中。

#### 编程使用

|  |
| --- |
| **模块参数：** `inertia_e` |
| **类型：** character vector |
| **值：** `'eye(3)'` | 3-by-3 matrix |
| **默认值：** `'eye(3)'` |

### **体轴中的满载惯性矩阵** — 满载惯性的惯性张量矩阵 `2*eye(3)` (默认) | 3-by-3 matrix

机体满载惯性的惯性张量矩阵，指定为 3-by-3 matrix，位于体轴系中。

#### 编程使用

|  |
| --- |
| **模块参数：** `inertia_f` |
| **类型：** character vector |
| **值：** `'2*eye(3)'` | 3-by-3 matrix |
| **默认值：** `'2*eye(3)'` |

### **包含质量流相对速度** — 质量流相对速度端口 `off` (默认) | `on`

选中此复选框可添加质量流相对速度端口。这是质量积聚或消融时的相对速度。

#### 编程使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `off` |

### **包含惯性加速度** — 包含惯性加速度端口 `off` (默认) | `on`

选中此复选框可添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，请选择此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用大括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅应用于具有该名称参数的选定模块。
- 状态数必须能被状态名称数整除。
- 指定的名称数可以少于状态数，但不能多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **位置：例如，{'Xe','Ye','Ze'}** — 位置状态名称 `''` (默认) | comma-separated list surrounded by braces

位置状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `xme_statename` |
| **类型：** character vector |
| **值：** `''` | comma-separated list surrounded by braces |
| **默认值：** `''` |

### **速度：例如，'V'** — 速度状态名称 `''` (默认) | character vector

速度状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | character vector |
| **默认值：** `''` |

### **迎角 例如，'alpha'** — 迎角状态名称 `''` (默认) | character vector

迎角状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `alpha_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **侧滑角 例如，'beta'** — 侧滑角状态名称 `''` (默认) | character vector

侧滑角状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `beta_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **风姿态 例如，{'mu', 'gamma', 'chi'}** — 风姿态状态名称 `''` (默认) | comma-separated list surrounded by braces

风姿态状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `wind_statename` |
| **类型：** character vector |
| **值：** `''` |
| **默认值：** `''` |

### **体旋转速率：例如，{'p','q','r'}** — 体旋转状态名称 `''` (默认) | comma-separated list surrounded by braces

体旋转速率状态名称，指定为用大括号括起来的逗号分隔列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | comma-separated list surrounded by braces |
| **默认值：** `''` |

### **质量：例如，'mass'** — 质量状态名称 `''` (默认) | character vector

质量状态名称，指定为 character vector。

#### 编程使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** character vector |
| **值：** `''` | character vector |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 中引入**

## 描述

实现简单变质量六自由度运动方程的风角表示

Simple Variable Mass 6DOF Wind (Wind Angles) 模块实现简单变质量六自由度运动方程的风角表示。有关风角之间关系的更多信息，请参阅算法。有关所用坐标系和平移动力学的描述，请参阅 Simple Variable Mass 6DOF (Quaternion) 模块的模块描述。
