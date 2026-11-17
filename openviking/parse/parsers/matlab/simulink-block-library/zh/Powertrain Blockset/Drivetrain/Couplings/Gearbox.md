---
type: simulink-block
title: 'Gearbox'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'gearbox'
documentation_source_path: 'ref/gearbox.html'
language: zh-CN
chinese_source: worker-translation
---

# Gearbox

## 端口

### 输入

### **BTrq** — 基齿轮输入扭矩 `scalar`

基齿轮输入扭矩，*TB*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Simulink`。

### **FTrq** — 从动齿轮输出扭矩 `scalar`

从动齿轮输出扭矩，*TF*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Simulink`。

### **B** — 基齿轮角速度和扭矩双向连接端口

基齿轮角速度，*ωB*，单位为 rad/s。基齿轮扭矩，*TB*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Two-way connection`。

### **AirTemp** — 环境空气温度 `scalar`

环境空气温度，*Tair*，单位为 K。

#### 依赖

要启用此端口：

- 将 **Efficiency factors** 设置为 `Driveshaft
  torque, speed and temperature`。
- 选中 **Input ambient temperature**。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Base | `BaseTrq` | | 基齿轮输入扭矩 | *TB* | N·m |
| `BaseSpd` | | 基齿轮角速度 | *ωB* | rad/s |
| Flwr | `FlwrTrq` | | 从动齿轮扭矩 | *TF* | N·m |
| `FlwrSpd` | | 从动齿轮角速度 | *ωF* | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrBase` | 来自基轴的机械功率 | *PBase* | W |
| `PwrFlwr` | 来自从动轴的机械功率 | *PFlwr* | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | 总齿轮功率损失 | *Png* | W |
| `PwrDampLoss` | 阻尼导致的功率损失 | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | 存储内部动能的变化率 | *Ps* | W |

### **BSpd** — 输入齿轮角速度 `scalar`

基齿轮角速度，*ωB*，单位为 rad/s。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Simulink`。

### **FSpd** — 输出齿轮角速度 `scalar`

从动齿轮角速度，*ωF*，单位为 rad/s。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Simulink`。

### **F** — 输出齿轮角速度和扭矩双向连接端口

从动齿轮角速度，*ωF*，单位为 rad/s。从动齿轮扭矩，*TF*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为 `Two-way connection`。

## 参数

#### 模块选项

### **Port Configuration** — 指定配置 `Simulink`（默认）| `Two-way connection`

指定端口配置。

#### 依赖

指定 `Simulink` 会创建以下端口：

- `BSpd`
- `FSpd`
- `BTrq`
- `FTrq`

指定 `Two-way connection` 会创建以下端口：

- `B`
- `F`

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **值**：| `Simulink`（默认）| `Two-way connection` |
| **Data Types:** | `character vector` |

### **Efficiency factors** — 指定配置 `Constant`（默认）| `Driveshaft torque, speed and temperature`

要计入模块效率，请使用 **Efficiency factors** 参数。下表总结了每种设置下的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和传动轴转速的函数。使用以下参数指定查找表和断点：  - **Efficiency lookup table,   eta\_tbl** - **Efficiency torque breakpoints,   Trq\_bpts** - **Efficiency speed breakpoints,   omega\_bpts** - **Efficiency temperature breakpoints,   Temp\_bpts**    对于空气温度，您可以：  - 选择 **Input ambient temperature** 以   创建输入端口。 - 设置 **Ambient temperature, Tamb**   参数值。    要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅 Interpolation Methods。 |

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `input_config` |
| **值**：| `Constant`（默认）| `Driveshaft torque, speed and temperature` |
| **Data Types:** | `character vector` |

### **Interpolation method** — 方法 `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline`

有关详细信息，请参阅 Interpolation Methods。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InterpMethod` |
| **值**：| `Flat` | `Nearest` | `Linear point-slope` | `Linear Lagrange` | `Cubic spline` |
| **Data Types:** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Output shaft rotates in same direction as input** — 旋转 `off`（默认）| `on`

选择此项以指定输出轴与输入轴旋转方向相同。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `dirSwitch` |
| **值**：| `off`（默认）| `on` |
| **Data Types:** | `character vector` |

### **Input ambient temperature** — 创建输入端口 `off`（默认）| `on`

选择此项以创建用于环境空气温度的输入端口 `AirTemp`。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `extTamb` |
| **值**：| `off`（默认）| `on` |
| **Data Types:** | `character vector` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为
`Driveshaft torque, speed and temperature`。

### **Input to output gear ratio, N** — 传动比 `2`（默认）| 正标量

基础轴与从动轴的齿轮传动比，无量纲。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `N` |
| **值**：| `2`（默认）| 正标量 |
| **Data Types:** | `double` |

### **Input shaft inertia, J1** — 惯量 `.01`（默认）| 正标量

基础轴惯量，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `J1` |
| **值:** | `.01`（默认）| 正标量 |
| **数据类型:** | `double` |

### **输出轴惯量，J2** — 惯量 `.01`（默认）| 正标量

从动轴惯量，单位为 kg·m^2。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `J2` |
| **值:** | `.01`（默认）| 正标量 |
| **数据类型:** | `double` |

### **输入轴阻尼，b1** — 阻尼 `.001`（默认）| 正标量

基础粘性轴阻尼，单位为 N·m· s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `b1` |
| **值:** | `.001`（默认）| 正标量 |
| **数据类型:** | `double` |

### **输出轴阻尼，b2** — 阻尼 `.001`（默认）| 正标量

从动粘性轴阻尼，单位为 N·m· s/rad。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `b2` |
| **值:** | `.001`（默认）| 正标量 |
| **数据类型:** | `double` |

### **输入轴初始速度，w1\_o** — 初始速度 `0`（默认）| 大于或等于 0 的标量

基础轴初始速度，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `w1_o` |
| **值:** | `0`（默认）| 大于或等于 0 的标量 |
| **数据类型:** | `double` |

#### 效率

### **恒定效率因子，eta** — 效率 `1`（默认）| 正标量

恒定效率，*η*。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `eta` |
| **值:** | `1`（默认）| 正标量 |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为 `Constant`。

### **效率查找表，eta\_tbl** — 查找表 `M`×`N`×`L` 数组

效率值的无量纲数组，作为以下量的函数：

- `M` 个输入扭矩
- `N` 个输入转速
- `L` 个空气温度

每个值指定了特定扭矩、转速和温度组合下的效率。数组大小必须与扭矩、转速和温度断点向量定义的维度匹配。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `eta_tbl` |
| **值:** | `M`×`N`×`L` 数组 |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请将 **效率因子** 设置为 `Driveshaft torque, speed and temperature`。

### **效率扭矩断点，Trq\_bpts** — 扭矩断点 `[25, 50, 75, 100, 150, 200, 250]`（默认）| `1`×`M` 向量

输入扭矩向量，效率的断点，单位为 N·m。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Trq_bpts` |
| **值：** | `[25, 50, 75, 100, 150, 200, 250]`（默认）| `1`×`M` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency speed breakpoints, omega\_bpts** — 速度断点 `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `1`×`N` 向量

效率的速度断点向量，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_bpts` |
| **值：** | `[52.4 78.5 105 131 157 183 209 262 314 419 524]`（默认）| `1`×`N` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Efficiency temperature breakpoints, Temp\_bpts** — 温度断点 `[290 358]`（默认）| `1`×`L` 向量

效率的环境温度断点向量，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Temp_bpts` |
| **值：** | `[290 358]`（默认）| `1`×`L` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。

### **Air temperature, Tair** — 环境空气温度 `297.15`（默认）| 大于 0 的标量

环境空气温度 *Tair*，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tair` |
| **值：** | `297.15`（默认）| 大于 0 的标量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数：

- 将 **Efficiency factors** 设置为 `Driveshaft torque, speed and temperature`。
- 清除 **Input ambient temperature**。

## 所属库

Powertrain Blockset / Drivetrain / Couplings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

理想旋转齿轮箱

Gearbox 模块实现理想旋转齿轮箱。该模块使用齿轮惯量和阻尼来计算对基齿轮和从动齿轮对输入扭矩的速度响应。

在燃油经济性和动力总成效率研究中，您可以使用 Gearbox 模块来建模理想齿轮耦合以及常见传动系统元件（如变速器、发动机、离合器和差速器）之间的功率传递。

Gearbox 模块使用以下方程来近似传动动力学。

ω˙BJB=ωBbB+ηNTFω˙FJF=ωFbF+ηTF

该约束方程将系统简化为单自由度系统。

ωB=NωF

为表达理想扭矩传递，该模块使用以下关系。

ηNTB+TF=0

### 效率

要计入模块效率，请使用 **Efficiency factors** 参数。下表总结了每种设置对应的模块实现。

| 设置 | 实现 |
| --- | --- |
| `Constant` | 恒定效率，可通过 **Constant efficiency factor, eta** 参数设置。 |
| `Driveshaft torque, temperature and speed` | 效率作为基础齿轮输入扭矩、空气温度和传动轴转速的函数。使用以下参数指定查找表和断点： - **Efficiency lookup table, eta\_tbl** - **Efficiency torque breakpoints, Trq\_bpts** - **Efficiency speed breakpoints, omega\_bpts** - **Efficiency temperature breakpoints, Temp\_bpts** 对于空气温度，您可以： - 选择 **Input ambient temperature** 以创建输入端口。 - 设置 **Ambient temperature, Tamb** 参数值。 要选择插值方法，请使用 **Interpolation method** 参数。有关详细信息，请参阅插值方法。 |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率 - 正信号表示流入模块 - 负信号表示流出模块 | `PwrBase` | 来自基础轴的机械功率 | *PBase* | PBase= ηTBωB |
| `PwrFlwr` | 来自从动轴的机械功率 | *PFlwr* | PFlwr= ηTFωF |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率 - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 总功率损失 | *Png* | Png= −(Pt+Pd)+PsPt=ηTBωB+ηTFωF |
| `PwrDampLoss` | 阻尼导致的功率损失 | *Pd* | Pd=−(bF|ωF|2+bB|ωB|2) |
| `PwrStored` — 存储能量的变化率 - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储的内部动能变化率 | *Ps* | Ps=(ωBω˙BJB+ωFω˙FJF) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *TB* | 基础齿轮输入扭矩 |
| *TF* | 从动齿轮输出扭矩 |
| *ωB* | 基础齿轮角速度 |
| *ωF* | 从动齿轮角速度 |
| *JB* | 基础齿轮转动惯量 |
| *JF* | 从动齿轮转动惯量 |
| *bB* | 基础齿轮旋转粘性阻尼 |
| *bF* | 从动齿轮旋转粘性阻尼 |
| *N* | 扭矩传输齿轮比 |
| *η* | 齿轮效率 |
| *Pt* | 总功率 |
| *Pd* | 阻尼导致的功率损失 |
| *Ps* | 存储的内部动能变化率 |
