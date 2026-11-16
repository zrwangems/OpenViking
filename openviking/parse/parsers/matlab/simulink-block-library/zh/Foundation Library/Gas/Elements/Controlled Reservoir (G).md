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

提供储气库压力控制信号的物理信号端口。

### **T** — 温度控制信号，K 物理信号

提供储气库温度控制信号的物理信号端口。
### 守恒

### **A** — 储气库入口气体

与储气库入口关联的气体守恒端口。

## 参数

### **Cross-sectional area at port A** — 储气库入口处垂直于流动路径的面积 `0.01 m^2`（默认）

储气库入口在垂直于气体流动路径方向上的横截面积。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体管网在时变压力和温度下的边界条件

Controlled Reservoir (G) 模块表示一个在可变压力和温度下的无限储气库。端口 **A** 是一个气体守恒端口，表示储气库入口。端口 **P** 是一个物理信号端口，提供储气库压力控制信号。端口 **T** 是一个物理信号端口，提供储气库温度控制信号。

储气库内的气体体积假定为无限大。因此，流动假定为准稳态。

气体在储气库压力下进入和离开储气库，但其温度由气体流动方向决定。如果气体流入储气库，其温度由上游气体管网决定。储气库充当散热器。如果气体流出储气库，其温度等于储气库的温度。储气库充当热源。

### 假设和限制

- 储气库中的气体为准稳态。
