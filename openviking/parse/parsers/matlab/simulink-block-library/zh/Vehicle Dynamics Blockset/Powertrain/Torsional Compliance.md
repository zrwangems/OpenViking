---
type: simulink-block
title: 'Torsional Compliance'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Powertrain'
documentation_page: 'torsionalcompliance'
documentation_source_path: 'ref/torsionalcompliance.html'
language: zh-CN
chinese_source: worker-translation
---

# Torsional Compliance

## 端口

### 输入

### **RSpd** — 驱动轴 R 角速度 `scalar`

输入驱动轴角速度，单位为 rad/s。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Simulink`。

### **CSpd** — 驱动轴 C 角速度 `scalar`

输出驱动轴角速度，单位为 rad/s。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Simulink`。

### **R** — 角速度和扭矩双向连接端口

角速度单位为 rad/s。扭矩单位为 N·m。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Two-way connection`。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | 输入驱动轴扭矩 | *TR* | N·m |
| `C` | | 输出驱动轴扭矩 | *TC* | N·m |
| `Damp` | | 阻尼扭矩 | Ts=bθ˙ | N·m |
| `Spring` | | 弹簧扭矩 | *Td* = *k**θ* | N·m |
| Spd | `R` | | 输入驱动轴角速度 | *ωR* | rad/s |
| `C` | | 输出驱动轴角速度 | *ωC* | rad/s |
| `deltadot` | | 输入和输出驱动轴角速度之差 | θ˙ | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | 来自驱动轴 R 的机械功率 | *PTR* | W |
| `PwrC` | 来自驱动轴 C 的机械功率 | *PTC* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 阻尼导致的功率损耗 | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | 存储的内部动能变化率 | *Ps* | W |

#### 依赖关系

要启用此端口，选择 **输出 Info 总线**。

### **RTrq** — 驱动轴 R 扭矩 `scalar`

输入驱动轴扭矩，单位为 N·m。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Simulink`。

### **CTrq** — 驱动轴 C 扭矩 `scalar`

施加的输出驱动轴扭矩，单位为 N·m。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Simulink`。

### **C** — 角速度和扭矩双向连接端口

角速度单位为 rad/s。扭矩单位为 N·m。

#### 依赖关系

要启用此端口，对于 **端口配置**，
选择 `Two-way connection`。

## 参数

#### 模块选项

### **端口配置** — 指定配置 `Simulink`（默认） | `Two-way connection`

指定端口配置。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Simulink`（默认） | `Two-way connection` |
| **数据类型：** | `character vector` |

#### 依赖关系

指定 `Simulink` 会创建这些端口：

- `RSpd`
- `CSpd`
- `RTrq`
- `CTrq`

指定 `Two-way connection` 会创建这些端口：

- `R`
- `C`

### **输出 Info 总线** — 选择 `off`（默认） | `on`

选择以创建 `Info` 输出端口。

### **扭转刚度, k** — 惯性 `1e4`（默认） | 大于或等于 0 的 scalar

扭转刚度，单位为 N·m/rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `k` |
| **值：** | `1e4`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **扭转阻尼, b** — 阻尼 `1e2`（默认） | 大于或等于 0 的 scalar

扭转阻尼，单位为 N·m· s/rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `b` |
| **值：** | `1e2`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **初始偏转, theta\_o** — 角度 `0`（默认） | 大于或等于 0 的 scalar

初始偏转，单位为 rad。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `theta_o` |
| **值：** | `0`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **初始速度差, domega\_o** — 角度 `0`（默认） | 大于或等于 0 的 scalar

初始速度差，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `domega_o` |
| **值：** | `0`（默认） | 大于或等于 0 的 scalar |
| **数据类型：** | `double` |

### **阻尼截止频率, omega\_c** — 频率 `3000`（默认） | 正 scalar

阻尼截止频率，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_c` |
| **值：** | `3000`（默认） | 正 scalar |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

并联弹簧-阻尼器

Torsional Compliance 模块实现并联弹簧-阻尼器，以耦合两个旋转驱动轴。该模块使用驱动轴角速度、扭转刚度和扭转阻尼来确定扭矩。

TR=−(ωR−ωC)b−θkTC=(ωR−ωC)b+θkθ˙=(ωR−ωC)

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrR` | 来自驱动轴 R 的机械功率 | *PTR* | PTR= TRωR |
| `PwrC` | 来自驱动轴 C 的机械功率 | *PTC* | PTC= Tcωc |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrDampLoss` | 机械阻尼损耗 | *Pd* | Pd=−b|θ˙|2 |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 弹簧能量变化率 | *PS* | Ps=−θkθ˙ |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *TR* | 驱动轴 R 扭矩 |
| *TC* | 驱动轴 C 扭矩 |
| *ωR* | 驱动轴 R 角速度 |
| *ωC* | 驱动轴 C 角速度 |
| *θ* | 耦合驱动轴旋转 |
| *k* | 驱动轴扭转刚度 |
| *b* | 旋转粘性阻尼 |
| *Pd* | 阻尼导致的功率损耗 |
| *Ps* | 存储的弹簧能量变化率 |
