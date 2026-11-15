---
type: simulink-block
title: 'Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'button'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/button.html'
language: zh-CN
chinese_source: worker-translation
---

# Button

## 端口

### 输出

### **Status** — EV3 主控按钮的状态 `0` | `1`

此模块输出 LEGO
MINDSTORMS EV3 主控按钮的状态。

- `0` — 表示未按下 EV3 主控按钮。
- `1` — 表示已按下 EV3 主控按钮。

**数据类型：** `uint8`

## 参数

### **Button** — EV3 主控按钮 `Up`（默认）| `Center` | `Down` | `Right` | `Left`

选择要确定其状态的 LEGO
MINDSTORMS EV3 主控按钮。

### **采样时间** — 模块读取 EV3 主控按钮状态的时间间隔 `0.1`（默认）| 正整数

指定模块读取 EV3 主控按钮状态的频率。
较短的采样时间（如 `0.01`）可能会产生不可靠的
测量结果。

较小的采样时间要求处理器在更短的时间内完成相同数量的
指令，这可能导致任务超限。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

检测 EV3 主控按钮的状态

使用 Button 模块检测 LEGO®
MINDSTORMS® EV3 主控按钮是否按下。您可以将模块配置为检测
center、left、right、up 和 down 按钮的状态。但是，您无法将模块配置为
检测 back 按钮的状态，因为 EV3 主控保留该按钮用于停止和关闭
程序。

在无硬件的仿真期间，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
