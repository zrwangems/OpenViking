---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'dcmotor'
documentation_source_path: 'vexv5/ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

### 输入

### **Port\_1** — 输入模拟信号，用于以 [ –128 127] 范围内的整数设置电机速度

模块输入值的范围可以为 –128 到 127。符号决定电机的旋转方向，幅值决定速度。模块输入值为 `0` 时会使电机停止。

**数据类型：** `double`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的 smart port `None`（默认）| `1` 到 `21`

如果使用 3-Wire Expander，请指定 VEX EDR V5 Robot Brain 上扩展器所连接的 smart port。

### **Port** — 选择连接到直流电机的 3 线端口 `A`（默认）| `A` 到 `H`

选择 VEX EDR V5 Robot Brain 上连接到直流电机的 3 线端口。

不要在同一模型中将同一端口号分配给多个 DC Motor 模块。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示已连接的直流电机并设置电机速度

DC Motor 模块表示一个连接到 VEX® EDR V5 Robot Brain 上指定 3 线端口的直流电机。输入信号设置电机速度。VEX EDR V5 Robot Brain 上有八个 3 线端口，可连接到直流电机。
