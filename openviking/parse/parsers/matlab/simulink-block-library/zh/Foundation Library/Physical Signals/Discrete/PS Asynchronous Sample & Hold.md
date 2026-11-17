---
type: simulink-block
title: 'PS Asynchronous Sample & Hold'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Discrete'
documentation_page: 'psasynchronoussamplehold'
documentation_source_path: 'ref/psasynchronoussamplehold.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Asynchronous Sample & Hold

## 端口

### 输入

### **U** — 输入物理信号，无类型物理信号

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

### **T** — 触发物理信号，无量纲物理信号

触发采样保持动作的输入物理信号。在模块图标中，此端口标记有（上升沿）符号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
### 输出

### **Y** — 输出物理信号，无类型物理信号

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。

## 参数

### **Initial output** — 零时刻的输出 `0 1`（默认）

零时刻输出信号的值和单位。第一个编辑框表示信号值。模块的输出保持此值，直到模块被变为正值的上升触发信号触发。

第二个组合框表示信号单位。默认情况下，单位为 `1`（无量纲）。指定与输入端口 **U** 处信号单位一致的单位。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`），或有效的表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

## 所属库

Simscape / Foundation Library / Physical Signals / Discrete

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用升级顾问将模块升级到最新版本。有关更多信息，请参阅升级具有旧版物理信号模块的模型。

## 描述

带外部触发的输出采样保持信号

当触发输入的上升沿变为大于零时，PS Asynchronous Sample & Hold 模块将输出信号 *Y* 设置为等于输入信号 *U*。将此模块与其他物理信号模块结合使用，以对离散和基于事件的行为进行建模。

Asynchronous PWM Voltage Source 示例说明了如何使用 PS Asynchronous Sample & Hold 模块构建具有更复杂行为的组件。有关替代的离散时间实现，请参阅 Discrete-Time PWM Voltage Source 示例。离散时间版本更适合固定步长求解器和硬件在环应用，而异步实现更适合使用变步长求解器进行快速桌面仿真。

输出端口处的信号单位由单位传播规则确定。
