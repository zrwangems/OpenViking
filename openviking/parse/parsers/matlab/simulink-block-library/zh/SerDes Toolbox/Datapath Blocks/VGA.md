---
type: simulink-block
title: 'VGA'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'vga'
documentation_source_path: 'ref/vga.html'
language: zh-CN
chinese_source: worker-translation
---

# VGA

## 端口
```yaml
ports:
- name: WaveIn
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 估计的信道输出 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入信号 标量 | 向量

要缩放的输入信号，指定为标量或向量。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出，以与输入信号对应的标量或向量形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Mode
  summary: VGA 工作模式 On（默认）| Off
  group: ''
- name: Gain
  summary: 用于缩放输入波形的乘法增益 1（默认）| 标量
  group: ''
- name: Mode
  summary: 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off
  group: ''
- name: Gain
  summary: 在 IBIS-AMI 模型中包含 Gain 参数 on（默认）| off
  group: ''
```

### **Mode** — VGA 工作模式 `On`（默认）| `Off`

VGA 工作模式：

- `Off` — VGA 被旁路，输入波形保持不变。
- `On` — VGA 根据指定的 `Gain` 对输入波形进行缩放。

#### 程序化使用

- 使用 `get_param(gcb,'Mode')` 查看当前 VGA 的 **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 VGA 设置为特定的 **Mode**。

### **Gain** — 用于缩放输入波形的乘法增益 `1`（默认）| 标量

用于缩放输入波形的乘法增益，指定为无量纲标量。

#### 程序化使用

- 使用 `get_param(gcb,'Gain')` 查看 **Gain** 的当前值。
- 使用 `set_param(gcb,'Gain',value)` 将 VGA 的 **Gain** 设置为特定值。

**数据类型：** `double`

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择此项以将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，它将从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Gain** — 在 IBIS-AMI 模型中包含 Gain 参数 on（默认）| off

选择此项以将 **Gain** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Gain**，它将从 AMI 文件中移除，实际上将 **Gain** 硬编码为其当前值。
## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

对可变增益放大器进行建模

VGA 模块根据用户指定的增益对输入波形的幅度进行缩放。
