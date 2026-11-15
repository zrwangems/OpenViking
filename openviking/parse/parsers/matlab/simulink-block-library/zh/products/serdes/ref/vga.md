---
type: simulink-block
title: 'VGA'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'vga'
documentation_source_path: 'ref/vga.html'
language: zh-CN
chinese_source: worker-translation
---

# VGA

## 端口

### 输入

### **WaveIn** — 输入信号 标量 | 向量

要缩放的输入信号，指定为标量或向量。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出，以对应于输入信号的标量或向量返回。

**数据类型：** `double`

## 参数

### **Mode** — VGA 工作模式 `On`（默认）| `Off`

VGA 工作模式：

- `Off` — VGA 被旁路，输入波形
  保持不变。
- `On` — VGA 根据指定的 `Gain` 缩放输入波形。

#### 程序化使用

- 使用 `get_param(gcb,'Mode')` 查看当前 VGA
  **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 VGA 设置为特定的
  **Mode**。

### **Gain** — 用于缩放输入波形的乘法增益 `1`（默认）| 标量

用于缩放输入波形的乘法增益，指定为无量纲标量。

#### 程序化使用

- 使用 `get_param(gcb,'Gain')` 查看
  **Gain** 的当前值。
- 使用 `set_param(gcb,'Gain',value)` 将 VGA
  **Gain** 设置为特定值。

**数据类型：** `double`

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择此项可将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，则会将其从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Gain** — 在 IBIS-AMI 模型中包含 Gain 参数 on（默认）| off

选择此项可将 **Gain** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Gain**，则会将其从 AMI 文件中移除，实际上将 **Gain** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对可变增益放大器进行建模

VGA 模块根据用户指定的增益缩放输入波形的幅度。
