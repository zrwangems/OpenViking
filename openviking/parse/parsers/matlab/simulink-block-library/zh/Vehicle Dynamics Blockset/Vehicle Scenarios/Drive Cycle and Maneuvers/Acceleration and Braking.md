---
type: simulink-block
title: 'Acceleration and Braking'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'accelerationandbraking'
documentation_source_path: 'ref/accelerationandbraking.html'
language: zh-CN
chinese_source: worker-translation
---

# Acceleration and Braking

## 端口

### 输入

### **xdot** — 车辆纵向速度标量

车辆在车身固定坐标系下的纵向速度，指定为标量，单位为 m/s。

**数据类型：** `double`

### **r** — 车辆横摆角速度标量

车辆横摆角速度，指定为标量，单位为 rad/s。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

**数据类型：** `double`

### **SteerCmd** — 车辆方向盘转角标量

车辆方向盘转角，指定为标量，单位为 rad。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

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

驾驶员参考数据，以包含以下模块值的总线形式返回。

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
| `DecelCmd` | 归一化减速踏板或制动输入。 | one |
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

Bus Assignment 模块覆盖 Acceleration and Braking 模块的 TransModeCmd 输出的框图。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 机动参数

### **Maneuver start time, tStart [s]** — 起始时间 `2`（默认）| 正标量

机动起始时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `2`（默认）| 正标量 |
| **数据类型：** | `double` |

### **tStart 处的纵向加速度，ax [g]** — 仿真开始时的纵向加速度 `0.5`（默认）| 正标量

仿真开始时间 **tStart** 处的纵向加速度，单位为 m/s^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ax` |
| **值：** | `0.5`（默认）| 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点，velRef** — 目标速度 `50`（默认）| 正标量

目标速度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `50`（默认）| 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点单位，velRefUnit []** — 单位 `mph`（默认）

目标速度的单位。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph`（默认）| 字符向量 |
| **数据类型：** | `character vector` |

### **制动踏板 actuation** — 制动踏板 actuation `Time`（默认）| `Longitudinal displacement`

开始减速的方法。要指定开始使车辆减速的时间，请选择 `Time`。要指定开始使车辆减速的位移，请选择 `Longitudinal displacement`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `brakingType` |
| **值：** | `Time`（默认）| `Longitudinal displacement` |
| **数据类型：** | `character vector` |

### **制动 actuation 时间，tBrake [s]** — 制动 actuation 时间 `15`（默认）| 正标量

启动制动时的仿真时间，单位为 s。

#### 依赖关系

要启用此参数，请将 **制动踏板 actuation** 设置为 `Time`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tBrake` |
| **值：** | `15`（默认）| 正标量 |
| **数据类型：** | `double` |

### **车辆 CG 的纵向位移，xBrake [m]** — 标称横向偏移 `200`（默认）| 正标量

启动制动时车辆的纵向位移，单位为 m。

#### 依赖关系

要启用此参数，请将 **制动踏板 actuation** 设置为 `Longitudinal displacement`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `xBrake` |
| **值：** | `200`（默认）| 正标量 |
| **数据类型：** | `double` |

### **tBrake 处的纵向减速度，axDecel [g]** — 减速度 `1`（默认）| 正标量

启动制动时的减速度，单位为 g。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `axDecel` |
| **值：** | `1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **制动后将方向盘角度设置为 0 度** — 制动后将方向盘角度设置为零度的选项 `on`（默认）| `off`

选择此参数可在制动后将方向盘角度设置为零度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerZero` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

### 跟踪参数

### **Enable fault tracking before braking** — 在制动前启用故障跟踪的选项 `off`（默认） | `on`

选择此参数以在制动前启用故障跟踪。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `faultTracking` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Transport delay buffer size, bufferSize []** — 传输延迟缓冲区大小 `4096`（默认） | 正标量

传输延迟缓冲区大小。此参数用于在线诊断计算。使用仿真步长或硬件内存可用性来指定缓冲区大小。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bufferSize` |
| **值：** | `4096`（默认） | 正标量 |
| **数据类型：** | `double` |

### **Longitudinal velocity and mean longitudinal velocity, velMaxDiff** — 速度差 `1`（默认） | 正标量

在制动开始前的八秒时间间隔内，纵向速度与平均纵向速度之间允许的最大差值，单位为 m/s。

设置该值以符合 ISO 14512 关于在具有分离摩擦系数的表面上制动的规定。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velMaxDiff` |
| **值：** | `1`（默认） | 正标量 |
| **数据类型：** | `double` |

### **Mean longitudinal velocity and longitudinal velocity reference, velMeanDiff** — 速度容差 `2`（默认） | 正标量

在制动开始前的八秒时间间隔内，平均纵向速度与纵向速度参考值之间允许的最大差值，单位为 m/s。

设置该值以符合 ISO 14512 关于在具有分离摩擦系数的表面上制动的规定。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velMeanDiff` |
| **值：** | `2`（默认） | 正标量 |
| **数据类型：** | `double` |

### **Yaw velocity and mean yaw velocity, rMaxDiff [deg/s]** — 速度容差 `1`（默认） | 正标量

在制动开始前的八秒时间间隔内，横摆角速度与平均横摆角速度之间允许的最大差值，单位为 deg/s。

设置该值以符合 ISO 14512 关于在具有分离摩擦系数的表面上制动的规定。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rMaxDiff` |
| **值：** | `1`（默认）| 正标量 |
| **数据类型：** | `double` |

### **方向盘转角与平均方向盘转角，steerMaxDiff [deg]** — 方向盘转角容差 `3`（默认）| 正标量

在制动开始前的八秒时间间隔内，方向盘转角与平均方向盘转角之间允许的最大差值，单位为 deg。

设置该值以符合 ISO 14512 关于在具有分离摩擦系数的表面上制动的规定。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerMaxDiff` |
| **值：** | `3`（默认）| 正标量 |
| **数据类型：** | `double` |

### **发生故障时停止仿真** — 发生故障时停止仿真的选项 `off`（默认）| `on`

选择此参数可在发生故障时停止仿真。

#### 依赖关系

要启用此参数，请选择 **Enable fault tracking before braking**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `stopOnFault` |
| **值：** | `off`（默认）| `on` |
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

生成转向、加速和制动命令

Acceleration and Braking 模块根据纵向位移或时间生成直线参考轨迹。初始参考加速度和减速度可调。一旦达到目标纵向速度，该模块执行减速度信号。该减速度信号可以按指定时间或纵向位移执行。

一个额外的故障跟踪选项允许您在制动前监测参数的一致性。默认设定值是标准 split-mu 测试（ISO Standard 141512）的上限。

**注意**

有关制动测试参考应用中使用的参考生成器模块的信息，请参见 Straight Maneuver Reference Generator。
