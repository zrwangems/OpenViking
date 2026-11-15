---
type: simulink-block
title: 'Cross Product'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'crossproduct'
documentation_source_path: 'crossproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# Cross Product

## 端口

### 输入

### **端口 1 (a)** — 3 元素向量向量

输入向量 a→，其中各元素表示平行于 *x*、*y* 和
*z* 坐标轴的向量的幅值。

**数据类型：** `double`

### **端口 2 (b)** — 3 元素向量向量

输入向量 b→，其中各元素表示平行于 *x*、*y* 和
*z* 坐标轴的向量的幅值。

**数据类型：** `double`
### 输出

### **端口 1 (y)** — 合成向量向量

输出向量 y→=a→×b→，其与 a→ 和 b→ 正交。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**R2006a 中引入**

### R2023b: 将删除

`Cross Product` 将在未来版本中删除。相反，请使用 `sim3d` 类和 Simulation 3D 模块将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境对接。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将删除）两个三维向量的叉积

返回两个 3×1 向量的叉积——或向量积。每个输入都是形如 a1i^+a2j^+a3k^ 的向量，其中 *i*、*j* 和
*k* 是平行于 *x*、
*y* 和 *z* 坐标轴的单位向量。输出向量 y→=a→×b→ 是一个 3 元素向量，与输入向量 a→ 和 b→ 正交。
