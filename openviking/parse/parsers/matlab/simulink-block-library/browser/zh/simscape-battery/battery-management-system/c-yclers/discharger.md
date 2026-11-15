---
type: simulink-block
title: 'Discharger'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / C\u200byclers'
documentation_page: 'discharger'
documentation_source_path: 'ref/discharger.html'
language: zh-CN
chinese_source: worker-translation
---

# Discharger

## 端口

### 输入

### **t** — 触发，无单位物理信号

控制模块放电行为的物理信号输入端口。
### 守恒

### **+** — 正极端子（电气）

与放电器正端子关联的电气守恒端口。

### **-** — 负极端子（电气）

与放电器负端子关联的电气守恒端口。

## 参数

### **Constant discharging current** — 恒定放电电流 `5` `A`（默认）| 正标量

模块对电池进行放电时的恒定放电电流值。

### **Voltage threshold** — 恒定放电电流的电压阈值 `10` `V`（默认）| 正标量

模块停止对电池执行恒流放电的阈值。

## 所属库

Simscape / Battery / Cyclers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

理想电池放电器

此模块实现一个理想放电器。当输入端口 **t** 处的信号从低于 `0.5` 的值变为等于或大于 `0.5` 的值时，模块以 **Constant discharging current** 参数的值执行恒流放电，直到电压小于或等于 **Voltage threshold** 参数的值。

此图显示当 **t** 输入越过 `0.5` 时 Discharger 模块的行为：
