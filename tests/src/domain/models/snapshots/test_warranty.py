from unittest.mock import MagicMock

import pytest

from func.src.domain.models.snapshots.warranty import Warranty

dummy_user = {}


@pytest.fixture()
def fake_warranty_model():
    return Warranty(MagicMock(available="Pendente de Definição"))


expected_snapshot = [{'value': 'Pendente de Definição', 'label': 'Disponível em Garantia'}]


def test_get_snapshot(fake_warranty_model):
    snapshot = fake_warranty_model.get_snapshot()
    assert expected_snapshot == snapshot

