---
type: simulink-block
title: 'Rotational Multibody Interface'
family: 'mechanical'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Multibody Interfaces'
documentation_page: 'rotationalmultibodyinterface'
documentation_source_path: 'ref/rotationalmultibodyinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Multibody Interface

## 端口

### 输入

### **w** — 相对角速度，rad/s，物理信号

物理信号输入端口，接受来自关节基元的相对角速度传感输出。将此端口连接到 Simscape Multibody 关节的速度传感端口 **w**。

### 输出

### **t** — 扭矩，N\*m，物理信号

物理信号输出端口，向关节基元提供扭矩驱动输入。将此端口连接到 Simscape Multibody 关节的扭矩驱动端口 **t**。

### 守恒

### **R** — 杆机械旋转

机械旋转守恒端口，具有与关节基元相同的扭矩和相对角速度。将此端口连接到机械旋转网络中其他模块的 **R** 端口。

### **C** — 外壳机械旋转

机械旋转守恒端口，具有与关节基元相同的扭矩和相对角速度。将此端口连接到机械旋转网络中其他模块的 **C** 端口。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Mechanical / Multibody Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**于 R2021a 推出**

## 描述

机械旋转网络与 Simscape Multibody 关节之间的接口

Rotational Multibody Interface 模块提供了一种直观的方式，可将具有机械旋转端口的 Simscape™ 模块与具有旋转基元的 Simscape Multibody™ 关节连接起来。可连接到 Rotational Multibody Interface 模块的 Simscape 模块包括：

- Foundation > Mechanical > Rotational Elements 库中的模块，例如
  Rotational Friction 或 Rotational Damper。
- 其他 Foundation 库中具有机械旋转端口的模块，例如
  Rotational Mechanical Converter (G) 或
  Rotational Mechanical Converter (IL)。
- 附加产品中具有机械旋转端口的模块，例如 Simscape
  Fluids™ 库中的液压执行器。

Rotational Multibody Interface 模块使接口两侧的扭矩和相对角速度相匹配。您可以将其连接到任何具有旋转基元的 Simscape Multibody 关节：

1. 在关节上启用速度传感端口 **w** 和扭矩驱动端口
   **t**。如果关节具有多个自由度，请确保所选的速度传感和扭矩驱动对应于同一自由度。
2. 将 Rotational Multibody Interface 模块的物理信号端口 **w** 和 **t** 连接到 Simscape
   Multibody 关节的端口 **w** 和 **t**。
3. 将 Rotational Multibody Interface 模块的端口 **C** 和 **R** 连接到 Simscape 机械旋转网络。

显示如何连接 Rotational Multibody Interface 模块的框图

有关详细的分步说明，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

Rotational Friction 和
Rotational Damper 等模块不需要位置信息，对于这些模块，基于扭矩和相对角速度的接口就足够了。其他模块（如液压执行器）需要其端口之间的相对位置信息。要将这些模块连接到 Simscape
Multibody 关节，请执行以下操作：

1. 使用 Rotational Multibody Interface 模块。在关节上启用速度传感端口 **w** 和扭矩驱动端口
   **t**，并按照上述说明连接端口。
2. 此外，在关节上启用位置传感端口 **q**。如果关节具有多个自由度，请确保位置传感、速度传感和扭矩驱动均对应于同一自由度。
3. 在执行器模块上，通过将 **Interface rotation** 参数设置为 `Provide
   input signal from Multibody joint`，启用位置输入端口 **q**。将执行器模块上的位置输入端口
   **q** 连接到 Simscape
   Multibody 关节的位置传感端口 **q**。

显示如何连接 Rotational Multibody Interface 模块并传递位置信息的框图

### 假设和限制

对于包含 Translational Multibody Interface 或 Rotational Multibody Interface 模块的模型，建议您使用 Simscape
Multibody 模块对质量和惯量进行建模。原因是 Simscape 网络需要具有接地（参考）节点，网络中的所有质量和惯量均相对于此节点加速。在 Simscape
Multibody 关节中，基座坐标系和从动坐标系都可能处于加速状态。因此，连接到关节的 Simscape 网络中的质量或惯量可能不具有正确的惯性参考。
