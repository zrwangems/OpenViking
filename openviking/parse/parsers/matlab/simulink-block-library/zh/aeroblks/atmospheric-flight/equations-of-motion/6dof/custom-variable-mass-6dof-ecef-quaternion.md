---
type: simulink-block
title: 'Custom Variable Mass 6DOF ECEF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: 'customvariablemass6dofecefquaternion'
documentation_source_path: 'customvariablemass6dofecefquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Variable Mass 6DOF ECEF (Quaternion)

## 端口

### 输入

### **Fxyz** — 施加力三元素向量

施加力，指定为体轴中的三元素向量。

**数据类型：** `double`

### **Mxyz** — 施加力矩三元素向量

施加力矩，指定为体轴中的三元素向量。

**数据类型：** `double`

### **dm/dt** — 质量变化率标量

一个或多个质量变化率（如果增加则为正，如果减少则为负），指定为标量

**数据类型：** `double`

### **m** — 质量标量

质量，指定为标量。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Custom
Variable`。

**数据类型：** `double`

### **dI/dt** — 惯性张量矩阵变化率 3×3 矩阵

惯性张量矩阵变化率，指定为 3×3 矩阵，单位在 **单位** 中选择。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Custom
Variable`。

**数据类型：** `double`

### **I** — 惯性张量矩阵 3×3 矩阵

惯性张量矩阵，指定为 3×3 矩阵。

#### 依赖关系

要启用此端口，请将 **质量类型** 设置为 `Custom
Variable`。

**数据类型：** `double`

### **LG(0)** — Greenwich 初始天球经度标量

Greenwich 子午线初始天球经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **Greenwich 天球经度** 设置为
  `External`。
- 将 **行星模型** 设置为
  `Earth`。

**数据类型：** `double`

### **LPM(0)** — 本初子午线初始天球经度角标量

本初子午线初始天球经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **本初子午线天球经度** 设置为
  `External`。
- 将 **行星模型** 设置为
  `Custom`。

**数据类型：** `double`

### **Vre** — 相对速度三元素向量

一个或多个相对速度，质量以该速度在机体固连轴中增加至或减少自机体，指定为三元素向量。

#### 依赖关系

要启用此端口，请选择 **包含质量流相对速度**。

**数据类型：** `double`
### 输出

### **Vff** — 机体相对于 ECEF 坐标系的速度，三元素向量

机体相对于 ECEF 坐标系的速度，在 ECEF 坐标系中表示，返回为三元素向量。

**数据类型：** `double`

### **Xff** — ECEF 参考坐标系中的位置三元素向量

ECEF 参考坐标系中的位置，返回为三元素向量。

**数据类型：** `double`

### **μ l h** — 大地纬度、经度和高度中的位置三元素向量 | M×3 数组

大地纬度、经度和高度中的位置，纬度和经度以度为单位，返回为三元素向量或 M×3 数组，高度以所选长度单位表示。

**数据类型：** `double`

### **φ θ Ψ (rad)** — 机体旋转角三元素向量

机体旋转角 [roll, pitch, yaw]，返回为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与 NED 坐标系之间的角度。

**数据类型：** `double`

### **DCMbi** — 从 ECI 轴的坐标变换 3×3 矩阵

从 ECI 轴到机体固连轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **DCMbe** — 从 NED 轴到机体固连轴的坐标变换 3×3 矩阵

从 NED 轴到机体固连轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **DCMef** — 从固定坐标系轴的坐标变换 3×3 矩阵

从固定坐标系轴到 NED 轴的坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

### **Vb** — 机体相对于固定坐标系的速度三元素向量

机体相对于固定坐标系的速度，返回为三元素向量。

**数据类型：** `double`

### **ωrel** — 机体相对于 NED 坐标系的相对角速率三元素向量

机体相对于 NED 坐标系的相对角速率，在机体坐标系中表示，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **ωb** — 机体相对于惯性坐标系的角速率三元素向量

机体相对于惯性坐标系的角速率，在机体坐标系中表示，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **dωb/dt** — 机体相对于惯性坐标系的角加速度三元素向量

机体相对于惯性坐标系的角加速度，在机体坐标系中表示，返回为三元素向量，以弧度每秒平方为单位。

**数据类型：** `double`

### **Abb** — 机体固连轴中的加速度三元素向量

机体相对于固定坐标系的加速度，返回为三元素向量。

**数据类型：** `double`

### **Ab ff** — 机体固连轴中的加速度三元素向量

机体固连轴中相对于固定坐标系的加速度，返回为三元素向量。

#### 依赖关系

要启用此端口，请选择 **包含惯性加速度**。

**数据类型：** `double`

## 参数

### 主要

### **单位** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

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
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **质量类型** — 质量类型 `Custom Variable`（默认） | `Fixed` | `Simple Variable`

质量类型，指定为：

|  |  |
| --- | --- |
| `Fixed` | 质量在整个仿真过程中保持恒定（请参阅 6DOF ECEF (Quaternion)）。 |
| `Simple Variable` | 质量和惯性作为质量变化率的函数线性变化。 |
| `Custom Variable` | 质量和惯性变化可自定义（请参阅 Custom Variable Mass 6DOF ECEF (Quaternion)）。 |

`Custom Variable` 选择符合前面描述的运动方程。

#### 程序化使用

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `'Fixed'` | `'Simple Variable'` | `'Custom Variable'` |
| **默认值：** `'Custom Variable'` |

### **大地纬度、经度和高度中的初始位置 [mu,l,h]** — 刚体的初始位置 `[0 0 0]`（默认） | 三元素向量

刚体在大地参考坐标系中的初始位置，指定为三元素向量。纬度和经度值可以为任意值。但是，由于极点处的奇异性，纬度值 +90 和 -90 可能返回意外值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `xg_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **体轴中的初始速度 [U,v,w]** — 体轴中的速度 `[0 0 0]`（默认） | 三元素向量

机体相对于 ECEF 坐标系的初始速度，在机体坐标系中表示，指定为三元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **初始欧拉姿态 [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]`（默认） | 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与北-东-地 (NED) 坐标系之间的角度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **初始机体旋转速率 [p,q,r]** — 初始机体旋转 `[0 0 0]`（默认） | 三元素向量

相对于 NED 坐标系的初始体固连角速率，指定为三元素向量，以弧度每秒为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **包含质量流相对速度** — 质量流相对速度端口 `off`（默认） | `on`

选中此复选框可添加质量流相对速度端口。这是质量增加或减少时的相对速度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vre_flag` |
| **类型：** character vector |
| **值：** `off` | `on` |
| **默认值：** `off` |

### **包含惯性加速度** — 包含惯性加速度端口 `off`（默认） | `on`

选中此复选框可添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，请选择此参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 行星

### **行星模型** — 行星模型 `Earth (WGS84)`（默认） | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `ptype` |
| **类型**： character vector |
| **值**： `'Earth (WGS84)'` | `'Custom'` |
| **默认**： `'Earth (WGS84)'` |

### **行星赤道半径** — 行星在赤道处的半径 `6378137`（默认） | 标量

行星在其赤道处的半径，指定为 double 标量，单位与 ECEF 位置所需单位相同。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `R` |
| **类型**： character vector |
| **值**： double scalar |
| **默认**： `'6378137'` |

### **扁率** — 行星扁率 `1/298.257223563`（默认） | 标量

行星的扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `F` |
| **类型**： character vector |
| **值**： double scalar |
| **默认**： `'1/298.257223563'` |

### **旋转速率** — 旋转速率 `7292115e-11`（默认） | 标量

行星的旋转速率，指定为标量，以 rad/s 为单位。

#### 依赖关系

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**： `w_E` |
| **类型**： character vector |
| **值**： double scalar |
| **默认**： `'7292115e-11'` |

### **Greenwich 天球经度源** — Greenwich 子午线初始天球经度的来源 `Internal`（默认） | `External`

Greenwich 子午线初始天球经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Greenwich 天球经度** 中的天球经度值。 |
| `External` | 使用天球经度值的外部输入。 |

#### 依赖关系

- 要启用此参数，请将
  **行星模型** 设置为
  `Earth`。
- 将此参数设置为
  `External` 会启用
  **LG(0)**
  端口。
- 如果 **行星模型** 设置为
  `Custom`，参数名称将更改为
  **本初子午线天球经度源**。

#### 程序化使用

|  |
| --- |
| **模块参数**： `angle_in` |
| **类型**： character vector |
| **值**： `'Internal'` | `'External'` |
| **默认**： `'Internal'` |

### **Greenwich 天球经度 [deg]** — 初始角度 `0`（默认） | 标量

Greenwich 子午线与惯性坐标系 *x* 轴之间的初始角度，指定为 double 标量。

#### 依赖关系

- 要启用此参数，请设置：

  - **Greenwich 天球经度源** 为
    `Internal`。
  - **行星模型** 为 `Earth
    (WGS84)`。
- 如果 **行星模型** 设置为
  `Custom`，参数名称将更改为
  **本初子午线天球经度 [deg]**。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LPM0` |
| **类型**： character vector |
| **值**： double scalar |
| **默认**： `'0'` |

### **本初子午线天球经度源** — 本初子午线初始天球经度的来源 `Internal`（默认） | `External`

本初子午线初始天球经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **本初子午线天球经度** 中的天球经度值。 |
| `External` | 使用天球经度值的外部输入。 |

#### 依赖关系

- 要启用此参数，请将 **行星模型** 设置为
  `Custom`。
- 将此参数设置为 `External`
  会启用
  **LPM(0)**
  端口。
- 如果 **行星模型** 设置为 `Earth
  (WGS84)`，参数名称将更改为 **Greenwich 天球经度源**。

#### 程序化使用

|  |
| --- |
| **模块参数**： `angle_in` |
| **类型**： character vector |
| **值**： `'Internal'` | `'External'` |
| **默认**： `'Internal'` |

### **本初子午线天球经度 [deg]** — 初始角度 `0`（默认） | 标量

本初子午线与 ECI 坐标系 *x* 轴之间的初始角度，指定为 double 标量。

#### 依赖关系

- 要启用此参数，请设置：

  - **本初子午线天球经度源** 为
    `Internal`。
  - **行星模型** 为
    `Custom`。
- 如果 **行星模型** 设置为
  `Earth (WGS84)`，参数名称将更改为 **Greenwich 天球经度 [deg]**。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LPM0` |
| **类型**： character vector |
| **值**： double scalar |
| **默认**： `'0'` |

### 状态属性

为每个状态分配唯一名称。在整个线性化过程中，使用状态名称而不是模块路径。

- 要为单个状态分配名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态分配名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不分配名称。
- 状态名称仅适用于带名称参数的所选模块。
- 状态数必须能被状态名称数整除。
- 指定的名称数可以少于状态数，但不能多于状态数。

  例如，可以在具有四个状态的系统中指定两个名称。第一个名称适用于前两个状态，第二个名称适用于后两个状态。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **四元数：例如，{'qr','qi','qj','qk'}** — 四元数向量状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

四元数向量状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **机体旋转速率：例如，{'p','q','r'}** — 机体旋转状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

机体旋转速率状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **速度：例如，{'U','v','w'}** — 速度状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **固定坐标系位置：例如，{'Xff', 'Yff', 'Zff'}** — ECEF 位置状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

ECEF 位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `posfixedframe_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **惯性位置：例如，{'Xinertial', 'Yinertial', 'Zinertial'}** — 惯性位置状态名称 `''`（默认） | 用花括号括起来的逗号分隔列表

惯性位置状态名称，指定为用花括号括起来的逗号分隔列表。

默认值为 `''`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `posinertial_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Greenwich 天球经度：例如，'LG'** — 天球经度状态名称 `''`（默认） | character vector

Greenwich 天球经度状态名称，指定为 character vector。

#### 依赖关系

- 要启用此参数，请将 **行星模型** 设置为
  `Earth (WGS84)`。
- 如果 **行星模型** 设置为
  `Custom`，参数名称将更改为
  **本初子午线天球经度：例如，'LPM'**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LPM_statename` |
| **类型：** character vector |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **本初子午线天球经度：例如，'LPM'** — 本初子午线天球经度 `''`（默认） | character vector

本初子午线天球经度状态名称，指定为 character vector。

#### 依赖关系

- 要启用此参数，请将 **行星模型** 设置为
  `Custom`。
- 如果 **行星模型** 设置为
  `Earth (WGS84)`，参数名称将更改为 **Greenwich 天球经度：例如，'LG'**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `LPM_statename` |
| **类型：** character vector |
| **值：** `''` | 标量 |
| **默认值：** `''` |

## 所属库

Aerospace Blockset / Equations of Motion / 6DOF

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 中引入**

### R2023b：Custom Variable Mass 6DOF ECEF (Quaternion) 模块坐标系更改

当 **中心天体** 为 `Custom` 时，这些更新更好地阐明了 Custom Variable Mass 6DOF ECEF (Quaternion) 模块的坐标系：

- 新的模块图标。

  Custom Variable Mass 6DOF ECEF (Quaternion) 模块
- 端口名下标 `ecef` 已更改为 `ff`。
- **Greenwich 天球经度源** 的程序化名称已从 `LG0` 更改为 `LPM`。现有脚本继续有效。
- 更新了模块参数名称，但之前版本的模型继续有效。

  | 旧参数名称或设置 | 新参数名称 |
  | --- | --- |
  | **ECEF 位置**... | **固定坐标系位置**... |
  | 当 **行星模型** 为 `Earth` | **Greenwich 天球经度源** 和 **Greenwich 天球经度 [deg]** |
  | 当 **行星模型** 为 `Custom` | **本初子午线天球经度源** 和 **本初子午线天球经度 [deg]** |

## 描述

实现地心地球固定 (ECEF) 坐标中自定义可变质量六自由度运动方程的四元数表示

Custom Variable Mass 6DOF ECEF (Quaternion) 模块实现地心地球固定 (ECEF) 坐标中自定义可变质量六自由度运动方程的四元数表示。它考虑地心地球固定 (ECEF) 坐标系（*XECEF, YECEF,
ZECEF*）绕地心惯性 (ECI) 参考坐标系（*XECI, YECI,
ZECI*）的旋转。ECEF 坐标系的原点是地球中心。有关 ECEF 坐标系的详细信息，请参阅 Algorithms。

Aerospace Blockset™ 使用按 scalar-first 约定定义的四元数。
