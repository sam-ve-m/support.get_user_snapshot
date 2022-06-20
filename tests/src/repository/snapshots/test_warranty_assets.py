from func.src.repository.snapshots.warranty_assets import WarrantySnapshotRepository

dummy_user = {}
expected_fields = "Disponível em Garantia",


def test_snapshot():
    response = WarrantySnapshotRepository.snapshot(dummy_user)
    assert all((field in response.keys() for field in expected_fields))

