---
type: simulink-block
title: 'Constant Radius'
family: 'vehicle-scenarios'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'constantradius'
documentation_source_path: 'ref/constantradius.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Radius

## 端口

### 输入

### **X** — 车辆质心纵向位置 标量

全局坐标系中车辆质心的纵向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **Y** — 车辆质心横向位置 标量

全局坐标系中车辆质心的横向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **psi** — 车辆横摆角 标量

车辆相对于全局坐标系的横摆角，指定为标量，单位为 m。

**数据类型：** `double`

### **ay** — 车辆横向加速度 标量

停止仿真所需的车辆横向加速度，指定为标量，单位为 gee。

#### 依赖关系

要启用此参数，请选择 **在横向加速度阈值处停止仿真**。

**数据类型：** `double`
### 输出

### **DrvRef** — 驾驶员参考数据总线

驾驶员参考数据，返回为一个总线，其中包含以下模块值。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `LngRef` | 纵向参考速度 | m/s |
| `LtrRef` | 横向参考位移 | m |
| `XRef` | 车辆全局纵向参考位置 | m |
| `YRef` | 车辆全局横向参考位置 | m |
| `PhiRef` | 车辆全局横摆参考位置 | rad |
| `CurvRef` | 参考路径曲率 | 1/m |
| `CurvGradRef` | 参考路径曲率梯度 | 1/m^2 |

**数据类型：** `bus`

### **DrvCmd** — 驾驶员命令数据总线

驾驶员命令数据，返回为一个总线，其中包含以下模块值。

| 信号 | | 描述 | 单位 |
| --- | --- | --- | --- |
| `SteerCmd` | `EnblSteerCmd` | Boolean 信号，用于覆盖驾驶员模型转向命令 | one |
| `SteerCmd` | 方向盘转角 | one |
| `SteerZero` | 当值为 `true` 时，用于将驾驶员模型转向命令覆盖为零的 Boolean 信号 | one |
| `SteerHld` | 当为 `true` 时，用于保持当前驾驶员模型转向输出的 Boolean 信号 | one |
| `AccelCmd` | `EnblAccelCmd` | Boolean 信号，用于覆盖驾驶员模型加速命令 | one |
| `AccelCmd` | 归一化加速踏板输入 | one |
| `AccelHld` | 当为 `true` 时，用于保持当前驾驶员模型加速输出的 Boolean 信号 | one |
| `AccelZero` | 当值为 `true` 时，用于将驾驶员模型加速命令覆盖为零的 Boolean 信号 | one |
| `DecelCmd` | `EnblDecelCmd` | Boolean 信号，用于覆盖驾驶员模型减速命令 | one |
| `DecelCmd` | 归一化减速踏板或制动输入 | one |
| `DecelHld` | 当为 `true` 时，用于保持当前驾驶员模型减速输出的 Boolean 信号 | one |
| `DecelZero` | 当值为 `true` 时，用于将驾驶员模型减速命令覆盖为零的 Boolean 信号 | one |
| `HndBrkCmd` | 归一化手刹或驻车制动输入 | one |
| `TransCmd` | `TransModeCmd` | 用于指定变速器模式的命令 | one |
| `GearCmd` | 用于指定手动挡位编号或自动变速器换挡杆位置的命令 | one |
| `UpShiftCmd` | 升挡命令 | one |
| `DwnShiftCmd` | 降挡命令 | one |
| `ClutchCmd` | 手动变速器的归一化离合器分离命令 | one |

**注意**

默认情况下，`TransCmd` 总线不会主动使用。使用 Bus Assignment 模块覆盖 `TransCmd` 总线，以自定义并扩展场景。

框图，其中 Bus Assignment 模块覆盖 Constant Radius 模块的 TransCmd 输出。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **机动开始时间, tStart [s]** — 开始时间 `2` (default) | 正标量

机动开始时间，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `2` (default) | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定值, velRef** — 目标速度 `35` (default) | 正标量

目标速度。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `35` (default) | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定值单位, velRefUnit []** — 单位 `mph` (default)

目标速度的单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph` (default) | character vector |
| **数据类型：** | `character vector` |

### **R** — 要跟踪的半径 `100` (default) | 正标量

要跟踪的半径，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `100` (default) | 正标量 |
| **数据类型：** | `double` |

### **初始纵向位置, X\_o [m]** — 初始纵向起点 `0` (default) | 标量

圆形参考在全局坐标中的初始纵向起点，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `X_o` |
| **值：** | `0` (default) | 标量 |
| **数据类型：** | `double` |

### **初始横向位置, Y\_o [m]** — 初始横向起点 `0` (default) | 标量

圆形参考在全局坐标中的初始横向起点，单位为 m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Y_o` |
| **值：** | `0` (default) | 标量 |
| **数据类型：** | `double` |

### **初始横摆角, psi\_o [rad]** — 起始航向角 `0` (default) | 标量

圆形参考在全局坐标中的起始航向角，单位为 rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `psi_o` |
| **值：** | `0` (default) | 标量 |
| **数据类型：** | `double` |

### **内侧和外侧锥桶边界之间的距离, radialConeDist [m]** — 锥桶之间的径向距离 `6` (default) | 正标量

锥桶之间的径向距离，单位为 m。

#### 依赖关系

要启用此参数，请选择 **实例化 3D 锥桶（需要 Simulation 3D Scene Configuration）**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `radialConeDist` |
| **值：** | `6` (default) | 正标量 |
| **数据类型：** | `double` |

### **横向加速度绝对阈值, ayMax [g]** — 停止仿真前允许的最大横向加速度 `0.5` (default) | 正标量

停止仿真前允许的最大横向加速度，单位为 g。

#### 依赖关系

要启用此参数，请选择 **在横向加速度阈值处停止仿真**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ayMax` |
| **值：** | `0.5` (default) | 正标量 |
| **数据类型：** | `double` |

### **机动方向, steerDir** — 机动方向 `Right` (default) | `Left`

将机动方向设置为 `Right` 或 `Left`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerDir` |
| **值：** | `Right` (default) | `Left` |
| **数据类型：** | `character vector` |

### **在横向加速度阈值处停止仿真** — 在横向加速度阈值处停止仿真的选项 `off` (default) | `on`

选择此参数可在横向加速度阈值处停止仿真。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ayStop` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

### **实例化 3D 锥桶（需要 Simulation 3D Scene Configuration）** — 实例化 3D 锥桶的选项 `off` (default) | `on`

选择此参数可实例化 3D 锥桶。需要 Simulation 3D Scene Configuration 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `use3DCones` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

生成用于跟踪恒定半径路径的命令

Constant Radius 模块使用车辆反馈生成开环纵向速度参考和参考位姿，以跟踪恒定半径路径，这有助于表征车辆的侧倾和不足转向响应，通常是在不同速度下。您可以将这些参考直接与 Predictive Driver 模块一起使用，并将 **横向控制类型, controlTypeLat** 参数设置为 `Stanley`。您还可以改变半径和行驶方向，并可选地在指定的横向加速度限值处停止仿真。
