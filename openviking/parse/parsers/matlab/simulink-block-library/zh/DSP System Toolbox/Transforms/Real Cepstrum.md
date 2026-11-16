---
type: simulink-block
title: 'Real Cepstrum'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'realcepstrum'
documentation_source_path: 'ref/realcepstrum.html'
language: zh-CN
chinese_source: worker-translation
---

# Real Cepstrum

## 端口

### 输入

### **输入** — 输入向量 | 矩阵

将输入 *u* 指定为大小为 *M*×*N* 的向量或矩阵。该模块将输入的每一列视为一个独立通道，其中包含 *M* 个连续样本。该模块始终将无方向向量输入作为单个通道处理，并将结果返回为长度为 *M* 的列向量。该模块不接受复数值输入。

**数据类型：** `single` | `double`

### 输出

### **输出** — 实倒谱输出向量 | 矩阵

实倒谱输出，返回为 *Mo*×*N* 矩阵。

当清除 **从输入端口维度继承 FFT 长度** 参数时，*Mo* 是你在 **FFT 长度** 参数中指定的值。当选择 **从输入端口维度继承 FFT 长度** 参数时，*Mo* = *M*，其中 *M* 是输入信号的帧大小（行数）。

每个输出列包含对应输入列的长度为 *Mo* 的实倒谱。

输出端口速率与输入端口速率相同。

**数据类型：** `single` | `double`

## 参数

### **从输入端口维度继承 FFT 长度** — 使 FFT 长度与输入端口的维度匹配 `on`（默认） | `off`

当选中此复选框时，输出帧大小 *Mo* 与输入帧大小 *M* 匹配。

### **FFT 长度** — 计算 FFT 长度 `64`（默认） | 正整数

用于计算 FFT 的频率点数，同时也是输出帧大小 *Mo*。

#### 依赖项

要启用此参数，请清除 **从输入端口维度继承 FFT 长度** 参数。

## 所属库

DSP System Toolbox / Transforms

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

生成的代码在某些情况下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算输入的实倒谱

Real Cepstrum 模块计算输入的实倒谱。
