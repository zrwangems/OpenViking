---
type: simulink-block
title: 'DCT Controller'
family: 'transmission'
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

### **GearReq** — 要接合的挡位编号 `scalar`

挡位编号请求，*Greq*。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 |
| --- | --- | --- |
| `GearReq` | 挡位编号请求 | *Greq* |
| `GearEngd` | 控制器指令的标称挡位 | *Go* |
| `GearEffct` | 有效挡位 | NA |
| `CltchACmd` | 奇数挡的离合器压力命令，介于 `0` 和 `1` 之间 | NA |
| `CltchBCmd` | 偶数挡的离合器压力命令，介于 `0` 和 `1` 之间 | NA |

### **NomGear** — 用于换挡的标称挡位 `scalar`

用于换挡的标称挡位。Dual Clutch Transmission 模块使用此信号来平滑应用惯性、效率、传动比和阻尼参数。

### **CltchACmd** — 奇数挡命令 `scalar`

奇数挡的离合器压力命令，介于 `0` 和 `1` 之间。

### **CltchBCmd** — 偶数挡命令 `scalar`

偶数挡的离合器压力命令，介于 `0` 和 `1` 之间。

## 参数

### **初始挡位, G\_o** — 接合挡位 `0`（默认） | `scalar`

要接合的初始挡位，*Go*。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **离合器致动时间, tc** — 时间 `.1`（默认） | `scalar`

在换挡事件期间接合和分离离合器所需的时间，*tc*，以 s 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tc` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **同步器时间, ts** — 时间 `.01`（默认） | `scalar`

挡位选择和同步所需的时间，*ts*，以 s 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ts` |
| **值：** | `.01`（默认） | `scalar` |
| **数据类型：** | `double` |

### **采样周期, dt** — 时间 `-1`（默认） | `scalar`

采样周期，*dt*，以 s 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dt` |
| **值：** | `-1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **在离合器锁止状态下开始仿真** — 选择以初始锁定离合器 `off`（默认） | `on`

选择此参数将初始锁定离合器。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClutchLocked` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **在同步器锁止状态下开始仿真** — 选择以初始锁定同步器 `off`（默认） | `on`

选择此参数将初始锁定同步器。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SynchLocked` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

## 所属库

Powertrain Blockset / Transmission / Transmission Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

双离合器变速器控制器

DCT Controller 模块实现双离合器变速器（DCT）控制器。您可以指定离合器打开、关闭和同步定时参数。该模块使用基于积分器的计时器和锁存逻辑确定离合器命令，这些计时器和逻辑基于指定的定时参数和挡位请求。
