---
type: simulink-block
title: 'Slider-Crank'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
documentation_page: 'slidercrank'
documentation_source_path: 'ref/slidercrank.html'
language: zh-CN
chinese_source: worker-translation
---

# Slider-Crank

## 端口

### 守恒

### **C** — 曲柄机械旋转

与曲柄关联的机械旋转守恒端口。

### **S** — 滑块机械平移

与滑块关联的机械平移守恒端口。

## 参数

### **Crank radius** — 曲柄的半径 `0.1 m`（默认）

曲柄的半径。参数值必须大于零。

### **Rod length** — 连杆的长度 `0.2 m`（默认）

连接曲柄和滑块的连杆的长度。参数值必须大于 **Crank radius**。

### **Crank inertia** — 曲柄的惯量 `0.01 kg*m^2`（默认）

曲柄的惯量，有助于当连杆与曲柄中心完全对齐时，使机构通过顶部和底部位置。参数值必须大于零。

### **Slider stiffness** — 施加到滑块位置的刚度 `1e6 N/m`（默认）

与 **Slider damping** 一起引入柔顺性，有助于减少端口之间的惯量耦合。较高的刚度使运动更接近理想，但会增加系统刚度。参数值必须大于零。

### **Slider damping** — 施加到滑块位置的阻尼 `1e3 N/(m/s)`（默认）

与 **Slider stiffness** 一起引入柔顺性，有助于减少端口之间的惯量耦合。较高的阻尼值可平滑由刚度引起的振铃。参数值必须大于零。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

通用曲柄滑块机构

Slider-Crank 模块表示曲柄滑块机构，作为曲柄连续旋转运动与滑块振荡平移运动之间的转换器。

该机构有两个连接：

- 端口 C 对应曲柄，并且是机械旋转守恒端口。
- 端口 S 对应滑块，并且是机械平移守恒端口。

**Crank radius** 和 **Rod length** 参数描述机构几何结构。**Crank inertia** 参数有助于当连杆与曲柄中心完全对齐时，使机构通过顶部和底部位置。

**Slider stiffness** 和 **Slider damping** 参数的目的是减少端口之间的惯量耦合，这种耦合可能导致计算问题。该模块在滑块的理想位置（由几何结构计算得出）与平移守恒端口 **S** 的实际位置之间施加刚度和阻尼。这种柔顺性避免了端口之间的直接非线性耦合。较高的刚度使运动更接近理想，但会增加系统刚度。阻尼有助于平滑可能由刚度引起的振铃。

### 变量

可以在仿真开始时为曲柄角度和速度设置初始化目标，可使用正值和负值。

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种在模型中指定变量预期量级的方法。基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅修改模块变量的标称值。
