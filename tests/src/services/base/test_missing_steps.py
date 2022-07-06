from unittest.mock import MagicMock

from func.src.services.base.missing_steps import BaseGetMissingStep

fake_get_missing_step = MagicMock()
missing_step = MagicMock(return_value=True)
complete_step = MagicMock(return_value=False)
nothing_response = "Nada"

first_step_missing = {
    1: missing_step,
    2: complete_step,
    3: complete_step,
    4: complete_step,
}

second_step_missing = {
    1: complete_step,
    2: missing_step,
    3: complete_step,
    4: complete_step,
}

last_step_missing = {
    1: complete_step,
    2: complete_step,
    3: complete_step,
    4: missing_step,
}

no_step_missing = {
    1: complete_step,
    2: complete_step,
    3: complete_step,
    4: complete_step,
}


def test_get_missing_step_nothing_missing():
    fake_get_missing_step._nothing_is_missing.return_value = True
    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_not_called()
    fake_get_missing_step._get_steps.assert_not_called()
    assert response == nothing_response


def test_get_missing_step_empty_steps():
    fake_get_missing_step._nothing_is_missing.return_value = False
    fake_get_missing_step._get_steps.return_value = {}

    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_not_called()
    fake_get_missing_step._get_steps.assert_called_with()
    complete_step.assert_not_called()
    missing_step.assert_not_called()
    assert response == nothing_response


dummy_step_label = "Dummy"


def test_get_missing_step_no_missing():
    fake_get_missing_step._get_steps.return_value = no_step_missing
    fake_get_missing_step._nothing_is_missing.return_value = False

    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_not_called()
    fake_get_missing_step._get_steps.assert_called_with()
    complete_step.assert_called_with()
    missing_step.assert_not_called()
    assert response == nothing_response


def test_get_missing_step_first():
    fake_get_missing_step._nothing_is_missing.return_value = False
    fake_get_missing_step._get_steps.return_value = first_step_missing
    fake_get_missing_step._steps_labels.get.return_value = dummy_step_label

    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_called_with(1)
    fake_get_missing_step._get_steps.assert_called_with()
    missing_step.assert_called_with()
    assert response == dummy_step_label


def test_get_missing_step_second():
    fake_get_missing_step._nothing_is_missing.return_value = False
    fake_get_missing_step._get_steps.return_value = second_step_missing
    fake_get_missing_step._steps_labels.get.return_value = dummy_step_label

    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_called_with(2)
    fake_get_missing_step._get_steps.assert_called_with()
    missing_step.assert_called_with()
    complete_step.assert_called_with()
    assert response == dummy_step_label


def test_get_missing_step_last():
    fake_get_missing_step._nothing_is_missing.return_value = False
    fake_get_missing_step._get_steps.return_value = last_step_missing
    fake_get_missing_step._steps_labels.get.return_value = dummy_step_label

    response = BaseGetMissingStep.get_missing_step(fake_get_missing_step)
    fake_get_missing_step._steps_labels.get.assert_called_with(4)
    fake_get_missing_step._get_steps.assert_called_with()
    missing_step.assert_called_with()
    complete_step.assert_called_with()
    assert response == dummy_step_label
