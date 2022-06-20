from func.src.repository.snapshots.warranty import WarrantyAssetsSnapshotRepository

dummy_user = {}
expected_fields = "Ativo", "Valor", "Quantidade"


def test_snapshot():
    response = WarrantyAssetsSnapshotRepository.snapshot(dummy_user)
    for row in response:
        assert all((field in row.keys() for field in expected_fields))
