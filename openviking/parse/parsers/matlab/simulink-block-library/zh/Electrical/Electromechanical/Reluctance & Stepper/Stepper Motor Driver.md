---
type: simulink-block
title: 'Stepper Motor Driver'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Reluctance & Stepper'
documentation_page: 'steppermotordriver'
documentation_source_path: 'ref/steppermotordriver.html'
language: zh-CN
chinese_source: worker-translation
---

# Stepper Motor Driver

## 端口

### 守恒

### **A+** — *A* 相正端电气

与 *A* 相正端关联的电气守恒端口。

### **A-** — *A* 相负端电气

与 *A* 相负端关联的电气守恒端口。

### **B+** — *B* 相正端电气

与 *B* 相正端关联的电气守恒端口。

### **B-** — *B* 相负端电气

与 *B* 相负端关联的电气守恒端口。

### **ENA** — 触发输入步进电压电气

与步进触发输入关联的电气守恒端口。

### **REF** — 输入浮动参考电压电气

与浮动参考电压关联的电气守恒端口。

### **REV** — 控制电机方向的输入电压电气

与电机方向输入关联的电气守恒端口。

### **VM** — 电源电压电气

与电源电压关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Power supply** 设置为 `External`。

### **GND** — 电源接地参考电气

与电源接地参考关联的电气守恒端口。

在外部电源模式下，**A-** 和 **B-** 端口内部连接到 **GND**。您必须提供正电源电压，并且电源必须始终连接（例如，不能在电源和驱动器之间放置串联开关）。

#### 依赖关系

要启用此端口，请将 **Power supply** 设置为 `External`。

## 参数

### **Simulation mode** — 仿真模式 `Stepping` (default) | `Averaged`

仅当该模块直接连接到同样以 Averaged 模式运行的 Stepper Motor 模块时，才使用 `Averaged`。

### **Step rate sensitivity** — 步进速率需求灵敏度 `10` `Hz/V` (default) | 正数

此参数将 **ENA** 和 **REF** 端口两端的电压转换为步进速率需求。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Enable threshold voltage** — 步进电压阈值 `2.5` `V` (default) | 正数

当 **ENA** 端口处的电压上升到高于此阈值时，Stepper Motor Driver 模块会启动一个步进。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Reverse threshold voltage** — 反转电压阈值 `2.5` `V` (default) | 正数

当 **REV** 端口处的电压上升到高于此阈值时，脉冲 *B* 比脉冲 *A* 超前 90 degrees，并且电机方向反转。

### **Output voltage amplitude** — 脉冲输出幅值 `10` `V` (default) | 正数

输出脉冲序列的幅值。

#### 依赖关系

要启用此参数，需满足以下任一条件：

- 将 **Simulation mode** 设置为 `Averaged`。
- 将 **Simulation mode** 设置为 `Stepping`，并将 **Power supply** 设置为 `Internal`。

### **Supply voltage** — 电源电压 `10` `V` (default) | 正数

来自外部电源的电压。

#### 依赖关系

要启用此参数，请将 **Stepping mode** 设置为 `Microstepping`，并将 **Power supply** 设置为 `Internal`。

### **Stepping mode (averaged)** — 平均仿真的步长 `Full stepping` (default) | `Half stepping`

是否启用 `Full stepping` 或 `Half stepping` 模式。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Averaged`。

### **Stepping mode** — 步进仿真的步长 `Full stepping` (default) | `Half stepping` | `Microstepping`

是否启用 `Full stepping`、`Half stepping` 或 `Microstepping` 模式。

#### 依赖关系

要启用此参数，请将 **Simulation mode** 设置为 `Stepping`。

### **Number of microsteps per step** — 每步微步数 `4` (default) | 正数

每步的微步数。此值必须为 2 的正整数次幂。

#### 依赖关系

要启用此参数，请将 **Stepping mode** 设置为 `Microstepping`。

### **Maximum continuous current per phase** — 每相最大连续电流 `1.2` `A` (default)

每相最大连续电流

#### 依赖关系

要启用此参数，请将 **Stepping mode** 设置为 `Microstepping`。

## 所属库

Simscape / Electrical / Electromechanical / Reluctance & Stepper

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

步进电机驱动器

Stepper Motor Driver 模块表示步进电机的驱动器。它创建控制电机所需的脉冲序列 *A* 和 *B*。每当 **ENA** 端口处的电压上升到高于 **Enable threshold voltage** 参数值时，此模块会启动一个步进。

如果 **REV** 端口处的电压小于或等于 **Reverse threshold voltage** 参数值，则脉冲 *A* 比脉冲 *B* 超前 90 degrees。如果 **REV** 端口处的电压大于 **Reverse threshold voltage** 值，则脉冲 *B* 比脉冲 *A* 超前 90 degrees，并且电机方向反转。

在时间零点，脉冲 *A* 为正，脉冲 *B* 为负。

如果将 **Stepping mode** 参数设置为 `Half stepping`，Stepper Motor Driver 模块可以生成半步进所需的输出波形。在此模式下，全步之间有一个中间状态，其中仅 *A* 或 *B* 半绕组中的一个通电。因此，步长是步进电机全步长的一半。在半步时，未通电的绕组短路。这近似于连接在绕组两端的续流二极管的效果。

### Microstepping

要使转子前进一个步长的一部分而不是全步或半步，请将 **Stepping mode** 参数设置为 `Microstepping`。此模式启用循环电流控制微步进，并提高转子位置的分辨率。要选择分数步进分辨率，请指定 **Number of microsteps per step** 参数的值。

每当 **ENA** 端口处的电压上升到高于 **Enable threshold voltage** 参数的值时，该模块会启动一个微步。

在微步进模式下，每个电机绕组中的电流遵循离散正弦波形。电流波形的幅值等于 **Maximum continuous current per phase** 参数的值。

要在每个微步中增加或减少电流，驱动器会施加正或负过压，直到电流达到目标值。

如果将 **Power supply** 参数设置为 `Internal`，则施加的过压等于 **Supply voltage** 参数的值。如果将 **Power supply** 参数设置为 `External`，则施加的过压等于 **VM** 和 **GND** 端口之间的电压。

### Averaged 模式

如果将 **Simulation mode** 参数设置为 `Averaged`，并且 Stepper Motor Driver 模块和连接到它的 Stepper Motor 模块都如此设置，则不会仿真各个步。这可以是加快仿真的好方法。`Averaged` 模式假设外部控制器提供步进速率需求。此步进速率需求根据施加在 Stepper Motor Driver 模块上的 **ENA** 和 **REF** 端口之间的电压确定，方法是将此电压乘以 **Step rate sensitivity** 参数的值。旋转方向由 **REF** 端口以与 `Stepping` 模式相同的方式设置。

`Averaged` 模式需要将步进速率需求和输出电压幅值信息传递给 Stepper Motor 模块。为此，步进速率需求作为等效电压施加在 **A+** 和 **A-** 端口两端。类似地，输出电压幅值信息通过将稳态电压施加在 **B+** 和 **B-** 端口两端来传递，其值等于 **Output voltage amplitude** 参数。
