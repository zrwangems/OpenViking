---
type: simulink-block
title: 'Cycler'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / C\u200byclers'
documentation_page: 'cycler'
documentation_source_path: 'ref/cycler.html'
language: zh-CN
chinese_source: worker-translation
---

# Cycler

## 端口

### 输入

### **i** — 电流，A 物理信号

与流过 Cycler 的电流关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将**配置**参数设置为 `Galvanostat, specify current` 或 `Cycler, specify current or voltage`。

### **v** — 电压，V 物理信号

与 Cycler 两端电压关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将**配置**参数设置为 `Potentiostat, specify voltage` 或 `Cycler, specify current or voltage`。

### **c** — 控制，无量纲物理信号

控制 Cycler 行为的物理信号输入端口。

#### 依赖关系

要启用此端口，请将**配置**参数设置为 `Cycler, specify current or voltage`。

### 守恒

### **+** — 正极端子电气

与 Cycler 正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与 Cycler 负极端子关联的电气守恒端口。

## 参数

### **电流符号约定** — 电流的符号约定选项 `Positive for device discharge (IEC 62660)`（默认） | `Positive for device charge`

电流符号的约定选项。

### **配置** — 模块配置 `Cycler, specify current or voltage`（默认） | `Galvanostat, specify current` | `Potentiostat, specify voltage`

用于配置模块行为的选项。

## 所属库

Simscape / Battery / Cyclers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

理想恒电流仪、恒电位仪或循环仪

Cycler 模块实现理想恒电流仪、恒电位仪或循环仪。

要将此模块配置为恒电流仪，请将**配置**参数设置为 `Galvanostat, specify current`。然后，Cycler 模块表示理想电流源或电流汇，其强度足以维持流过它的指定电流，而无论其两端电压如何。输出电流是物理信号端口 **i** 处的值。

要将此模块配置为恒电位仪，请将**配置**参数设置为 `Potentiostat, specify voltage`。然后，Cycler 模块表示理想电压源，其强度足以维持其输出端的指定电压，而无论流过它的电流如何。输出电压是物理信号端口 **v** 处的值。

要将此模块配置为循环仪，请将**配置**参数设置为 `Cycler, specify current or voltage`。当控制物理信号端口 **c** 处的值等于 `0` 时，循环仪关闭。当控制物理信号端口 **c** 处的值等于 `1` 时，此模块表示恒电流仪。当控制物理信号端口 **c** 处的值等于 `2` 时，此模块表示恒电位仪。

下表显示了 Cycler 模块的整体行为：

| 配置 | | | | |
| --- | --- | --- | --- | --- |
| `Galvanostat, specify current` | `Potentiostat, specify voltage` | `Cycler, specify current or voltage` | | |
| 输入端口 **c** 处的值 | | |
| 0 | 1 | 2 |
| Cycler 模块表示理想电流源。 | Cycler 模块表示理想电压源。 | Cycler 模块关闭。 | Cycler 模块表示恒电流仪。 | Cycler 模块表示恒电位仪。 |
