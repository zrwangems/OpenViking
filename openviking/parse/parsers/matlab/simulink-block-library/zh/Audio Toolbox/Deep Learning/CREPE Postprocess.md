---
type: simulink-block
title: 'CREPE Postprocess'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning'
documentation_page: 'crepepostprocessblock'
documentation_source_path: 'ref/crepepostprocessblock.html'
language: zh-CN
chinese_source: worker-translation
---

# CREPE Postprocess

## 端口

### 输入

### **Port\_1** — CREPE 网络激活矩阵

CREPE 网络激活，指定为 *N*×360 矩阵，其中 *N* 是 CREPE 神经网络输出的帧数。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 估计的基频列向量

估计的基频，以 Hz 为单位返回，为 *N*×1 向量，其中 *N* 是输入中的帧数。

**数据类型：** `single` | `double`

## 参数

### **Confidence threshold** — 音高置信度阈值 `0.5`（默认值） | 范围 [0, 1) 内的标量

音高置信度阈值，指定为范围 [0, 1) 内的标量。在后处理中，该模块会抑制网络置信度低于阈值的基频。

**注意**

如果网络输出的最大值小于置信度阈值，该模块返回 `NaN`。

**可调：** 是

## 所属库

Audio Toolbox / Deep Learning

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

**在 R2023a 中引入**

## 描述

对 CREPE 音高估计网络的输出进行后处理

CREPE Postprocess 模块将 CREPE 预训练网络的输出转换为以 Hz 为单位的音高估计值。
