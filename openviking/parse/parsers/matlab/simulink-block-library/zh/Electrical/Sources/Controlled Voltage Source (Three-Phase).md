---
type: simulink-block
title: 'Controlled Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'controlledvoltagesourcethreephase'
documentation_source_path: 'ref/controlledvoltagesourcethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Voltage Source (Three-Phase)

## 端口

### 输入

### **S** — 控制物理信号 | vector

与控制信号关联的物理信号输入端口。输出电压为 [*va* *vb* *vc*] = *S*。
对于理想正弦源，输入三个正弦波，其所需幅值和相位延迟为 [0−2π32π3]。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为 `Instantaneous`。

### **Vt** — 相间 RMS 电压物理信号

与相间 RMS 电压关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为 `Sinusoidal magnitude and phase shift`。

### **ph** — 相移物理信号

与相移关联的物理信号输入端口，单位为 radians。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为 `Sinusoidal magnitude and phase shift`。

### 守恒

### **n** — 中性电气

与中性相位关联的电气守恒端口。

### **~** — 三相电压电气

与输出电压关联的可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电压电气

与 *a* 相输出电压关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电压电气

与 *b* 相输出电压关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电压电气

与 *c* 相输出电压关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Expanded three-phase ports`。

## 参数

### **Modeling option** — 是建模复合还是扩展三相端口 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

是建模复合还是扩展三相端口。

复合三相端口用单个模块端口表示三个单独的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个单独的电气守恒端口表示三相系统的各个相。

### **Input type** — 输入类型 `Instantaneous` (默认) | `Sinusoidal magnitude and phase shift`

物理信号输入的类型。可选择：

- `Instantaneous` — 输出电压 [*va* *vb* *vc*] 等于输入端口 **S** 的值。
- `Sinusoidal magnitude and phase shift` — 输出电压等于：

  va=(2Vt3)sin(2πFrated+ph)vb=(2Vt3)sin(2πFrated+ph−2π3)vc=(2Vt3)sin(2πFrated+ph+2π3)

### **Rated electrical frequency** — 额定电气频率 `60` `Hz` | scalar

额定电气频率。此参数的值必须等于模型中其他正弦源（如果存在）的额定电气频率的值。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Sinusoidal magnitude and phase shift`。

## 所属库

Simscape / Electrical / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

理想三相受控电压源

Controlled Voltage Source (Three-Phase) 模块表示理想三相电压源，该电源无论流过它的电流如何都维持指定电压。

要选择此模块的输入类型，请将 **Input type** 参数设置为 `Instantaneous` 或 `Sinusoidal magnitude and phase shift`。如果选择 `Instantaneous`，此模块仅在时间仿真模式下工作。如果选择 `Sinusoidal magnitude and phase shift`，此模块在时间和频率-时间仿真模式下均可工作。有关详细信息，请参阅频率和时间仿真模式。

要访问具有扩展三相端口的实现，请双击该模块，并将 **Modeling option** 参数设置为 `Expanded three-phase ports`。
