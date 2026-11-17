---
type: simulink-block
title: 'Hysteresis Current Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control'
documentation_page: 'hysteresiscurrentcontrollerthreephase'
documentation_source_path: 'ref/hysteresiscurrentcontrollerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Hysteresis Current Controller (Three-Phase)

## 端口

### 输入

### **iabc\*** — 电流向量

三相参考电流。

**数据类型：** `single` | `double`

### **iabc** — 电流向量

测得的三相电流。

**数据类型：** `single` | `double`
### 输出

### **S** — 控制器输出向量

用于功率变换器控制的六脉冲向量。

**数据类型：** `single` | `double`

## 参数

### **Current hysteresis band (A)** — 滞环带宽 `1`（默认）| 正数

电流控制器的滞环带宽 *h*。开通点为
*h*/2，关断点为
-*h*/2。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，
模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承
采样时间。如果此模块位于连续变步长模型中，请使用正
标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

三相滞环电流控制

Hysteresis Current Controller (Three-Phase) 模块为功率变换器实现三相
滞环电流控制。
