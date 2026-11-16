---
type: simulink-block
title: 'Quadrature Shaft Decoder'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Observers'
documentation_page: 'quadratureshaftdecoder'
documentation_source_path: 'ref/quadratureshaftdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quadrature Shaft Decoder

## 端口

### 输入

### **A** — 数字信号 *A* 标量

Simulink 数字信号 *A*，指定为标量，它与数字信号 *B* 相位相差 90°。

**数据类型：** `single` | `double`

### **B** — 数字信号 *B* 标量

Simulink 数字信号 *B*，指定为标量，它与数字信号 *A* 相位相差 90°。

**数据类型：** `single` | `double`

### **Z** — 索引脉冲标量

Simulink 信号，指定为标量，与用于复位位置计算的解码器索引脉冲关联。

**数据类型：** `single` | `double`

### 输出

### **Velocity** — 轴旋转速度标量

Simulink 信号，指定为标量，与轴旋转速度关联。

**数据类型：** `single` | `double`

### **Position** — 轴旋转角度标量

Simulink 信号，指定为标量，与轴旋转角度关联。

**数据类型：** `single` | `double`

## 参数

### **每转脉冲数** — 每转脉冲数 4（默认）| integer > 0

编码器轴的每转脉冲数。

### **采样时间（继承时为 -1）** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，该模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

如果此模块位于触发子系统内，您可以通过将此参数设置为 `-1` 来让此模块继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / Observers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

解码增量式轴编码器输出

Quadrature Shaft Decoder 模块测量来自编码器模块（例如 Incremental Shaft Encoder）的轴旋转，并输出速度和位置。

该模块对一对数字信号 *A* 和 *B* 的跳变进行计数，这两个信号相位相差 90°。该模块通过每个 tick 仅对两个信号中一个信号的变化进行计数来确定方向和相对位置。角速度通过测量任一信号的频率来获得。
