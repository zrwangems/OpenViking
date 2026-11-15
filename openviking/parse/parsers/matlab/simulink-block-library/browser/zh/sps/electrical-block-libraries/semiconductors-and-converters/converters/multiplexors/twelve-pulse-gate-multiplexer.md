---
type: simulink-block
title: 'Twelve-Pulse Gate Multiplexer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Multiplexors'
documentation_page: 'twelvepulsegatemultiplexer'
documentation_source_path: 'ref/twelvepulsegatemultiplexer.html'
language: zh-CN
chinese_source: worker-translation
---

# Twelve-Pulse Gate Multiplexer

## 端口

### 输入

### **Ga(1),Ga(2),Ga(3),Ga(4)** — Ga(1),Ga(2),Ga(3),Ga(4) 物理信号

与 Three-Level Converter (Three-Phase) *a* 相开关器件的门极端子关联的物理信号端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

### **Gb(1),Gb(2),Gb(3),Gb(4)** — Gb(1),Gb(2),Gb(3),Gb(4) 物理信号

与 Three-Level Converter (Three-Phase) *b* 相开关器件的门极端子关联的物理信号端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

### **Gc(1),Gc(2),Gc(3),Gc(4)** — Gc(1),Gc(2),Gc(3),Gc(4) 物理信号

与 Three-Level Converter (Three-Phase) *c* 相开关器件的门极端子关联的物理信号端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

### 守恒

### **Ga(1),Ga(2),Ga(3),Ga(4)** — Ga(1),Ga(2),Ga(3),Ga(4) 电气

与 Three-Level Converter (Three-Phase) *a* 相开关器件的门极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **Gb(1),Gb(2),Gb(3),Gb(4)** — Gb(1),Gb(2),Gb(3),Gb(4) 电气

与 Three-Level Converter (Three-Phase) *b* 相开关器件的门极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **Gc(1),Gc(2),Gc(3),Gc(4)** — Gc(1),Gc(2),Gc(3),Gc(4) 电气

与 Three-Level Converter (Three-Phase) *c* 相开关器件的门极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G** — G 电气

与多路复用门极信号关联的向量输出端口。将此端口连接到 Three-Level Converter (Three-Phase) 模块的 G 端口。

### **Ka(1),Ka(2),Ka(3),Ka(4)** — Ka(1),Ka(2),Ka(3),Ka(4) 电气

与 Three-Level Converter (Three-Phase) 模块 *a* 相开关器件对应的各个阴极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **Kb(1),Kb(2),Kb(3),Kb(4)** — Kb(1),Kb(2),Kb(3),Kb(4) 电气

与 Three-Level Converter (Three-Phase) 模块 *b* 相开关器件对应的各个阴极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **Kc(1),Kc(2),Kc(3),Kc(4)** — Kc(1),Kc(2),Kc(3),Kc(4) 电气

与 Three-Level Converter (Three-Phase) 模块 *c* 相开关器件对应的各个阴极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

## 参数

### **Gate-control port** — 门极控制端口 `PS`（默认） | `Electrical`

是否公开 PS 或电气控制端口。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：物理和电气连接端口更新

从 R2021b 起，要在物理端口和电气端口之间切换，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **Gate-control port** 参数。

## 描述

将门极输入信号多路复用至 Three-Level Converter (Three-Phase) 模块

Twelve-Pulse Gate Multiplexer 模块将门极电压信号路由到 Three-Level Converter (Three-Phase) 模块中的 12 个开关器件。该模块将 12 个门极信号多路复用为单个向量。门极信号按 *a* 相、*b* 相，然后是 *c* 相的顺序排列，每相四个门极信号。

当您将模块输入切换为电气端口时，该模块会显示 12 对电气连接，每对对应一个开关器件的门极和阴极。
