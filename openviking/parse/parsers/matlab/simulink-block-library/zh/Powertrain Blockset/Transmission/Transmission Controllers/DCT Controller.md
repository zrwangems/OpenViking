---
type: simulink-block
title: 'DCT Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Transmission Controllers'
documentation_page: 'dctcontroller'
documentation_source_path: 'ref/dctcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# DCT Controller

## 端口

### 输入

### **GearReq** — 要接合的挡位号 `scalar`

挡位号请求，*Greq*。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 |
| --- | --- | --- |
| `GearReq` | 挡位号请求 | *Greq* |
| `GearEngd` | 控制器指令的标称挡位 | *Go* |
| `GearEffct` | 有效挡位 | NA |
| `CltchACmd` | 奇数挡的离合器压力指令，介于 `0` 和 `1` 之间 | NA |
| `CltchBCmd` | 偶数挡的离合器压力指令，介于 `0` 和 `1` 之间 | NA |

### **NomGear** — 用于换挡的标称挡位 `scalar`

用于换挡的标称挡位。Dual Clutch Transmission 模块
使用此信号来平滑应用惯性、效率、
传动比和阻尼参数。

### **CltchACmd** — 奇数挡指令 `scalar`

奇数挡的离合器压力指令，介于
`0` 和 `1` 之间。

### **CltchBCmd** — 偶数挡指令 `scalar`

偶数挡的离合器压力指令，介于
`0` 和 `1` 之间。

## 参数

### **Initial gear, G\_o** — 接合的挡位 `0` (default) | `scalar`

要接合的初始挡位，
*Go*。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `G_o` |
| **值**：| `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Clutch actuation time, tc** — 时间 `.1` (default) | `scalar`

在换挡事件期间接合和分离离合器所需的时间，
*tc*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `tc` |
| **值**：| `.1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Synchronizer time, ts** — 时间 `.01` (default) | `scalar`

挡位选择和同步所需的时间，
*ts*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ts` |
| **值**：| `.01` (default) | `scalar` |
| **Data Types:** | `double` |

### **Sample period, dt** — 时间 `-1` (default) | `scalar`

采样周期，*dt*，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `dt` |
| **值**：| `-1` (default) | `scalar` |
| **Data Types:** | `double` |

### **Start simulation with clutch locked** — 选择以初始锁定离合器 `off` (default) | `on`

选择此参数将初始锁定离合器。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ClutchLocked` |
| **值**：| `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Start simulation with synchronizer locked** — 选择以初始锁定同步器 `off` (default) | `on`

选择此参数将初始锁定同步器。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SynchLocked` |
| **值**：| `off` (default) | `on` |
| **Data Types:** | `character vector` |

## 所属库

Powertrain Blockset / Transmission / Transmission Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

双离合变速器控制器

DCT Controller 模块实现双离合变速器（DCT）控制器。您可以指定离合器打开、关闭和同步正时参数。该模块使用基于积分器的定时器和基于指定正时参数与挡位请求的锁存逻辑来确定离合器命令。
