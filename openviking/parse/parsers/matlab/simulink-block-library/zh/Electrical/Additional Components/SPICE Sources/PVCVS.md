---
type: simulink-block
title: 'PVCVS'
family: 'additional-components'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'pvcvs'
documentation_source_path: 'ref/pvcvs.html'
language: zh-CN
chinese_source: worker-translation
---

# PVCVS

## 端口

### 守恒

### **p1** — 控制输入电气的正电压

与 PVCVS 控制输入正电压关联的电气守恒端口。

### **n1** — 控制输入电气的负电压

与 PVCVS 控制输入负电压关联的电气守恒端口。

### **p2** — 正输出电压电气

与 PVCVS 正输出电压关联的电气守恒端口。

### **n2** — 负输出电压电气

与 PVCVS 负输出电压关联的电气守恒端口。

## 参数

### **多项式系数** — 多项式系数 `[0, 1]`（默认）

将输入电压与输出电压关联起来的多项式系数，如前面部分所述。

## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

多项式压控电压源

PVCVS (Polynomial Voltage-Controlled Voltage Source) 模块表示一个电压源，其输出电压值是输入端口两端电压的多项式函数。以下方程将源两端的电压描述为时间的函数：

- 如果为 **多项式系数** 参数指定一个 *n* 元素的多项式系数向量：

  Vout=p(0)+p(1)\*Vin+...+p(n−1)\*Vin^(n−1)+p(n)\*Vin^n
- 如果为 **多项式系数** 参数指定标量系数：

  Vout=p\*Vin

其中：

- *Vin* 是输入端口两端的电压。
- *p* 是 **多项式系数** 参数值。
