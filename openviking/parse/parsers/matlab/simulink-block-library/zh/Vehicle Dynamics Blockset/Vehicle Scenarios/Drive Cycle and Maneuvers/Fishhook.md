---
type: simulink-block
title: 'Fishhook'
family: 'vehicle-scenarios'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / Drive Cycle and Maneuvers'
documentation_page: 'fishhook'
documentation_source_path: 'ref/fishhook.html'
language: zh-CN
chinese_source: worker-translation
---

# Fishhook

## 端口

### 输入

### **xdot** — 车辆纵向速度标量

在车体固定坐标系中的车辆纵向速度，指定为标量，单位为 m/s。

**数据类型：** `double`

### **p** — 车辆侧倾角速度标量

车辆侧倾角速度，指定为标量，单位为 rad/s。

#### 依赖关系

要启用此参数，请选择**使用侧倾角速度确定初始转向驻留时间**。

**数据类型：** `double`

### 输出

### **DrvRef** — 驾驶员参考数据总线

驾驶员参考数据，作为总线返回，包含以下模块值。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `LngRef` | 纵向参考速度 | m/s |
| `LtrRef` | 横向参考位移 | m |
| `XRef` | 车辆全局纵向参考位置 | m |
| `YRef` | 车辆全局横向参考位置 | m |
| `PhiRef` | 车辆全局偏航参考位置 | rad |
| `CurvRef` | 参考路径曲率 | 1/m |
| `CurvGradRef` | 参考路径曲率梯度 | 1/m^2 |

**数据类型：** `bus`

### **DrvCmd** — 驾驶员指令数据总线

驾驶员指令数据，作为总线返回，包含以下模块值。

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
| `TransCmd` | `TransModeCmd` | 变速器或驱动模式指令 | one |
| `GearCmd` | 用于指定手动挡位或自动变速器换挡杆位置的指令 | one |
| `UpShiftCmd` | 升挡指令 | one |
| `DwnShiftCmd` | 降挡指令 | one |
| `ClutchCmd` | 用于手动变速器的归一化离合器踏板指令 | one |

**注意**

默认情况下，不会主动使用 `TransCmd` 总线。使用 Bus Assignment 模块覆盖 `TransCmd` 总线，以自定义并扩展场景。

框图，其中 Bus Assignment 模块覆盖 Fishhook 模块的 TransModeCmd 输出。

**数据类型：** `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在**仿真**选项卡上的**准备**库中，选择**属性检查器**。

### **机动开始时间, tStart [s]** — 开始时间 `2`（默认）| 正标量

机动开始时间，单位为 s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tStart` |
| **值：** | `2`（默认）| 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点, velRef** — 目标速度 `30`（默认）| 正标量

目标速度。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRef` |
| **值：** | `30`（默认）| 正标量 |
| **数据类型：** | `double` |

### **纵向速度设定点单位, velRefUnit []** — 单位 `mph`（默认）

目标速度的单位。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `velRefUnit` |
| **值：** | `mph`（默认）| character vector |
| **数据类型：** | `character vector` |

### **转向和反向转向速率, steerRate [deg/s]** — 转向和反向转向速率 `720`（默认）| 正标量

转向和反向转向速率，单位为 deg/s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerRate` |
| **值：** | `720`（默认）| 正标量 |
| **数据类型：** | `double` |

### **转向幅值, steerAmp [deg]** — 方向盘转向幅值 `540`（默认）| 正标量

转向幅值，单位为 deg。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerAmp` |
| **值：** | `540`（默认）| 正标量 |
| **数据类型：** | `double` |

### **使用侧倾角速度确定初始转向驻留时间** — 使用侧倾角速度确定初始转向驻留时间的选项 `off`（默认）| `on`

选择此参数可使用侧倾角速度确定初始转向驻留时间。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `pFdbk` |
| **值：** | `off`（默认）| `on` |
| **数据类型：** | `character vector` |

### **初始驻留时间, tDwellSteer [s]** — 初始驻留时间 `0.5`（默认）| 正标量

保持初始转向幅值的驻留时段，指定为正标量，单位为 s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tDwellSteer` |
| **值：** | `0.5`（默认）| 正标量 |
| **数据类型：** | `double` |

### **反向转向驻留时间, tDwellCntrSteer [s]** — 反向转向驻留时间 `3`（默认）| 正标量

保持反向转向幅值的驻留时段。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tDwellCntrSteer` |
| **值：** | `3`（默认）| 正标量 |
| **数据类型：** | `double` |

### **回正时间, tZero [s]** — 将反向转向幅值恢复至零转向的时间 `2`（默认）| 正标量

将反向转向幅值恢复至零转向的时间，单位为 s。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tZero` |
| **值：** | `2`（默认）| 正标量 |
| **数据类型：** | `double` |

### **侧倾角速度反向转向启动过零阈值, pZero [deg/s]** — 侧倾角速度容差 `1.5`（默认）| 正标量

围绕零的侧倾角速度容差，用于启动反向转向，单位为 deg/s。

#### 依赖关系

要启用此参数，请选择**使用侧倾角速度确定初始转向驻留时间**。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `pZero` |
| **值：** | `1.5`（默认）| 正标量 |
| **数据类型：** | `double` |

### **初始转向方向** — 初始转向方向 `Right`（默认）| `Left`

将初始转向方向设置为 `Right` 或 `Left`。

#### 以编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `steerDir` |
| **值：** | `Right`（默认）| `Left` |
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

生成用于执行鱼钩机动的指令

Fishhook 模块在达到目标纵向速度时生成参数化转向和反向转向指令。请注意，时间或侧倾角速度反馈均可触发反向转向动作，从而优化反向转向的严重程度。此过程对于评估侧翻倾向很有价值，通常通过先执行 Slowly Increasing Steer 测试来确定转向幅值，从而进行参数化。
