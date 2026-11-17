---
type: simulink-block
title: 'Serial-In Parallel-Out Shift Register'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'serialinparalleloutshiftregister'
documentation_source_path: 'ref/serialinparalleloutshiftregister.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial-In Parallel-Out Shift Register

## 端口

### 输入

### **u** — 串行输入标量 | 向量

串行输入信号。

**数据类型：** `single` | `double`
### 输出

### **y** — 并行输出向量

并行输出信号。

**数据类型：** `single` | `double`

## 参数

### **样本数** — 输入样本数 `4`（默认）| 正整数

寄存器级数或样本数。

### **初始条件** — 输入样本的初始值 `0`（默认）| 实数

仿真开始时间之前的 *N-1* 个样本的初始值。该值必须是与输入信号大小相同的标量或向量。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 0 | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间，请指定 `-1`。对于离散时间，请指定正整数。对于连续时间，请指定 `0`。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散时间串入并出移位寄存器

Serial-In Parallel-Out Shift Register 模块在离散时间中实现串入并出移位寄存器。您可以使用移位寄存器在串行和并行接口之间转换，或实现电路延迟或硬件堆栈。

此模块输出输入信号最近 *N* 个样本组成的向量。如果输入信号是向量，则模块输出每个输入信号的最近 *N* 个样本。
