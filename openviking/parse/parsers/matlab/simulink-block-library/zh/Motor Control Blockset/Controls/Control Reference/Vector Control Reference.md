---
type: simulink-block
title: 'Vector Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'vectorcontrolreference'
documentation_source_path: 'ref/vectorcontrolreference.html'
language: zh-CN
chinese_source: official
---

# Vector Control Reference

## 端口

### 输入

### **magref** — 参考矢量的幅值 标量

作为输入提供给模块的参考电压、电流或磁通矢量的幅值。

**数据类型:** `single` | `double` | `fixed point`

### **θe** — 参考矢量的电气位置 标量

作为输入提供给模块的参考电压、电流或磁通矢量的电气位置。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **dref** — 参考矢量的 *d* 轴分量 标量

参考电压、电流或磁通矢量在 *dq* 旋转参考系的直轴上的分量。

**数据类型:** `single` | `double` | `fixed point`

### **qref** — 参考矢量的 *q* 轴分量 标量

参考电压、电流或磁通矢量在 *dq* 旋转参考系的交轴上的分量。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **alpha (a 相)轴对齐** — *dq* 参考系对齐 **D 轴** (默认) | **Q 轴**

将旋转参考系的 *d* 或 *q* 轴与静止参考系的 *α* 轴对齐。

### **Theta 单位** — 输入位置值的单位 **标幺** (默认) | **弧度** | **度**

参考电压、电流或磁通矢量的输入电气位置的单位。

### **三角查找表的数据点数** — 查找表数组的大小 `1024` (默认) | 标量

查找表数组的大小。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

计算参考矢量的 d 轴和 q 轴分量

Vector Control Reference 模块可计算您作为输入提供给模块的参考电压、电流或磁通矢量的 *d* 轴和 *q* 轴分量。

该模块接受参考矢量的幅值和位置作为输入。该模块沿 *dq* 旋转参考系的直轴和交轴输出参考矢量分量。

### 方程

该模块使用以下方程来计算 *d* 轴和 *q* 轴矢量分量输出。

dref=magref×cosθe

qref=magref×sinθe

其中：

- dref 是参考矢量的 *d* 轴分量。
- qref 是参考矢量的 *q* 轴分量。
- magref 是参考矢量的幅值。
- θe 是参考矢量的电气位置。
