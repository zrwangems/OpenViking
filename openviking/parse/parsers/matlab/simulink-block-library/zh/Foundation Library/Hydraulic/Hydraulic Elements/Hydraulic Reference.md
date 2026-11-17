---
type: simulink-block
title: 'Hydraulic Reference'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'hydraulicreference'
documentation_source_path: 'ref/hydraulicreference.html'
language: zh-CN
chinese_source: worker-translation
---

# Hydraulic Reference

## 端口

该模块具有一个液压守恒端口。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）大气压力连接

Hydraulic Reference 模块表示与大气压力的连接。所有以大气为参考的模块的液压守恒端口（例如，液压泵的吸油端口，或阀、缸、管路的回油端口，如果它们被视为直接连接到大气）必须连接到一个 Hydraulic Reference 模块。
