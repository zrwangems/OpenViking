---
type: simulink-block
title: 'Fractional Clock Divider with DSM'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'fractionalclockdividerwithdsm'
documentation_source_path: 'ref/fractionalclockdividerwithdsm.html'
language: zh-CN
chinese_source: worker-translation
---

# Fractional Clock Divider with DSM

## 端口

### 输入

### **clk in** — 输入时钟频率标量

需要分频的输入时钟频率，指定为标量。在锁相环 (PLL) 系统中，**clk in** 端口连接到 VCO 模块的输出。

**数据类型：** `double`

### **div-by** — 输出与输入时钟频率之比的小数标量

输出与输入时钟频率之比，指定为小数标量。**div-by** 端口的值 *N.FF* 分为两部分：整数部分 (*N*) 和小数部分 (*.FF*)。

对于 *n* 阶 delta sigma 调制器，**div-by** 端口的值通过将 *N* 在 2n 个不同的整数值之间变化来实现。

**注意**

对于 *n* 阶 delta sigma 调制器，请在 **div-by** 端口使用 ≥ 2n 的值。

**数据类型：** `double`

### 输出

### **clk out** — 输出时钟频率标量

输出时钟频率，指定为标量。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口的输出是幅度为 1 V 的方波脉冲串。

**数据类型：** `double`

## 参数

### **Delta Sigma Modulator order** — Delta Sigma Modulator 的阶数 `3rd order`（默认） | `1st order` | `2nd order` | `4th order`

delta sigma 调制器的阶数。

对于 *n* 阶 delta sigma 调制器，**div-by** 端口的值通过将 *N* 计数器值在 2n 个不同值之间变化来实现。调制器阶数定义了 **clk in** 端口信号将被分频的值范围，从而提供类似于 **div-by** 端口处 *N.FF* 值的分频效果。

#### 编程用法

- 使用 `get_param(gcb,'dsm')` 查看
  当前的 **Delta Sigma Modulator order**。
- 使用 `set_param(gcb,'dsm',value)` 将
  **Delta Sigma Modulator order** 设置为
  特定值。

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认） | on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Fractional Clock Divider with DSM 模块内部 Logic Decision 的缓冲区大小。默认情况下，此选项处于未选中状态。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `1`（默认） | 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 Fractional Clock Divider with DSM 模块内部 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。请将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 Block Parameters 对话框中选择 **Enable increased buffer size** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看
  **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将
  **Buffer size** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

基于 Delta Sigma Modulator 的小数时钟分频器

使用 delta sigma (Δ-Σ) 调制技术，Fractional Clock Divider with DSM 通过扩展 **div-by** 值变化的范围来减少主要小数杂散。此模块允许进行最高 4 阶的 delta sigma 调制。
