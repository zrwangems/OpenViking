---
type: simulink-block
title: 'Model Type Converter'
family: 'ident'
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
```yaml
ports: []
```

| 端口 | 端口类型（输入/输出） | 描述 |
| --- | --- | --- |
| u | 输入 | 估计的 A、B、C、D 和 F 多项式系数，指定为包含以下元素的总线：A、B、C、D 和 F。 |
| y | 输出 | 状态空间模型，返回为包含对应于 A、B、C 和 D 矩阵的元素的总线。 |
## 参数
```yaml
parameters: []
```

### 输入模型类型

指定要转换为状态空间模型矩阵的模型类型系数。指定以下模型类型之一：

- `ARX`
- `ARMAX`
- `OE`
- `BJ`
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2014a 中引入**

## 描述

将多项式模型系数转换为状态空间模型矩阵

使用 Model Type Converter 模块将 ARX、ARMAX、OE 或 BJ 模型系数转换为状态空间模型矩阵。

该模块的输入端口 u 需要总线。元素数量取决于输入多项式模型类型：

- ARX — A、B
- ARMAX — A、B、C
- OE — B、F
- BJ — B、C、D、F

这些总线元素必须包含由 Recursive Polynomial Model Estimator 模块输出的估计系数值的行向量。对于 MISO 数据，将 *B* 多项式系数指定为矩阵，其中第 *i* 行参数对应于第 *i* 个输入。系数值可以随时间变化。Model Type Converter 模块将这些系数转换为离散时间状态空间模型的 A、B、C 和 D 矩阵。Model Type Converter 模块的输出端口 y 返回一个总线，其元素对应于状态空间模型的 A、B、C 和 D 矩阵。如果 u 中的信号是时变的，则状态空间矩阵也是时变的。

您还可以通过将 Recursive Polynomial Model Estimator 和 Model Type Converter 模块一起使用来在线估计状态空间模型。将 Recursive Polynomial Model Estimator 模块的输出端口连接到 Model Type Converter 模块的输入端口，以获得状态空间矩阵的在线值。转换忽略模型的噪声分量。换句话说，状态空间矩阵仅捕获 y(t)/u(t) 关系。
