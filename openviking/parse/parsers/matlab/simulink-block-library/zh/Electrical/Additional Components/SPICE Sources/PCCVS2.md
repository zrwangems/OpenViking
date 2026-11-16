---
type: simulink-block
title: 'PCCVS2'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pccvs2'
documentation_source_path: 'ref/pccvs2.html'
language: zh-CN
chinese_source: worker-translation
---

# PCCVS2

## 端口

### 守恒

### **1+** — 第一个控制输入的正电压（电气）

与 PCCVS2 的第一个控制输入的正电压关联的电气守恒端口。

### **1-** — 第一个控制输入的负电压（电气）

与 PCCVS2 的第一个控制输入的负电压关联的电气守恒端口。

### **2+** — 第二个控制输入的正电压（电气）

与 PCCVS2 的第二个控制输入的正电压关联的电气守恒端口。

### **2-** — 第二个控制输入的负电压（电气）

与 PCCVS2 的第二个控制输入的负电压关联的电气守恒端口。

### **+** — 正输出电压（电气）

与 PCCVS2 的正输出电压关联的电气守恒端口。

### **-** — 负输出电压（电气）

与 PCCVS2 的负输出电压关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[ 0 1 1 ]`（默认）

将输入电流与输出电压关联的多项式系数，如前文所述。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式电流控制电压源

PCCVS2（Two-Input Polynomial Current-Controlled Voltage Source）模块表示一个电压源，其输出电压值是流经各对控制输入端口的电流的多项式函数。以下方程描述了该电压源两端电压随时间的变化：

Vout=p1+p2\*Iin1+p3\*Iin2+p4\*Iin12+p5Iin1\*Iin2+p6\*Iin22+…

其中：

- *Iin1* 是流经第一对输入端口的电流。
- *Iin2* 是流经第二对输入端口的电流。
- *p* 是 **Polynomial coefficients** 参数值。
