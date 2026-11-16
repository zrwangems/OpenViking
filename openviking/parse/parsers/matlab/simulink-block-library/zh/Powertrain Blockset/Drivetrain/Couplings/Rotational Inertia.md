---
type: simulink-block
title: 'Rotational Inertia'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'rotationalinertia'
documentation_source_path: 'ref/rotationalinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Inertia

## 端口

### 输入

### **RTrq** — 输入扭矩 `scalar`

施加的输入驱动轴扭矩，*TR*，单位为 N·m。

#### 依赖关系

要启用此端口，请在 **端口配置** 中选择 `Simulink`。

### **CTrq** — 输出扭矩 `scalar`

负载驱动轴扭矩，*TC*，单位为 N·m。

#### 依赖关系

要启用此端口，请在 **端口配置** 中选择 `Simulink`。

### **R** — 角速度和扭矩双向连接端口

角速度单位为 rad/s。扭矩单位为 N·m。

#### 依赖关系

要启用此端口，请在 **端口配置** 中选择 `Two-way connection`。

### **Inertia** — 输入 `scalar`

转动惯量，单位为 kg·m^2。

#### 依赖关系

要创建 `Inertia` 端口，请选择 **外部惯量输入**。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| Trq | `R` | | 施加的输入驱动轴扭矩 | *TR* | N·m |
| `C` | | 输出驱动轴扭矩 | *TC* | N·m |
| `Damp` | | 阻尼扭矩 | *Td*=*b**ω* | N·m |
| Spd | | | 驱动轴角速度 | *ω* | rad/s |
| PwrInfo | `PwrTrnsfrd` | `PwrR` | 来自基础轴的机械功率 | *PTR* | W |
| `PwrC` | 来自从动轴的机械功率 | *PTC* | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 由于阻尼导致的功率损失 | *Pd* | W |
| `PwrStored` | `PwrStoredShft` | 存储的内部扭转能量的变化率 | *Ps* | W |

#### 依赖关系

要启用此端口，请选择 **输出 Info 总线**。

### **Spd** — 驱动轴速度 `scalar`

驱动轴角速度，*ω*，单位为 rad/s。

#### 依赖关系

要启用此端口，请在 **端口配置** 中选择 `Simulink`。

### **C** — 角速度和扭矩双向连接端口

角速度单位为 rad/s。扭矩单位为 N·m。

#### 依赖关系

要启用此端口，请在 **端口配置** 中选择 `Two-way connection`。

## 参数

#### 模块选项

### **端口配置** — 指定配置 `Simulink` （默认） | `Two-way connection`

指定端口配置。

#### 依赖关系

指定 `Simulink` 会创建以下端口：

- `RTrq`
- `CTrq`
- `Spd`

指定 `Two-way connection` 会创建以下端口：

- `R`
- `C`

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Simulink` （默认） | `Two-way connection` |
| **数据类型：** | `character vector` |

### **输出 Info 总线** — 选择 `off` （默认） | `on`

选择以创建 `Info` 输出端口。

### **外部惯量输入** — 输入转动惯量 `off` （默认） | `on`

输入转动惯量。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `externJ` |
| **值：** | `off` （默认） | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建 `Inertia` 端口，请选择 **外部惯量输入**。

#### 参数

### **转动惯量, J** — 惯量 `.01` （默认） | scalar 大于或等于 0

转动惯量，单位为 kg·m^2。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J` |
| **值：** | `.01` （默认） | scalar 大于或等于 0 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请清除 **外部惯量输入**。

### **扭转阻尼, b** — 阻尼 `.001` （默认） | scalar 大于或等于 0

扭转阻尼，单位为 N·m· s/rad。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bc` |
| **值：** | `.001` （默认） | scalar 大于或等于 0 |
| **数据类型：** | `double` |

### **初始速度, omega\_o** — 角 `0` （默认） | scalar 大于或等于 0

初始角速度，单位为 rad/s。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_o` |
| **值：** | `0` （默认） | scalar 大于或等于 0 |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

理想机械转动惯量

Rotational Inertia 模块实现理想机械转动惯量。

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrR` | 来自基础轴的机械功率 | *PTR* | PTR= TRω |
| `PwrC` | 来自从动轴的机械功率 | *PTC* | PTC= TCω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 由于阻尼导致的功率损失 | *Pd* | Pd=−b|ω|2 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredShft` | 存储的内部扭转能量的变化率 | *Ps* | Ps=ωω˙J |

方程使用以下变量。

|  |  |
| --- | --- |
| *TR* | 输入扭矩 |
| *TC* | 输出扭矩 |
| *ω* | 驱动轴角速度 |
| *J* | 转动惯量 |
| *b* | 旋转粘性阻尼 |
| *Pd* | 由于阻尼导致的功率损失 |
| *Ps* | 存储的内部扭转能量的变化率 |
