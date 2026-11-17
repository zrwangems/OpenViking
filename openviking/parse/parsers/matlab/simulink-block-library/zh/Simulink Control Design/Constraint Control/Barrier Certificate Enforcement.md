---
type: simulink-block
title: 'Barrier Certificate Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Constraint Control'
documentation_page: 'barriercertificateenforcement'
documentation_source_path: 'ug/barriercertificateenforcement.html'
language: zh-CN
chinese_source: worker-translation
---

# Barrier Certificate Enforcement

## 端口

### 输入

### **u0** — 控制动作 标量 | 向量

未修改的控制动作，指定为标量或向量。

如果 **Number of actions** 参数为 `1`，则将 **u0** 连接到标量信号。否则，将 **u0** 连接到长度等于 **Number of actions** 的向量信号。

### **fx** — 状态函数 标量 | 向量

以下被控对象动力学方程中的状态函数 *f*(*x*)。

x˙=f(x)+g(x)u

将 **fx** 连接到 *Nx*×1 信号，其中 *Nx* 等于 **Number of states** 参数。

### **gx** — 输入函数 标量 | 向量 | 矩阵

以下被控对象动力学方程中的输入函数 *g*(*x*)。

x˙=f(x)+g(x)u

将 **gx** 连接到 *Nx*×*Nu* 信号，其中 *Nx* 等于 **Number of states** 参数，*Nu* 等于 **Number of actions** 参数。

### **hx** — 控制屏障函数 标量 | 向量

控制屏障函数，定义为以下被控对象状态的安全集。

{x:h(x)≥0}

将 **hx** 连接到 *Nc*×1 信号，其中 *Nc* 等于 **Number of barrier certificates** 参数。

### **qx** — 控制屏障函数的偏导数 标量 | 向量 | 矩阵

控制屏障函数对被控对象状态的偏导数。

q(x)=∂h∂x

将 **qx** 连接到 *Nc*×*Nx* 信号，其中 *Nc* 等于 **Number of barrier certificates** 参数，*Nx* 等于 **Number of states** 参数。

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

由 QP 求解器返回的修改后的控制动作。

如果求解器在达到最大迭代次数之前找到解，**u\*** 输出此最优解。

如果求解器达到最大迭代次数，优化停止，**u\*** 输出次优解。

如果初始优化问题不可行，返回的控制动作取决于模块是否配置为忽略约束或动作边界。有关详细信息，请参阅 **exitflag** 参数。

如果 **Number of actions** 参数为 `1`，**u\*** 输出标量信号。否则，**u\*** 输出长度等于 **Number of actions** 的向量信号。

### **exitflag** — 优化状态 `1` | `0` | 负整数

QP 求解器的优化状态。下表显示了可能的状态值。

| 退出标志 | 描述 |
| --- | --- |
| `1` | 求解器收敛到最优解，且所有约束和边界均有效。在这种情况下，**u\*** 输出最优控制动作。 |
| `0` | 求解器达到最大迭代次数。**u\*** 中输出的控制动作可能是次优的。 |
| 负整数 | 初始优化问题不可行，且适用以下场景之一。 - 在没有动作边界的情况下重新运行优化未产生可行解。 - 在没有约束边界的情况下重新运行优化未产生可行解。 在这种情况下，**u\*** 中输出的控制动作为零。 |

#### 依赖

要启用此输出端口，请选择 **Optimization status** 参数。

## 参数

#### 参数选项卡

### **Number of states** — 被控对象状态数 `1`（默认）| 正整数

指定被控对象中的状态数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nx` |
| **类型：** 字符向量 |
| **默认：** `'1'` |

### **Number of actions** — 控制动作数 `1`（默认）| 正整数

指定要施加边界并优化的动作数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nu` |
| **类型：** 字符向量 |
| **默认：** `'1'` |

### **Number of barrier certificates** — 障碍证书约束数 `1`（默认）| 正整数

指定要施加的障碍证书约束数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nc` |
| **类型：** 字符向量 |
| **默认：** `'1'` |

### **Constraint factor** — 约束因子 `10`（默认）| 正标量 | 向量

指定障碍证书约束中的约束因子 *γ*。

如果 **Number of barrier certificates** 参数为 `1`，则将 **Constraint factor** 指定为有限正标量。否则，可以将 **Constraint factor** 指定为有限正标量值或长度等于 **Number of barrier certificates** 的正标量列向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `gamma` |
| **类型：** 字符向量 |
| **默认：** `'10'` |

### **Constraint power** — 约束幂 `1`（默认）| 正奇整数 | 向量

指定障碍证书约束中的约束幂 *β*。

如果 **Number of barrier certificates** 参数为 `1`，则将 **Constraint power** 指定为正奇整数。否则，可以将 **Constraint power** 指定为正奇整数或长度等于 **Number of barrier certificates** 的正奇整数列向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `beta` |
| **类型：** 字符向量 |
| **默认：** `'1'` |

### **Use external source for upper bound** — 添加上动作边界输入端口 `off`（默认）| `on`

选择此参数以添加 **umax** 输入端口，用于外部上动作边界。

#### 程序化使用

|  |
| --- |
| **模块参数：** `external_umax` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认：** `'off'` |

### **Use external source for lower bound** — 添加下动作边界输入端口 off（默认）| on

选择此参数以添加 **umin** 输入端口，用于外部下动作边界。

#### 程序化使用

|  |
| --- |
| **模块参数：** `external_umin` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认：** `'off'` |

#### 模块选项卡

### **Sample time** — 优化采样时间 `0.1`（默认）| 正标量

指定运行优化的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** 字符向量 |
| **默认：** `'0.1'` |

### **Maximum iterations** — 最大优化迭代次数 `200`（默认）| 正整数

指定最大优化迭代次数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `maxiter` |
| **类型：** 字符向量 |
| **默认值：** `'200'` |

### **Constraint tolerance** — 约束违反容差 `1e-6`（默认）| 非负标量

指定约束违反的容差值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `tol` |
| **类型：** 字符向量 |
| **默认值：** `'1e-6'` |

### **Optimization status** — 添加退出标志输出端口 `off`（默认）| `on`

选择此参数以添加 **exitflag** 输出端口，用于表示 QP 求解器的优化状态。

#### 程序化使用

|  |
| --- |
| **模块参数：** `exitflag` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

## 所属库

Simulink Control Design / Constraint Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Barrier Certificate Enforcement 模块仅支持双精度信号的代码生成。

## 版本历史

**在 R2022a 中引入**

### R2023b：库位置变更

Barrier Certificate Enforcement 模块现在位于 **Simulink Control Design/Constraint Control** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Barrier Certificate Enforcement 模块的库链接会自动更新。

## 描述

修改控制动作以满足障碍证书约束和动作边界

Barrier Certificate Enforcement 模块计算在障碍证书约束和动作边界约束下最接近指定控制动作的修改后控制动作。

该模块使用二次规划（QP）求解器来寻找使函数 |u−u0|2 最小化的控制动作 *u*。此处，*u*0 是未修改的控制动作。

求解器对优化问题施加以下约束。

qxfx+qxgxu+γhxβ≥0umin≤u≤umax

此处：

- *f*x** 和
  *g*x** 是由被控对象动态 x˙=f(x)+g(x)u 定义的函数。
- *h*x** 是控制障碍函数。
- *q*x** 是控制障碍函数关于状态
  *x* 的偏导数。
- *γ* 是约束因子。
- *β* 是约束幂。
- *u*min 是控制动作的下界。
- *u*max 是控制动作的上界。

Barrier Certificate Enforcement 模块需要 Optimization Toolbox™ 软件。

有关障碍证书执行的更多信息，请参阅 Barrier Certificate Enforcement for Control Design。
