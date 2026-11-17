---
type: simulink-block
title: 'PVCVS'
family: 'sps'
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
```yaml
ports:
- name: p1
  summary: 控制输入电气的正电压
  direction: conserving
- name: n1
  summary: 控制输入电气的负电压
  direction: conserving
- name: p2
  summary: 正输出电压电气
  direction: conserving
- name: n2
  summary: 负输出电压电气
  direction: conserving
```

### 守恒端口

### **p1** — 控制输入电气的正电压

与控制输入的正电压 PVCVS 相关联的电气守恒端口。

### **n1** — 控制输入电气的负电压

与控制输入的负电压 PVCVS 相关联的电气守恒端口。

### **p2** — 正输出电压电气

与 PVCVS 正输出电压相关联的电气守恒端口。

### **n2** — 负输出电压电气

与 PVCVS 负输出电压相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Polynomial coefficients
  summary: 多项式系数 [0, 1]（默认值）
  group: ''
```

### **Polynomial coefficients** — 多项式系数 `[0, 1]`（默认值）

将输入电压与输出电压关联起来的多项式系数，如上一节所述。
## 所属库

Simscape / Electrical / Additional Components / SPICE Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

多项式电压控制电压源

PVCVS（多项式电压控制电压源）模块表示一个电压源，其输出电压值是输入端口两端电压的多项式函数。以下方程描述了源两端电压随时间的变化：

- 如果为 **Polynomial coefficients** 参数指定一个 *n* 元素的多项式系数向量：

  Vout=p(0)+p(1)\*Vin+...+p(n−1)\*Vinn−1+p(n)\*Vinn
- 如果为 **Polynomial coefficients** 参数指定一个标量系数：

  Vout=p\*Vin

其中：

- *Vin* 是输入端口两端的电压。
- *p* 是 **Polynomial coefficients** 参数值。
