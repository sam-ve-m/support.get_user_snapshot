from func.src.domain.models.snapshots.warranty import Warranty
from unittest.mock import patch
import pytest

dummy_user = {}
dummy_missed_step_br = "Missed Step BR"
dummy_missed_step_us = "Missed Step Us"


@pytest.fixture()
def fake_warranty_model():
    return Warranty(dummy_user)


expected_snapshot = [{'value': 'Pendente de Definição', 'label': 'Disponível em Garantia'}]


def test_get_snapshot(fake_warranty_model):
    snapshot = fake_warranty_model.get_snapshot()
    assert expected_snapshot == snapshot

