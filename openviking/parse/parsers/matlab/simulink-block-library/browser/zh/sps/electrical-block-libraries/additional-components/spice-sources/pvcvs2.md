---
type: simulink-block
title: 'PVCVS2'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Sources'
documentation_page: 'pvcvs2'
documentation_source_path: 'ref/pvcvs2.html'
language: zh-CN
chinese_source: worker-translation
---

# PVCVS2

## 端口

### 守恒

### **1+** — 第一个控制输入的正输入电压电气

与 PVCVS2 的第一个控制输入的正输入电压相关联的电气守恒端口。

### **1-** — 第一个控制输入的负输入电压电气

与 PVCVS2 的第一个控制输入的负输入电压相关联的电气守恒端口。

### **2+** — 第二个控制输入的正输入电压电气

与 PVCVS2 的第二个控制输入的正输入电压相关联的电气守恒端口。

### **2-** — 第二个控制输入的负输入电压电气

与 PVCVS2 的第二个控制输入的负输入电压相关联的电气守恒端口。

### **+** — 正输出电压电气

与 PVCVS2 的正输出电压相关联的电气守恒端口。

### **-** — 负输出电压电气

与 PVCVS2 的负输出电压相关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[ 0 1 1 ]`（默认）

将输入电压与输出电压关联的多项式系数，如上一节所述。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式压控电压源

PVCVS2（Two-Input Polynomial Voltage-Controlled Voltage Source）模块表示一个电压源，其输出电压值是各对控制输入端口两端电压的多项式函数。此方程将源两端的电压描述为时间的函数：

Vout=p1+p2\*Vin1+p3\*Vin2+p4\*Vin12+p5Vin1\*Vin2+p6\*Vin22+…

其中：

- *Vin1* 是第一对输入端口两端的电压。
- *Vin2* 是第二对输入端口两端的电压。
- *p* 是 **Polynomial coefficients** 参数值。
