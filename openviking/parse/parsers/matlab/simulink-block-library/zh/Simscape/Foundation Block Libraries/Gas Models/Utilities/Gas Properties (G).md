---
type: simulink-block
title: 'Gas Properties (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Gas Models / Utilities'
documentation_page: 'gaspropertiesg'
documentation_source_path: 'ref/gaspropertiesg.html'
language: zh-CN
chinese_source: worker-translation
---

# Gas Properties (G)

## 端口

### 守恒

### **A** — 气体连接端口

气体守恒端口，用于将模块连接到气体网络。您可以将其连接到框图中气体连接线上的任意点。当您将 Gas Properties (G) 模块连接到气体管线时，软件会自动识别连接到特定回路的气体模块，并将气体属性传播到该回路中的所有模块。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Gas / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a：控制仿真期间气体属性超出范围时的模块行为

以前，如果仿真期间气体属性超出有效范围，模块会返回错误。现在，您可以使用新的 **Pressure and temperature outside valid range** 参数来控制仿真期间气体属性超出范围时的模块行为。

## 描述

所连接回路的全局气体属性

Gas Properties (G) 模块定义气体属性，这些属性充当连接到某个回路的所有模块的全局参数。默认气体为干空气。

框图中每个拓扑上不同的气体回路都可以连接一个 Gas Properties (G) 模块。如果某个回路未连接 Gas Properties (G) 模块，则该回路中的模块使用与默认 Gas Properties (G) 模块参数值对应的气体属性。

Gas Properties (G) 模块允许您在三种气体属性模型之间进行选择：完全气体、半完全气体和真实气体。这三种气体属性模型在仿真速度和精度之间提供权衡。它们还支持增量工作流：您从简单模型开始，该模型只需要有关工作气体的最少信息，然后在获得更详细的气体属性数据时，基于该模型进行构建。下表列出了必须为这三种气体属性模型中的每一种指定的信息。

| 气体属性模型 | 物理属性 | |
| --- | --- | --- |
| 完全 | *R* | 比气体常数 |
| *Z* | 压缩因子，*Z* = *p*/(*ρ**R**T*) |
| *T*ref | 参考温度 |
| *h*ref | 参考温度下的比焓 |
| *c*p | 定压比热，cp=(∂h∂T)p |
| *μ* | 动力黏度 |
| *k* | 导热系数 |
| 半完全 | *R* | 比气体常数 |
| *Z* | 压缩因子 |
| *h* | 比焓向量 |
| *c*p | 定压比热向量 |
| *μ* | 动力黏度向量 |
| *k* | 导热系数向量 |
| *T* | 温度向量 |
| 真实 | *ρ* | 密度表 |
| *s* | 比熵表 |
| *h* | 比焓表 |
| *c*p | 定压比热表 |
| *μ* | 动力黏度表 |
| *k* | 导热系数表 |
| *β* | 等温体积模量表，β=ρ(∂p∂ρ)T |
| *α* | 等压热膨胀系数表，α=−1ρ(∂ρ∂T)p |
| *T* | 温度向量 |
| *p* | 压力向量 |

对于半完全气体，热力学属性和输运属性是温度的函数。您将它们指定为与 **Temperature vector** 对应的一维数组。对于真实气体，所有属性都是温度和压力的函数。您将它们指定为二维数组，其中行对应于 **Temperature vector**，列对应于 **Pressure vector**。

当温度或压力超出范围时，仿真会报错：

- 对于完全气体，您在 **参数** 部分指定压力和温度的最小和最大允许值。
- 对于半完全气体，**Valid temperature range parameterization** 参数为您提供选项，可通过使用温度向量的最低值和最高值来定义允许的温度范围。您必须指定压力的最小和最大允许值。
- 对于真实气体，**Valid pressure-temperature region parameterization** 参数为您提供选项，可分别通过使用压力向量和温度向量的最低值和最高值来定义允许的压力和温度范围。您还可以为压力-温度值组合指定有效性矩阵。

### 数据可视化

该模块提供选项，可绘制所指定气体属性随温度和压力变化的曲线。绘制属性可以让您在仿真模型之前可视化数据。

要绘制数据，请在模型中右键单击 Gas Properties (G) 模块，然后从上下文菜单中选择 **Foundation Library** > **Plot Gas Properties**。使用绘图顶部的下拉列表选择要可视化的气体属性。在模块参数更新后，单击 **Reload** 按钮重新生成绘图。

**气体属性绘图**

**注意**

为便于绘图可读性，密度数据显示为双对数刻度，而其他属性以半对数刻度绘制。也就是说，对于作为温度和压力函数的密度图，密度和压力均采用对数刻度，而温度值不采用对数刻度。对于其他属性，仅压力采用对数刻度。
