---
type: simulink-block
title: 'Digital Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-R Processors / Modeling'
documentation_page: 'digitalread'
documentation_source_path: 'armcortexr/ref/digitalread.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Read

## 端口

### 输出

### **Port\_1** — 指定 GIO 引脚逻辑值的 boolean 标量

指定 GIO 引脚逻辑值，以 boolean 标量形式返回。

**数据类型：** `uint32`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **Pin** — GIO 引脚 `GIOB_4 (User Switch A)`（默认）| `GIOB_5 (User Switch B)`

选择要从中读取逻辑状态的 Texas Instruments Hercules RM57Lx Launchpad 硬件板上的 `GIO` 引脚。

#### 编程用法

|  |
| --- |
| **模块参数：** `Whichpin` |

## 所属库

Embedded Coder Support Package for ARM Cortex-R Processors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从 Texas Instruments Hercules RM57Lx 微控制器上的 GIOB[4] 或 GIOB[5] 引脚读取值

从基于 ARM® Cortex®-R 处理器内核的 Texas Instruments® Hercules `RM57Lx` 微控制器的 `GIOB[4]` 或 `GIOB[5]` 引脚读取逻辑值。

Digital Read 模块输出 `uint32` 类型的信号。

`GIOB[4]` 或 `GIOB[5]` 引脚分别连接到 Texas Instruments Hercules RM57Lx Launchpad 硬件板上的 `User Switch A` 和 `User Switch B`。
