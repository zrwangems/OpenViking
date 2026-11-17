---
type: simulink-block
title: 'SRM Hysteresis Current Controller'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control'
documentation_page: 'srmhysteresiscurrentcontroller'
documentation_source_path: 'ref/srmhysteresiscurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# SRM Hysteresis Current Controller

## 端口

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **iabc** — 测量电流向量

测得的三相电流。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **theta** — Theta 转子角度标量

转子角度，位于区间 [0, *β* ] 内。

**数据类型：** `single` | `double`

### **thetaON** — 开通角标量

用于接通相供电的角度。

**数据类型：** `single` | `double`

### **thetaOFF** — 关断角标量

用于关断相供电的角度。

**数据类型：** `single` | `double`

### 输出

### **Sabc** — 电压开关信号向量 | `0 or 1`

用于接通和关断三相电压的信号。

**数据类型：** `single` | `double`

## 参数

### **转矩能力角 (rad)** — 转矩能力角 pi/2（默认） | [0, 2\*pi/转子磁极数]

一个转子磁极的转矩产生能力，以弧度为单位。

### **滞环带宽 (A)** — 滞环带宽 `5`（默认）

电流控制器的滞环带宽，*h*。开通点为 *h*/2，关断点为 -*h*/2。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认） | 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续可变步长模型中，请使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / SRM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

开关磁阻电机的滞环电流控制

SRM Hysteresis Current Controller 模块为 Switched Reluctance Machine (SRM) 模块实现滞环电流控制。
