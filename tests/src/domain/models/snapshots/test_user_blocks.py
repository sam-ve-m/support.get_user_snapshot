from func.src.domain.models.snapshots.user_blocks import UserBlocks
from unittest.mock import patch, MagicMock
import pytest

dummy_user = MagicMock(
    block_type="Pendente de Definição",
    description="Pendente de Definição",
    date="Pendente de Definição",
    lawsuit_number="Pendente de Definição",
)
dummy_missed_step_br = "Missed Step BR"
dummy_missed_step_us = "Missed Step Us"


@pytest.fixture()
def fake_user_blocks_model():
    return UserBlocks(dummy_user)


expected_snapshot = [
    {'value': 'Pendente de Definição', 'label': 'Tipo de bloqueio'},
    {'value': 'Pendente de Definição', 'label': 'Descrição'},
    {'value': 'Pendente de Definição', 'label': 'Data e Hora'},
    {'value': 'Pendente de Definição', 'label': 'Numero do Processo (Caso bloqueio judicial)'}
]


def test_get_snapshot(fake_user_blocks_model):
    snapshot = fake_user_blocks_model.get_snapshot()
    assert expected_snapshot == snapshot
