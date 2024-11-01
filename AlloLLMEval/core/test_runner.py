from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional
from .base import PromptExecutorBase, ExecutorConfig
from .metrics import MetricEvaluatorBase, MetricOutput


@dataclass
class TestConfig:
    """Configuration for test execution"""

    executor_config: ExecutorConfig
    metric_config: Dict[str, Any]


@dataclass
class TestResult:
    """Test execution results"""

    metric_output: MetricOutput
    executor_output: Any
    configs_used: TestConfig
    metadata: Dict[str, Any]
    timestamp: datetime


class TestRunner:
    """Manages test execution and evaluation"""

    def __init__(self, executor: PromptExecutorBase, evaluator: MetricEvaluatorBase, config: TestConfig):
        self.executor = executor
        self.evaluator = evaluator
        self.config = config
        self._validate_components()

    def _validate_components(self):
        """Validate the test runner components"""
        if not isinstance(self.executor, PromptExecutorBase):
            raise ValueError("Executor must be an instance of PromptExecutorBase")
        if not isinstance(self.evaluator, MetricEvaluatorBase):
            raise ValueError("Evaluator must be an instance of MetricEvaluatorBase")
        if not isinstance(self.config, TestConfig):
            raise ValueError("Config must be an instance of TestConfig")

    def _merge_configs(self, base_config: TestConfig, override_config: Optional[TestConfig]) -> TestConfig:
        """Merge base and override configurations"""
        if not override_config:
            return base_config

        merged_executor_config = {**base_config.executor_config, **override_config.executor_config}
        merged_metric_config = {**base_config.metric_config, **override_config.metric_config}

        return TestConfig(executor_config=merged_executor_config, metric_config=merged_metric_config)

    def _get_metadata(self) -> Dict[str, Any]:
        """Get metadata about the test execution"""
        return {
            "executor_type": self.executor.__class__.__name__,
            "evaluator_type": self.evaluator.__class__.__name__,
            "timestamp": datetime.now().isoformat(),
        }

    def run(
        self,
        input_data: Any,
        evaluation_params: Optional[Dict[str, Any]] = None,
        override_config: Optional[TestConfig] = None,
    ) -> TestResult:
        """Run the test with given input and configurations"""
        effective_config = self._merge_configs(self.config, override_config)
        base_output = self.executor.execute(input_data, effective_config.executor_config)

        metric_result = self.evaluator.evaluate(
            executor=self.executor,
            input_data=input_data,
            base_output=base_output,
            executor_config=effective_config.executor_config,
            test_config=effective_config.metric_config,
            evaluation_params=evaluation_params or {},
        )

        return TestResult(
            metric_output=metric_result,
            executor_output=base_output,
            configs_used=effective_config,
            metadata=self._get_metadata(),
            timestamp=datetime.now(),
        )
