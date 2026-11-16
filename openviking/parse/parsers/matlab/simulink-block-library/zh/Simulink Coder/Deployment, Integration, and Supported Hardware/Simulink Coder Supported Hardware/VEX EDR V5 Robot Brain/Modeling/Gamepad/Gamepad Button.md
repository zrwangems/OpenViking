---
type: simulink-block
title: 'Gamepad Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Gamepad'
documentation_page: 'gamepadbutton'
documentation_source_path: 'vexv5/ref/gamepadbutton.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamepad Button

## 端口

### 输出

### **Port\_1** — 具有逻辑值（1 或 0）的输出端口 `1` 或 `0`

按下按钮时，模块输出为 1；否则（按钮处于释放状态时），模块输出为 0。

**数据类型：** `Boolean`

## 参数

### **Gamepad type** — 选择游戏手柄控制的类型 `Primary`（默认） | `Partner`

您可以使用一对 VEX V5 Controller 游戏手柄来控制连接到 VEX EDR V5 Robot Brain 的外设。

### **Button** — 选择 V5 Controller 游戏手柄上的一个按钮 `R1`（默认）

在进行选择之前，请查看 VEX V5 Controller 游戏手柄上按钮的标签。

### **Sample time** — 获取按钮逻辑值的采样时间 `0.02`（默认） | seconds

指定 Gamepad Button 模块读取按钮逻辑值的频率。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定为该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Gamepad

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示 VEX V5 Controller 游戏手柄上的 12 个按钮之一，并读取该按钮的逻辑值

Gamepad Button 模块用于表示 VEX® V5 Controller 游戏手柄上的 12 个按钮之一，并根据按钮是按下还是释放来读取相应的逻辑值（1 或 0）。
