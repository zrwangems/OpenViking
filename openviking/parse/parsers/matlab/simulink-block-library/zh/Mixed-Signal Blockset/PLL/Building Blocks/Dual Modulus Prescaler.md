---
type: simulink-block
title: 'Dual Modulus Prescaler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Building Blocks'
documentation_page: 'dualmodulusprescaler'
documentation_source_path: 'ref/dualmodulusprescaler.html'
language: zh-CN
chinese_source: worker-translation
---

# Dual Modulus Prescaler

## 端口
```yaml
ports:
- name: clk in
  summary: 输入时钟频率标量
  direction: input
  data_types: double
- name: clk out
  summary: 输出时钟频率标量
  direction: output
  data_types: double
```

### 输入

### **clk in** — 输入时钟频率标量

输入时钟频率，指定为标量。在锁相环（PLL）系统中，**clk in** 端口连接到 VCO 模块的输出端口。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟频率标量

输出时钟频率，指定为标量。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口的输出是幅度为 1 V 的方波脉冲序列。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Program counter value, P
  summary: 程序计数器的最大值 12（默认）| 标量整数
  group: ''
- name: Prescaler divider value, N
  summary: 预分频器分频值 4（默认）| 标量整数
  group: ''
- name: Swallow counter value, S
  summary: 吞脉冲计数器的最大值 2（默认）| 标量整数
  group: ''
- name: Enable increased buffer size
  summary: 启用增大的缓冲区大小 off（默认）| on
  group: ''
- name: Buffer size
  summary: 仿真期间可用的输入缓冲采样数 1（默认）| 正整数标量
  group: ''
```

### **Program counter value, P** — 程序计数器的最大值 `12`（默认）| 标量整数

程序计数器的最大值，指定为标量整数。计数器在 *P* 个周期后复位。此参数可调。

#### 编程方式使用

- 使用 `get_param(gcb,'P')` 查看当前的 **Program counter value** 值。
- 使用 `set_param(gcb,'P',value)` 将 **Program counter value** 设置为特定值。

### **Prescaler divider value, N** — 预分频器分频值 `4`（默认）| 标量整数

预分频器分频值，指定为标量整数。*N*/(*N*+1) 双模预分频器根据模数控制线的逻辑状态，将输入频率除以 *N* 或 *N*+1。此参数可调。

#### 编程方式使用

- 使用 `get_param(gcb,'N')` 查看当前的 **Prescaler divider value**。
- 使用 `set_param(gcb,'N',value)` 将 **Prescaler divider value** 设置为特定值。

### **Swallow counter value, S** — 吞脉冲计数器的最大值 `2`（默认）| 标量整数

吞脉冲计数器的最大值，指定为标量整数。当吞脉冲计数器在 *S* 个周期后复位时，脉冲吞没功能被停用。

#### 编程方式使用

- 使用 `get_param(gcb,'S')` 查看当前的 **Swallow counter value** 值。
- 使用 `set_param(gcb,'S',value)` 将 **Swallow counter value** 设置为特定值。

### **Enable increased buffer size** — 启用增大的缓冲区大小 off（默认）| on

选择以在仿真期间启用增大的缓冲区大小。这会增大 Dual Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。默认情况下，此选项未选中。

### **Buffer size** — 仿真期间可用的输入缓冲采样数 `1`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。这会设置 Dual Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，以便输入缓冲区包含所有所需的输入采样。

#### 依赖关系

此参数仅在“模块参数”对话框中选中 **Enable increased buffer size** 选项时可用。

#### 编程方式使用

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

具有两个分频比率的整数时钟分频器

双模预分频器子系统模块由一个程序计数器、一个吞脉冲计数器和一个预分频器组成。

当模块首次接收到输入信号时，脉冲吞脉冲功能被激活。预分频器将输入信号频率除以 (*N*+1)，其中 *N* 由 **预分频器分频值 (N)** 参数定义。程序计数器和吞脉冲计数器同时开始计数。吞脉冲计数器在计数到 *S* 个脉冲后复位，即 (*N*+1)S 个周期，其中 *S* 由 **吞脉冲计数器值 (S)** 参数定义。然后，脉冲吞脉冲功能被停用，预分频器将输入频率除以 *N*。

由于程序计数器已经检测到 S 个脉冲，它还需要 (*P*-*S*) 个脉冲，即 (*P*-*S*)*N* 个周期才能达到溢出，其中 *P* 由 **程序计数器值 (P)** 参数定义。在两个计数器都复位后，该循环重复。

双模预分频器的有效分频值是输入频率与输出频率之比：

finfout=(N+1)S+N(P−S)=NP+S

**注意**

为了防止程序计数器和预分频器在吞脉冲计数器完成计数之前过早复位，必须满足条件 P≥S。

双模预分频器也称为脉冲吞脉冲分频器。
