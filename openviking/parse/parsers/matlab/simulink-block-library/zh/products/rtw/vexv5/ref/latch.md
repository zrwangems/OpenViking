---
type: simulink-block
title: 'Latch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'latch'
documentation_source_path: 'vexv5/ref/latch.html'
language: zh-CN
chinese_source: worker-translation
---

# Latch

## 端口

R2025b 中未提供文档。

## 参数

**如果初始输出为 1，则选中；如果为 0，则取消选中**
:   此参数仅适用于仿真行为。如果初始输出值必须为 1，请选中此复选框。否则，初始输出值为
    0。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2018b 中引入**

## 描述

根据输入信号的变化锁存逻辑值

根据输入信号在零值和非零值之间的变化锁存逻辑值。对于输入信号的每次上升沿跳变，Latch 模块都会在 1 和 0 之间切换。当使用此模块锁存 Gamepad Button 模块的输出时，按下指定按钮，输出就会在 1 和 0 之间切换。释放按钮时，输出不会切换。例如，可在模型中使用此模块，通过按下按钮将机器人手臂或夹爪的角位置锁存为特定值。再次按下按钮即可切换回原始位置。
