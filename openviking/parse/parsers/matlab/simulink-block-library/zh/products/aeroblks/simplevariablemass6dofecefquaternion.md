---
type: simulink-block
title: 'Simple Variable Mass 6DOF ECEF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'simplevariablemass6dofecefquaternion'
documentation_source_path: 'simplevariablemass6dofecefquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Variable Mass 6DOF ECEF (Quaternion)

## 端口

### 输入

### **Fxyz** — 施加力三元素向量

施加力，指定为三元素向量，采用 **Units** 中选择的单位。

**数据类型：** `double`

### **Mxyz** — 施加力矩三元素向量

施加力矩，指定为三元素向量，采用 **Units** 中选择的单位。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（吸积为正，烧蚀为负），指定为标量

**数据类型：** `double`

### **LG(0)** — Greenwich 初始天球经度标量

Greenwich 子午线初始天球经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **Celestial longitude of Greenwich** 设置为 `External`。
- 将 **Planet model** 设置为 `Earth`。

**数据类型：** `double`

### **LPM(0)** — 本初子午线初始天球经度角标量

本初子午线初始天球经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **Celestial longitude of prime meridian** 设置为 `External`。
- 将 **Planet model** 设置为 `Custom`。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，质量以该速度沿体固联轴吸积到机体或从机体烧蚀，指定为三元素向量。

#### 依赖关系

要启用此端口，选择 **Include mass flow relative velocity**。

**数据类型：** `double`

### 输出

### **Vff** — 机体相对于 ECEF 坐标系的速度，三元素向量

机体相对于 ECEF 坐标系的速度，以 ECEF 坐标系表示，返回为三元素向量。

**数据类型：** `double`

### **Xff** — ECEF 参考坐标系中的位置三元素向量

ECEF 参考坐标系中的位置，返回为三元素向量。

**数据类型：** `double`

### **μ l h** — 大地纬度、经度和高度中的位置三元素向量 | M-by-3 数组

以度为单位的大地纬度、经度和高度中的位置，分别以所选长度单位返回为三元素向量或 M-by-3 数组。

**数据类型：** `double`

### **φ θ Ψ (rad)** — 机体旋转角三元素向量

机体旋转角 [roll, pitch, yaw]，返回为三元素向量，单位为弧度。Euler 旋转角是机体坐标系与 NED 坐标系之间的角度。

**数据类型：** `double`

### **DCMbi** — 从 ECI 轴到机体系的坐标变换 3×3 矩阵

从 ECI 轴到体固联轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **DCMbe** — 从 NED 轴到体固联轴的坐标变换 3×3 矩阵

从 NED 轴到体固联轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **DCMef** — 从固定坐标系轴的坐标变换 3×3 矩阵

从固定坐标系轴到 NED 轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 机体相对于固定坐标系的速度三元素向量

机体相对于固定坐标系的速度，返回为三元素向量。

**数据类型：** `double`

### **ωrel** — 机体相对于 NED 坐标系的相对角速率三元素向量

机体相对于 NED 坐标系的相对角速率，以机体坐标系表示并返回为三元素向量，单位为弧度每秒。

**数据类型：** `double`

### **ωb** — 机体相对于惯性坐标系的角速率三元素向量

机体相对于惯性坐标系的角速率，以机体坐标系表示并返回为三元素向量，单位为弧度每秒。

**数据类型：** `double`

### **dωb/dt** — 机体相对于惯性坐标系的角加速度三元素向量

机体相对于惯性坐标系的角加速度，以机体坐标系表示并返回为三元素向量，单位为弧度每二次方秒。

**数据类型：** `double`

### **Abb** — 体固联轴中的加速度三元素向量

机体相对于体固联轴的加速度，采用体固联坐标系，返回为三元素向量，采用 **Units** 中选择的单位。

**数据类型：** `double`

### **Fuel** — 燃料箱状态标量

燃料箱状态，返回为：

- `1` — 箱已满。
- `0` — 箱既未满也未空。
- `-1` — 箱为空。

**数据类型：** `double`

### **Ab ff** — 体固联轴中的加速度三元素向量

相对于固定坐标系的体固联轴中的加速度，返回为三元素向量。

#### 依赖关系

要启用此点，选择 **Include inertial acceleration**。

**数据类型：** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 程序化使用

|  |
| --- |
| **模块参数：** `units` |
| **类型：** 字符向量 |
| **取值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Simple Variable`（默认） | `Fixed` | `Custom Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 质量在整个仿真过程中保持不变（参见 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯性变化可自定义（参见 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Simple Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** 字符向量 |
| **取值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认值：** `'Simple Variable'` |

### **Initial position in geodetic latitude, longitude and altitude [mu,l,h]** — 刚体的初始位置 `[0 0 0]`（默认） | 三元素向量

刚体在大地参考坐标系中的初始位置，指定为三元素向量。纬度和经度值可为任意值。但是，由于极点处的奇异性，纬度值 +90 和 -90 可能返回意外值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xg_0` |
| **类型：** 字符向量 |
| **取值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial velocity in body axes [U,v,w]** — 机体轴中的速度 `[0 0 0]`（默认） | 三元素向量

机体相对于 ECEF 坐标系的初始速度，以机体坐标系表示，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** 字符向量 |
| **取值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial Euler orientation [roll, pitch, yaw]** — 初始 Euler 姿态 `[0 0 0]`（默认） | 三元素向量

初始 Euler 姿态角 [roll, pitch, yaw]，指定为三元素向量，单位为弧度。Euler 旋转角是机体坐标系与 north-east-down (NED) 坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** 字符向量 |
| **取值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始机体旋转 `[0 0 0]`（默认） | 三元素向量

相对于 NED 坐标系的初始体固联角速率，指定为三元素向量，单位为弧度每秒。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** 字符向量 |
| **取值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial mass** — 初始质量 `1.0`（默认） | 标量

刚体的初始质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** 字符向量 |
| **取值：** `'1.0'` | double 标量 |
| **默认值：** `'1.0'` |

### **Empty mass** — 空质量 `0.5`（默认） | 标量

机体的空质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_e` |
| **类型：** 字符向量 |
| **取值：** double 标量 |
| **默认值：** `'0.5'` |

### **Full mass** — 机体满载质量 `2.0`（默认） | 标量

机体的满载质量，指定为 double 标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_f` |
| **类型：** 字符向量 |
| **取值：** double 标量 |
| **默认值：** `'2.0'` |

### **Inertia** — 惯性 `eye(3)`（默认） | 标量

机体的惯性，指定为 double 标量。

#### 依赖关系

要启用此参数，将 **Mass type** 设置为 `Fixed`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** 字符向量 |
| **取值：** `eye(3)` | double 标量 |
| **默认值：** `eye(3)` |

### **Empty inertia** — 空惯性矩阵 `eye(3)`（默认） | 3×3 矩阵

机体空惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_e` |
| **类型：** 字符向量 |
| **取值：** `'eye(3)'` | 3×3 矩阵 |
| **默认值：** `'eye(3)'` |

### **Full inertia** — 机体满载惯性 `2*eye(3)`（默认） | 3×3 矩阵

机体满载惯性的惯性张量矩阵，指定为 3×3 矩阵。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inertia_f` |
| **类型：** 字符向量 |
| **取值：** `'2*eye(3)'` | 3×3 矩阵 |
| **默认值：** `'2*eye(3)'` |

### **Include mass flow relative velocity** — 质量流相对速度端口 `off`（默认） | `on`

选中此复选框以添加质量流相对速度端口。这是质量被吸积或烧蚀时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** 字符向量 |
| **取值：** `off` | `on` |
| **默认值：** `off` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off`（默认） | `on`

选中此复选框以添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** 字符向量 |
| **取值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 行星

### **Planet model** — 行星模型 `Earth (WGS84)`（默认） | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：字符向量 |
| **取值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **Equatorial radius** — 赤道处行星半径 `6378137`（默认） | 标量

行星赤道处的半径，指定为 double 标量，单位与 ECEF 位置所需单位相同。

#### 依赖关系

要启用此参数，将 **Planet model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`R` |
| **类型**：字符向量 |
| **取值**：double 标量 |
| **默认值**：`'6378137'` |

### **Flattening** — 行星扁率 `1/298.257223563`（默认） | 标量

行星的扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，将 **Planet model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`F` |
| **类型**：字符向量 |
| **取值**：double 标量 |
| **默认值**：`'1/298.257223563'` |

### **Rotational rate** — 旋转速率 `7292115e-11`（默认） | 标量

行星的旋转速率，指定为标量，单位为 rad/s。

#### 依赖关系

要启用此参数，将 **Planet model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`w_E` |
| **类型**：字符向量 |
| **取值**：double 标量 |
| **默认值**：`'7292115e-11'` |

### **Celestial longitude of Greenwich source** — Greenwich 子午线初始天球经度的来源 `Internal`（默认） | `External`

Greenwich 子午线初始天球经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Celestial longitude of Greenwich** 中的天球经度值。 |
| `External` | 对天球经度值使用外部输入。 |

#### 依赖关系

- 要启用此参数，将 **Planet model** 设置为 `Earth`。
- 将此参数设置为 `External` 会启用 **LG(0)** 端口。
- 如果 **Planet model** 设置为 `Custom`，参数名变为 **Celestial longitude of prime meridian source**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`angle_in` |
| **类型**：字符向量 |
| **取值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Celestial longitude of Greenwich [deg]** — 初始角 `0`（默认） | 标量

Greenwich 子午线与惯性坐标系的 *x* 轴之间的初始角，指定为 double 标量。

#### 依赖关系

- 要启用此参数，设置：

  - **Celestial longitude of Greenwich source** 为 `Internal`。
  - **Planet model** 为 `Earth (WGS84)`。
- 如果 **Planet model** 设置为 `Custom`，参数名变为 **Celestial longitude of prime meridian [deg]**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LPM0` |
| **类型**：字符向量 |
| **取值**：double 标量 |
| **默认值**：`'0'` |

### **Celestial longitude of prime meridian source** — 本初子午线初始天球经度的来源 `Internal`（默认） | `External`

本初子午线初始天球经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Celestial longitude of prime meridian** 中的天球经度值。 |
| `External` | 对天球经度值使用外部输入。 |

#### 依赖关系

- 要启用此参数，将 **Planet model** 设置为 `Custom`。
- 将此参数设置为 `External` 会启用 **LPM(0)** 端口。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名变为 **Celestial longitude of Greenwich source**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`angle_in` |
| **类型**：字符向量 |
| **取值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Celestial longitude of prime meridian [deg]** — 初始角 `0`（默认） | 标量

本初子午线与 ECI 坐标系的 *x* 轴之间的初始角，指定为 double 标量。

#### 依赖关系

- 要启用此参数，设置：

  - **Celestial longitude of prime meridian source** 为 `Internal`。
  - **Planet model** 为 `Custom`。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名变为 **Celestial longitude of Greenwich [deg]**。

#### 程序化使用

|  |
| --- |
| **模块参数**：`LPM0` |
| **类型**：字符向量 |
| **取值**：double 标量 |
| **默认值**：`'0'` |

### 状态属性

为每个状态分配唯一名称。在线性化期间，可以使用状态名称代替模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入由花括号包围的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅适用于使用 name 参数的所选模块。
- 状态数必须能被状态名称数整除。
- 可以指定的名称数少于状态数，但不能指定多于状态数的名称。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、元胞数组或结构体。

### **Quaternion vector: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''`（默认） | 由花括号包围的逗号分隔列表

四元数向量状态名称，指定为由花括号包围的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 由花括号包围的逗号分隔列表 |
| **默认值：** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 机体旋转状态名称 `''`（默认） | 由花括号包围的逗号分隔列表

机体旋转速率状态名称，指定为由花括号包围的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 由花括号包围的逗号分隔列表 |
| **默认值：** `''` |

### **Velocity: e.g., {'U','v','w'}** — 速度状态名称 `''`（默认） | 由花括号包围的逗号分隔列表

速度状态名称，指定为由花括号包围的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 由花括号包围的逗号分隔列表 |
| **默认值：** `''` |

### **Fixed frame position: e.g., {'Xff', 'Yff', 'Zff'}** — ECEF 位置状态名称 `''`（默认） | 由花括号包围的逗号分隔列表

ECEF 位置状态名称，指定为由花括号包围的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `posfixedframe_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 由花括号包围的逗号分隔列表 |
| **默认值：** `''` |

### **Inertial position: e.g., {'Xinertial', 'Yinertial', 'Zinertial'}** — 惯性位置状态名称 `''`（默认） | 由花括号包围的逗号分隔列表

惯性位置状态名称，指定为由花括号包围的逗号分隔列表。

默认值为 `''`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `posinertial_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 由花括号包围的逗号分隔列表 |
| **默认值：** `''` |

### **Celestial longitude of Greenwich: e.g., 'LG'** — 天球经度状态名称 `''`（默认） | 字符向量

Greenwich 天球经度状态名称，指定为字符向量。

#### 依赖关系

- 要启用此参数，设置：**Planet model** 为 `Earth (WGS84)`。
- 如果 **Planet model** 设置为 `Custom`，参数名变为 **Celestial longitude of prime meridian: e.g., 'LPM'**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LPM_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 标量 |
| **默认值：** `''` |

### **Celestial longitude of prime meridian: e.g., 'LPM'** — 本初子午线天球经度 `''`（默认） | 字符向量

本初子午线天球经度状态名称，指定为字符向量。

#### 依赖关系

- 要启用此参数，设置：**Planet model** 为 `Custom`。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名变为 **Celestial longitude of Greenwich: e.g., 'LG'**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LPM_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 标量 |
| **默认值：** `''` |

### **Mass: e.g., 'mass'** — 质量状态名称 `''`（默认） | 字符向量

质量状态名称，指定为字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mass_statename` |
| **类型：** 字符向量 |
| **取值：** `''` | 字符向量 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2023b：Simple Variable Mass 6DOF ECEF (Quaternion) 模块坐标系更改

这些更新更好地阐明了当 **Central body** 为 `Custom` 时，Simple Variable Mass 6DOF ECEF (Quaternion) 模块的坐标系：

- 新的模块图标。

  Simple Variable Mass 6DOF ECEF (Quaternion) 模块
- 端口名下标 `ecef` 已更改为 `ff`。
- **Celestial longitude of Greenwich source** 的 programmatic 名称已从 `LG0` 更改为 `LPM`。现有脚本继续有效。
- 更新了模块参数名，但先前版本的模型继续有效。

  | 旧参数名或设置 | 新参数名 |
  | --- | --- |
  | **ECEF position**... | **Fixed frame position**... |
  | 当 **Planet model** 为 `Earth` | **Celestial longitude of Greenwich source** 和 **Celestial longitude of Greenwich [deg]** |
  | 当 **Planet model** 为 `Custom` | **Celestial longitude of prime meridian source** 和 **Celestial longitude of prime meridian [deg]** |

## 描述

实现简单变质量在 Earth-centered Earth-fixed (ECEF) 坐标中的六自由度运动方程的四元数表示

Simple Variable Mass 6DOF ECEF (Quaternion) 模块实现简单变质量在 Earth-centered Earth-fixed (ECEF) 坐标中的六自由度运动方程的四元数表示。它考虑 Earth-centered Earth-fixed (ECEF) 坐标系（*XECEF, YECEF, ZECEF*）绕 Earth-centered inertial (ECI) 参考坐标系（*XECI, YECI, ZECI*）的旋转。ECEF 坐标系的原点是地球中心。有关 ECEF 坐标系的更多信息，参见 Algorithms。

Aerospace Blockset™ 使用按标量优先约定定义的四元数。
