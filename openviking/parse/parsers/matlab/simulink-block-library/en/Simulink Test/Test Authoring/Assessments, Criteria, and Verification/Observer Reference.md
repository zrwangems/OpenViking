---
type: simulink-block
title: 'Observer Reference'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: 'Test Authoring / Assessments, Criteria, and Verification'
documentation_page: 'observerreference'
documentation_source_path: 'ref/observerreference.html'
language: en
---

# Observer Reference

## Ports

Not documented in R2025b.

## Parameters

### **Observer Model name** — Filename of Observer model `''` (default) | character vector

Path to the Observer model. The filename must be a valid MATLAB® identifier. The extension, for example, `.slx`, is
optional. You enter the Observer model name in the Observer Reference
block parameters dialog box, which you access by right-clicking on the block and
selecting **Block Parameters**. You can also open the model you
specify from the dialog box.

#### Programmatic Use

|  |
| --- |
| **Parameter**: `ObserverModelName` |
| **Type**: character vector |
| **Value**: `''` | `'<observer model name>'` |
| **Default**: `''` |

## Libraries

Simulink Test

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Create and contain an Observer model

An Observer Reference block references a separate model called the Observer
model. The Observer model and Observer Reference block enable wireless
monitoring of the signals in the main model. When you click or select **Add Observer
Reference** from the **Test** tab or the context menu,
respectively, an Observer Reference block is automatically added to the top
level of your main Simulink® model, and an Observer model is created. You can add Observer
Reference blocks only at the top level of the model.

The Observer model contains an Observer Port block
and can contain blocks such as scopes or a verification subsystem to monitor or verify the
observed signals, respectively. Signals are mapped to the Observer model through the
Observer Port block. The Observer Reference block does not
have inports or outports. For more information and an example of using Observers, see Access Model Data Wirelessly by Using Observers.

To stop observing signals, delete all the
Observer Reference blocks from the main model.
