---
type: simulink-block
title: 'Status Light'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'statuslight'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/statuslight.html'
language: zh-CN
chinese_source: worker-translation
---

# Status Light

## 端口

### 输入

### **Status light** — 设置 EV3 程序块按钮的状态灯 integer

该模块输入这些值，以设置 EV3 程序块按钮的状态灯。

- `0` — Off
- `1` — 将 EV3 程序块的状态灯颜色设置为常亮绿色。
- `2` — 将 EV3 程序块的状态灯颜色设置为常亮红色。
- `3` — 将 EV3 程序块的状态灯颜色设置为常亮橙色。
- `4` — 将 EV3 程序块的状态灯颜色设置为脉冲绿色。
- `5` — 将 EV3 程序块的状态灯颜色设置为脉冲红色。
- `6` — 将 EV3 程序块的状态灯颜色设置为脉冲橙色。
- 其他值 — Off

该模块会转换其接收到的值的数据类型。您无需转换输入信号的数据类型。

**数据类型：** `int8`

## 参数

R2025b 中未记录。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

控制 EV3 程序块上的状态灯

使用 Status Light 模块控制 EV3 程序块上按钮背后的状态灯的颜色和效果。

在没有硬件的仿真期间，该模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
