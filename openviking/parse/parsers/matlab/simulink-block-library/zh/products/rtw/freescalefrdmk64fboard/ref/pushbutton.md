---
type: simulink-block
title: 'Push Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'pushbutton'
documentation_source_path: 'freescalefrdmk64fboard/ref/pushbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Push Button

## 端口

### 输出

### **Port\_1** — 按钮的逻辑状态（标量）

当按下开关时，模块输出 `1`。
否则输出 `0`

**数据类型：** `uint8`

## 参数

### **Switch** — 用于读取逻辑状态的开关 `SW2`（默认） | `SW3`

选择要读取其逻辑状态的开关。

### **Sample time** — 读取按钮状态的频率 `-1`（默认）

指定 Push Button 模块读取你在 **Switch** 参数中选择的按钮状态的频率。默认情况下，该模块根据模型内该模块的上下文继承其采样时间。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

读取 Push button 的逻辑状态

Push Button 模块读取 FRDM-K64F 板上可用的按钮 SW2 或 SW3 的逻辑状态（按下或释放）。SW2 按钮连接到板上的 PTC6 引脚。SW3 按钮连接到板上的 PTA4 引脚。当按下该开关时，模块输出 `1`。否则输出 `0`。
