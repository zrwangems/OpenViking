---
type: simulink-block
title: 'Cycler'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cyclers'
documentation_page: 'cycler'
documentation_source_path: 'ref/cycler.html'
language: zh-CN
chinese_source: worker-translation
---

# Cycler

## 端口
```yaml
ports:
- name: i
  summary: 电流，A 物理信号
  direction: input
- name: v
  summary: 电压，V 物理信号
  direction: input
- name: c
  summary: 控制，无量纲物理信号
  direction: input
- name: +
  summary: 正极端子 电气
  direction: input
- name: '-'
  summary: 负极端子 电气
  direction: input
```

### 输入

### **i** — 电流，A 物理信号

与通过 cycler 的电流相关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为 `Galvanostat, specify current` 或 `Cycler, specify current or voltage`。

### **v** — 电压，V 物理信号

与 cycler 两端电压相关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为 `Potentiostat, specify voltage` 或 `Cycler, specify current or voltage`。

### **c** — 控制，无量纲物理信号

控制 cycler 行为的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Configuration** 参数设置为 `Cycler, specify current or voltage`。

### 守恒

### **+** — 正极端子 电气

与 cycler 正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与 cycler 负极端子相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Current sign convention
  summary: 电流的符号约定选项 Positive for device discharge (IEC 62660)（默认）| Positive for device charge
  group: ''
- name: Configuration
  summary: 模块配置 Cycler, specify current or voltage（默认）| Galvanostat, specify current | Potentiostat, specify voltage
  group: ''
```

### **Current sign convention** — 电流的符号约定选项 `Positive for device discharge (IEC 62660)`（默认）| `Positive for device charge`

电流符号的约定选项。

### **Configuration** — 模块配置 `Cycler, specify current or voltage`（默认）| `Galvanostat, specify current` | `Potentiostat, specify voltage`

用于配置模块行为的选项。
## 所属库

Simscape / Battery / Cyclers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

理想恒流仪、恒压仪或 cycler

Cycler 模块实现理想的恒流仪、恒压仪或 cycler。

要将此模块配置为恒流仪，请将 **Configuration** 参数设置为 `Galvanostat, specify current`。此时 Cycler 模块表示一个理想的电流源或电流吸收器，其能力足以维持通过它的指定电流，而不受其两端电压的影响。输出电流为物理信号端口 **i** 处的值。

要将此模块配置为恒压仪，请将 **Configuration** 参数设置为 `Potentiostat, specify voltage`。此时 Cycler 模块表示一个理想的电压源，其能力足以维持其输出端的指定电压，而不受通过它的电流的影响。输出电压为物理信号端口 **v** 处的值。

要将此模块配置为 cycler，请将 **Configuration** 参数设置为 `Cycler, specify current or voltage`。当控制物理信号端口 **c** 处的值等于 `0` 时，cycler 关闭。当控制物理信号端口 **c** 处的值等于 `1` 时，此模块表示恒流仪。当控制物理信号端口 **c** 处的值等于 `2` 时，此模块表示恒压仪。

此表显示了 Cycler 模块的整体行为：

| Configuration | | | | |
| --- | --- | --- | --- | --- |
| `Galvanostat, specify current` | `Potentiostat, specify voltage` | `Cycler, specify current or voltage` | | |
| 输入端口 **c** 处的值 | | |
| 0 | 1 | 2 |
| Cycler 模块表示理想电流源。 | Cycler 模块表示理想电压源。 | Cycler 模块关闭。 | Cycler 模块表示恒流仪。 | Cycler 模块表示恒压仪。 |
