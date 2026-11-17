---
type: simulink-block
title: 'Multiplier'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'multiplier'
documentation_source_path: 'ref/multiplier.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiplier

## 端口

### 守恒端口

### **X1** — X 输入同相输入端电气

与乘法器 X1 同相输入端关联的电气守恒端口。

### **X2** — X 输入反相输入端电气

与乘法器 X2 反相输入端关联的电气守恒端口。

### **Y1** — Y 输入同相输入端电气

与乘法器 Y1 同相输入端关联的电气守恒端口。

### **Y2** — Y 输入反相输入端电气

与乘法器 Y2 反相输入端关联的电气守恒端口。

### **Z1** — Z 输入同相输入端电气

与乘法器 Z1 同相输入端关联的电气守恒端口。

### **Z2** — Z 输入反相输入端电气

与乘法器 Z2 反相输入端关联的电气守恒端口。

### **~** — 乘法输出信号电气

与乘法器输出端口关联的电气守恒端口。

## 参数

### 主要

### **Scaling factor, K** — 比例因子 `10` `V`（默认）

定义输出电压的方程中的比例因子 *K*。数据手册中有时将其称为 scale factor 或 SF。

### **Gain, A** — 增益 `3000`（默认）

内部运算放大器的增益，对应于定义输出电压的方程中的增益 *A*。

### 输入

### **Differential resistance, Rin** — 差分电阻 `10e6` `Ohm`（默认）

每个差分输入近似为值为 *Rin* 的线性电阻。将此值设置为数据手册中的差分电阻值。

### **Differential signal voltage range** — 差分信号电压范围 `10` `V`（默认）

此值 *Vdiff\_max* 用于限制三个差分输入电压各自的幅值。将此值设置为数据手册中的差分信号电压范围值。

### 输出

### **Output resistance, Rout** — 输出电阻 `0.1` `Ohm`（默认）

乘法器输出级在 Band-Limited Op-Amp 模块内部建模为电压源加串联电阻。此参数指定该串联电阻的值。

### **Minimum output, Vmin** — 最小输出 `-11` `V`（默认）

输出电压的下限。

### **Maximum output, Vmax** — 最大输出 `11` `V`（默认）

输出电压的上限。

### **Maximum slew rate, Vdot** — 最大压摆率 `20` `V/us`（默认）

输出电压幅值的最大正向或负向变化率。

### **Bandwidth, f** — 带宽 `1` `MHz`（默认）

Band-Limited Op-Amp 模块的带宽。

### **Initial output voltage, V0** — 初始输出电压 `0` `V`（默认）

如果在 Solver 模块中未选择 **Start simulation from steady-state** 选项，则为 Multiplier 模块输出的初始值。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010b 中引入**

## 描述

集成电路乘法器

Multiplier 模块对集成电路乘法器进行建模。该模块实现以下方程，该方程定义了施加到输出端口的电压：

Vout=A((X1−X2)(Y1−Y2)K−(Z1−Z2))

其中 *X1*、*X2*、*Y1*、*Y2*、*Z1*、*Z2* 为输入端口处的电压，*A* 为增益，*K* 为比例因子。

在典型乘法电路中，输出被反馈到输入 Z1，从而产生以下增益（假设 *A* 很大）：

Vout=((X1−X2)(Y1−Y2)K+Z2)

比例因子 *K* 的值通常由外部电阻偏置网络改变。Multiplier 模块将 *K* 实现为内部增益，系统仿真不需要外部偏置网络。*K* 的典型值为 10，典型可调低至 3。

除了乘法之外，您还可以使用 Multiplier 模块实现许多其他功能。示例包括除法、平方和平方根。有关示例电路，请查阅制造商数据手册。

下图显示了 Multiplier 模块的内部模型结构。它包含 Band-Limited Op-Amp 模块，用于对有限带宽和压摆率限制进行建模。

下一图显示了其中一个差分子系统模块。所有三个差分子系统模块在结构上完全相同。
