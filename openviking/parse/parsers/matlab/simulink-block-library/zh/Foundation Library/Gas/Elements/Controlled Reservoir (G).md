---
type: simulink-block
title: 'Controlled Reservoir (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'controlledreservoirg'
documentation_source_path: 'ref/controlledreservoirg.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Reservoir (G)

## 端口

### 输入

### **P** — 压力控制信号，Pa 物理信号

提供储层压力控制信号的物理信号端口。

### **T** — 温度控制信号，K 物理信号

提供储层温度控制信号的物理信号端口。
### 守恒

### **A** — 储层入口气体

与储层入口关联的气体守恒端口。

## 参数

### **Cross-sectional area at port A** — 储层入口处垂直于流动路径的面积 `0.01 m^2`（默认值）

储层入口处沿垂直于气体流动路径方向的横截面积。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体网络在时变压力和温度下的边界条件

Controlled Reservoir (G) 模块表示一个在可变压力和温度下的无限储层。端口 **A** 是气体守恒端口，表示储层入口。端口 **P** 是物理信号端口，提供储层压力控制信号。端口 **T** 是物理信号端口，提供储层温度控制信号。

储层内部的气体体积假定为无限大。因此，流动假定为准稳态。

气体以储层压力进入和离开储层，但其温度由气体流动方向决定。如果气体流入储层，其温度由上游气体网络决定。储层充当散热器。如果气体流出储层，其温度等于储层温度。储层充当热源。

### 假设和限制

- 储层中的气体为准稳态。
