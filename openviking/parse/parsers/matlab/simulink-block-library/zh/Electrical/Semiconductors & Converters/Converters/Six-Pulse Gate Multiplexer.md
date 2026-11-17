---
type: simulink-block
title: 'Six-Pulse Gate Multiplexer'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'sixpulsegatemultiplexer'
documentation_source_path: 'ref/sixpulsegatemultiplexer.html'
language: zh-CN
chinese_source: worker-translation
---

# Six-Pulse Gate Multiplexer

## 端口

### 输入

### **Ga(H),Gb(H),Gc(H)** — Ga(H),Gb(H),Gc(H) 物理信号

与 Converter (Three-Phase) 模块的高侧开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

### **Ga(L),Gb(L),Gc(L)** — Ga(L),Gb(L),Gc(L) 物理信号

与 Converter (Three-Phase) 模块的低侧开关器件的栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

### 守恒

### **Ga(H),Gb(H),Gc(H)** — Ga(H),Gb(H),Gc(H) 电气

与 Converter (Three-Phase) 模块的高侧开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **Ga(L),Gb(L),Gc(L)** — Ga(L),Gb(L),Gc(L) 电气

与 Converter (Three-Phase) 模块的低侧开关器件的栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **G** — G 电气

与多路复用栅极信号关联的向量输出端口。将此端口连接到 Converter (Three-Phase) 模块的 `G` 端口。

### **a** — *A* 相交流参考点 电气

与 Converter (Three-Phase) 模块的高侧开关器件的 *A* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **b** — *B* 相交流参考点 电气

与 Converter (Three-Phase) 模块的高侧开关器件的 *B* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **c** — *C* 相交流参考点 电气

与 Converter (Three-Phase) 模块的高侧开关器件的 *C* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

### **L** — L 电气

与 Converter (Three-Phase) 模块中每个低侧开关器件共用的负直流电压关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

## 参数

### **Gate-control port** — 栅极控制端口 `PS` (默认) | `Electrical`

是否公开 PS 或电气控制端口。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2021b: 物理和电气连接端口更新

从 R2021b 开始，要在物理端口和电气端口之间切换，请将 **Gate-control port** 参数设置为 `PS` 或 `Electrical`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **Gate-control port** 参数。

## 描述

将栅极输入信号多路复用到 Converter 模块

Six-Pulse Gate Multiplexer 模块将栅极电压信号路由到 Converter (Three-Phase) 模块中的六个开关器件。该模块将六个单独的栅极信号多路复用为单个向量。

当您将模块输入切换为电气端口时，该模块会显示附加电气参考输入端口。附加电气参考端口与连接至 Converter (Three-Phase) 模块中高侧开关器件的各相电压，以及 Converter (Three-Phase) 模块中每个低侧开关器件共用的负直流电压相关联。
