---
type: simulink-block
title: 'Logitech G29 Steering Wheel'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Logitech G29'
documentation_page: 'logitechg29steeringwheel'
documentation_source_path: 'io_ref/logitechg29steeringwheel.html'
language: zh-CN
chinese_source: worker-translation
---

# Logitech G29 Steering Wheel

## 端口
```yaml
ports:
- name: Buttons
  summary: 方向盘按钮状态 0（= 未按下）| 1（= 已按下）
  direction: output
  data_types: Boolean
- name: Steering
  summary: 方向盘位置值 0（= 最左）| 65535（= 最右）
  direction: output
  data_types: uint16
- name: Pedals
  summary: 油门、制动和离合器踏板状态 0（= 未踩下）| 255（= 完全踩下）
  direction: output
  data_types: uint8
- name: Direction
  summary: 方向盘方向板按钮状态 0（= UP）| 2（= RIGHT）| 4（= DOWN）| 6（= LEFT）| 8（= UNPRESSED）
  direction: output
  data_types: uint8
- name: Status
  summary: 与方向盘通信的状态 0（默认）| 负值
  direction: output
  data_types: int32
```

### 输出

### **Buttons** — 方向盘按钮状态 0（= 未按下）| 1（= 已按下）

`Buttons` 输出是一个布尔值向量，用于指示方向盘上按钮的状态。向量中按钮值的顺序为：

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

**数据类型：** `Boolean`

### **Steering** — 方向盘位置值 0（= 最左）| 65535（= 最右）

`Steering` 输出值指示方向盘的位置。

**数据类型：** `uint16`

### **Pedals** — 油门、制动和离合器踏板状态 0（= 未踩下）| 255（= 完全踩下）

`Pedals` 输出是一个值向量，用于指示油门、制动和离合器踏板的状态。向量中踏板值的顺序为：

1. Throttle
2. Brake
3. Clutch

**数据类型：** `uint8`

### **Direction** — 方向盘方向板按钮状态 0（= UP）| 2（= RIGHT）| 4（= DOWN）| 6（= LEFT）| 8（= UNPRESSED）

`Direction` 输出值指示方向板上按钮的按下情况。当您在方向板的按钮之间按下方向板时，会出现中间值。

**数据类型：** `uint8`

### **Status** — 与方向盘通信的状态 0（默认）| 负值

`Status` 输出值指示与方向盘通信成功（0）或通信失败（负值）。

**数据类型：** `int32`
## 参数
```yaml
parameters:
- name: sampleTime
  summary: 方向盘数据的采样时间 -1（继承）（默认）
  group: ''
  block_parameter: sampleTime
```

### **sampleTime** — 方向盘数据的采样时间 -1（继承）（默认）

选择方向盘数据的采样时间。推荐的 `sampleTime` 为 10ms。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampleTime` |
## 所属库

Simulink Real-Time / Logitech G29

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

接收 Logitech G29 Steering Wheel 读取数据

Logitech G29 Steering Wheel 模块从 Logitech® G29 Steering Wheel（仅限 PS3）读取数据。该模块不支持 Stick Shift 模块。

**注意**

将 Logitech G29 Steering Wheel 设备连接到目标计算机上的 USB 端口。
