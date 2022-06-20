from func.src.repository.snapshots.user_blocks import UserBlocksSnapshotRepository

dummy_user = {}
expected_fields = "Tipo de bloqueio", "Descrição", "Data e Hora", "Numero do Processo (Caso bloqueio judicial)"


def test_snapshot():
    response = UserBlocksSnapshotRepository.snapshot(dummy_user)
    assert all((field in response.keys() for field in expected_fields))
