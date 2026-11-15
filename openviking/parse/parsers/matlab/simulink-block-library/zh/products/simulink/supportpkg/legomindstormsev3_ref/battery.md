---
type: simulink-block
title: 'Battery'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'battery'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/battery.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery

## 端口

### 输出

### **voltage** — EV3 brick 电池电压标量

该模块以 millivolts 为单位输出 LEGO MINDSTORMS EV3 brick 的电池电压。

**数据类型：** `uint16`

## 参数

### **采样时间** — 模块读取 EV3 brick 电池电压的时间间隔 `0.1`（默认）| 正整数

指定模块读取 EV3 brick 电池值的频率。
较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

测量 EV3 brick 中电池的电压水平

使用 Battery 模块测量 LEGO® MINDSTORMS® EV3 brick 中电池的电压，单位为 millivolts。例如，当六节 1.5-volt 电池完全充满电时，输出值约为 `9000` millivolts。

在没有硬件的仿真期间，该模块输出零。请参阅模块在仿真中产生零或不执行任何操作。
