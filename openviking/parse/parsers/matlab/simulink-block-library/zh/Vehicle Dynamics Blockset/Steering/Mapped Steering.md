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

转向角，*δin*，以 rad 为单位。

使用 **转向角断点, StrgAngBpts** 参数指定转向角范围。默认情况下，该值设置为 1.25\*pi，这将转向角限制在 -1.25\*pi 到 1.25\*pi 范围内。

### **VehSpd** — 车辆速度 `scalar`

车辆速度，*Vehspd*，以 m/s 为单位。

#### 依赖关系

要创建此端口，请选择 **速度相关**。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `AngLft` | 左车轮转角 | *δL* | rad |
| `AngRght` | 右车轮转角 | *δR* | rad |

### **AngLft** — 左车轮转角 `scalar`

左车轮转角，*δL*，以 rad 为单位。

### **AngRght** — 右车轮转角 `scalar`

右车轮转角，*δR*，以 rad 为单位。

## 参数

#### 选项

### **速度相关** — 使用速度相关表 on（默认）| off

选择以使用速度相关表。

#### 依赖关系

选择此参数会创建输入端口 `VehSpd`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdDpd` |
| **值：** | on（默认）| off |
| **数据类型：** | `character vector` |

### **转向类型** — 使用速度相关表 `Steering wheel angle`（默认）| `Rack travel displacement`

如果将 **转向类型** 设置为 `Steering wheel angle`，模块将实现以下表。

| 速度相关 | 实现 |
| --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs*   — 车辆速度的函数 - *fL*   — 叠加转向盘转角的函数 - *fR*   — 叠加转向盘转角的函数 |
| `off` | 模块使用两个表：  - *fL*   — 转向盘转角的函数 - *fR*   — 转向盘转角的函数 |

如果将 **转向类型** 设置为 `Rack travel displacement`，模块将实现以下表。

| 速度相关 | 实现 |
| --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs*   — 车辆速度的函数 - *fL*   — 齿条行程位移的函数 - *fR*   — 齿条行程位移的函数 |
| `off` | 模块使用两个表：  - *fL*   — 齿条行程位移的函数 - *fR*   — 齿条行程位移的函数 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `IndexType` |
| **值：** | `Steering wheel angle`（默认）| `Rack travel displacement` |
| **数据类型：** | `character vector` |

### **转向角断点, StrgAngBpts** — 转向角断点 `[-1.5*pi 1.5*pi]`（默认）| `vector`

转向角断点，以 rad 为单位。

#### 依赖关系

如果将 **转向类型** 设置为 `Rack travel displacement`，要启用此参数，请将 **齿轮比参数化方式** 设置为 `Lookup table`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `StrgAngBpts` |
| **值：** | `[-1.5*pi 1.5*pi]`（默认）| `vector` |
| **数据类型：** | `double` |

### **齿条行程位移断点, RackDispBpts** — 齿条行程位移断点 `[-40 -19.2 -4.53 4.53 19.2 40]`（默认）| `vector`

齿条行程位移断点，以 mm 为单位。

#### 依赖关系

要启用此参数，请将 **转向类型** 设置为 `Rack travel displacement`，并将 **齿轮比参数化方式** 设置为 `Lookup table`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RackDispBpts` |
| **值：** | `[-40 -19.2 -4.53 4.53 19.2 40]`（默认）| `vector` |
| **数据类型：** | `double` |

### **齿轮比表, GrTbl** — 齿轮比表 `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi`（默认）| `vector`

作为齿条行程位移函数的齿轮比表，以 mm/rev 为单位。

#### 依赖关系

要启用此参数，请将 **转向类型** 设置为 `Rack travel displacement`，并将 **齿轮比参数化方式** 设置为 `Lookup table`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `GrTbl` |
| **值：** | `[9.87 9.87 7.16 7.16 9.87 9.87]*2*pi`（默认）| `vector` |
| **数据类型：** | `double` |

### **齿轮比常数, Gr** — 齿轮比常数 `8.28*2*pi`（默认）| `scalar`

齿轮比常数，以 mm/rev 为单位。

#### 依赖关系

要启用此参数，请将 **转向类型** 设置为 `Rack travel displacement`，并将 **齿轮比参数化方式** 设置为 `Constant`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Gr` |
| **值：** | `8.28*2*pi`（默认）| `scalar` |
| **数据类型：** | `double` |

### **左车轮转角表, WhlLftTbl** — 左车轮转角表 `[-1.5*pi 1.5*pi]/13.5]`（默认）| `vector`

左车轮转角表，*δL*，以 rad 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlLftTbl` |
| **值：** | `[-1.5*pi 1.5*pi]/13.5]`（默认）| `vector` |
| **数据类型：** | `double` |

### **右车轮转角表, WhlRghtTbl** — 右车轮转角表 `[-1.5*pi 1.5*pi]/13.5]`（默认）| `vector`

右车轮转角表，*δR*，以 rad 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `WhlRghtTbl` |
| **值：** | `[-1.5*pi 1.5*pi]/13.5]`（默认）| `vector` |
| **数据类型：** | `double` |

### **车辆速度断点, VehSpdBpts** — 车辆速度断点 `[-1 1]`（默认）| `vector`

车辆速度断点，以 m/s 为单位。

#### 依赖关系

要创建此参数，请选择 **速度相关**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `VehSpdBpts` |
| **值：** | `[-1 1]`（默认）| `vector` |
| **数据类型：** | `double` |

### **叠加速度因子表, SpdFctTbl** — 速度因子 `[1 1]`（默认）| `vector`

叠加速度因子表，*ƒs*，无量纲。该表是车辆速度 *v* 的因子。

#### 依赖关系

要创建此参数，请选择 **速度相关**。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SpdFctTbl` |
| **值：** | `[1 1]`（默认）| `vector` |
| **数据类型：** | `double` |

## 所属库

Vehicle Dynamics Blockset / Steering

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带速度相关选项的 Mapped Steering

Mapped Steering 模块实现查找表以计算右车轮转角和左车轮转角。使用 **速度相关** 参数实现用于转向角计算的速度相关表。该模块使用车辆坐标系。

### 转向盘转角

如果将 **转向类型** 设置为 `Steering wheel angle`，模块将实现以下表。

| 速度相关 | 实现 | 计算 |
| --- | --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs* — 车辆速度的函数 - *fL* — 叠加转向盘转角的函数 - *fR* — 叠加转向盘转角的函数 | δSpdF=fs(v)δSuprImp=δSpdF⋅δinδL=fL(δSuprImp)δR=fR(δSuprImp) |
| `off` | 模块使用两个表：  - *fL* — 转向盘转角的函数 - *fR* — 转向盘转角的函数 | δL=fL(δin)δR=fR(δin) |

### 齿条行程位移

如果将 **转向类型** 设置为 `Rack travel displacement`，模块将实现以下表。

| 速度相关 | 实现 | 计算 |
| --- | --- | --- |
| `on`（默认） | 模块使用三个表：  - *fs* — 车辆速度的函数 - *fL* — 齿条行程位移的函数 - *fR* — 齿条行程位移的函数 | δSpdF=fs(v)δSuprImp=δSpdF⋅δinΔRack=δSuprImp⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |
| `off` | 模块使用两个表：  - *fL* — 齿条行程位移的函数 - *fR* — 齿条行程位移的函数 | ΔRack=δin⋅GrδL=fL(ΔRack)δR=fR(ΔRack) |

该模块使用齿轮比调整齿条行程位移。要使用

- 恒定齿轮比，请将 **齿轮比参数化方式** 设置为 `Constant`。
- 作为转向角函数的齿轮比，请将 **齿轮比参数化方式** 设置为 `Lookup table`。

方程使用以下变量。

|  |  |
| --- | --- |
| *δin* | 转向盘转角 |
| *δSpdF* | 转向盘转角速度因子 |
| *δSuprImp* | 叠加转向盘转角 |
| *δL*, *δR* | 分别为左车轮转角和右车轮转角 |
| *ΔRack* | 齿条行程位移 |
| *Gr* | 齿轮比 |
