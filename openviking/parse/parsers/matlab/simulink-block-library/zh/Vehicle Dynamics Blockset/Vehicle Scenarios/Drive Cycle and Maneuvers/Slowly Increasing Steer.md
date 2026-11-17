---
type: simulink-block
title: 'Slowly Increasing Steer'
family: 'vehicle-scenarios'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'slowlyincreasingsteer'
documentation_source_path: 'ref/slowlyincreasingsteer.html'
language: zh-CN
chinese_source: worker-translation
---

# Slowly Increasing Steer

## 端口

### 输入

### **xdot** — 车辆纵向速度标量

车辆在车体固定坐标系中的纵向速度，指定为标量，单位为 m/s。

**数据类型：** `single` | `double`

### **ay** — 车辆横向加速度阈值标量

停止仿真所需的车辆横向加速度，指定为标量，单位为 m/s^2。

#### 依赖关系

要启用此参数，请选择 **在横向加速度阈值时停止仿真**。

**数据类型：** `single` | `double`

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
| `SteerZero` | Boolean 信号，当值为 `true` 时用于以零覆盖驾驶员模型转向命令 | one |
| `SteerHld` | Boolean 信号，当为 `true` 时用于保持当前驾驶员模型转向输出 | one |
| `AccelCmd` | `EnblAccelCmd` | Boolean 信号，用于覆盖驾驶员模型加速命令 | one |
| `AccelCmd` | 归一化加速器输入 | one |
| `AccelHld` | Boolean 信号，当为 `true` 时用于保持当前驾驶员模型加速输出 | one |
| `AccelZero` | Boolean 信号，当值为 `true` 时用于以零覆盖驾驶员模型加速命令 | one |
| `DecelCmd` | `EnblDecelCmd` | Boolean 信号，用于覆盖驾驶员模型减速命令 | one |
| `DecelCmd` | 归一化减速器或制动输入 | one |
| `DecelHld` | Boolean 信号，当为 `true` 时用于保持当前驾驶员模型减速输出 | one |
| `DecelZero` | Boolean 信号，当值为 `true` 时用于以零覆盖驾驶员模型减速命令 | one |
| `HndBrkCmd` | 归一化手刹或驻车制动输入 | one |
| `TransCmd` | `TransModeCmd` | 用于指定变速器模式的命令 | one |
| `GearCmd` | 用于指定手动挡位编号或自动变速器换挡器位置的命令 | one |
| `UpShiftCmd` | 升挡命令 | one |
| `DwnShiftCmd` | 降挡命令 | one |
| `ClutchCmd` | 手动变速器的归一化离合器打开命令 | one |

**注意**

默认情况下，`TransCmd` 总线不会被主动使用。使用 Bus Assignment 模块覆盖 `TransCmd` 信号，以自定义和扩展场景。

模块图，其中 Bus Assignment 模块覆盖 Slowly Increasing Steer 模块的 TransModeCmd 输出。

**数据类型：** `bus`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### 机动参数

### **机动开始时间，tStart [s]** — 开始时间 `2` (默认) | 正标量

机动开始时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `2` (默认) | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定值，velRef** — 目标速度 `50` (默认) | 正标量

目标速度。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `50` (默认) | 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定值单位，velRefUnit []** — 单位 `mph` (默认)

目标速度的单位。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph` (默认) | character vector |
| **数据类型：** | `character vector` |

### **转向和反转向速率，steerRate [deg/s]** — 转向和反转向速率 `13.5` (默认) | 正标量

转向和反转向速率，单位为 deg/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerRate` |
| **值：** | `13.5` (默认) | 正标量 |
| **数据类型：** | `double` |

### **转向幅度，steerAmp [deg]** — 方向盘转向幅度 `270` (默认) | 正标量

方向盘转向幅度，单位为 deg。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerAmp` |
| **值：** | `270` (默认) | 正标量 |
| **数据类型：** | `double` |

### **达到最大角度后的转向保持时间，tStop [s]** — 转向保持时间 `2` (默认) | 正标量

达到最大转向幅度后的转向保持时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStop` |
| **值：** | `2` (默认) | 正标量 |
| **数据类型：** | `double` |

### **横向加速度绝对阈值，ay\_max [g]** — 横向加速度阈值 `0.5` (默认) | 正标量

停止仿真时的横向加速度阈值，以 gee 为单位。

#### 依赖关系

要启用此参数，请选择 **在横向加速度阈值时停止仿真**。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ay_max` |
| **值：** | `0.5` (默认) | 正标量 |
| **数据类型：** | `double` |

### **初始转向方向** — 初始转向方向 `Right` (默认) | `Left`

将初始转向方向设置为 `Right` 或 `Left`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerDir` |
| **值：** | `Right` (默认) | `Left` |
| **数据类型：** | `character vector` |

### **在横向加速度阈值时停止仿真** — 在横向加速度阈值时停止仿真的选项 `off` (默认) | `on`

选择此参数可在输入横向加速度阈值时停止仿真。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ayStop` |
| **值：** | `off` (默认) | `on` |
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

生成用于执行线性递增转向机动的命令

Slowly Increasing Steer 模块生成转向、加速和制动命令，以执行线性递增转向机动。一旦车辆达到纵向速度设定值，转向命令即以指定速率开始。车辆达到最大转向角后，车辆将在设定持续时间段内保持该转向角。随后，模块以相同速率将转向角减小到零。纵向控制器在整个机动过程中将车辆调节到规定速度。您可以选择在横向加速度阈值时停止仿真。

缓慢递增转向机动是一项基础测试，有助于评估车辆的横向动力学和不足转向特性。您还可以使用该机动来设置其他测试，例如扫频正弦（swept sine）、正弦停留（sine with dwell）和鱼钩（fishhook）。

**注意**

有关缓慢递增转向参考应用中所用参考生成器模块的信息，请参阅 Slowly Increasing Steer Reference Generator。
