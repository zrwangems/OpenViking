---
type: simulink-block
title: 'Mu-Law Compressor'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'mulawcompressor'
documentation_source_path: 'ref/mulawcompressor.html'
language: en
---

# Mu-Law Compressor

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**mu value**
:   The µ-law parameter of the compressor.

**Peak signal magnitude**
:   The peak value of the input signal. This is also the peak value of the
    output.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Implement µ-law compressor for source coding

The Mu-Law Compressor block implements a µ-law compressor for the input signal. The
formula for the µ-law compressor is

y=Vlog(1+μ|x|/V)log(1+μ)sgn(x)

where µ is the µ-law parameter of the compressor, *V* is the peak
magnitude of *x*, log is the natural logarithm, and sgn is the signum
function (`sign` in MATLAB®).

The input can have any shape or frame status. This block processes each vector element
independently.
