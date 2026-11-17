---
type: simulink-block
title: 'Environment Parameters'
family: 'utilities'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'environmentparameters'
documentation_source_path: 'ref/environmentparameters.html'
language: zh-CN
chinese_source: worker-translation
---

# Environment Parameters

## 端口

### 守恒端口

### **OUT** — 电气输出端口

与环境参数输出关联的电气守恒端口。

## 参数

### **Temperature** — SPICE 温度 `300.15` `K`（默认值） | 正标量

已连接 SPICE 兼容模块的温度。

### **GMIN** — 最小电导 `1e-12` `1/Ohm`（默认值） | 正标量

适用于已连接 SPICE 兼容模块的最小电导。

## 所属库

Simscape / Electrical / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

设置适用于所有已连接 SPICE 兼容模块的参数

Environment Parameters 模块允许你设置适用于电气网络中所有 SPICE 兼容模块的参数：

- 电路温度
- 最小电导

如果你的模型不包含 Environment Parameters 模块，则所有模块都使用这些参数的默认值。要覆盖默认值，请将系统中的每个网络连接到 Environment Parameters 模块。

**注意**

Semiconductors 子库中的简单半导体模型不依赖于温度，因此 Environment Parameters 模块仅更改指数二极管和双极型晶体管模型使用的最小电导参数。
