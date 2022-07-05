import pytest

from func.src.domain.models.snapshots.onboarding import Onboarding

dummy_user = {}
dummy_missed_step_br = "Missed Step BR"
dummy_missed_step_us = "Missed Step Us"
dummy_date_of_missed_steps_br = "??/??/????"
dummy_date_of_missed_steps_us = "??/??/????"


@pytest.fixture()
def fake_onboarding_model():
    return Onboarding(
        dummy_missed_step_br,
        dummy_date_of_missed_steps_br,
        dummy_missed_step_us,
        dummy_date_of_missed_steps_us
    )


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
