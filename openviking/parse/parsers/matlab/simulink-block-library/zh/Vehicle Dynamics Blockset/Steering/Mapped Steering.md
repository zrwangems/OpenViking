---
type: simulink-block
title: 'Mapped Steering'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'mappedsteering'
documentation_source_path: 'ref/mappedsteering.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped Steering

## 端口

### 输入

### **AngIn** — 转向角 `scalar`

转向角，*δin*，单位为
rad。

使用 **Steering angle breakpoints, StrgAngBpts**
参数指定转向角范围。默认情况下，该值设置为 1.25\*pi，这将转向角限制在 -1.25\*pi
到 1.25\*pi 的范围内。

### **VehSpd** — 车速 `scalar`

车速，*Vehspd*，单位为
m/s。

#### 依赖

要创建此端口，请选择 **Speed
dependent**。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `AngLft` | 左轮转角 | *δL* | rad |
| `AngRght` | 左轮转角 | *δR* | rad |

### **AngLft** — 左轮转角 `scalar`

左轮转角，*δL*，单位为
rad。

### **AngRght** — 右轮转角 `scalar`

右轮转角，*δR*，单位为
rad。

## 参数

#### 选项

### **Speed dependent** — 使用车速相关表 on（默认）| off

选择以使用车速相关表。

#### 依赖

选择此参数将创建输入端口
`VehSpd`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdDpd` |
| **值：** | on（默认）| off |
| **数据类型：** | `character vector` |

### **Steering type** — 使用车速相关表 `Steering wheel angle`（默认）| `Rack travel displacement`

如果将 **Steering type** 设置为 `Steering
wheel angle`，则该模块实现这些表。

| 车速相关 | 实现 |
| --- | --- |
| `on`（默认）| 模块使用三个表：  - *fs*   — 车速的函数 - *fL*   — 叠加方向盘转角的函数 - *fR*   — 叠加方向盘转角的函数 |
| `off` | 模块使用两个表：  - *fL*   — 方向盘转角的函数 - *fR*   — 方向盘转角的函数 |

如果将 **Steering type** 设置为 `Rack travel
displacement`，则该模块实现这些表。

| 车速相关 | 实现 |
| --- | --- |
| `on`（默认）| 模块使用三个表：  - *fs*   — 车速的函数 - *fL*   — 齿条行程位移的函数 - *fR*   — 齿条行程位移的函数 |
| `off` | 模块使用两个表：  - *fL*   — 齿条行程位移的函数 - *fR*   — 齿条行程位移的函数 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IndexType` |
| **值：** | `Steering wheel angle`（默认）| `Rack travel displacement` |
| **数据类型：** | `character vector` |

### **Steering angle breakpoints, StrgAngBpts** — 转向角断点 `[-1.5*pi 1.5*pi]`（默认）| `vector`

转向角断点，单位为 rad。

#### 依赖

如果将 **Steering type** 设置为 `Rack
travel displacement`，要启用此参数，请将
**Gear ratio parameterized by** 设置为
`Lookup table`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgAngBpts` |
| **值：** | `[-1.5*pi 1.5*pi]`（默认）| `vector` |
| **数据类型：** | `double` |

### **Rack travel displacement breakpoints, RackDispBpts** — 齿条行程位移断点 `[-40 -19.2 -4.53 4.53 19.2 40]`（默认）| `vector`

齿条行程位移断点，单位为 mm。

#### 依赖

要启用此参数，请将 **Steering type** 设置为
`Rack travel displacement`，并将
**Gear ratio parameterized by** 设置为
`Lookup table`。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RackDispBpts` |
| **值：** | `[-40 -19.2 -4.53 4.53 19.2 40]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Gear ratio table, GrTbl** — 传动比表 `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi`（默认） | `vector`

作为齿条行程位移函数的传动比表，单位为
mm/rev。

#### 依赖关系

要启用此参数，请将 **Steering type** 设置为
`Rack travel displacement`，并将
**Gear ratio parameterized by** 设置为
`Lookup table`。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GrTbl` |
| **值：** | `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi`（默认） | `vector` |
| **数据类型：** | `double` |

### **Gear ratio constant, Gr** — 传动比常数 `8.28*2*pi`（默认） | `scalar`

传动比常数，单位为 mm/rev。

#### 依赖关系

要启用此参数，请将 **Steering type** 设置为
`Rack travel displacement`，并将
**Gear ratio parameterized by** 设置为
`Constant`。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Gr` |
| **值：** | `8.28*2*pi`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Left wheel angle table, WhlLftTbl** — 左车轮角度表 `[-1.5*pi 1.5*pi]/13.5]`（默认） | `vector`

左车轮角度表，*δL*，单位为
rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlLftTbl` |
| **值：** | `[-1.5*pi 1.5*pi]/13.5]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Right wheel angle table, WhlRghtTbl** — 右车轮角度表 `[-1.5*pi 1.5*pi]/13.5]`（默认） | `vector`

右车轮角度表，*δR*，单位为
rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlRghtTbl` |
| **值：** | `[-1.5*pi 1.5*pi]/13.5]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Vehicle speed breakpoints, VehSpdBpts** — 车速断点 `[-1 1]`（默认） | `vector`

车速断点，单位为 m/s。

#### 依赖关系

要创建此参数，请选择 **Speed dependent**。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VehSpdBpts` |
| **值：** | `[-1 1]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Superimposed speed factor table, SpdFctTbl** — 速度因子 `[1 1]`（默认） | `vector`

叠加速度因子表，
*ƒs*，无量纲。该表
是车速 *v* 的因子。

#### 依赖关系

要创建此参数，请选择 **Speed dependent**。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdFctTbl` |
| **值：** | `[1 1]`（默认） | `vector` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带速度相关选项的映射转向

Mapped Steering 模块使用查找表来计算右轮和左轮角度。使用 **Speed dependent** 参数来实现用于转向角计算的速度相关表。该模块使用车辆坐标系。

### 方向盘角度

如果将 **Steering type** 设置为 `Steering wheel
angle`，则该模块实现这些表。

| Speed Dependent | 实现 | 计算 |
| --- | --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs* —   车辆速度的函数 - *fL* —   叠加方向盘角度的函数 - *fR* —   叠加方向盘角度的函数 | δSpdF=fs(v)δSuprImp=δSpdF⋅δinδL=fL(δSuprImp)δR=fR(δSuprImp) |
| `off` | 模块使用两个表：  - *fL* —   方向盘角度的函数 - *fR* —   方向盘角度的函数 | δL=fL(δin)δR=fR(δin) |

### 齿条行程位移

如果将 **Steering type** 设置为 `Rack travel
displacement`，则该模块实现这些表。

| Speed Dependent | 实现 | 计算 |
| --- | --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs* —   车辆速度的函数 - *fL* —   齿条行程位移的函数 - *fR* —   齿条行程位移的函数 | δSpdF=fs(v)δSuprImp=δSpdF⋅δinΔRack=δSuprImp⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |
| `off` | 模块使用两个表：  - *fL* —   齿条行程位移的函数 - *fR* —   齿条行程位移的函数 | ΔRack=δin⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |

该模块使用传动比来调整齿条行程位移。要使用

- 恒定传动比，将 **Gear ratio parameterized
  by** 设置为 `Constant`。
- 作为转向角函数的传动比，将 **Gear ratio
  parameterized by** 设置为 `Lookup
  table`。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 方向盘角度 |
| *δSpdF* | 方向盘角度速度因子 |
| *δSuprImp* | 叠加方向盘角度 |
| *δL*、*δR* | 分别为左轮和右轮角度 |
| *ΔRack* | 齿条行程位移 |
| *Gr* | 传动比 |
