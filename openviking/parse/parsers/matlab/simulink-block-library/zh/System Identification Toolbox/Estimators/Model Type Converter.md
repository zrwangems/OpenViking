---
type: simulink-block
title: 'Model Type Converter'
family: 'estimators'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Estimators'
documentation_page: 'modeltypeconverter'
documentation_source_path: 'ref/modeltypeconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Model Type Converter

## 端口

| 端口 | 端口类型（In/Out） | 描述 |
| --- | --- | --- |
| u | In | 估计的 A、B、C、D 和 F 多项式系数，指定为包含以下元素的总线：A、B、C、D 和 F。 |
| y | Out | 状态空间模型，以总线形式返回，其元素与 A、B、C 和 D 矩阵对应。 |

## 参数

### 输入模型类型

指定要将其系数转换为状态空间模型矩阵的模型类型。请指定以下模型类型之一：

- `ARX`
- `ARMAX`
- `OE`
- `BJ`

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

将多项式模型系数转换为状态空间模型矩阵

使用 Model Type Converter 模块将 ARX、ARMAX、OE 或 BJ 模型系数转换为状态空间模型矩阵。

模块的输入端口 u 要求输入为总线。总线中的元素数量取决于输入多项式模型类型：

- ARX — A、B
- ARMAX — A、B、C
- OE — B、F
- BJ — B、C、D、F

这些总线元素必须包含由 Recursive Polynomial Model Estimator 模块输出的估计系数值行向量。对于 MISO 数据，将 *B* 多项式系数指定为一个矩阵，其中第 *i* 行的参数对应于第 *i* 个输入。系数值可以随时间变化。Model Type Converter 模块将这些系数转换为离散时间状态空间模型的 A、B、C 和 D 矩阵。Model Type Converter 模块的输出端口 y 返回一个总线，其元素与状态空间模型的 A、B、C 和 D 矩阵对应。如果 u 中的信号随时间变化，则状态空间矩阵也随时间变化。

您还可以将 Recursive Polynomial Model Estimator 和 Model Type Converter 模块结合使用，在线估计状态空间模型。将 Recursive Polynomial Model Estimator 模块的输出端口连接到 Model Type Converter 模块的输入端口，以获得状态空间矩阵的在线值。该转换会忽略模型的噪声分量。换言之，状态空间矩阵仅反映 y(t)/u(t) 关系。
