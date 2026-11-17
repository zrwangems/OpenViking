---
type: simulink-block
title: 'SimEvents Common Design Patterns'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'common-design-patterns'
documentation_source_path: 'gs/common-design-patterns.html'
language: en
---

# SimEvents Common Design Patterns

The SimEvents ® library provides design patterns that you can refer to while modeling. To access these patterns, open the SimEvents library and double-click the Design Patterns block.

The SimEvents® library provides design patterns that you
can refer to while modeling. To access these patterns, open the SimEvents library
and double-click the Design Patterns block.

SimEvents custom design patterns provided in the library

Consider these design patterns while modeling:

| Design Pattern | Description | Input Specifications | Output Specifications | Application |
| --- | --- | --- | --- | --- |
| Entities with exponential random inter-generation times | Generates entities with random inter-generation times in exponential distribution fashion. | Not applicable | Structured entity with specified attributes | Model:  - Customers entering a store - Incoming phone calls of a hotline |
| Service time from random distribution | Specifies waiting time in the Entity Server as a random number uniformly distributed from 0 through 1. | Any entity type | Inherited from the input | Model:  - Extension of an event that is random within a range   (for example, length of a call - Purposeful holding of an entity for a random   time |
| Extract attributes of entities as signals | Extracts one or more attributes of entities as signals. | A structured entity or bus object with specified attribute | `getAttribute` — Real double scalar signal  Extracted Attribute — Inherited from the input | Inspect or use a specific entity attribute |
| Timestamp entities upon generation | Generates entities with an attribute **TimeStamp** that records the simulation time upon generation. | Not applicable | Structured entity with attributes `Data` and `TimeStamp` | Use when generation time of entities is needed, for example, when calculating the priority in a combined scheduling algorithm. |
| Release entity upon signal value change | Releases an incoming entity when there is a jump in the step function. | Any entity type | Inherited from the input | Use to control the passing of entities based on the change of a function. |
| Open gate on service completion | Upon service completion, the gate opens and releases an entity. | Any entity type | Inherited from the input | Use task completion to trigger entity processing. |
| Sense an entity passing from A to B and open a gate | Passing an entity from *A* to *B* opens the gate and releases an entity. | Any entity type | Inherited from the input | Use to model the passing of an entity in one route to control the passing of another route. |
| Select an entity with a matching attribute | Select entities to advance whose specified attributes are matching the anonymous entity at the control port | A structured entity or bus object with a specified attribute | Inherited from the input | Select entities with a specified attribute to output |
| Discrete Event Chart: Single Server with Pause | A Ctrl message triggers pause of service for the incoming entity. A second Ctrl message continues the service. Entity data conveys the service time. | Ctrl — Anonymous entity specifying the pause and resume  Entity — Anonymous entity specifying service time | Inherited from the input | Use external events or signals to pause the service of entities. |
| Discrete Event Chart: Single Server with Timeout | If the service time (which is random) exceeds the timeout limit specified by the entity data, the entity leaves the server. | Anonymous entity with specified timeout limit | Inherited from the input | Model:  - A protocol that explicitly calls for timeouts. - Implementation of special routing or other handling of   entities that exceed a time limit. - Entities that represent perishable items. |
| Discrete Event Chart: Custom Output Switch | Randomly routes entities to one of the three output ports. | Anonymous entity | Inherited from the input | Implement a more complicated routing algorithm for an output switch. |
| MATLAB Discrete Event System: Custom Generator | The Custom Generator block, defined using the MATLAB Discrete Event System block, is a basic entity generator. The generator block requires specification of generation period. | Not applicable | Anonymous entity | Implement a more complicated entity generator. |
| MATLAB Discrete Event System: Custom Server | Custom Server block, defined using the MATLAB Discrete Event System block, is a basic entity server. The server block requires specification of server number and service time. | Any entity type | Inherited from the input | Implement a more complicated entity server. |
| MATLAB Discrete Event System: Selection Queue | The Selection Queue block, defined using the MATLAB Discrete Event System block, stores entities of bus type `passenger` arriving at the IN port. Keys from the call port select `passenger` entities with the matching `trainNum` field and send them to the OUT port. | Key — Anonymous entity carrying the selection key  IN — A structured entity or bus object with specified attribute | Inherit from IN | Select a specific entity to output from a queue. |

## See Also

MATLAB Discrete-Event System | Discrete-Event Chart

### Topics

- Block Authoring
- Discrete-Event System Objects
- Implement Discrete-Event Systems with Charts

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
