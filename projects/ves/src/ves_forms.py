"""Small deterministic schema-driven form validation primitives for VES."""
from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Any


@dataclass(frozen=True)
class FormField:
    id: str
    label: str
    type: str
    required: bool = False
    minimum: float | None = None
    maximum: float | None = None
    choices: tuple[str, ...] = ()
    pattern: str | None = None


@dataclass(frozen=True)
class FormDefinition:
    id: str
    fields: tuple[FormField, ...] | list[FormField]
    allow_extra: bool = False

    def __post_init__(self):
        ids = [field.id for field in self.fields]
        if len(ids) != len(set(ids)):
            raise ValueError("form field IDs must be unique")
        if any(not field.id.strip() or not field.label.strip() for field in self.fields):
            raise ValueError("form field id and label are required")


@dataclass(frozen=True)
class FormError:
    code: str
    field_id: str
    message: str


def _matches_type(value: Any, field_type: str) -> bool:
    if field_type == "text":
        return isinstance(value, str)
    if field_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if field_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if field_type == "boolean":
        return isinstance(value, bool)
    if field_type == "enum":
        return isinstance(value, str)
    return False


def validate_form_data(form: FormDefinition, data: dict[str, Any]) -> list[FormError]:
    errors: list[FormError] = []
    known = {field.id for field in form.fields}
    if not form.allow_extra:
        for key in sorted(set(data) - known):
            errors.append(FormError("VES-FORM-UNKNOWN", key, "Field is not declared by this form"))
    for spec in form.fields:
        if spec.id not in data or data[spec.id] is None:
            if spec.required:
                errors.append(FormError("VES-FORM-REQUIRED", spec.id, "Required field is missing"))
            continue
        value = data[spec.id]
        if not _matches_type(value, spec.type):
            errors.append(FormError("VES-FORM-TYPE", spec.id, f"Expected {spec.type}"))
            continue
        if spec.type in {"number", "integer"}:
            if spec.minimum is not None and value < spec.minimum:
                errors.append(FormError("VES-FORM-RANGE", spec.id, f"Value is below minimum {spec.minimum}"))
            if spec.maximum is not None and value > spec.maximum:
                errors.append(FormError("VES-FORM-RANGE", spec.id, f"Value is above maximum {spec.maximum}"))
        if spec.type == "enum" and spec.choices and value not in spec.choices:
            errors.append(FormError("VES-FORM-CHOICE", spec.id, "Value is not in the allowed choices"))
        if spec.type == "text" and spec.pattern and re.fullmatch(spec.pattern, value) is None:
            errors.append(FormError("VES-FORM-PATTERN", spec.id, "Value does not match the required pattern"))
    return errors
