---
type: simulink-block
title: 'Unipolar Stepper Motor Driver'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'unipolarsteppermotordriver'
documentation_source_path: 'ref/unipolarsteppermotordriver.html'
language: zh-CN
chinese_source: worker-translation
---

# Unipolar Stepper Motor Driver

## 端口

### 守恒

### **A+** — 顶部 A 相电气连接 electrical

与顶部 A 相电气连接相关联的电气守恒端口。

### **A0** — A 相中心抽头连接 electrical

与 A 相中心抽头连接相关联的电气守恒端口。

### **A-** — 下部 A 相电气连接 electrical

与下部 A 相电气连接相关联的电气守恒端口。

### **B+** — 顶部 B 相电气连接 electrical

与顶部 B 相电气连接相关联的电气守恒端口。

### **B0** — B 相中心抽头连接 electrical

与 B 相中心抽头连接相关联的电气守恒端口。

### **B-** — 下部 B 相电气连接 electrical

与下部 B 相电气连接相关联的电气守恒端口。

### **ENA** — 触发输入步进电压 electrical

与触发输入步进电压相关联的电气守恒端口。

### **REF** — 转子 electrical

与输入浮置参考电压相关联的电气守恒端口。

### **REV** — 电机方向控制电压 electrical

与用于控制电机方向的电压相关联的电气守恒端口。

## 参数

### **仿真模式** — 仿真模式 `Stepping`（默认）| `Averaged`

选择 `Stepping` 或 `Averaged`。仅当该模块直接连接到同样以 **Averaged** 模式运行的 Unipolar Stepper Motor 模块时，才使用 `Averaged`。

### **步进速率灵敏度** — 步进速率灵敏度 `10` `Hz/V`（默认）

此参数将 **ENA** 和 **REF** 端口之间的电压转换为步进速率需求。

#### 依赖项

仅当您将 **仿真模式** 参数设置为 `Averaged` 时，此参数才可见。

### **使能阈值电压** — 使能阈值电压 `2.5` `V`（默认）

当 **ENA** 端口处的电压升高到超过此阈值时，Unipolar Stepper Motor Driver 模块会启动一个步进。

#### 依赖项

仅当您将 **仿真模式** 参数设置为 `Stepping` 时，此参数才可见。

### **反向阈值电压** — 反向阈值电压 `2.5` `V`（默认）

当 **REV** 端口处的电压升高到超过此阈值时，脉冲 *B* 领先脉冲 *A* 90 度，并且电机方向反向。

### **输出电压幅值** — 输出电压幅值 `10` `V`（默认）

输出脉冲序列的幅值。

### **步进模式** — 步进模式 `Full stepping`（默认）| `Half stepping`

选择 `Full stepping` 或 `Half stepping`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

用于单极步进电机的驱动器

Unipolar Stepper Motor Driver 模块表示专门配置用于 Unipolar Stepper Motor 模块的驱动器。它将两个绕组中心抽头连接 A0 和 B0 连接到正电源，电压等于您为 **输出电压幅值** 参数提供的值。**A+**、**A-**、**B+** 和 **B-** 端口按适当的顺序接地，以产生步进运动。每当 **ENA** 端口处的电压升高到超过 **使能阈值电压** 参数值时，该模块就会启动一个步进。

如果 **REV** 端口处的电压小于或等于 **反向阈值电压** 参数值，则脉冲 *A* 领先脉冲 *B* 90 度。如果 **REV** 端口处的电压大于 **反向阈值电压** 值，则脉冲 *B* 领先脉冲 *A* 90 度，并且电机方向反向。

在零时刻，**A-** 和 **B+** 接地。

如果您将 **步进模式** 参数设置为 `Half stepping`，则 Unipolar Stepper Motor Driver 模块可以生成半步步进所需的输出波形。在此模式下，全步之间有一个中间状态，其中仅 *A* 或 *B* 半绕组中的一个通电。因此，步长是步进电机全步长的一半。在半步时，未通电的绕组被短路。这近似于跨接在绕组两端的续流二极管的效果。

### Averaged 模式

如果您将 **仿真模式** 参数设置为 `Averaged`，对于 Unipolar Stepper Motor Driver 模块以及连接到它的 Unipolar Stepper Motor 模块都是如此，则不会仿真各个步进。这可能是加快仿真的好方法。`Averaged` 模式假定外部控制器提供步进速率需求。此步进速率需求由施加在 Unipolar Stepper Motor Driver 模块上 **ENA** 和 **REF** 端口之间的电压乘以 **步进速率灵敏度** 参数的值来确定。旋转方向由 **REF** 端口以与 Stepping 模式相同的方式设置。

`Averaged` 模式需要将步进速率需求和输出电压幅值信息传递给 Unipolar Stepper Motor 模块。为此，步进速率需求作为等效电压施加在 **A+** 和 **A-** 端口两端。类似地，输出电压幅值信息通过以下方式传递：在 **B+** 和 **B-** 端口两端施加稳态电压，其值等于 **输出电压幅值** 参数。
