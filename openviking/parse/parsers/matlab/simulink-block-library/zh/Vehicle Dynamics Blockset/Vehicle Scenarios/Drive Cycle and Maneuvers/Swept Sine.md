---
type: simulink-block
title: 'Swept Sine'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'sweptsine'
documentation_source_path: 'ref/sweptsine.html'
language: zh-CN
chinese_source: worker-translation
---

# Swept Sine

## 端口

### 输入

### **xdot** — 车辆纵向速度标量

在车体坐标系中的车辆纵向速度，指定为标量，单位为 m/s。

**数据类型：** `single` | `double`
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
| `SteerZero` | 当值为 `true` 时用于以零覆盖驾驶员模型转向指令的布尔信号 | one |
| `SteerHld` | 当为 `true` 时用于保持当前驾驶员模型转向输出的布尔信号 | one |
| `AccelCmd` | `EnblAccelCmd` | 用于覆盖驾驶员模型加速指令的布尔信号 | one |
| `AccelCmd` | 归一化加速踏板输入 | one |
| `AccelHld` | 当为 `true` 时用于保持当前驾驶员模型加速输出的布尔信号 | one |
| `AccelZero` | 当值为 `true` 时用于以零覆盖驾驶员模型加速指令的布尔信号 | one |
| `DecelCmd` | `EnblDecelCmd` | 用于覆盖驾驶员模型减速指令的布尔信号 | one |
| `DecelCmd` | 归一化减速踏板或制动输入 | one |
| `DecelHld` | 当为 `true` 时用于保持当前驾驶员模型减速输出的布尔信号 | one |
| `DecelZero` | 当值为 `true` 时用于以零覆盖驾驶员模型减速指令的布尔信号 | one |
| `HndBrkCmd` | 归一化手刹或驻车制动输入 | one |
| `TransCmd` | `TransModeCmd` | 用于指定变速器模式的指令 | one |
| `GearCmd` | 用于指定手动挡位编号或自动变速器换挡杆位置的指令 | one |
| `UpShiftCmd` | 升挡指令 | one |
| `DwnShiftCmd` | 降挡指令 | one |
| `ClutchCmd` | 手动变速器的归一化离合器分离指令 | one |

**注意**

默认情况下，`TransCmd` 总线不会被主动使用。使用 Bus Assignment 模块覆盖 `TransCmd` 总线，以自定义和扩展场景。

Bus Assignment 模块覆盖 Swept Sine 模块的 TransModeCmd 输出的框图。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 机动参数

### **Maneuver start time, tStart [s]** — 开始时间 `2`（默认）| 正标量

机动开始时间，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tStart` |
| **值**：| `2`（默认）| 正标量 |
| **Data Types:** | `double` |

### **Longitudinal velocity setpoint, velRef** — 目标速度 `30`（默认）| 正标量

目标速度。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `velRef` |
| **值**：| `30`（默认）| 正标量 |
| **Data Types:** | `double` |

### **纵向速度设定点单位，velRefUnit []** — 单位 `mph`（默认）

目标速度的单位。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph`（默认） | 字符向量 |
| **数据类型：** | `character vector` |

### **转向幅值，steerAmp [deg]** — 方向盘转向幅值 `90`（默认） | 正标量

方向盘转向幅值，单位为 deg。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerAmp` |
| **值：** | `90`（默认） | 正标量 |
| **数据类型：** | `double` |

### **最终频率，steerFinalFreq [Hz]** — 达到最大转向幅值后的保持时间 `0.7`（默认） | 正标量

达到最大转向幅值后的保持时间，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerFreq` |
| **值：** | `0.7`（默认） | 正标量 |
| **数据类型：** | `double` |

### **扫描时间，tSweep [s]** — 扫描过程的持续时间 `30`（默认） | 正标量

扫描过程的持续时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tSweep` |
| **值：** | `30`（默认） | 正标量 |
| **数据类型：** | `double` |

### **初始转向方向** — 初始转向方向 `Right`（默认） | `Left`

将初始转向方向设置为 `Right` 或 `Left`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerDir` |
| **值：** | `Right`（默认） | `Left` |
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

生成用于执行扫频正弦机动的命令

Swept Sine 模块生成转向、加速和制动命令，以执行扫频正弦机动。一旦车辆达到目标纵向速度，该模块将使用规定的幅值、最终频率和持续时间启动扫频正弦转向命令。

您可以使用扫频正弦机动来表征车辆的瞬态响应，如 ISO 7401:2011 中所述。

**注意**

有关扫频正弦参考应用中使用的参考生成器模块的信息，请参阅 Swept Sine Reference Generator。
