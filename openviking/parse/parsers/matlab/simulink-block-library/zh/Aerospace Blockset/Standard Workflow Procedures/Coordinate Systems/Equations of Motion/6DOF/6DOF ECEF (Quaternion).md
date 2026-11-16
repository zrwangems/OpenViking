---
type: simulink-block
title: '6DOF ECEF (Quaternion)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Equations of Motion / 6DOF'
documentation_page: '6dofecefquaternion'
documentation_source_path: '6dofecefquaternion.html'
language: zh-CN
chinese_source: worker-translation
---

# 6DOF ECEF (Quaternion)

## 端口

### 输入

### **Fxyz** — 施加的力三元素向量

施加的力，指定为三元素向量，采用在 **Units** 中选择的单位。

**数据类型：** `double`

### **Mxyz** — 施加的力矩三元素向量

施加的力矩，指定为三元素向量，采用在 **Units** 中选择的单位。

**数据类型：** `double`

### **LG(0)** — Greenwich 初始天体经度标量

Greenwich 子午线初始天体经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **Celestial longitude of Greenwich** 设置为 `External`。
- 将 **Planet model** 设置为 `Earth`。

**数据类型：** `double`

### **LPM(0)** — 本初子午线初始天体经度角标量

本初子午线初始天体经度角，指定为标量。

#### 依赖关系

要启用此端口

- 将 **Celestial longitude of prime meridian** 设置为 `External`。
- 将 **Planet model** 设置为 `Custom`。

**数据类型：** `double`

### 输出

### **Vff** — 机体相对于 ECEF 坐标系的速度，三元素向量

机体相对于 ECEF 坐标系的速度，以 ECEF 坐标系表示，返回为三元素向量。

**数据类型：** `double`

### **Xff** — ECEF 参考坐标系中的位置，三元素向量

ECEF 参考坐标系中的位置，返回为三元素向量。

**数据类型：** `double`

### **μ l h** — 大地纬度、经度和高度中的位置，三元素向量 | M-by-3 数组

大地纬度、经度和高度中的位置，以度为单位，返回为三元素向量或 M-by-3 数组，长度分别采用所选单位。

**数据类型：** `double`

### **φ θ Ψ (rad)** — 机体旋转角，三元素向量

机体旋转角 [roll, pitch, yaw]，返回为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与 NED 坐标系之间的角度。

**数据类型：** `double`

### **DCMbi** — 从 ECI 轴到机体固定轴的坐标变换，3-by-3 矩阵

从 ECI 轴到机体固定轴的坐标变换，返回为 3-by-3 矩阵。

**数据类型：** `double`

### **DCMbe** — 从 NED 轴到机体固定轴的坐标变换，3-by-3 矩阵

从 NED 轴到机体固定轴的坐标变换，返回为 3-by-3 矩阵。

**数据类型：** `double`

### **DCMef** — 从固定坐标系轴的坐标变换，3-by-3 矩阵

从固定坐标系轴到 NED 轴的坐标变换，返回为 3-by-3 矩阵。

**数据类型：** `double`

### **Vb** — 机体相对于固定坐标系的速度，三元素向量

机体相对于固定坐标系的速度，返回为三元素向量。

**数据类型：** `double`

### **ωrel** — 机体相对于 NED 坐标系的相对角速率，三元素向量

机体相对于 NED 坐标系的相对角速率，以机体坐标系表示，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **ωb** — 机体相对于惯性坐标系的角速率，三元素向量

机体相对于惯性坐标系的角速率，以机体坐标系表示，返回为三元素向量，以弧度每秒为单位。

**数据类型：** `double`

### **dωb/dt** — 机体相对于惯性坐标系的角加速度，三元素向量

机体相对于惯性坐标系的角加速度，以机体坐标系表示，返回为三元素向量，以弧度每秒平方为单位。

**数据类型：** `double`

### **Abb** — 机体固定轴中的加速度，三元素向量

机体相对于固定坐标系的加速度，返回为三元素向量。

**数据类型：** `double`

### **Ab ff** — 机体固定轴中的加速度，三元素向量

相对于固定坐标系的机体固定轴中的加速度，返回为三元素向量。

#### 依赖关系

要启用此端口，请选择 **Include inertial acceleration**。

**数据类型：** `double`

## 参数

### 主要

### **Units** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为 `Metric (MKS)`、`English (Velocity in ft/s)` 或 `English (Velocity in kts)`。

| 单位 | 力 | 力矩 | 加速度 | 速度 | 位置 | 质量 | 惯性 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-meter | Meters per second squared | Meters per second | Meters | Kilogram | Kilogram meter squared |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet per second squared | Feet per second | Feet | Slug | Slug foot squared |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet per second squared | Knots | Feet | Slug | Slug foot squared |

#### 编程用法

|  |
| --- |
| **模块参数：** `units` |
| **类型：** character vector |
| **值：** `Metric (MKS)` | `English (Velocity in ft/s)` | `English (Velocity in kts)` |
| **默认值：** `Metric (MKS)` |

### **Mass type** — 质量类型 `Fixed` (默认) | `Simple Variable` | `Custom Variable`

选择要使用的质量类型：

| 质量类型 | 描述 | 默认用于 |
| --- | --- | --- |
| `Fixed` | 在整个仿真过程中质量恒定。 | - 6DOF (Euler   Angles) - 6DOF   (Quaternion) - 6DOF Wind   (Wind Angles) - 6DOF Wind   (Quaternion) - 6DOF ECEF   (Quaternion) |
| `Simple Variable` | 质量和惯性随质量速率线性变化。 | - Simple   Variable Mass 6DOF (Euler Angles) - Simple   Variable Mass 6DOF (Quaternion) - Simple   Variable Mass 6DOF Wind (Wind   Angles) - Simple   Variable Mass 6DOF Wind   (Quaternion) - Simple   Variable Mass 6DOF ECEF   (Quaternion) |
| `Custom Variable` | 质量和惯性变化可自定义。 | - Custom   Variable Mass 6DOF (Euler Angles) - Custom   Variable Mass 6DOF (Quaternion) - Custom   Variable Mass 6DOF Wind (Wind   Angles) - Custom   Variable Mass 6DOF Wind   (Quaternion) - Custom   Variable Mass 6DOF ECEF   (Quaternion) |

`Fixed` 选择符合前面描述的运动方程。

#### 编程用法

|  |
| --- |
| **模块参数：** `mtype` |
| **类型：** character vector |
| **值：** `Fixed` | `Simple Variable` | `Custom Variable` |
| **默认值：** `'Simple Variable'` |

### **Initial position in geodetic latitude, longitude and altitude [mu,l,h]** — 刚体的初始位置 `[0 0 0]` (默认) | 三元素向量

刚体在大地参考坐标系中的初始位置，指定为三元素向量。纬度和经度值可以是任意值。但是，由于极点处的奇异性，+90 和 -90 的纬度值可能返回意外值。

#### 编程用法

|  |
| --- |
| **模块参数：** `xg_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial velocity in body axes [U,v,w]** — 机体轴中的速度 `[0 0 0]` (默认) | 三元素向量

机体轴中的初始速度，指定为三元素向量，在机体固定坐标系中。

#### 编程用法

|  |
| --- |
| **模块参数：** `Vm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial Euler orientation [roll, pitch, yaw]** — 初始欧拉姿态 `[0 0 0]` (默认) | 三元素向量

初始欧拉姿态角 [roll, pitch, yaw]，指定为三元素向量，以弧度为单位。欧拉旋转角是机体坐标系与北东地（NED）坐标系之间的角度。

#### 编程用法

|  |
| --- |
| **模块参数：** `eul_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial body rotation rates [p,q,r]** — 初始机体旋转 `[0 0 0]` (默认) | 三元素向量

相对于 NED 坐标系的初始机体固定角速率，指定为三元素向量，以弧度每秒为单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `pm_0` |
| **类型：** character vector |
| **值：** `'[0 0 0]'` | 三元素向量 |
| **默认值：** `'[0 0 0]'` |

### **Initial mass** — 初始质量 `1.0` (默认) | 标量

刚体的初始质量，指定为 double 标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `mass_0` |
| **类型：** character vector |
| **值：** `'1.0'` | double scalar |
| **默认值：** `'1.0'` |

### **Inertia** — 惯性 `eye(3)` (默认) | 标量

机体的惯性，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **Mass type** 设置为 `Fixed`。

#### 编程用法

|  |
| --- |
| **模块参数：** `inertia` |
| **类型：** character vector |
| **值：** `eye(3)` | double scalar |
| **默认值：** `eye(3)` |

### **Include inertial acceleration** — 包含惯性加速度端口 `off` (默认) | `on`

选中此复选框以添加惯性加速度端口。

#### 依赖关系

要启用 **Ab ff** 端口，请选择此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `abi_flag` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `off` |

### 行星

### **Planet model** — 行星模型 `Earth (WGS84)` (默认) | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 编程用法

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **Equatorial radius of planet** — 行星赤道半径 `6378137` (默认) | 标量

行星赤道半径，指定为 double 标量，其单位与 ECEF 位置所需单位相同。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`R` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'6378137'` |

### **Flattening** — 行星扁率 `1/298.257223563` (默认) | 标量

行星扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`F` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'1/298.257223563'` |

### **Rotational rate** — 旋转速率 `7292115e-11` (默认) | 标量

行星的旋转速率，指定为标量，单位为 rad/s。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`w_E` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'7292115e-11'` |

### **Celestial longitude of Greenwich source** — Greenwich 子午线初始天体经度的来源 `Internal` (默认) | `External`

Greenwich 子午线初始天体经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Celestial longitude of Greenwich** 中的天体经度值。 |
| `External` | 使用外部输入作为天体经度值。 |

#### 依赖关系

- 要启用此参数，请将 **Planet model** 设置为 `Earth`。
- 将此参数设置为 `External` 会启用 **LG(0)** 端口。
- 如果 **Planet model** 设置为 `Custom`，参数名称将变为 **Celestial longitude of prime meridian source**。

#### 编程用法

|  |
| --- |
| **模块参数**：`angle_in` |
| **类型**：character vector |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Celestial longitude of Greenwich [deg]** — 初始角度 `0` (默认) | 标量

Greenwich 子午线与惯性坐标系 *x* 轴之间的初始角度，指定为 double 标量。

#### 依赖关系

- 要启用此参数，请设置：

  - **Celestial longitude of Greenwich source** 为 `Internal`。
  - **Planet model** 为 `Earth (WGS84)`。
- 如果 **Planet model** 设置为 `Custom`，参数名称将变为 **Celestial longitude of prime meridian [deg]**。

#### 编程用法

|  |
| --- |
| **模块参数**：`LPM0` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'0'` |

### **Celestial longitude of prime meridian source** — 本初子午线初始天体经度的来源 `Internal` (默认) | `External`

本初子午线初始天体经度的来源，指定为：

|  |  |
| --- | --- |
| `Internal` | 使用 **Celestial longitude of prime meridian** 中的天体经度值。 |
| `External` | 使用外部输入作为天体经度值。 |

#### 依赖关系

- 要启用此参数，请将 **Planet model** 设置为 `Custom`。
- 将此参数设置为 `External` 会启用 **LPM(0)** 端口。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名称将变为 **Celestial longitude of Greenwich source**。

#### 编程用法

|  |
| --- |
| **模块参数**：`angle_in` |
| **类型**：character vector |
| **值**：`'Internal'` | `'External'` |
| **默认值**：`'Internal'` |

### **Celestial longitude of prime meridian [deg]** — 初始角度 `0` (默认) | 标量

本初子午线与 ECI 坐标系 *x* 轴之间的初始角度，指定为 double 标量。

#### 依赖关系

- 要启用此参数，请设置：

  - **Celestial longitude of prime meridian source** 为 `Internal`。
  - **Planet model** 为 `Custom`。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名称将变为 **Celestial longitude of Greenwich [deg]**。

#### 编程用法

|  |
| --- |
| **模块参数**：`LPM0` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'0'` |

### 状态属性

为每个状态指定唯一名称。在线性化期间，您可以使用状态名称代替模块路径。

- 要为单个状态指定名称，请在引号之间输入唯一名称，例如 `'velocity'`。
- 要为多个状态指定名称，请输入用花括号括起来的逗号分隔列表，例如 `{'a', 'b', 'c'}`。每个名称必须唯一。
- 如果参数为空（`' '`），则不指定名称。
- 状态名称仅适用于具有名称参数的所选模块。
- 状态数必须能被状态名称数整除。
- 您可以指定的名称数少于状态数，但不能指定的名称数多于状态数。

  例如，您可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。
- 要使用 MATLAB® 工作区中的变量指定状态名称，请输入不带引号的变量。变量可以是 character vector、cell array 或 structure。

### **Quaternion: e.g., {'qr','qi','qj','qk'}** — 四元数向量状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

四元数向量状态名称，指定为用花括号括起来的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `quat_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Body rotation rates: e.g., {'p','q','r'}** — 机体旋转状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

机体旋转速率状态名称，指定为用花括号括起来的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `pm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Velocity: e.g., {'U','v','w'}** — 速度状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

速度状态名称，指定为用花括号括起来的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `Vm_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Fixed frame position: e.g., {'Xff', 'Yff', 'Zff'}** — ECEF 位置状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

ECEF 位置状态名称，指定为用花括号括起来的逗号分隔列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `posfixedframe_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Inertial position: e.g., {'Xinertial', 'Yinertial', 'Zinertial'}** — 惯性位置状态名称 `''` (默认) | 用花括号括起来的逗号分隔列表

惯性位置状态名称，指定为用花括号括起来的逗号分隔列表。

默认值为 `''`。

#### 编程用法

|  |
| --- |
| **模块参数：** `posinertial_statename` |
| **类型：** character vector |
| **值：** `''` | 用花括号括起来的逗号分隔列表 |
| **默认值：** `''` |

### **Celestial longitude of Greenwich: e.g., 'LG'** — 天体经度状态名称 `''` (默认) | character vector

Greenwich 天体经度状态名称，指定为 character vector。

#### 依赖关系

- 要启用此参数，请设置：**Planet model** 为 `Earth (WGS84)`。
- 如果 **Planet model** 设置为 `Custom`，参数名称将变为 **Celestial longitude of prime meridian: e.g., 'LPM'**。

#### 编程用法

|  |
| --- |
| **模块参数：** `LPM_statename` |
| **类型：** character vector |
| **值：** `''` | 标量 |
| **默认值：** `''` |

### **Celestial longitude of prime meridian: e.g., 'LPM'** — 本初子午线天体经度 `''` (默认) | character vector

本初子午线天体经度状态名称，指定为 character vector。

#### 依赖关系

- 要启用此参数，请设置：**Planet model** 为 `Custom`。
- 如果 **Planet model** 设置为 `Earth (WGS84)`，参数名称将变为 **Celestial longitude of Greenwich: e.g., 'LG'**。

#### 编程用法

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

### R2023b：6DOF ECEF (Quaternion) 模块坐标系变化

这些更新更好地阐明了当 **Central body** 为 `Custom` 时 6DOF ECEF (Quaternion) 模块的坐标系：

- 新的模块图标。

  6DOF ECEF (Quaternion) 模块
- `ecef` 的端口名下标已更改为 `ff`。
- **Celestial longitude of Greenwich source** 的编程名称已从 `LG0` 更改为 `LPM`。现有脚本仍可继续工作。
- 更新了模块参数名称，但以前版本的模型仍可继续工作。

  | 旧参数名称或设置 | 新参数名称 |
  | --- | --- |
  | **ECEF position**... | **Fixed frame position**... |
  | 当 **Planet model** 为 `Earth` 时 | **Celestial longitude of Greenwich source** 和 **Celestial longitude of Greenwich [deg]** |
  | 当 **Planet model** 为 `Custom` 时 | **Celestial longitude of prime meridian source** 和 **Celestial longitude of prime meridian [deg]** |

## 描述

在地心地球固定（ECEF）坐标中实现六自由度运动方程的四元数表示

6DOF ECEF (Quaternion) 模块在地心地球固定（ECEF）坐标中实现六自由度运动方程的四元数表示。它考虑地心地球固定（ECEF）坐标系（*XECEF, YECEF, ZECEF*）绕地心惯性（ECI）参考坐标系（*XECI, YECI, ZECI*）的旋转。ECEF 坐标系的原点是地球中心。有关 ECEF 坐标系的详细信息，请参阅算法。
