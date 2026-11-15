---
type: simulink-block
title: 'S-Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunction'
language: zh-CN
chinese_source: official
---

# S-Function

在模型中包含 S-Function

## 所属库

Simulink / User-Defined Functions

## 描述

S-Function 模块允许您将用 C、C++ 或 Fortran® 编写的 S-Function 或系统函数算法（称为 C MEX S-Function）集成到 Simulink 模型中。您可以使用该模块来实现 1 级或 2 级 C MEX S-Function。要将您的 S-Function 合并到一个模型中，请在编译 C MEX S-Function 后执行以下操作：

1. 将 S-function 模块从 **Simulink 库浏览器**拖到您的模型中。
2. 打开**模块参数**对话框，在 **S-Function 名称**字段指定 S-Function 名称，以便为 S-function 模块提供功能。例如，键入 `timestwo` 并选择**应用**。

*S-Function* 是以 MATLAB®、C、C++ 或 Fortran 语言编写的 Simulink® 模块的计算机语言描述。如果您有 C、C++ 或 Fortran S-Function，则需要使用 `mex` 实用工具将它们编译为 MEX 文件（请参阅编译 C MEX 函数）。S-Function 定义模块在仿真的不同部分（例如初始化、更新、求导、输出和终止）如何工作。S-Function 使用一种称为 S-Function API 的特殊调用语法，使您能够与 Simulink 引擎进行交互。这种交互与该引擎和内置 Simulink 模块之间发生的交互非常相似。在仿真的每一步，仿真引擎都会调用一个方法来完成特定任务。

例如，下面是名为 `timestwo.c` 的简单 C MEX S-Function 的示例，其输出是其输入的两倍。

```
#define S_FUNCTION_NAME timestwo /* Specifies the name of the S-function (timestwo) */
#define S_FUNCTION_LEVEL 2 /* Specifies that the S-function is in the Level 2 format */

#include "simstruc.h" /* Defines the data structure */
static void mdlInitializeSizes(SimStruct *S) /* Initialize the input and output ports and their size */
{
    ssSetNumSFcnParams(S, 0);
    if (ssGetNumSFcnParams(S) != ssGetSFcnParamsCount(S)) {
        return; /* Parameter mismatch reported by the Simulink engine*/
    }

    if (!ssSetNumInputPorts(S, 1)) return;
    ssSetInputPortWidth(S, 0, DYNAMICALLY_SIZED);
    ssSetInputPortDirectFeedThrough(S, 0, 1);

    if (!ssSetNumOutputPorts(S,1)) return;
    ssSetOutputPortWidth(S, 0, DYNAMICALLY_SIZED);

    ssSetNumSampleTimes(S, 1);

    /* Take care when specifying exception free code - see sfuntmpl.doc */
    ssSetOptions(S, SS_OPTION_EXCEPTION_FREE_CODE);
    }
static void mdlInitializeSampleTimes(SimStruct *S) /* Set the sample time of the S-function as inherited */
{
    ssSetSampleTime(S, 0, INHERITED_SAMPLE_TIME);
    ssSetOffsetTime(S, 0, 0.0);
}
static void mdlOutputs(SimStruct *S, int_T tid) /* Calculate the block output for each time step */
{
    int_T i;
    InputRealPtrsType uPtrs = ssGetInputPortRealSignalPtrs(S,0);
    real_T *y = ssGetOutputPortRealSignal(S,0);
    int_T width = ssGetOutputPortWidth(S,0);

    for (i=0; i<width; i++) {
        *y++ = 5.0 *(*uPtrs[i]);
    }
}
static void mdlTerminate(SimStruct *S){} /* Perform tasks at the end of the simulation */

#ifdef MATLAB_MEX_FILE /* Is this file being compiled as a MEX-file? */
#include "simulink.c" /* MEX-file interface mechanism */
#else
#include "cg_sfun.h" /* Code generation registration function */
#endif
```

S-Function 遵循一般形式，可以适应连续、离散和混合系统。您可以在 S-Function 中实现算法，并使用 S-Function 模块将其添加到 Simulink 模型。在编写 S-Function 并将其名称放入 S-Function 模块（在 User-Defined Functions 模块库中提供）后，您可以使用封装来自定义用户界面。在此示例中，使用 `mex timestwo.c` 编译 `timestwo.c` 函数，并使用 S-Function 模块实现它。

Timestwo S-function is implemented using the S-Function block. The input to the block is a sine wave and the output of the block is connected to a Scope block.

S-Function 模块显示指定的 S-Function 的名称，以及该 S-Function 指定的输入和输出端口的数量。连接输入端口的信号必须具有 S-Function 为输入端口指定的维度。

**注意**

使用 Level-2 MATLAB S-Function 模块，在模块图中包含一个 2 级 MATLAB S-Function。

## 端口

### 输入

### **In** — S-Function 模块的信号输入 标量 | 向量 | 矩阵

您可以使用 `mdlInitializeSizes` 回调函数来配置输入端口。使用 `mdlInitializeSizes` 函数指定输入端口的数量、输入信号的维度、每个端口的采样时间以及端口是否为直接馈通。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — S-Function 模块的信号输出 标量 | 向量 | 矩阵

您可以使用 `mdlInitializeSizes` 回调函数来配置输出端口。使用 `mdlInitializeSizes` 函数指定输出端口的数量、输出信号的维度以及每个端口的采样时间。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **S-Function 名称** — S-Function 的名称 `system` (默认) | S-Function 名称

使用此参数指定 S-Function 的名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionName` |
| **值:** | `'system'` (默认) | S-function name in quotes |

### **S-Function 参数** — 其他 S-Function 参数。 MATLAB 表达式 | 以逗号分隔的变量

指定其他 S-Function 参数。

函数参数可以指定为 MATLAB 表达式或以逗号分隔的变量。例如：

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

尽管单个参数可以用括号括起来，但参数列表一定不能用括号括起来。

#### 编程用法

|  |  |
| --- | --- |
| **参数:** | `Parameters` |
| **值:** | `''` (默认) | S-function parameters in quotes |

### **S-Function 模块** — 用于代码生成的其他文件 `''` (默认) | 文件名

仅当此模块代表 C MEX S-Function，并且您打算使用 Simulink Coder™ 软件从包含该模块的模型中生成代码时，此参数才适用。如果您使用此参数，当您准备好生成代码时，必须按照Control Regeneration of Top Model Code (Simulink Coder)中所述，强制代码生成器重新生成顶层模型。

有关使用此参数的详细信息，请参阅为 S-Function 指定其他源文件 (Simulink Coder)。

#### 编程用法

|  |  |
| --- | --- |
| **参数:** | `SFunctionModules` |
| **值:** | `''` (默认) | filenames in quotes |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `是a` |
| **多维信号** | `是a` |
| **可变大小信号** | `是a` |
| **过零检测** | `是a` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

- 实际代码生成支持取决于模块实现。
- 调用 MATLAB 的 S-Function 不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

- 实际数据类型支持取决于模块实现。
- 有关在 S-Function 中使用定点数据类型的详细信息，请参阅集成外部代码 (Fixed-Point Designer)。

## 版本历史记录

**在 R2006a 之前推出**
