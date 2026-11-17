---
type: simulink-block
title: 'Single Modulus Prescaler'
family: 'pll'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'singlemodulusprescaler'
documentation_source_path: 'ref/singlemodulusprescaler.html'
language: zh-CN
chinese_source: worker-translation
---

# Single Modulus Prescaler

## 端口

### 输入

### **clk in** — 输入时钟频率标量

输入时钟频率，指定为标量。在 PLL 系统中，**clk in** 端口连接到 VCO 模块的输出端口。

**数据类型：** `double`

### **div-by** — 输出与输入时钟频率之比，标量整数

输出与输入时钟频率之比，表示为标量整数。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟频率标量

输出时钟频率，表示为标量。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口处的输出是幅度为 1 V 的方波脉冲串。

**数据类型：** `double`

## 参数

### **启用增大缓冲区大小** — 启用增大缓冲区大小 off (默认) | on

选中此项可在仿真期间启用增大的缓冲区大小。这会增大 Single Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。默认情况下，此选项未选中。

### **缓冲区大小** — 仿真期间可用的输入缓冲采样数 `1` (默认) | 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 Single Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

仅当在模块参数对话框中选中 **启用增大缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看
  **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将
  **缓冲区大小** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对输入信号频率进行分频的整数时钟分频器

Single Modulus Prescaler 子系统模块将输入信号的频率除以可调整数 *N*，该值传递到 **div-by** 端口。在频率合成器电路（例如锁相环 (PLL) 系统）中，这些预分频器将 VCO 输出频率除以整数值。预分频器输出端口得到的较低频率与 PFD 模块的参考输入相当。Single Modulus Prescaler 也称为整数时钟分频器。
