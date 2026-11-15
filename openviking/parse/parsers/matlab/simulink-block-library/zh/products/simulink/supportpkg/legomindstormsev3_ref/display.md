---
type: simulink-block
title: 'Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'display'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/display.html'
language: zh-CN
chinese_source: worker-translation
---

# Display

## 端口

### 输入

### **Data** — 要在 EV3 显示屏上显示的数据：正整数或负整数、字符数组

该模块输入要在 EV3 上显示的数据。

**数据类型：** `int32`

## 参数

### **Label** — 静态标签字符

输入静态标签。EV3 主机在输入值左侧显示该前缀。前缀长度不能超过 8 个字符。例如，要显示 EVR Button 的状态，请输入 `Button:`。

### **Row** — EV3 显示屏行号 `1` (默认) | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10`

选择要在其上显示数字的 EV3 显示屏行号。行 1 表示 EV3 显示屏的顶部，行 10 表示底部。

### **Format** — 显示格式 `Decimal` (默认) | `Hex`

选择要在 EV3 主机上显示的数字格式。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

在 EV3 显示屏上显示标签和整数

使用 Display 模块在 EV3 显示屏的特定行上显示整数或标签。

在没有硬件的仿真期间，此模块不执行任何操作。请参阅模块在仿真中产生零值或不执行任何操作。
