# MUA Research and Standards Register

**Status:** RESEARCHED — initial standards mapping, not a complete survey  
**Reviewed:** 2026-11-24

## Design conclusion

MUA should not invent replacements for mature mathematical representation standards. It should provide an EKTA-level identity, lifecycle, relation, constraint, provenance, and representation envelope, then use established standards through adapters where appropriate.

## Primary standards and references

| Reference | Contribution | MUA use | Limitation / status |
|---|---|---|---|
| [OpenMath 2.0 Revision 2](https://openmath.org/standard/) | Semantics and encoding of mathematical objects; content dictionaries | Semantic payload adapter and symbol vocabulary | Does not define full MUA lifecycle or workspace |
| [OpenMath documentation](https://openmath.org/documents/) | Standard, content dictionaries, SCSCP and type-system material | Interoperability research | Evaluate individual dictionaries and licensing |
| [MathML Core](https://www.w3.org/TR/mathml-core/) | Browser-oriented notation/content representation | Web notation renderer and expression interchange | Not a complete geometry or computation model |
| [MathML 4.0 Working Draft](https://www.w3.org/TR/mathml4/) | Broader mathematical markup specification work | Monitor for adapter opportunities | Working Draft as reviewed 2026-11-24 |
| [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) | Machine-readable structural validation | UMO and coordinate-frame schemas | Structural validity is not mathematical correctness |

## Key distinctions

1. Notation is not semantics. A rendered formula may leave the mathematical object under-specified.
2. Semantics is not computation. An expression still needs a defined domain, algorithm, precision, and execution context.
3. Computation is not proof. A numerical result is not a formal proof.
4. Representation is not identity. One UMO can have multiple symbolic, tabular, graphical, spatial, and procedural forms.
5. Schema validity is not mathematical validity. JSON Schema checks record structure, not theorem truth or numerical stability.

## Research questions

- Which OpenMath Content Dictionaries cover the first target entity families, and what are their maturity statuses?
- Which MathML Core and MathML 4 features support presentation, content semantics, intent, and accessibility?
- Which interchange formats should support graphs, geometry, units, and scientific arrays?
- How should UMO represent units and dimensional analysis without hard-coding one unit system?
- How should proof artifacts link to Lean or other proof assistants while keeping the core schema tool-neutral?
- Which numerical metadata is mandatory for reproducibility?
- What smallest vertical slice proves semantic-to-visual consistency?

## Source assessment

OpenMath identifies Version 2.0 Revision 2 as its normative standard. W3C MathML Core is a Candidate Recommendation Snapshot dated 24 June 2025. W3C MathML 4.0 is a Working Draft, not a final Recommendation. JSON Schema's published current specification family is Draft 2020-12.

Re-check upstream status before implementation decisions.
