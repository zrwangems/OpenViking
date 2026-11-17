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
```yaml
ports:
- name: 1+
  summary: 第一个控制输入电气正电压
  direction: conserving
- name: 1-
  summary: 第一个控制输入电气负电压
  direction: conserving
- name: 2+
  summary: 第二个控制输入电气正电压
  direction: conserving
- name: 2-
  summary: 第二个控制输入电气负电压
  direction: conserving
- name: +
  summary: 输出正电压电气端口
  direction: conserving
- name: '-'
  summary: 输出负电压电气端口
  direction: conserving
```

### 守恒端口

### **1+** — 第一个控制输入电气正电压

与 PCCVS2 第一个控制输入正电压相关联的电气守恒端口。

### **1-** — 第一个控制输入电气负电压

与 PCCVS2 第一个控制输入负电压相关联的电气守恒端口。

### **2+** — 第二个控制输入电气正电压

与 PCCVS2 第二个控制输入正电压相关联的电气守恒端口。

### **2-** — 第二个控制输入电气负电压

与 PCCVS2 第二个控制输入负电压相关联的电气守恒端口。

### **+** — 输出正电压电气端口

与 PCCVS2 输出正电压相关联的电气守恒端口。

### **-** — 输出负电压电气端口

与 PCCVS2 输出负电压相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Polynomial coefficients
  summary: 多项式系数 [ 0 1 1 ]（默认值）
  group: ''
```

### **Polynomial coefficients** — 多项式系数 `[ 0 1 1 ]`（默认值）

将输入电流与输出电压关联起来的多项式系数，如前一节所述。
## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

具有两个控制输入的多项式电流控制电压源

PCCVS2（双输入多项式电流控制电压源）模块表示一个电压源，其输出电压值是流经各对控制输入端口电流的多项式函数。以下方程描述了源两端电压随时间的变化：

Vout=p1+p2\*Iin1+p3\*Iin2+p4\*Iin12+p5Iin1\*Iin2+p6\*Iin22+…

其中：

- *Iin1* 是流经第一对输入端口的电流。
- *Iin2* 是流经第二对输入端口的电流。
- *p* 是 **Polynomial coefficients** 参数值。
