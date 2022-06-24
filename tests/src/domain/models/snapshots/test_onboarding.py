from func.src.domain.entity.onboarding_step_br import OnboardingBR
from func.src.domain.entity.onboarding_step_us import OnboardingUS
from func.src.domain.models.snapshots.onboarding import Onboarding
from unittest.mock import patch
import pytest

dummy_user = {}
dummy_missed_step_br = "Missed Step BR"
dummy_missed_step_us = "Missed Step Us"


@pytest.fixture()
def fake_onboarding_model():
    with patch.object(OnboardingBR, "find_missing_step", return_value=dummy_missed_step_br):
        with patch.object(OnboardingUS, "find_missing_step", return_value=dummy_missed_step_us):
            return Onboarding(dummy_user)


@patch.object(OnboardingBR, "find_missing_step")
@patch.object(OnboardingUS, "find_missing_step")
def test_model_instance(mocked_onboarding_us, mocked_onboarding_br):
    Onboarding(dummy_user)
    mocked_onboarding_br.assert_called_once_with(dummy_user)
    mocked_onboarding_us.assert_called_once_with(dummy_user)


expected_snapshot = [[
    {'value': 'Faltou fazer', 'label': 'Campo'},
    {'value': 'Missed Step BR', 'label': 'BR'},
    {'value': 'Missed Step Us', 'label': 'US'}
], [
    {'value': 'Data da Ultima', 'label': 'Campo'},
    {'value': '??/??/????', 'label': 'BR'},
    {'value': '??/??/????', 'label': 'US'}
]]


def test_get_snapshot(fake_onboarding_model):
    snapshot = fake_onboarding_model.get_snapshot()
    assert expected_snapshot == snapshot
