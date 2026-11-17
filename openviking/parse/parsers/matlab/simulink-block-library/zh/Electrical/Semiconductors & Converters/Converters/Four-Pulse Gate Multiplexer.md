---
type: simulink-block
title: 'Four-Pulse Gate Multiplexer'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'fourpulsegatemultiplexer'
documentation_source_path: 'ref/fourpulsegatemultiplexer.html'
language: zh-CN
chinese_source: worker-translation
---

# Four-Pulse Gate Multiplexer

## 端口

### 输入

### **G1** — 栅极控制电压信号 1 物理信号

与所连接变换器模块中第一个开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

**数据类型：** `double`

### **G2** — 栅极控制电压信号 2 物理信号

与所连接变换器模块中第二个开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

**数据类型：** `double`

### **G3** — 栅极控制电压信号 3 物理信号

与所连接变换器模块中第三个开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

**数据类型：** `double`

### **G4** — 栅极控制电压信号 4 物理信号

与所连接变换器模块中第四个开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

**数据类型：** `double`
### 守恒

### **G1** — 栅极控制电压信号 1 电气

与所连接变换器模块中第一个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **a** — *A* 相交流参考点电气

与高侧开关器件的 *A* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G2** — 栅极控制电压信号 2 电气

与所连接变换器模块中第二个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **b** — *B* 相交流参考点电气

与高侧开关器件的 *B* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G3** — 栅极控制电压信号 3 电气

与所连接变换器模块中第三个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G4** — 栅极控制电压信号 4 电气

与所连接变换器模块中第四个开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **L** — 直流参考点电气

与低侧开关器件的直流负连接关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

## 参数

### **Gate-control port** — 栅极控制端口 `PS`（默认） | `Electrical`

是否公开 PS 或电气控制端口。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2021b：物理和电气连接端口更新

从 R2021b 开始，要在物理端口和电气端口之间切换，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Gate-control port** 参数。

## 描述

将栅极输入信号多路复用至四象限

Four-Pulse Gate Multiplexer 模块将四个单独的电压信号多路复用为单个向量。该向量化信号可以控制变换器（例如 Four-Quadrant Chopper 模块）中四个开关器件的栅极。

### 模型

此模块可以通过物理信号端口或电气端口来建模四脉冲栅极多路复用器：

- PS 端口 — 具有物理信号端口的四脉冲栅极多路复用器。将 **Gate-control port** 参数设置为 `PS`，以使用 Simulink® 栅极控制电压信号控制变换器模块中的开关器件栅极。要将 Simulink 信号多路复用并连接到变换器模块的栅极控制输入端口：

  1. 使用 Simulink-PS Converter 模块转换每个电压信号。
  2. 使用多路复用器模块将转换后的栅极信号多路复用为单个向量。
  3. 将向量信号连接到变换器的 **G** 端口。
- 电气端口 — 具有电气守恒端口的四脉冲栅极多路复用器。要使用 Simscape™ Electrical™ Electronics and Mechatronics 模块控制变换器模块中的开关器件栅极，请将 **Gate-control port** 参数设置为 `Electrical`。电气端口包括成对的电气连接。每对对应所连接变换器模块中一个开关器件的栅极和阴极。
