---
type: simulink-block
title: 'Neutral Port (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'neutralportthreephase'
documentation_source_path: 'ref/neutralportthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Neutral Port (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口电气
  direction: conserving
- name: n
  summary: 中性点电气
  direction: conserving
```

### 守恒端口

### **~** — 三相端口电气

可扩展复合（**a**、**b**、
**c**）三相
端口。

### **n** — 中性点电气

与中性点相关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否对复合或展开的三相端口进行建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Parasitic ground conductance
  summary: 寄生对地电导 1e-12 1/Ohm（默认）
  group: ''
```

### **Modeling option** — 是否对复合或展开的三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或展开的三相端口进行建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

展开三相端口使用三个独立的电气守恒端口表示三相系统的各个相。

### **Parasitic ground conductance** — 寄生对地电导 `1e-12` `1/Ohm`（默认）

寄生对地电导。对于某些电路拓扑的仿真，需要非零值。
## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

将三相系统的各相连接到电气守恒端口

Neutral Port (Three-Phase) 模块将三相系统的各相连接到一个电气守恒端口。

**注意**

如果您不需要将中性端口连接到其他模块，请改用 Floating Neutral (Three-Phase) 模块。如果您想将中性端口接地，请使用 Grounded Neutral (Three-Phase) 模块。
