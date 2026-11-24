# VES Form Engine — Initial Contract

## Purpose
Forms are typed editors over model properties. They must validate data before the model is marked reviewed or verified. A form definition is reusable and independent from its visual rendering.

## v0.1 supported field types
- text
- number
- integer
- boolean
- enum

## Field constraints
Required, minimum, maximum, enumerated choices and full-string regular-expression pattern. Unknown fields are rejected by default unless the form explicitly allows extras.

## Deterministic findings
- VES-FORM-REQUIRED
- VES-FORM-TYPE
- VES-FORM-RANGE
- VES-FORM-CHOICE
- VES-FORM-PATTERN
- VES-FORM-UNKNOWN

## Current implementation
The Python module src/ves_forms.py provides FormField, FormDefinition, FormError and validate_form_data. JSON Schema contract is in schemas/form.schema.json.

## Deferred
Conditional visibility, computed fields, cross-field constraints, nested/repeating groups, localization, UI Form Builder and schema migration are not implemented in v0.1.
