---
type: simulink-block
title: 'Digital Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-R Processors / Modeling'
documentation_page: 'digitalwrite'
documentation_source_path: 'armcortexr/ref/digitalwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Write

## 端口

### 输入

### **Port\_1** — 所选 GIO 引脚的非负标量逻辑值

所选 GIO 引脚的逻辑值，指定为 Simulink® 信号。此端口接受任何数据类型的信号，并在内部将其转换为 `boolean`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **Pin** — GIO 引脚 `GIOB_6 (LED 2)`（默认） | `GIOB_7 (LED 3)`

选择 Texas Instruments Hercules RM57Lx Launchpad 硬件板上要写入逻辑状态的 `GIO` 引脚。

#### 编程使用

|  |
| --- |
| **模块参数：** `Whichpin` |

## 所属库

Embedded Coder Support Package for ARM Cortex-R Processors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将值写入 Texas Instruments Hercules RM57Lx 微控制器上的 GIOB[6] 或 GIOB[7] 引脚

将逻辑值写入基于 ARM® Cortex®-R 处理器内核的 Texas Instruments® Hercules `RM57Lx` 微控制器的 `GIOB[6]` 或 `GIOB[7]` 引脚。

`GIOB[6]` 或 `GIOB[7]` 引脚分别连接到 Texas Instruments Hercules RM57Lx Launchpad 硬件板上的 `LED 2` 和 `LED 3`。
