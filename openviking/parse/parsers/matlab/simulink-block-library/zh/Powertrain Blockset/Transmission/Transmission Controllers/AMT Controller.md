---
type: simulink-block
title: 'AMT Controller'
family: 'transmission'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Transmission Controllers'
documentation_page: 'amtcontroller'
documentation_source_path: 'ref/amtcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# AMT Controller

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
| `Cltch` | 用于挡位的离合器压力指令，介于 `0` 和 `1` 之间 | NA |

### **GearEffct** — 用于换挡的有效挡位 `scalar`

用于换挡的有效挡位。该模块使用此信号来平滑应用惯性、效率、传动比和阻尼参数。

### **Cltch** — 离合器压力指令 `scalar`

离合器压力指令，介于 `0` 和 `1` 之间。

## 参数

### **初始挡位, G\_o** — 接合的挡位 `0` (default) | `scalar`

要接合的初始挡位，*Go*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `G_o` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **离合器执行时间, tc** — 时间 `.1` (default) | `scalar`

换挡事件期间接合和分离离合器所需的时间，*tc*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tc` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **同步器时间, ts** — 时间 `.01` (default) | `scalar`

挡位选择和同步所需的时间，*ts*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ts` |
| **值：** | `.01` (default) | `scalar` |
| **数据类型：** | `double` |

### **采样周期, dt** — 时间 `-1` (default) | `scalar`

采样周期，*dt*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `dt` |
| **值：** | `-1` (default) | `scalar` |
| **数据类型：** | `double` |

### **仿真开始时离合器锁止** — 选择以在初始时锁止离合器 `off` (default) | `on`

选择此参数会在初始时锁止离合器。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ClutchLocked` |
| **值：** | `off` (default) | `on` |
| **数据类型：** | `character vector` |

### **仿真开始时同步器锁止** — 选择以在初始时锁止同步器 `off` (default) | `on`

选择此参数会在初始时锁止同步器。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SynchLocked` |
| **值：** | `off` (default) | `on` |
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

具有离合器打开、关闭和同步定时的自动手动变速器控制器

AMT Controller 模块实现自动手动变速器（AMT）控制器。您可以指定离合器打开、关闭和同步定时参数。该模块使用基于积分器的定时器和锁存逻辑确定离合器指令，这些逻辑基于指定的定时参数和挡位请求。
