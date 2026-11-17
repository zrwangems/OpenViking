---
type: simulink-block
title: 'PCCVS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pccvs'
documentation_source_path: 'ref/pccvs.html'
language: zh-CN
chinese_source: worker-translation
---

# PCCVS

## 端口

### 守恒端口

### **p1** — 控制输入电气的正电压

与控制输入的正电压 PCCVS 相关联的电气守恒端口。

### **n1** — 控制输入电气的负电压

与控制输入的负电压 PCCVS 相关联的电气守恒端口。

### **p2** — 正输出电压电气

与 PCCVS 正输出电压相关联的电气守恒端口。

### **n2** — 负输出电压电气

与 PCCVS 负输出电压相关联的电气守恒端口。

## 参数

### **Polynomial coefficients** — 多项式系数 `[0, 1]`（默认）

将输入电流与输出电压关联起来的多项式系数，如上一节所述。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

多项式电流控制电压源

PCCVS（多项式电流控制电压源）模块表示一个电压源，其输出电压值是流过输入端口电流的多项式函数。以下方程描述了源两端电压随时间的变化：

- 如果为 **Polynomial coefficients** 参数指定一个 *n* 元素的多项式系数向量：

  Vout=p(0)+p(1)\*Iin+...+p(n−1)\*Iinn−1+p(n)\*Iinn
- 如果为 **Polynomial coefficients** 参数指定一个标量系数：

  Vout=p\*Iin

其中：

- *Iin* 是流过输入端口的电流。
- *p* 是 **Polynomial coefficients** 参数值。
