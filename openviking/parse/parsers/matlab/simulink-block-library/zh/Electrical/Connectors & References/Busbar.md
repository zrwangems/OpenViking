---
type: simulink-block
title: 'Busbar'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'busbar'
documentation_source_path: 'ref/busbar.html'
language: zh-CN
chinese_source: worker-translation
---

# Busbar

## 端口
```yaml
ports:
- name: Vt
  summary: 电压物理信号
  direction: output
- name: ph
  summary: 相位物理信号
  direction: output
- name: P
  summary: 有功功率物理信号
  direction: output
- name: Q
  summary: 无功功率物理信号
  direction: output
- name: ~1
  summary: 三相连接 1 电气
  direction: output
- name: ~2
  summary: 三相连接 2 电气
  direction: output
- name: ~3
  summary: 三相连接 3 电气
  direction: output
- name: ~4
  summary: 三相连接 4 电气
  direction: output
```

### 输出

### **Vt** — 电压物理信号

与电压测量相关联的物理信号端口。该值以标幺值报告，即相间均方根电压除以**Rated busbar voltage (phase-to-phase RMS)**。

#### 依赖关系

仅当在**参数**设置中将 **Measurement ports** 参数设置为 `Yes` 时，此端口才可见。

### **ph** — 相位物理信号

与电压相位测量相关联的物理信号端口。

#### 依赖关系

仅当在**参数**设置中将 **Measurement ports** 参数设置为 `Yes` 时，此端口才可见。

### **P** — 有功功率物理信号

与有功（实际）功率测量相关联的物理信号端口。

#### 依赖关系

仅当在**参数**设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4`，且将 **Measurement ports** 参数设置为 `Yes` 时，此端口才可见。

### **Q** — 无功功率物理信号

与无功（虚）功率测量相关联的物理信号端口。

#### 依赖关系

仅当在**参数**设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4`，且将 **Measurement ports** 参数设置为 `Yes` 时，此端口才可见。
### 守恒

### **~1** — 三相连接 1 电气

与第一个三相连接相关联的复合三相电气守恒端口。

### **~2** — 三相连接 2 电气

与第二个三相连接相关联的复合三相电气守恒端口。

#### 依赖关系

仅当在**参数**设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4` 时，此端口才可见。

### **~3** — 三相连接 3 电气

与第三个三相连接相关联的复合三相电气守恒端口。

#### 依赖关系

仅当在**参数**设置中将 **Number of connections** 参数设置为 `3` 或 `4` 时，此端口才可见。

### **~4** — 三相连接 4 电气

与第四个三相连接相关联的复合三相电气守恒端口。

#### 依赖关系

仅当在**参数**设置中将 **Number of connections** 参数设置为 `4` 时，此端口才可见。
## 参数
```yaml
parameters:
- name: Number of connections
  summary: 端口连接数 2（默认）| 1 | 3 | 4
  group: ''
- name: Rated busbar voltage (phase-to-phase RMS)
  summary: 母线额定电压 sqrt(3) * 100 / sqrt(2) V（默认）
  group: ''
- name: Network frequency
  summary: 网络频率 60 Hz（默认）
  group: ''
- name: Measurement ports
  summary: 测量端口暴露 No（默认）| Yes
  group: ''
```

### **Number of connections** — 端口连接数 `2`（默认）| `1` | `3` | `4`

模块上暴露的端口连接数。

模块上暴露的端口数量与此参数相关。

### **Rated busbar voltage (phase-to-phase RMS)** — 母线额定电压 `sqrt(3) * 100 / sqrt(2)` `V`（默认）

母线的额定相间均方根电压。

### **Network frequency** — 网络频率 `60` `Hz`（默认）

所连接网络的频率。

### **Measurement ports** — 测量端口暴露 `No`（默认）| `Yes`

电压、相位、有功功率和无功功率物理信号输出测量端口的可见性。

#### 依赖关系

端口 **Vt** 和 **ph** 仅当此参数设置为 `Yes` 时才可见。

端口 **P** 和 **Q** 仅当此参数设置为 `Yes`，且在**参数**设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4` 时才可见。
## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

潮流分析母线连接器

Busbar 模块是用于潮流分析的连接器。将此模块与兼容频率-时间仿真模式的三相 Simscape™ Electrical™ 网络一起使用。仿真完成后，该模块会添加一个注释，显示仿真开始时其每个三相电气守恒端口处的电压、相位、有功功率和无功功率。要添加注释，必须启用 Simscape 日志记录。

该模块将在基于时间的仿真模式下进行仿真，但是除非网络兼容频率-时间仿真模式，并且在 Solver Configuration 模块上选中 `Start simulation from steady state`，否则它不会添加带有初始潮流结果的注释。但是，当使用基于时间的仿真模式时，该模块会计算电压、相位、有功功率和无功功率的近似值。您可以从 Simscape 日志记录中查看这些值，也可以通过暴露模块上的可选测量端口来查看这些值。近似程度取决于系统的平衡程度以及存在的谐波水平。
