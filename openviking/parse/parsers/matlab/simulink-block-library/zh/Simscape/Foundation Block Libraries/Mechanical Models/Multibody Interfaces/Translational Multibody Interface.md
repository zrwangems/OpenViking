---
type: simulink-block
title: 'Translational Multibody Interface'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Multibody Interfaces'
documentation_page: 'translationalmultibodyinterface'
documentation_source_path: 'ref/translationalmultibodyinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Multibody Interface

## 端口

### 输入

### **v** — 相对速度，m/s 物理信号

物理信号输入端口，接受来自关节基元的相对速度传感输出。将此端口连接到 Simscape Multibody 关节的速度传感端口 **v**。

### 输出

### **f** — 力，N 物理信号

物理信号输出端口，向关节基元提供力驱动输入。将此端口连接到 Simscape Multibody 关节的力驱动端口 **f**。

### 守恒

### **R** — 杆机械平动

机械平动守恒端口，其力和相对速度与关节基元相同。将此端口连接到机械平动网络中其他模块的端口 **R**。

### **C** — 壳体机械平动

机械平动守恒端口，其力和相对速度与关节基元相同。将此端口连接到机械平动网络中其他模块的端口 **C**。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Mechanical / Multibody Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021a 中引入**

## 描述

机械平动网络与 Simscape Multibody 关节之间的接口

Translational Multibody Interface 模块实现了一种直观的方式，用于将具有机械平动端口的 Simscape™ 模块与具有移动副基元的 Simscape Multibody™ 关节连接起来。可连接到 Translational Multibody Interface 模块的 Simscape 模块包括：

- 来自 Foundation > Mechanical > Translational Elements 库的模块，例如 Translational Friction 或 Translational Damper。
- 来自其他 Foundation 库且具有机械平动端口的模块，例如 Translational Mechanical Converter (G) 或 Translational Mechanical Converter (IL)。
- 来自附加产品且具有机械平动端口的模块，例如来自 Simscape Fluids™ 库的液压执行器。

Translational Multibody Interface 模块匹配接口两侧的力和相对速度。您可以将其连接到任何具有移动副基元的 Simscape Multibody 关节：

1. 在关节上启用速度传感端口 **v** 和力驱动端口 **f**。如果关节具有多个自由度，请确保所选的速度传感和力驱动对应于同一自由度。
2. 将 Translational Multibody Interface 模块的物理信号端口 **v** 和 **f** 连接到 Simscape Multibody 关节的端口 **v** 和 **f**。
3. 将 Translational Multibody Interface 模块的端口 **C** 和 **R** 连接到 Simscape 机械平动网络。

显示如何连接 Translational Multibody Interface 模块的框图

有关详细的分步说明，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

像 Translational Friction 和 Translational Damper 这样的模块不需要位置信息，对于这些模块，基于力和相对速度的接口就足够了。其他模块（如液压执行器）需要其端口之间相对位置的信息。要将这些模块连接到 Simscape Multibody 关节：

1. 使用 Translational Multibody Interface 模块。在关节上启用速度传感端口 **v** 和力驱动端口 **f**，并按上述方式连接端口。
2. 此外，在关节上启用位置传感端口 **p**。如果关节具有多个自由度，请确保位置传感、速度传感和力驱动都对应于同一自由度。
3. 在执行器模块上，通过将 **Interface displacement** 参数设置为 `Provide input signal from Multibody joint` 来启用位置输入端口 **p**。将执行器模块上的位置输入端口 **p** 连接到 Simscape Multibody 关节的位置传感端口 **p**。

显示如何连接 Translational Multibody Interface 模块并传递位置信息的框图

### 假设和限制

对于包含 Translational Multibody Interface 或 Rotational Multibody Interface 模块的模型，建议使用 Simscape Multibody 模块对质量和惯量建模。原因是 Simscape 网络需要有一个接地（参考）节点，网络中的所有质量和惯量都相对于该节点加速。在 Simscape Multibody 关节中，基础坐标系和从动坐标系都可能正在加速。因此，连接到关节的 Simscape 网络中的质量或惯量可能没有正确的惯性参考。
