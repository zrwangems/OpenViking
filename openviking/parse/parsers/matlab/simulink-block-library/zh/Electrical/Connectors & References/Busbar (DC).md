---
type: simulink-block
title: 'Busbar (DC)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'busbardc'
documentation_source_path: 'ref/busbardc.html'
language: zh-CN
chinese_source: worker-translation
---

# Busbar (DC)

## 端口
```yaml
ports:
- name: Vt
  summary: 电压，V 物理信号
  direction: output
- name: P
  summary: 功率，W 物理信号
  direction: output
- name: 1+
  summary: 正极连接 1 电气
  direction: output
- name: 2+
  summary: 正极连接 2 电气
  direction: output
- name: 3+
  summary: 正极连接 3 电气
  direction: output
- name: 4+
  summary: 正极连接 4 电气
  direction: output
- name: 1-
  summary: 负极连接 1 电气
  direction: output
- name: 2-
  summary: 负极连接 2 电气
  direction: output
- name: 3-
  summary: 负极连接 3 电气
  direction: output
- name: 4-
  summary: 负极连接 4 电气
  direction: output
```

### 输出

### **Vt** — 电压，V 物理信号

与标幺电压测量相关联的物理信号端口，单位为伏特。

#### 依赖关系

要启用此端口，请在**参数**设置中将**测量端口**参数设置为 `Yes`。

### **P** — 功率，W 物理信号

与功率测量相关联的物理信号端口，单位为瓦特。

#### 依赖关系

要启用此端口，请在**参数**设置中将**测量端口**参数设置为 `Yes`，并将**连接数**参数设置为 `2`、`3` 或 `4`。

### 守恒

### **1+** — 正极连接 1 电气

与第一个正极连接相关联的电气守恒端口。

### **2+** — 正极连接 2 电气

与第二个正极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `2`、`3` 或 `4`。

### **3+** — 正极连接 3 电气

与第三个正极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `3` 或 `4`。

### **4+** — 正极连接 4 电气

与第四个正极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `4`。

### **1-** — 负极连接 1 电气

与第一个负极连接相关联的电气守恒端口。

### **2-** — 负极连接 2 电气

与第二个负极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `2`、`3` 或 `4`。

### **3-** — 负极连接 3 电气

与第三个负极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `3` 或 `4`。

### **4-** — 负极连接 4 电气

与第四个负极连接相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请在**参数**设置中将**连接数**参数设置为 `4`。
## 参数
```yaml
parameters:
- name: 连接数
  summary: 端口连接数 2（默认）| 1 | 3 | 4
  group: ''
- name: 额定直流电压
  summary: 母线额定直流电压 1e3 V（默认）| 正标量
  group: ''
- name: 测量类型
  summary: 测量类型 Instantaneous（默认）| Average over a specified period
  group: ''
- name: 平均周期
  summary: 测量平均周期 1e-2 s（默认）| 正标量
  group: ''
- name: 测量端口
  summary: 测量端口暴露 No（默认）| Yes
  group: ''
```

### **连接数** — 端口连接数 `2`（默认）| `1` | `3` | `4`

模块上要暴露的端口连接数。

### **额定直流电压** — 母线额定直流电压 `1e3` `V`（默认）| 正标量

母线的额定直流电压。此模块使用该值来缩放标幺电压值。

### **测量类型** — 测量类型 `Instantaneous`（默认）| `Average over a specified period`

测量类型。在时间仿真模式下，您可以将此参数设置为 `Instantaneous` 或 `Average over a specified period`。在频率-时间仿真模式下，您必须将此参数设置为 `Instantaneous`。

### **平均周期** — 测量平均周期 `1e-2` `s`（默认）| 正标量

电压和功率值进行平均的时间周期。

#### 依赖关系

要启用此参数，请将**测量类型**设置为 `Average over a specified period`。

### **测量端口** — 测量端口暴露 `No`（默认）| `Yes`

是否暴露 **Vt** 和 **P** 物理信号输出测量端口。
## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

用于潮流分析的直流母线连接器

Busbar (DC) 模块是用于潮流分析的直流连接器。您可以将此模块与配置为在时域或频率-时间仿真模式下运行的 Simscape™ Electrical™ 直流网络一起使用。您可以通过启用仿真数据记录或暴露模块上的可选测量端口来查看电压和功率值。有关数据记录的更多信息，请参阅关于 Simscape 数据记录。
