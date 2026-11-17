---
type: simulink-block
title: 'Cepstral Coefficients'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'cepstralcoefficientsblock'
documentation_source_path: 'ref/cepstralcoefficientsblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Cepstral Coefficients

## 端口
```yaml
ports:
- name: Port_1
  summary: 频谱图或听觉频谱图矩阵 | 三维数组
  direction: input
  data_types: single | double
- name: Port_1
  summary: 倒谱系数矩阵 | 三维数组
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 频谱图或听觉频谱图矩阵 | 三维数组

频谱图或听觉频谱图，指定为 *L*×*M* 矩阵或 *L*×*M*×*N* 数组，其中：

- *L* 是频带数量。
- *M* 是帧数。
- *N* 是通道数。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 倒谱系数矩阵 | 三维数组

倒谱系数，返回为 *M*×*B* 矩阵或 *M*×*B*×*N* 数组，其中：

- *M* 是输入频谱图中的帧数。
- *B* 是每帧返回的系数数量，由 **Number of cepstral coefficients** 参数指定。
- *N* 是输入频谱图中的通道数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Number of cepstral coefficients
  summary: 返回的倒谱系数数量 13（默认）| 大于 1 的正整数
  group: ''
- name: Rectification
  summary: 非线性整流类型 Logarithm（默认）| Cubic root | None
  group: ''
- name: Simulate using
  summary: 指定要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Number of cepstral coefficients** — 返回的倒谱系数数量 13（默认）| 大于 1 的正整数

倒谱系数数量，指定为大于 1 的正整数。

### **Rectification** — 非线性整流类型 `Logarithm`（默认）| `Cubic root` | `None`

在离散余弦变换之前应用于频谱的非线性整流类型，指定为 `Logarithm`、`Cubic root` 或 `None`。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
## 所属库

Audio Toolbox / Features

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

从频谱图中提取倒谱系数

Cepstral Coefficients 模块从实值频谱图或听觉频谱图中提取倒谱系数。倒谱系数通常用作音频信号的紧凑表示。
