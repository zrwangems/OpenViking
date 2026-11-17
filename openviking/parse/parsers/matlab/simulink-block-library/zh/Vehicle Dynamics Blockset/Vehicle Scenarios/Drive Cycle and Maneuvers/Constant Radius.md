---
type: simulink-block
title: 'Constant Radius'
family: 'vdynblks'
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
```yaml
ports:
- name: X
  summary: 车辆质心纵向位置 标量
  direction: input
  data_types: double
- name: Y
  summary: 车辆质心横向位置 标量
  direction: input
  data_types: double
- name: psi
  summary: 车辆横摆角 标量
  direction: input
  data_types: double
- name: ay
  summary: 车辆侧向加速度 标量
  direction: input
  data_types: double
- name: DrvRef
  summary: 驾驶员参考数据总线
  direction: output
  data_types: bus
- name: DrvCmd
  summary: 驾驶员指令数据总线
  direction: output
  data_types: bus
```

### 输入

### **X** — 车辆质心纵向位置 标量

车辆质心在全局坐标系中的纵向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **Y** — 车辆质心横向位置 标量

车辆质心在全局坐标系中的横向位置，指定为标量，单位为 m。

**数据类型：** `double`

### **psi** — 车辆横摆角 标量

车辆相对于全局坐标系的横摆角，指定为标量，单位为 m。

**数据类型：** `double`

### **ay** — 车辆侧向加速度 标量

停止仿真所需的车辆侧向加速度，指定为标量，单位为 gee。

#### 依赖关系

要启用此参数，请选中 **Stop simulation at lateral acceleration threshold**。

**数据类型：** `double`
### 输出

### **DrvRef** — 驾驶员参考数据总线

驾驶员参考数据，以包含以下模块值的总线形式返回。

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

### **DrvCmd** — 驾驶员指令数据总线

驾驶员指令数据，以包含以下模块值的总线形式返回。

| 信号 | | 描述 | 单位 |
| --- | --- | --- | --- |
| `SteerCmd` | `EnblSteerCmd` | 用于覆盖驾驶员模型转向指令的布尔信号 | one |
| `SteerCmd` | 方向盘转角 | one |
| `SteerZero` | 当值为 `true` 时，用于以零覆盖驾驶员模型转向指令的布尔信号 | one |
| `SteerHld` | 当为 `true` 时，用于保持当前驾驶员模型转向输出的布尔信号 | one |
| `AccelCmd` | `EnblAccelCmd` | 用于覆盖驾驶员模型加速指令的布尔信号 | one |
| `AccelCmd` | 归一化加速踏板输入 | one |
| `AccelHld` | 当为 `true` 时，用于保持当前驾驶员模型加速输出的布尔信号 | one |
| `AccelZero` | 当值为 `true` 时，用于以零覆盖驾驶员模型加速指令的布尔信号 | one |
| `DecelCmd` | `EnblDecelCmd` | 用于覆盖驾驶员模型减速指令的布尔信号 | one |
| `DecelCmd` | 归一化减速踏板或制动输入 | one |
| `DecelHld` | 当为 `true` 时，用于保持当前驾驶员模型减速输出的布尔信号 | one |
| `DecelZero` | 当值为 `true` 时，用于以零覆盖驾驶员模型减速指令的布尔信号 | one |
| `HndBrkCmd` | 归一化手刹或驻车制动输入 | one |
| `TransCmd` | `TransModeCmd` | 用于指定变速器模式的指令 | one |
| `GearCmd` | 用于指定手动挡位编号或自动变速器换挡杆位置的指令 | one |
| `UpShiftCmd` | 升挡指令 | one |
| `DwnShiftCmd` | 降挡指令 | one |
| `ClutchCmd` | 手动变速器的归一化离合器分离指令 | one |

**注意**

默认情况下，`TransCmd` 总线不会被主动使用。使用 Bus Assignment 模块覆盖 `TransCmd` 总线，以自定义和扩展场景。

Bus Assignment 模块覆盖 Constant Radius 模块的 TransCmd 输出的框图。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Maneuver start time, tStart [s]
  summary: 开始时间 2（默认）| 正标量
  group: ''
  block_parameter: tStart
  values: 2（默认） | 正标量
- name: 纵向速度设定点，velRef
  summary: 目标速度 35（默认） | 正标量
  group: ''
  block_parameter: velRef
  values: 35（默认） | 正标量
- name: 纵向速度设定点单位，velRefUnit []
  summary: 单位 mph（默认）
  group: ''
  block_parameter: velRefUnit
  values: mph（默认） | 字符向量
- name: R
  summary: 要跟踪的半径 100（默认） | 正标量
  group: ''
  block_parameter: R
  values: 100（默认） | 正标量
- name: 初始纵向位置，X_o [m]
  summary: 初始纵向起点 0（默认） | 标量
  group: ''
  block_parameter: X_o
  values: 0（默认） | 标量
- name: 初始横向位置，Y_o [m]
  summary: 初始横向起点 0（默认） | 标量
  group: ''
  block_parameter: Y_o
  values: 0（默认） | 标量
- name: 初始偏航角，psi_o [rad]
  summary: 起始航向角 0（默认） | 标量
  group: ''
  block_parameter: psi_o
  values: 0（默认） | 标量
- name: 内侧和外侧锥体边界之间的距离，radialConeDist [m]
  summary: 锥体之间的径向距离 6（默认） | 正标量
  group: ''
  block_parameter: radialConeDist
  values: 6（默认） | 正标量
- name: 横向加速度绝对阈值，ayMax [g]
  summary: 仿真停止前允许的最大横向加速度 0.5（默认） | 正标量
  group: ''
  block_parameter: ayMax
  values: 0.5（默认） | 正标量
- name: Maneuver direction, steerDir
  summary: 机动方向 Right（默认） | Left
  group: ''
  block_parameter: steerDir
  values: Right（默认） | Left
- name: Stop simulation at lateral acceleration threshold
  summary: 在横向加速度阈值处停止仿真的选项 off（默认） | on
  group: ''
  block_parameter: ayStop
  values: off（默认） | on
- name: Instantiate 3D cones (Simulation 3D Scene Configuration required)
  summary: 实例化 3D 锥桶的选项 off（默认） | on
  group: ''
  block_parameter: use3DCones
  values: off（默认） | on
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Maneuver start time, tStart [s]** — 开始时间 `2`（默认）| 正标量

机动开始时间，单位为 s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `2`（默认） | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点，velRef** — 目标速度 `35`（默认） | 正标量

目标速度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `35`（默认） | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点单位，velRefUnit []** — 单位 `mph`（默认）

目标速度的单位。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph`（默认） | 字符向量 |
| **数据类型：** | `character vector` |

### **R** — 要跟踪的半径 `100`（默认） | 正标量

要跟踪的半径，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `100`（默认） | 正标量 |
| **数据类型：** | `double` |

### **初始纵向位置，X\_o [m]** — 初始纵向起点 `0`（默认） | 标量

圆形参考轨迹在全局坐标系中的初始纵向起点，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `X_o` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **初始横向位置，Y\_o [m]** — 初始横向起点 `0`（默认） | 标量

圆形参考轨迹在全局坐标系中的初始横向起点，单位为 m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Y_o` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **初始偏航角，psi\_o [rad]** — 起始航向角 `0`（默认） | 标量

圆形参考轨迹在全局坐标系中的起始航向角，单位为 rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `psi_o` |
| **值：** | `0`（默认） | 标量 |
| **数据类型：** | `double` |

### **内侧和外侧锥体边界之间的距离，radialConeDist [m]** — 锥体之间的径向距离 `6`（默认） | 正标量

锥体之间的径向距离，单位为 m。

#### 依赖项

要启用此参数，请选择 **Instantiate 3D cones (Simulation 3D Scene Configuration required)**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `radialConeDist` |
| **值：** | `6`（默认） | 正标量 |
| **数据类型：** | `double` |

### **横向加速度绝对阈值，ayMax [g]** — 仿真停止前允许的最大横向加速度 `0.5`（默认） | 正标量

仿真停止前允许的最大横向加速度，单位为 g。

#### 依赖关系

要启用此参数，请选择 **Stop simulation at lateral acceleration threshold**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ayMax` |
| **值：** | `0.5`（默认） | 正标量 |
| **数据类型：** | `double` |

### **Maneuver direction, steerDir** — 机动方向 `Right`（默认） | `Left`

将机动方向设置为 `Right` 或 `Left`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerDir` |
| **值：** | `Right`（默认） | `Left` |
| **数据类型：** | `character vector` |

### **Stop simulation at lateral acceleration threshold** — 在横向加速度阈值处停止仿真的选项 `off`（默认） | `on`

选择此参数以在横向加速度阈值处停止仿真。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ayStop` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Instantiate 3D cones (Simulation 3D Scene Configuration required)** — 实例化 3D 锥桶的选项 `off`（默认） | `on`

选择此参数以实例化 3D 锥桶。需要 Simulation 3D Scene Configuration 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `use3DCones` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |
## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Drive Cycle and Maneuvers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

生成用于跟踪恒定半径路径的命令

Constant Radius 模块生成开环纵向速度参考和参考位姿，利用车辆反馈来跟踪恒定半径路径，这有助于表征车辆的侧倾和不足转向响应，通常在不同速度下进行。您可以将这些参考直接与 Predictive Driver 模块配合使用，并将 **Lateral control type, controlTypeLat** 参数设置为 `Stanley`。您还可以改变半径和行驶方向，并可选地在指定的横向加速度限制处停止仿真。
