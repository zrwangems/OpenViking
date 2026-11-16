---
type: simulink-block
title: 'Interface (H-IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Utilities'
documentation_page: 'interfacehil'
documentation_source_path: 'ref/interfacehil.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (H-IL)

## 端口

### 守恒

### **H** — 液压端口 hydraulic

液压守恒端口，表示穿过接口的通道点。将此端口连接到基于 Simscape 液压域构建的模块网络。

### **IL** — 等温液体端口 isothermal liquid

等温液体守恒端口，表示穿过接口的通道点。将此端口连接到基于 Simscape 等温液体域构建的模块网络。

## 参数

R2025b 中未提供文档。

## 所属库

Simscape / Foundation Library / Hydraulic / Hydraulic Utilities

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

液压网络与等温液体网络之间的流动连接

Interface (H-IL) 模块表示液压网络与等温液体网络之间的跨域流动连接：

- 接口两侧的压力和质量流率相等。
- 流体属性不会跨接口共享。每个网络都有自己的流体属性。

在包含 Foundation > Hydraulic 库或 Fluids > Hydraulics (Isothermal) 库模块的现有模型中使用此模块，可以通过 Isothermal Liquid 库模块实现模型的某些部分，而无需转换整个模型。如果您拥有 Simscape™ Fluids™ 许可证，则可以使用 Fluids > Hydraulics (Isothermal) 库。

`hydraulicToIsothermalLiquid` 转换工具会将模型中的 Hydraulic 模块替换为等效的 Isothermal Liquid 模块。如果模型包含对其他库、模型或子系统的引用或链接，您可以使用 Interface (H-IL) 恢复模块框图中已转换部分与仍需转换的库、模型或子系统之间中断的连接。
