---
type: simulink-block
title: 'Slider-Crank'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanisms'
documentation_page: 'slidercrank'
documentation_source_path: 'ref/slidercrank.html'
language: zh-CN
chinese_source: worker-translation
---

# Slider-Crank

## 端口

### 守恒端口

### **C** — 曲柄机械旋转

与曲柄关联的机械旋转守恒端口。

### **S** — 滑块机械平移

与滑块关联的机械平移守恒端口。

## 参数

### **Crank radius** — 曲柄半径 `0.1 m`（默认值）

曲柄的半径。参数值必须大于零。

### **Rod length** — 连杆长度 `0.2 m`（默认值）

连接曲柄和滑块的连杆长度。参数值必须大于 **Crank radius**。

### **Crank inertia** — 曲柄惯量 `0.01 kg*m^2`（默认值）

曲柄的惯量，有助于在连杆与曲柄中心完全对齐时使机构通过上下止点位置。参数值必须大于零。

### **Slider stiffness** — 施加到滑块位置的刚度 `1e6 N/m`（默认值）

与 **Slider damping** 一起引入柔度，有助于减少端口之间的惯量耦合。较高的刚度使运动更接近理想状态，但会增加系统刚度。参数值必须大于零。

### **Slider damping** — 施加到滑块位置的阻尼 `1e3 N/(m/s)`（默认值）

与 **Slider stiffness** 一起引入柔度，有助于减少端口之间的惯量耦合。较高的阻尼值可以平滑由刚度引起的振铃。参数值必须大于零。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

通用曲柄滑块机构

Slider-Crank 模块将曲柄滑块机构表示为曲柄连续旋转运动与滑块往复平移运动之间的转换器。

该机构有两个连接：

- 端口 C 对应曲柄，为机械旋转守恒端口。
- 端口 S 对应滑块，为机械平移守恒端口。

**Crank radius** 和 **Rod length** 参数描述机构几何形状。**Crank inertia** 参数有助于在连杆与曲柄中心完全对齐时使机构通过上下止点位置。

**Slider stiffness** 和 **Slider damping** 参数的目的是减少端口之间的惯量耦合，这种耦合可能导致计算问题。该模块在滑块的理想位置（由几何形状计算得出）与平移守恒端口 **S** 的实际位置之间施加刚度和阻尼。这种柔度避免了端口之间的直接非线性耦合。较高的刚度使运动更接近理想状态，但会增加系统刚度。阻尼有助于平滑由刚度引起的振铃。

### 变量

您可以在仿真开始时为曲柄角度和速度设置初始化目标，使用正值和负值均可。

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

额定值提供了一种在模型中指定变量预期量级的方法。使用基于额定值的系统缩放可提高仿真鲁棒性。额定值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
