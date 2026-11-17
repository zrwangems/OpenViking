---
type: simulink-block
title: 'Passivity Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Constraint Control'
documentation_page: 'passivityenforcement'
documentation_source_path: 'ug/passivityenforcement.html'
language: zh-CN
chinese_source: worker-translation
---

# Passivity Enforcement

## 端口

### 输入

### **u0** — 控制动作 标量 | 向量

未修改的控制动作，指定为标量或向量。

如果 **Number of actions** 参数为 `1`，则将 **u0** 连接到标量信号。否则，将 **u0** 连接到长度等于 **Number of actions** 的向量信号。

### **fp** — 无源性输入函数偏移系数 标量 | 向量

以下约束方程中的偏移系数 *fp*。

up=fp(x)+gp(x)u

将 **fp** 连接到 *Nu*×1 信号，其中 *Nu* 等于 **Number of actions** 参数。

### **gp** — 无源性输入函数线性系数 标量 | 矩阵

以下约束方程中的线性系数 *gp*。

up=fp(x)+gp(x)u

将 **gp** 连接到 *Nu*×*Nu* 信号，其中 *Nu* 等于 **Number of actions** 参数。

### **yp** — 无源性输出函数 标量 | 向量

无源性输出函数，定义为被控对象状态的以下函数。

yp=hp(x)

将 **yp** 连接到 *Nu*×1 信号，其中 *Nu* 等于 **Number of actions** 参数。

### **umax** — 动作信号上界 标量 | 向量

要指定动作信号的运行时上界，请启用此输入端口。如果此端口被禁用，模块不会对控制动作施加任何上界。

如果 **Number of actions** 参数为 `1`，则将 **umax** 连接到标量信号。否则，将 **umax** 连接到长度等于 **Number of actions** 的向量信号。

#### 依赖关系

要启用此输入端口，请选择 **Use external source for upper bound** 参数。

### **umin** — 动作信号下界 标量 | 向量

要指定动作信号的运行时下界，请启用此输入端口。如果此端口被禁用，模块不会对控制动作施加任何下界。

如果 **Number of actions** 参数为 `1`，则将 **umin** 连接到标量信号。否则，将 **umin** 连接到长度等于 **Number of actions** 的向量信号。

#### 依赖关系

要启用此输入端口，请选择 **Use external source for lower bound** 参数。
### 输出

### **u\*** — 修改后的控制动作 标量 | 向量

QP 求解器返回的修改后的控制动作。

如果求解器在达到最大迭代次数之前找到解，**u\*** 输出此最优解。

如果求解器达到最大迭代次数，优化停止，**u\*** 输出次优解。

如果初始优化问题不可行，返回的控制动作取决于模块是否配置为忽略约束或动作边界。有关详细信息，请参阅 **exitflag** 参数。

如果 **Number of actions** 参数为 `1`，**u\*** 输出标量信号。否则，**u\*** 输出长度等于 **Number of actions** 的向量信号。

### **exitflag** — 优化状态 `1` | `0` | 负整数

QP 求解器的优化状态。下表显示了可能的状态值。

| Exit Flag | Description |
| --- | --- |
| `1` | 求解器收敛到最优解，所有约束和边界均有效。在这种情况下，**u\*** 输出最优控制动作。 |
| `0` | 求解器达到最大迭代次数。**u\*** 中输出的控制动作可能是次优的。 |
| 负整数 | 初始优化问题不可行。 |

#### 依赖关系

要启用此输出端口，请选择 **Optimization status** 参数。

## 参数

#### 参数选项卡

### **Number of actions** — 控制动作数量 `1`（默认） | 正整数

指定要施加边界并优化的动作数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`nu` |
| **类型**：character vector |
| **默认值**：`'1'` |

### **Passivity index** — 无源性指标 `0.1`（默认）| 非负标量 | 非负向量

指定要强制满足的无源性指标。将 **Passivity index** 指定为非负标量，或指定为维度等于 *Nu*×1 的非负值向量，其中 *Nu* 等于 **Number of actions** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`rho` |
| **类型**：character vector |
| **默认值**：`'0.1'` |

### **Use external source for upper bound** — 添加上动作边界输入端口 `off`（默认）| `on`

选择此参数以添加 **umax** 输入端口，用于外部上动作边界。

#### 编程使用

|  |
| --- |
| **模块参数**：`external_umax` |
| **类型**：character vector |
| **值**：`'off'`|`'on'` |
| **默认值**：`'off'` |

### **Use external source for lower bound** — 添加下动作边界输入端口 off（默认）| on

选择此参数以添加 **umin** 输入端口，用于外部下动作边界。

#### 编程使用

|  |
| --- |
| **模块参数**：`external_umin` |
| **类型**：character vector |
| **值**：`'off'`|`'on'` |
| **默认值**：`'off'` |

#### Block Tab

### **Sample time** — 优化采样时间 `0.1`（默认）| 正标量

指定运行优化的采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`Ts` |
| **类型**：character vector |
| **默认值**：`'0.1'` |

### **Maximum iterations** — 最大优化迭代次数 `200`（默认）| 正整数

指定最大优化迭代次数。

#### 编程使用

|  |
| --- |
| **模块参数**：`maxiter` |
| **类型**：character vector |
| **默认值**：`'200'` |

### **Constraint tolerance** — 约束违反容差 `1e-6`（默认）| 非负标量

指定约束违反的容差值。

#### 编程使用

|  |
| --- |
| **模块参数**：`tol` |
| **类型**：character vector |
| **默认值**：`'1e-6'` |

### **Optimization status** — 添加退出标志输出端口 `off`（默认）| `on`

选择此参数以添加 **exitflag** 输出端口，用于 QP 求解器的优化状态。

#### 编程使用

|  |
| --- |
| **模块参数**：`exitflag` |
| **类型**：character vector |
| **值**：`'off'`|`'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink Control Design / Constraint Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Passivity Enforcement 模块仅支持双精度信号的代码生成。

## 版本历史

**在 R2023a 中引入**

### R2023b：库位置已更改

Passivity Enforcement 模块现在位于 **Simulink Control Design/Constraint Control** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Passivity Enforcement 模块的库链接会自动更新。

## 描述

修改控制动作以满足无源性约束和动作边界

Passivity Enforcement 模块计算在满足无源性约束和动作边界的情况下，最接近指定控制动作的修改后控制动作。

该模块使用二次规划（QP）求解器实时寻找使函数 |u−u0|2 最小化的控制动作 *u*。这里，*u*0 是来自控制器的未修改控制动作。

求解器对优化问题应用以下约束。

ρypTyp+ypTfp+ypTgpu≤0umin≤u≤umax

这里：

- *ρ* 是无源性指标。
- *y**p* 是无源性输出函数，定义为 yp=hp(x)。
- *f**p* 和 *g**p* 是由无源性输入函数 up=fp(x)+gp(x)u 定义的函数。
- *u*min 是控制动作的下界。
- *u*max 是控制动作的上界。

有关无源性强制实施的更多信息，请参阅 Passivity Enforcement for Control Design。
