---
type: simulink-block
title: '3-Phase Sine Voltage Generator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Math Transforms'
documentation_page: '3phasesinevoltagegenerator'
documentation_source_path: 'ref/3phasesinevoltagegenerator.html'
language: zh-CN
chinese_source: official
---

# 3-Phase Sine Voltage Generator

## 端口

### 输入

### **A** — 参考电压振幅 标量

参考电压信号的最大振幅。

**数据类型:** `single` | `double` | `fixed point`

### **θe** — 参考电压位置 标量

参考电压信号的位置或相位值。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **Va** — 平衡三相电压的 *a* 轴分量 标量

沿 *abc* 参考系的 *a* 轴的平衡三相电压信号分量。

**数据类型:** `single` | `double` | `fixed point`

### **Vb** — 平衡三相电压的 *b* 轴分量 标量

沿 *abc* 参考系的 *b* 轴的平衡三相电压信号分量。

**数据类型:** `single` | `double` | `fixed point`

### **Vc** — 平衡三相电压的 *c* 轴分量 标量

沿 *abc* 参考系的 *c* 轴的平衡三相电压信号分量。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **Theta 单位** — `θe` 的单位 **标幺** (默认) | **弧度** | **度**

您作为输入提供的参考电压位置的单位。

### **查找表的数据点数** — 查找表的大小 `1024` (默认) | 标量

查找表的大小。

## 所属库

Motor Control Blockset / Controls / Math Transforms

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

生成平衡的三相正弦信号

3-Phase Sine Voltage Generator 模块使用信号振幅和位置输入生成平衡的三相正弦信号。

该模块使用查找表方法。当与 Motor Control Blockset™ 中附带的示例所采用的模型设置和配置结合使用时，这种方法可以优化代码执行。您可以在**查找表的数据点数**参数中指定查找表点数。

下图显示位置输入和三相正弦输出信号随时间的变化。

### 方程

以下方程描述该模块如何计算平衡的三相正弦信号。

- Va=A×sinωt
- Vb=A×sin(ωt−2π3)
- Vc=A×sin(ωt−4π3)

其中：

- A 是参考电压振幅（伏特）。
- ω 是参考电压位置输入信号 (`θe`) 的频率（弧度/秒）。
- t 是时间（秒）。
