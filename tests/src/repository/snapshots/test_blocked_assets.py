from func.src.repository.snapshots.blocked_assets import BlockedAssetsSnapshotRepository


dummy_user = {}
expected_fields = "Ativo", "Preço Médio", "Quantidade"


def test_snapshot():
    response = BlockedAssetsSnapshotRepository.snapshot(dummy_user)
    for row in response:
        assert all((field in row.keys() for field in expected_fields))
