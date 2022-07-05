from abc import ABC, abstractmethod


class BaseGetMissingStep(ABC):
    _steps_labels: dict

    def __init__(self, user_data):
        self._user_data = user_data

    @abstractmethod
    def _get_steps(self) -> dict:
        pass

    @abstractmethod
    def _nothing_is_missing(self) -> bool:
        pass

    def get_missing_step(self) -> str:
        if self._nothing_is_missing():
            return "Nada"

        steps = self._get_steps()
        step_index = 1
        while is_missing_step := steps.get(step_index):
            if is_missing_step():
                return self._steps_labels.get(step_index)
            step_index += 1
        return "Nada"

