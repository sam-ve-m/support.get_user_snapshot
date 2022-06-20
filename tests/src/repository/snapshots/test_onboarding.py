from unittest.mock import MagicMock
from func.src.repository.snapshots.onboarding import OnboardingSnapshotRepository

dummy_onboarding = MagicMock()
expected_fields = "Campo", "BR"


def test_snapshot():
    response = OnboardingSnapshotRepository.snapshot(dummy_onboarding)
    for row in response:
        assert all((field in row.keys() for field in expected_fields))
    assert response[0].get("Campo") == "Faltou fazer"
    assert response[1].get("Campo") == "Data da Ultima"
