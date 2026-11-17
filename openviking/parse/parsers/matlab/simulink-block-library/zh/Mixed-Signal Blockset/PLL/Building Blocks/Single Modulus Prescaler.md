---
type: simulink-block
title: 'Single Modulus Prescaler'
family: 'msblks'
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
```yaml
ports:
- name: clk in
  summary: 输入时钟频率标量
  direction: input
  data_types: double
- name: div-by
  summary: 输出与输入时钟频率之比标量整数
  direction: input
  data_types: double
- name: clk out
  summary: 输出时钟频率标量
  direction: output
  data_types: double
```

### 输入

### **clk in** — 输入时钟频率标量

输入时钟频率，指定为标量。在 PLL 系统中，**clk in** 端口连接到 VCO 模块的输出端口。

**数据类型：** `double`

### **div-by** — 输出与输入时钟频率之比标量整数

输出与输入时钟频率之比，以标量整数表示。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟频率标量

输出时钟频率，以标量表示。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口的输出是幅度为 1 V 的方波脉冲序列。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Enable increased buffer size
  summary: 启用增大的缓冲区大小 off（默认）| on
  group: ''
- name: Buffer size
  summary: 仿真期间可用的输入缓冲采样数 1（默认）| 正整数标量
  group: ''
```

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。这会增大 Single Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `1`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 Single Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所需的所有输入采样。

#### 依赖关系

此参数仅在“模块参数”对话框中选中 **Enable increased buffer size** 选项时可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **Buffer size** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **Buffer size** 设置为特定值。
## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

将输入信号频率进行分频的整数时钟分频器

Single Modulus Prescaler 子系统模块将输入信号的频率除以传递给 **div-by** 端口的可调整数值 *N*。在频率合成器电路（如锁相环（PLL）系统）中，这些预分频器将 VCO 输出频率除以一个整数值。预分频器输出端口得到的较低频率与 PFD 模块的参考输入相当。Single Modulus Prescaler 也称为整数时钟分频器。
