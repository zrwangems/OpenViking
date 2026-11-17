---
type: simulink-block
title: 'Open Circuit (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'opencircuitthreephase'
documentation_source_path: 'ref/opencircuitthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Circuit (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口电气
  direction: conserving
```

### 守恒端口

### **~** — 三相端口电气

可扩展的复合（**a**、**b**、
**c**）三相
端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是对复合三相端口还是扩展三相端口进行建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
```

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。
## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2019b：不再需要对未连接的端口进行封端

不再需要此模块。从 R2019b 开始，禁止 Simscape™ 模型中存在未连接的守恒端口这一限制已被取消。现在，如果您让某个守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。
但是，您仍然可以使用终结器模块来提高图的可读性。

没有移除终结器模块的计划。所有使用这些模块的现有模型的工作方式与之前版本相同。

## 描述

不汲取电流的三相终结器

Open Circuit (Three-Phase) 模块对在三相中的任何一相上都不汲取电流的三相连接进行建模。
