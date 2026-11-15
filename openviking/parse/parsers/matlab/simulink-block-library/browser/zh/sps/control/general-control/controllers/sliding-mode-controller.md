---
type: simulink-block
title: 'Sliding Mode Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Control\u200b / Controllers'
documentation_page: 'slidingmodecontroller'
documentation_source_path: 'ref/slidingmodecontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Sliding Mode Controller

## 端口

### 输入

### **r** — 被控对象参考标量

被控对象系统参考信号。

**数据类型：** `single` | `double`

### **y** — 被控对象输出标量

被控对象系统输出信号。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制器输出标量

控制系统输出信号。

**数据类型：** `single` | `double`

## 参数

### **Sliding factor** — 滑动因子 `1`（默认值）| 非负标量

*自 R2024b 起*

滑动因子，会影响误差收敛到零的速度。

### **Hysteresis band** — 总滞环带宽 `0.2`（默认值）

总滞环带宽，围绕设定点对称分布。

### **Control action upper limit** — 控制信号上限，*umax* `10`（默认值）| 大于 **Control action lower limit** 参数值的标量

控制输出信号的上限。

### **Control action lower limit** — 控制信号下限，*umin* `-10`（默认值）| 标量

控制输出信号的下限。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：指定控制器的滑动因子

现在可以使用 **Sliding factor** 参数指定控制器的滑动因子值。**Sliding factor** 参数会影响误差收敛到零的速度，使您可以更快地获得所需响应。

## 描述

基于滞环的滑模控制

Sliding Mode Controller 模块实现基于滞环的滑模控制（SMC）。

滑模控制器具有以下结构。

Simulink 中滑模控制器的实现。有两个输入端口 r 和 y，以及一个输出端口 u。

在此控制器中，*lambda* 是 **Sliding factor** 参数的值。要改变误差收敛到零的速度，请为 **Sliding factor** 参数指定大于 `0` 的值。
