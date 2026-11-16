---
type: simulink-block
title: 'Logitech G29 Steering Wheel'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / I/O Connectivity / Logitech G29 Steering Wheel'
documentation_page: 'logitechg29steeringwheel'
documentation_source_path: 'io_ref/logitechg29steeringwheel.html'
language: zh-CN
chinese_source: official
---

# Logitech G29 Steering Wheel

## 端口

### 输出

### **Buttons** — 方向盘按钮状态 0（=未按下） | 1（=按下）

`Buttons` 的输出是一个布尔值向量，用于指示方向盘上按钮的状态。向量中按钮值的顺序为：

1. Square
2. X
3. Circle
4. Triangle
5. LPaddle
6. RPaddle
7. L2
8. R2
9. L3
10. R3
11. Share
12. Option
13. PS

**数据类型:** `Boolean`

### **Steering** — 方向盘位置的值 0（=最左侧） | 65535（=最右侧）

`Steering` 输出值表示方向盘的位置。

**数据类型:** `uint16`

### **Pedals** — 油门、刹车和离合器踏板状态 0（=未踩下） | 255（=完全踩下）

`Pedals` 的输出是一个值向量，用于指示油门、刹车和离合器踏板的状态。向量中踏板值的顺序为：

1. 节流阀
2. 制动器
3. 离合器

**数据类型:** `uint8`

### **Direction** — 方向盘方向键按钮状态 0（=上） | 2（=右） | 4（=下） | 6（=左） | 8（=未按下）

`Direction` 输出值表示方向键被按下。当您按下方向键时，在方向键按钮之间会出现中间值。

**数据类型:** `uint8`

### **Status** — 方向盘通信状态 0 (默认) | 负值

`Status` 输出值表示与方向盘通信成功（0）或通信失败（负值）。

**数据类型:** `int32`

## 参数

### **sampleTime** — 方向盘数据采样时间 -1（继承） (默认)

选择方向盘数据的采样时间。推荐的 `sampleTime` 为 10 毫秒。

#### 编程用法

|  |
| --- |
| **模块参数：**`sampleTime` |

## 所属库

Simulink Real-Time / Logitech G29

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018b 中推出**

## 描述

接收 Logitech G29 方向盘读取数据

Logitech G29 Steering Wheel 模块从 Logitech® G29 方向盘（仅限 PS3）读取数据。该模块不支持手动变速器模块。

**注意**

将罗技 G29 方向盘设备连接到目标计算机的 USB 端口。
