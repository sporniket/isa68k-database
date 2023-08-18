# The ISA 68k database

> [WARNING] Please read carefully this note before using this project. It contains important facts.

Content

1. What is **The ISA 68k database**, and when to use it ?
2. What should you know before using **The ISA 68k database** ?
3. How to use **The ISA 68k database** ?
4. Known issues
5. Miscellanous

## 1. What is **The ISA 68k database**, and when to use it ?

**The ISA 68k database** is a description of the Instruction Set Architecture (ISA) of a family of CPU from the 1980-2000 years known as "Motorola 68k".

The description takes the form of a relationnal database, with each table stored in an open format : Tabulation Separated Values (TSV).

The goal is to have enough description data to be able to generate "something", like :

* Documentation
* **Instruction compiler/decompiler** (this is my main motivation to initiate this work).
* Preparatory work to design a micro-code based implementation in a hardware description language by following the methodology described in *"Microprocessor Design using Verilog HDL"* by Monte Dalrymple. (This is another source of motivation)


### Licence

**The ISA 68k database** is published under the Creative Commons CC0 license. You can find a copy of the licence there : https://creativecommons.org/publicdomain/zero/1.0/legalcode

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

**The ISA 68k database** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

### Release notes

> No release yet.

## 2. What should you know before using **The ISA 68k database** ?

**The ISA 68k database** is written using Google Sheet, so that editing is easier : nice and efficient formatting for legibility. Then each sheet is exported as TSV.

> Do not use **The ISA 68k database** if this project is not suitable for your project.

## 3. How to use **The ISA 68k database** ?

### From sources

To get the latest available work, one must clone the git repository.

	git clone --recurse-submodules https://github.com/sporniket/isa68k-database.git

Then, open the project with Kicad 6.

## 4. Known issues
See the [project issues](https://github.com/sporniket/isa68k-database/issues) page.

## 5. Miscellanous

### Report issues
Use the [project issues](https://github.com/sporniket/isa68k-database/issues) page.
