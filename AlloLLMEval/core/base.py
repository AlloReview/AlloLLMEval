from typing import TypeVar, Generic, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")
ExecutorConfig = Dict[str, Any]


class PromptExecutorBase(Generic[InputType, OutputType]):
    """Base class for all execution units"""

    def __init__(self, config_schema: Dict[str, Any]):
        self.config_schema = config_schema
        self._validate_schema()

    def _validate_schema(self):
        """Validate the config schema format"""
        if not isinstance(self.config_schema, dict):
            raise ValueError("Config schema must be a dictionary")

    def execute(self, input_data: InputType, config: ExecutorConfig) -> OutputType:
        """Execute the prompt with given input and configuration"""
        raise NotImplementedError
