---
type: simulink-block
title: 'Audio Delta'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'audiodeltablock'
documentation_source_path: 'ref/audiodeltablock.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Delta

## 端口

### 输入

### **Port\_1** — 音频特征 标量 | 向量 | 矩阵 | 三维数组

音频特征，指定为标量、向量、矩阵或三维数组。delta 计算沿第一个维度进行。所有其他维度均被视为独立通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 音频特征的 Delta 标量 | 向量 | 矩阵 | 数组

音频特征的 Delta，返回为与输入具有相同大小和数据类型的数组。

**数据类型：** `single` | `double`

## 参数

### **Delta window length** — 用于计算 delta 的窗口长度 `9` (默认值) | 大于 2 的奇数

用于计算 delta 的窗口长度，指定为大于 2 的奇数。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution` (默认值) | `Code generation`

- `Interpreted execution` –– 使用
  MATLAB® 解释器仿真模型。此选项缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，
  您可以调试模块的源代码。
- `Code generation` –– 使用生成的 C
  代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的
  启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

## 所属库

Audio Toolbox / Features

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

计算 delta 特征

Audio Delta 模块计算输入音频特征的 delta。delta 是音频特征关于时间的一阶导数的近似值。
