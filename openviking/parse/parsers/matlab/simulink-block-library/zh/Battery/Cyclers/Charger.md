---
type: simulink-block
title: 'Charger'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Cyclers'
documentation_page: 'charger'
documentation_source_path: 'ref/charger.html'
language: zh-CN
chinese_source: worker-translation
---

# Charger

## 端口

### 输入

### **t** — 触发，无单位物理信号

控制模块充电行为的物理信号输入端口。
### 守恒

### **+** — 正极端子（电气）

与充电器正极端子关联的电气守恒端口。

### **-** — 负极端子（电气）

与充电器负极端子关联的电气守恒端口。

## 参数

### **Constant charging current** — 恒定充电电流 `5` `A`（默认）| 正标量

模块为电池充电时所使用的恒定充电电流值。

### **Voltage threshold** — 恒流充电的电压阈值 `12` `V`（默认）| 正标量

模块停止对电池执行恒流充电的阈值。

### **Constant charging voltage** — 恒定充电电压 `12` `V`（默认）| 正标量

模块为电池充电时所使用的恒定充电电压值。

### **Current threshold** — 恒压充电的电流阈值 `0.5` `A`（默认）| 正标量

模块停止对电池执行恒压充电的阈值。

## 所属库

Simscape / Battery / Cyclers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

理想电池充电器

Charger 模块实现一个理想电池充电器。
当输入端口 **t** 处的信号从低于 `0.5` 的值变为等于或大于 `0.5` 的值时，此模块以 **Constant charging current** 参数的值执行恒流充电。当电压大于或等于 **Voltage threshold** 参数的值时，此模块以 **Constant charging voltage** 参数的值执行恒压充电，直到电流小于或等于 **Current threshold** 参数的值。

下图显示当 **t** 输入越过 `0.5` 时 Charger 模块的行为：
