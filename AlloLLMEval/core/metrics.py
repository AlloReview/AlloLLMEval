from enum import Enum
from dataclasses import dataclass
from typing import Any, Dict, Optional
from .base import PromptExecutorBase


class MetricStatus(Enum):
    PASSED = "passed"
    WARNING = "warning"
    FAILED = "failed"
    INCONCLUSIVE = "inconclusive"


@dataclass
class MetricOutput:
    score: float  # 0-1 score
    status: MetricStatus
    visualization: Any  # Plot, table, etc.
    details: Dict[str, Any]
    threshold: Dict[str, float]


class MetricEvaluatorBase:
    """Base class for metric evaluation"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self._validate_config()

    def _validate_config(self):
        """Validate the evaluator configuration"""
        if not isinstance(self.config, dict):
            raise ValueError("Config must be a dictionary")

    def evaluate(
        self,
        executor: PromptExecutorBase,
        input_data: Any,
        base_output: Any,
        executor_config: Dict[str, Any],
        test_config: Dict[str, Any],
        evaluation_params: Dict[str, Any],
    ) -> MetricOutput:
        """Evaluate outputs and return metric results"""
        raise NotImplementedError
