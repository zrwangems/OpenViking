---
type: simulink-block
title: 'Fractional Clock Divider with Accumulator'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'fractionalclockdividerwithaccumulator'
documentation_source_path: 'ref/fractionalclockdividerwithaccumulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Fractional Clock Divider with Accumulator

## 端口

### 输入

### **clk in** — 输入时钟频率标量

输入时钟频率，指定为标量。在 PLL 系统中，**clk in** 端口连接到 VCO 模块的输出端口。

**数据类型：** `double`

### **div-by** — 输出与输入时钟频率之比的小数标量

输出与输入时钟频率之比，指定为小数标量。

**div-by** 端口处的值分为两部分：整数部分（*N*）和小数部分（*.FF*）。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟频率标量

输出时钟频率，指定为标量。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口处的输出是幅度为 1 V 的方波脉冲串。

**数据类型：** `double`

### **state** — 缺失的小数脉冲存储标量

缺失的小数脉冲存储。**state** 端口的值在上一周期的 **clk out** 值的每个上升沿增加 *F*。每当 **state** 端口值超过 `1` 时，该值溢出，并将 **carry** 端口值设置为 `1`。

**数据类型：** `double`

### **carry** — 当 state 端口溢出时激活脉冲吞除功能 `0`（默认） | `1`

当 **state** 端口溢出时激活脉冲吞除功能的输出端口。脉冲移除类似于将输入频率除以 *N*+1 而不是 *N*。

**数据类型：** `Boolean`

## 参数

### **启用增加的缓冲区大小** — 启用增加的缓冲区大小 off（默认） | on

选择此项可在仿真期间启用增加的缓冲区大小。这会增加 Fractional Clock Divider with Accumulator 模块内 Logic Decision 的缓冲区大小。默认情况下，此选项未选中。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `1`（默认） | 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。这会设置 Fractional Clock Divider with Accumulator 模块内 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，使输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在 Block Parameters 对话框中选择 **启用增加的缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看
  **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将
  **缓冲区大小** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

将输入信号频率除以小数的时钟分频器

Fractional Clock Divider with Accumulator 模块将输入信号的频率除以可调小数值（*N*.*FF*）。与 Single Modulus Prescaler 模块相比，Fractional Clock Divider with Accumulator 模块有助于实现窄信道间隔，该间隔可小于锁相环（PLL）系统的参考频率。
