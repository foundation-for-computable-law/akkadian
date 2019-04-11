# A Domain Specific Language (DSL) for Law

## Overview

This Python module is designed to support the representation of legal rules as code. Once encoded, the rules can be applied to fact patterns to answer legal questions.

General features supported by this library:

- Representation of legal rules as Python functions
- Identification of any missing information needed to reach a conclusion
- Ability to model complex temporal requirements
- Calculation of the certainty of each conclusion

For more information, see the [wiki](https://github.com/mpoulshock/python-dsl-for-law/wiki).

## Purpose

This DSL is intended to serve as the foundation for the Hammurabi Project, an open source representation of legal rules from a variety of jurisdictions, at mass scale. It can also be used as a standalone rules engine.

Other possible uses:

- Creation of tax preparation software
- Compliance engine for businesses
- Interview engine for a public-facing legal knowledge app

## Contributing

This DSL is written in Python and can be thought of as a dialect of that language. New contributors are welcome.

For more information, contact mp@computablelaw.org.

## License

This repository uses a dual licensing model. 

**License 1:** All versions of this codebase prior to version 1.0 (which has not yet been released) and all noncommercial users are subject to the MIT license:

> Copyright 2011-2019 Foundation for Computable Law

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**License 2:** Commercial entities using version 1.0 of this software, or a subsequent version, in production will be subject to a paid commercial software license, the terms of which have yet to be defined. Proceeds of that license will go to the Foundation for Computable Law.

