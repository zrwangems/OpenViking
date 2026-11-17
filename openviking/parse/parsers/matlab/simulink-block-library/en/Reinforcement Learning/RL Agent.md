---
type: simulink-block
title: 'RL Agent'
family: 'reinforcement-learning'
product_id: 'reinforcement-learning'
product_name: 'Reinforcement Learning'
documentation_release: R2025b
official_category: ''
documentation_page: 'rlagent'
documentation_source_path: 'ref/rlagent.html'
language: en
---

# RL Agent

## Ports
```yaml
ports:
- name: observation
  summary: Environment observations scalar | vector | nonvirtual bus
  direction: input
- name: reward
  summary: Reward from environment scalar
  direction: input
- name: isdone
  summary: Flag to terminate episode simulation logical
  direction: input
- name: external action
  summary: External action signal scalar | vector
  direction: input
- name: last action
  summary: Last action applied to environment signal scalar | vector
  direction: input
- name: use external action
  summary: Use external action signal 0 | 1
  direction: input
- name: action
  summary: Agent action scalar | vector | nonvirtual bus
  direction: output
- name: cumulative reward
  summary: Cumulative undiscounted reward scalar
  direction: output
```

### Input

### **observation** — Environment observations scalar | vector | nonvirtual bus

This port receives observation signals from the environment. Observation signals
represent measurements or other instantaneous system data. If you have multiple
observations, you can use a Mux block to combine them into a vector
signal. To use a nonvirtual bus signal, use `bus2RLSpec`.

### **reward** — Reward from environment scalar

This port receives the reward signal, which you compute based on the observation
data. The reward signal is used during agent training to maximize the expectation of
the long-term reward.

### **isdone** — Flag to terminate episode simulation logical

Use this signal to specify conditions under which to terminate a training episode.
You must configure logic appropriate to your system to determine the conditions for
episode termination. One application is to terminate an episode that is clearly going
well or going poorly. For instance, you can terminate an episode if the agent reaches
its goal or goes irrecoverably far from its goal.

### **external action** — External action signal scalar | vector

Use this signal to provide an external action to the block. This signal can be a
control action from a human expert, which can be used for safe or imitation learning
applications. When the value of the **use external action** signal is
`1`, the RL Agent block passes the
**external action** signal to the environment through the
**action** output port. The block also uses the external action to
update the agent policy based on the resulting observations and rewards.

#### Dependencies

To enable this port, select the **External action inputs**
parameter.

### **last action** — Last action applied to environment signal scalar | vector

For some applications, the action applied to the environment can differ from the
action output from the RL Agent block. For example, the Simulink model can contain a saturation block on the action output signal.

In such cases, to improve learning results for off-policy agents, you can enable
this input port and connect the actual action signal that is actually applied to your
environment, delayed by one sample time. For an example, see Custom Training Loop with Simulink Action Noise.

**Note**

The **last action** port should be used only with off-policy
agents, otherwise training can produce unexpected results.

#### Dependencies

To enable this port, select the **Last action input**
parameter.

### **use external action** — Use external action signal `0` | `1`

Use this signal to pass the **external action** signal to the
environment.

When the value of the **use external action** signal is
`1` the block passes the **external action**
signal to the environment. The block also uses the external action to update the agent
policy.

When the value of the **use external action** signal is
`0` the block does not pass the **external
action** signal to the environment and does not update the policy using the
external action. Instead, the action from the block uses the action from the agent
policy.

#### Dependencies

To enable this port, select the **External action inputs**
parameter.
### Output

### **action** — Agent action scalar | vector | nonvirtual bus

Action computed by the agent based on the observation and reward inputs. Connect
this port to the input of your environment. To use a nonvirtual bus signal, use
`bus2RLSpec`.

**Note**

Continuous action-space agents such as `rlACAgent`,
`rlPGAgent`,
or `rlPPOAgent`
(the ones using an `rlContinuousGaussianActor` object), do not enforce constraints set by
the action specification. In these cases, you must enforce action space
constraints within the environment.

### **cumulative reward** — Cumulative undiscounted reward scalar

This is the cumulative undiscounted sum of the reward signal from the beginning of
the simulation until the current time. Observe or log this signal to track how the
cumulative reward evolves over time.

#### Dependencies

To enable this port, select the **Cumulative reward output**
parameter.
## Parameters
```yaml
parameters:
- name: Agent object
  summary: Agent to train agentObj (default) | agent object
  group: ''
  block_parameter: Agent
  type: string, character vector
  default: '"agentObj"'
- name: Generate greedy policy block
  summary: Generate greedy policy block controller button
  group: ''
- name: External action inputs
  summary: Add input ports for external action off (default) | on
  group: ''
  block_parameter: ExternalActionAsInput
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Last action input
  summary: Add input ports for last action applied to environment off (default) | on
  group: ''
  block_parameter: ProvideLastAction
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Cumulative reward output
  summary: Add cumulative reward output port off (default) | on
  group: ''
  block_parameter: ProvideCumRwd
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Use strict observation data types
  summary: Enforce strict data types for observations off (default) | on
  group: ''
  block_parameter: UseStrictObservationDataTypes
  type: string, character vector
  values: '"off" | "on"'
  default: '"off"'
```

### **Agent object** — Agent to train `agentObj` (default) | agent object

Enter the name of an agent object stored in the MATLAB workspace or a data dictionary, such as an `rlACAgent` or
`rlDDPGAgent`
object. For information about agent objects, see Reinforcement Learning Agents.

If the RL Agent block is within a conditionally executed subsystem,
such as a Triggered Subsystem (Simulink) or a Function-Call Subsystem (Simulink), you must specify the sample time of the agent object
as `-1` so that the block can inherit the sample time of its parent
subsystem.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Agent` |
| **Type:** string, character vector |
| **Default:** `"agentObj"` |

### **Generate greedy policy block** — Generate greedy policy block controller button

Generate a Policy block that
implements a greedy policy for the agent specified in **Agent object**
by calling the `generatePolicyBlock` block function. To generate a greedy policy, the block
sets the `UseExplorationPolicy` property of the agent to
`false` before generating the policy block.

The generated block is added to a new Simulink model and the policy data is saved in
a MAT file in the current working folder.

### **External action inputs** — Add input ports for external action `off` (default) | `on`

Enable the **external action** and **use external
action** block input ports by selecting this parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExternalActionAsInput` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Last action input** — Add input ports for last action applied to environment `off` (default) | `on`

Enable the **last action** block input port by selecting this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ProvideLastAction` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Cumulative reward output** — Add cumulative reward output port `off` (default) | `on`

Enable the **cumulative reward** block output by selecting this
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ProvideCumRwd` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |

### **Use strict observation data types** — Enforce strict data types for observations `off` (default) | `on`

Select this parameter to enforce the observation data types. In this case, if the
data type of the signal connected to the **observation** input port
does not match the data type in the `ObservationInfo` property of the
agent, the block attempts to cast the signal to the correct data type. If casting the
data type is not possible, the block generates an error.

Enforcing strict data types:

- Lets you validate that the block is getting the correct data types.
- Allows other blocks to inherit their data type from the
  **observation** port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseStrictObservationDataTypes` |
| **Type:** string, character vector |
| **Values:** `"off"` | `"on"` |
| **Default:** `"off"` |
## Libraries

Reinforcement Learning Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Reinforcement learning agent

Use the RL Agent block to simulate and train a reinforcement learning agent
in Simulink®. You associate the block with an agent stored in the MATLAB® workspace or a data dictionary, such as an `rlACAgent` or
`rlDDPGAgent` object.
You connect the block so that it receives an observation and a computed reward. For instance,
consider the following block diagram of the `rlSimplePendulumModel`
model.

The **observation** input port of the RL Agent block
receives a signal that is derived from the instantaneous angle and angular velocity of the
pendulum. The **reward** port receives a reward calculated from the same two
values and the applied action. You configure the observations and reward computations that are
appropriate to your system.

The block uses the agent to generate an action based on the observation and reward you
provide. Connect the **action** output port to the appropriate input for your
system. For instance, in the `rlSimplePendulumModel`, the
**action** output port is a torque applied to the pendulum system. For more
information about this model, see Train DQN Agent to Swing Up and Balance Pendulum.

To train a reinforcement learning agent in Simulink, you generate an environment from the Simulink model. You then create and configure the agent for training against that
environment. For more information, see Create Custom Simulink Environments. When you call `train` using the
environment, `train` simulates the model and updates the agent associated
with the block.
