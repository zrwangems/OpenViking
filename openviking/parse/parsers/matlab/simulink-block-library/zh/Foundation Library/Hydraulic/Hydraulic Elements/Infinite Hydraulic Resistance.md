---
type: simulink-block
title: 'Infinite Hydraulic Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'infinitehydraulicresistance'
documentation_source_path: 'ref/infinitehydraulicresistance.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Hydraulic Resistance

## 端口
```yaml
ports: []
```

该模块具有两个液压守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2023a：将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）用于设置两个节点之间初始压力差的液压元件

Infinite Hydraulic Resistance 模块表示液压网络中的断点。流体不会通过该断点流动。但是，连接到回路的 Custom Hydraulic Fluid 模块所指定的流体属性在断点两侧是相同的。使用此模块可将优先级和初始目标值设置为端口 **A** 与端口 **B** 之间的压力差。

**Variables** 选项卡允许您在仿真前为 **Pressure difference** 变量设置优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
