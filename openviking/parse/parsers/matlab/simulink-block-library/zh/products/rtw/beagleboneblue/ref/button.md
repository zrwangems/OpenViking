---
type: simulink-block
title: 'Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'button'
documentation_source_path: 'beagleboneblue/ref/button.html'
language: zh-CN
chinese_source: worker-translation
---

# Button

## 端口

### 输出

### **Port\_1** — 按钮的逻辑状态，标量

当硬件上由 **Button** 参数指定的按钮被按下时，模块输出 `1`。当硬件上由 **Button** 参数指定的按钮被释放时，模块输出 `0`。例如，如果 Block Parameters 对话框中的 **Button** 参数设置为 `Mode`，并且硬件上的 Mode 按钮被按下，则模块输出 `1`。当 Mode 按钮被释放时，模块输出 `0`。

**数据类型：** `uint8`

## 参数

### **Button** — 硬件按钮 `Mode`（默认） | `Pause`

选择要读取其逻辑状态（按下或释放）的按钮。

### **Sample time** — 模块读取按钮状态的时间间隔 `0.1`（默认）

指定模块读取由 **Button** 参数指定的按钮状态的频率。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017b 中引入**

## 描述

读取按钮的逻辑状态

Button 模块读取硬件上用户可配置按钮的逻辑状态。该硬件有两个用户可配置按钮，Mode 和 Pause，具有两种逻辑状态：按下和释放。

在没有硬件的仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
