---
type: simulink-block
title: 'Constraint Enforcement'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Constraint Control'
documentation_page: 'constraintenforcement'
documentation_source_path: 'ug/constraintenforcement.html'
language: zh-CN
chinese_source: worker-translation
---

# Constraint Enforcement

## 端口

### 输入

### **u0** — 控制动作 标量 | 向量

未修改的控制动作，指定为标量或向量。

如果 **Number of actions** 参数为 `1`，则将 **u0** 连接到标量信号。否则，将 **u0** 连接到长度等于 **Number of actions** 的向量信号。

### **fx** — 约束函数偏移系数 标量 | 向量

以下约束方程中的偏移系数 *fx*。

fx+gxu≤c

如果 **Number of constraints** 参数为 `1`，则将 **fx** 连接到标量信号。否则，将 **fx** 连接到长度等于 **Number of constraints** 的向量信号。

### **gx** — 约束函数线性系数 标量 | 向量 | 矩阵

以下约束方程中的线性系数 *gx*。

fx+gxu≤c

将 **gx** 连接到 *Nc*×*Nu* 信号，其中 *Nc* 等于 **Number of constraints** 参数，*Nu* 等于 **Number of actions** 参数。

### **c** — 约束边界 标量 | 向量

以下约束函数中的运行时约束边界 *c*。

fx+gxu≤c

如果 **Number of constraints** 参数为 `1`，则将 **c** 连接到标量信号。否则，将 **c** 连接到长度等于 **Number of constraints** 的向量信号。

如果此端口被禁用，模块将使用通过 **Constraint bound** 参数指定的常量约束边界。

#### 依赖关系

要启用此输入端口，请选择 **Use external source** 参数。

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

如果求解器达到最大迭代次数，优化停止，**u\*** 输出一个次优解。

如果初始优化问题不可行，返回的控制动作取决于模块是否配置为忽略约束或动作边界。有关详细信息，请参阅 **exitflag** 参数。

如果 **Number of actions** 参数为 `1`，**u\*** 输出标量信号。否则，**u\*** 输出长度等于 **Number of actions** 的向量信号。

### **exitflag** — 优化状态 `1` | `2` | `3` | `4` | `0` | 负整数

QP 求解器的优化状态。下表显示了可能的状态值。

| Exit Flag | 描述 |
| --- | --- |
| `1` | 求解器收敛到最优解，且所有约束和边界均有效。在这种情况下，**u\*** 输出最优控制动作。 |
| `2` | 初始优化问题不可行，且模块配置为忽略所有约束和边界。在这种情况下，**u\*** 输出未修改的控制动作 **u0**。 |
| `3` | 初始优化问题不可行。模块在忽略动作边界的情况下重新运行优化，并找到了可行解，模块将其输出到 **u\*** 中。 |
| `4` | 初始优化问题不可行。模块在忽略约束边界的情况下重新运行优化，并找到了可行解，模块将其输出到 **u\*** 中。 |
| `0` | 求解器达到了最大迭代次数。**u\*** 中输出的控制动作可能是次优的。 |
| 负整数 | 初始优化问题不可行，且适用以下场景之一。  - 在无动作边界的情况下重新运行优化未产生可行解。 - 在无约束边界的情况下重新运行优化未产生可行解。 - 模块配置为不忽略约束和动作边界。  在这种情况下，**u\*** 中输出的控制动作为零。 |

#### 依赖关系

要启用此输出端口，请选择 **Optimization status** 参数。

## 参数

#### 参数选项卡

### **Number of constraints** — 约束数量 `1` （默认） | 正整数

指定要执行的约束数量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nc` |
| **类型：** 字符向量 |
| **默认值：** `'1'` |

### **Number of actions** — 动作数量 `1` （默认） | 正整数

指定要应用边界并优化的动作数量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nu` |
| **类型：** 字符向量 |
| **默认值：** `'1'` |

### **Constraint bound** — 约束边界 `0` （默认） | 有限标量 | 向量

指定约束的常数边界。如果 **Number of constraints** 参数为 `1`，则将 **Constraint bound** 指定为有限标量。否则，将 **Constraint bound** 指定为长度等于 **Number of constraints** 的有限值向量。

如果约束在运行时变化，请选择 **Use external source** 参数，并将运行时约束信号连接到 **c** 输入端口。

#### 依赖关系

要启用此参数，请清除 **Use external source** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `c` |
| **类型：** 字符向量 |
| **默认值：** `'0'` |

### **Use external source** — 添加外部约束边界输入端口 `off` （默认） | `on`

选择此参数以添加用于外部约束边界的 **c** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `external_c` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

### **Use external source for upper bound** — 添加上动作边界输入端口 `off` （默认） | `on`

选择此参数以添加用于外部上动作边界的 **umax** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `external_umax` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

### **Use external source for lower bound** — 添加下动作边界输入端口 off （默认） | on

选择此参数以添加用于外部下动作边界的 **umin** 输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数：** `external_umin` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

#### 模块选项卡

### **Sample time** — 优化采样时间 `0.1`（默认）| 正标量

指定运行优化时的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Ts` |
| **类型：** 字符向量 |
| **默认值：** `'0.1'` |

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

选择此参数可添加 **exitflag** 输出端口，用于指示 QP 求解器的优化状态。

#### 程序化使用

|  |
| --- |
| **模块参数：** `exitflag` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

### **Ignore constraints when QP is infeasible** — 当优化不可行时禁用约束 `off`（默认）| `on`

当您选择此参数时，如果初始 QP 问题不可行，模块将在禁用约束的情况下重新运行优化。

当您同时选择此参数和 **Ignore action bounds when QP is infeasible** 时，如果初始 QP 问题不可行，模块将输出未修改的动作信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `relax_c` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

### **Ignore action bounds when QP is infeasible** — 当优化不可行时禁用动作边界 `off`（默认）| `on`

当您选择此参数时，如果初始 QP 问题不可行，模块将在禁用动作边界的情况下重新运行优化。如果 **umax** 和 **umin** 输入端口均被禁用，模块将忽略此参数。

当您同时选择此参数和 **Ignore constraints when QP is infeasible** 时，如果初始 QP 问题不可行，模块将输出未修改的动作信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `relax_u` |
| **类型：** 字符向量 |
| **值：** `'off'`|`'on'` |
| **默认值：** `'off'` |

## 所属库

Simulink Control Design / Constraint Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Constraint Enforcement 模块仅支持双精度信号的代码生成。

## 版本历史

**在 R2021a 中引入**

### R2023b：库位置变更

Constraint Enforcement 模块现在位于 **Simulink Control Design/Constraint Control** 子库中。

在 R2023b 中，当您打开在先前版本中保存的模型时，Constraint Enforcement 模块的库链接会自动更新。

## 描述

修改控制动作以满足约束和动作边界

Constraint Enforcement 模块计算在约束和动作边界条件下最接近指定控制动作的修改后控制动作。

该模块使用二次规划（QP）求解器来寻找使函数 |u−u0|2 最小化的控制动作 *u*。其中，*u*0 是未修改的控制动作。

求解器对优化问题施加以下约束。

fx+gxu≤cumin≤u≤umax

其中：

- *fx* 和 *gx* 是约束函数的系数。
- *c* 是约束函数的边界。
- *u*min 是控制动作的下界。
- *u*max 是控制动作的上界。

Constraint Enforcement 模块需要 Optimization Toolbox™ 软件。

有关约束实施的更多信息，请参阅 Constraint Enforcement for Control Design。
