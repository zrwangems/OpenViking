---
type: simulink-block
title: 'Normalize Vector'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'normalizevector'
documentation_source_path: 'normalizevector.html'
language: zh-CN
chinese_source: worker-translation
---

# Normalize Vector

## 端口

### 输入

### **Input 1** — 输入信号向量

任意大小的向量。

**数据类型：** `single` | `double`
### 输出

### **Output 1** — 单位向量

与输入信号提供的向量平行的单位向量。

**数据类型：** `single` | `double`

## 参数

### **将向量视为零的最大模** — 输入信号阈值 `0`（默认）

如果输入的模等于或低于此值，输出设置为零。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 中引入**

### R2023b：将被移除

`Normalize Vector` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块来连接 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境。有关入门信息，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将被移除）输出与输入向量平行的单位向量

使用 Normalize Vector 模块获取与给定向量平行的单位向量。
