---
type: simulink-block
title: 'Latch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'latch'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/latch.html'
language: zh-CN
chinese_source: worker-translation
---

# Latch

## 端口

R2025b 中未记录。

## 参数

**初始输出为 1 时选中，为 0 时取消选中**
:   此参数仅适用于仿真行为。如果初始输出值必须为 1，请选中此复选框。否则，初始输出值为
    0。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**自 R2018b 起引入**

## 描述

根据输入信号的变化锁存逻辑值

根据输入信号在零值和非零值之间的变化锁存逻辑值。每当输入信号发生上升沿跳变时，
Latch 都会在 1 和 0 之间切换。当使用此模块锁存 Gamepad Button 模块的输出时，
按下指定按钮会使输出在 1 和 0 之间切换。释放按钮时，输出不会切换。例如，可在模型中使用此模块，通过按下
按钮将机器人手臂或机械爪的角位置锁存为特定值。再次按下该按钮可切换回原始位置。
