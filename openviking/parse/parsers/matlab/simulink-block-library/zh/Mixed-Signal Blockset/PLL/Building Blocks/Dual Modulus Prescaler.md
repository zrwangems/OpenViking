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

### 输入

### **clk in** — 输入时钟频率（标量）

输入时钟频率，指定为标量。在锁相环（PLL）系统中，**clk in** 端口连接到 VCO 模块的输出端口。

**数据类型：** `double`
### 输出

### **clk out** — 输出时钟频率（标量）

输出时钟频率，指定为标量。在 PLL 系统中，**clk out** 端口连接到 PFD 模块的反馈输入端口。**clk out** 端口处的输出是幅度为 1 V 的方波脉冲串。

**数据类型：** `double`

## 参数

### **程序计数器值，P** — 程序计数器的最大值 `12`（默认）| 标量整数

程序计数器的最大值，指定为标量整数。计数器在 *P* 个周期后复位。此参数可调。

#### 编程用法

- 使用 `get_param(gcb,'P')` 查看当前 **程序计数器值** 的取值。
- 使用 `set_param(gcb,'P',value)` 将 **程序计数器值** 设置为特定值。

### **预分频器分频值，N** — 预分频器分频值 `4`（默认）| 标量整数

预分频器分频值，指定为标量整数。*N*/(*N*+1) 双模预分频器根据模控制线的逻辑状态，将输入频率除以 *N* 或 *N*+1。此参数可调。

#### 编程用法

- 使用 `get_param(gcb,'N')` 查看当前 **预分频器分频值**。
- 使用 `set_param(gcb,'N',value)` 将 **预分频器分频值** 设置为特定值。

### **吞咽计数器值，S** — 吞咽计数器的最大值 `2`（默认）| 标量整数

吞咽计数器的最大值，指定为标量整数。当吞咽计数器在 *S* 个周期后复位时，脉冲吞咽功能被停用。

#### 编程用法

- 使用 `get_param(gcb,'S')` 查看当前 **吞咽计数器值** 的取值。
- 使用 `set_param(gcb,'S',value)` 将 **吞咽计数器值** 设置为特定值。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小 off（默认）| on

选中此选项可在仿真期间启用增大的缓冲区大小。这会增大 Dual Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。默认情况下，此选项处于未选中状态。

### **缓冲区大小** — 仿真期间可用的输入缓冲的样本数 `1`（默认）| 正整数标量

仿真期间可用的输入缓冲的样本数，指定为正整数标量。这会设置 Dual Modulus Prescaler 模块内部 Logic Decision 的缓冲区大小。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数。将 **缓冲区大小** 设置为足够大的值，以使输入缓冲区包含所需的全部输入样本。

#### 依赖关系

仅当在“模块参数”对话框中选中 **启用增大的缓冲区大小** 选项时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NBuffer')` 查看 **缓冲区大小** 的当前值。
- 使用 `set_param(gcb,'NBuffer',value)` 将 **缓冲区大小** 设置为特定值。

## 所属库

Mixed-Signal Blockset / PLL / Building Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

具有两个分频比的整数时钟分频器

Dual Modulus Prescaler 子系统模块由程序计数器、吞咽计数器和预分频器组成。

当模块首次接收到输入信号时，脉冲吞咽功能被激活。预分频器将输入信号频率除以 (*N*+1)，其中 *N* 由 **预分频器分频值 (N)** 参数定义。程序计数器和吞咽计数器都开始计数。吞咽计数器在计数到 *S* 个脉冲（即 (*N*+1)S 个周期）后复位，其中 *S* 由 **吞咽计数器值 (S)** 参数定义。然后，脉冲吞咽功能被停用，预分频器将输入频率除以 *N*。

由于程序计数器已经检测到 S 个脉冲，因此它还需要 (*P*-*S*) 个脉冲，即 (*P*-*S*)*N* 个周期才能达到溢出，其中 *P* 由 **程序计数器值 (P)** 参数定义。两个计数器复位后，该循环重复。

双模预分频器的有效分频值是输入频率与输出频率之比：

finfout=(N+1)S+N(P−S)=NP+S

**注意**

为避免程序计数器和预分频器在吞咽计数器完成计数之前过早复位，必须满足条件 P≥S。

双模预分频器也称为脉冲吞咽分频器。
