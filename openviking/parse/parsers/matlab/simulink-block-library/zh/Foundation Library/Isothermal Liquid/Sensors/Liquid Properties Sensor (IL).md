---
type: simulink-block
title: 'Liquid Properties Sensor (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Sensors'
documentation_page: 'liquidpropertiessensoril'
documentation_source_path: 'ref/liquidpropertiessensoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Liquid Properties Sensor (IL)

## 端口

### 输出

### **rho** — 密度测量，kg/m^3 物理信号

用于测量等温液体混合物密度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Density** 复选框。

### **beta** — 等温体积模量测量，Pa 物理信号

用于测量等温液体混合物体积模量的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Isothermal bulk modulus** 复选框。

### **theta** — 夹带空气分数测量，无量纲物理信号

用于测量夹带（未溶解）空气分数的物理信号输出端口，(*entrained air*)/(*entrained air* + *dissolved air*)。值为 1 表示没有空气溶解。值为 0 表示所有空气均已溶解。

#### 依赖

要启用此端口，请选中 **Fraction of air that is entrained** 复选框。

### 守恒

### **A** — 传感器入口等温液体

等温液体守恒端口。将此端口连接到等温液体网络中您想要测量液体属性的节点。所有测量均相对于绝对零度进行。

## 参数

### **Density** — 控制输出端口可见性以测量密度 `On`（默认）| `Off`

选中此复选框可显示输出端口 **rho**，从而允许您测量流体密度。

### **Isothermal bulk modulus** — 控制输出端口可见性以测量体积模量 `Off`（默认）| `On`

选中此复选框可显示输出端口 **beta**，从而允许您测量体积模量。

### **Fraction of air that is entrained** — 控制输出端口可见性以测量夹带空气分数 `Off`（默认）| `On`

选中此复选框可显示输出端口 **theta**，从而允许您测量未溶解空气的分数。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

测量等温液体网络中的密度、体积模量和夹带空气分数

Liquid Properties Sensor (IL) 模块表示一个理想传感器，允许您测量等温液体网络中的混合物密度、体积模量和夹带空气分数。传感器中没有质量流量。

该模块在连接到端口 **A** 的节点处测量这些属性。所有测量均相对于绝对零度进行。
