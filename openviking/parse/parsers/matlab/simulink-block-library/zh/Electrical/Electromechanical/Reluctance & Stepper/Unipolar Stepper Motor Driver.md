---
type: simulink-block
title: 'Unipolar Stepper Motor Driver'
family: 'sps'
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

### 守恒端口

### **A+** — A 相上端电气连接 electrical

与 A 相上端电气连接相关联的电气守恒端口。

### **A0** — A 相中心抽头连接 electrical

与 A 相中心抽头连接相关联的电气守恒端口。

### **A-** — A 相下端电气连接 electrical

与 A 相下端电气连接相关联的电气守恒端口。

### **B+** — B 相上端电气连接 electrical

与 B 相上端电气连接相关联的电气守恒端口。

### **B0** — B 相中心抽头连接 electrical

与 B 相中心抽头连接相关联的电气守恒端口。

### **B-** — B 相下端电气连接 electrical

与 B 相下端电气连接相关联的电气守恒端口。

### **ENA** — 触发输入阶跃电压 electrical

与触发输入阶跃电压相关联的电气守恒端口。

### **REF** — 转子 electrical

与输入浮置参考电压相关联的电气守恒端口。

### **REV** — 电机方向控制电压 electrical

与控制电机方向的电压相关联的电气守恒端口。

## 参数

### **Simulation mode** — 仿真模式 `Stepping`（默认）| `Averaged`

选择 `Stepping` 或 `Averaged`。仅当该模块直接连接到同样以 **Averaged** 模式运行的 Unipolar Stepper Motor 模块时，才使用 `Averaged`。

### **Step rate sensitivity** — 步进速率灵敏度 `10` `Hz/V`（默认）

该参数将 **ENA** 和 **REF** 端口之间的电压转换为步进速率需求。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Averaged` 时，该参数才可见。

### **Enable threshold voltage** — 使能阈值电压 `2.5` `V`（默认）

当 **ENA** 端口处的电压升至该阈值以上时，Unipolar Stepper Motor Driver 模块启动一个步进。

#### 依赖关系

仅当将 **Simulation mode** 参数设置为 `Stepping` 时，该参数才可见。

### **Reverse threshold voltage** — 反向阈值电压 `2.5` `V`（默认）

当 **REV** 端口处的电压升至该阈值以上时，脉冲 *B* 超前脉冲 *A* 90 度，电机方向反转。

### **Output voltage amplitude** — 输出电压幅值 `10` `V`（默认）

输出脉冲序列的幅值。

### **Stepping mode** — 步进模式 `Full stepping`（默认）| `Half stepping`

选择 `Full stepping` 或 `Half stepping`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

## 描述

单极性步进电机驱动器

Unipolar Stepper Motor Driver 模块表示一个专门配置用于与 Unipolar Stepper Motor 模块配合使用的驱动器。它将两个绕组中心抽头连接 A0 和 B0 连接到正电源，电压等于为 **Output voltage amplitude** 参数提供的值。**A+**、**A-**、**B+** 和 **B-** 端口按适当的顺序接地以产生步进运动。每当 **ENA** 端口处的电压升至 **Enable threshold voltage** 参数值以上时，该模块启动一个步进。

如果 **REV** 端口处的电压小于或等于 **Reverse threshold voltage** 参数值，脉冲 *A* 超前脉冲 *B* 90 度。如果 **REV** 端口处的电压大于 **Reverse threshold voltage** 值，脉冲 *B* 超前脉冲 *A* 90 度，电机方向反转。

在零时刻，**A-** 和 **B+** 接地。

如果将 **Stepping mode** 参数设置为 `Half stepping`，Unipolar Stepper Motor Driver 模块可以产生半步步进所需的输出波形。在此模式下，整步之间存在一个中间状态，其中只有 *A* 或 *B* 半绕组之一通电。因此，步长是步进电机整步步长的一半。在半步时，未通电的绕组被短路。这近似于在绕组两端连接续流二极管的效果。

### Averaged 模式

如果将 Unipolar Stepper Motor Driver 模块以及连接到它的 Unipolar Stepper Motor 模块的 **Simulation mode** 参数都设置为 `Averaged`，则不会仿真各个步进。这可能是加快仿真速度的好方法。`Averaged` 模式假定外部控制器提供步进速率需求。该步进速率需求由施加在 Unipolar Stepper Motor Driver 模块上 **ENA** 和 **REF** 端口之间的电压乘以 **Step rate sensitivity** 参数的值确定。旋转方向由 **REF** 端口以与 Stepping 模式相同的方式设置。

`Averaged` 模式需要将步进速率需求以及输出电压幅值信息传递给 Unipolar Stepper Motor 模块。为此，步进速率需求作为等效电压施加在 **A+** 和 **A-** 端口之间。类似地，输出电压幅值信息通过将等于 **Output voltage amplitude** 参数的稳态电压施加在 **B+** 和 **B-** 端口之间来传递。
