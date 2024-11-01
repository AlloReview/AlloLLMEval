from typing import Any, Dict, Type, TypeVar, Generic
from ..core.base import InputType, OutputType

T = TypeVar("T")


def validate_type(value: Any, expected_type: Type[T]) -> T:
    """Validate that a value is of the expected type"""
    if not isinstance(value, expected_type):
        raise TypeError(
            f"Expected type {expected_type.__name__}, got {type(value).__name__}"
        )
    return value


def validate_config_schema(config: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """Validate that a configuration matches its schema"""
    for key, value_type in schema.items():
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")
        if not isinstance(config[key], value_type):
            raise TypeError(
                f"Config key '{key}' should be of type {value_type.__name__}, "
                f"got {type(config[key]).__name__}"
            )
