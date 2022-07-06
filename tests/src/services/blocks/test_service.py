from func.src.domain.validator import BlockSummary, Asset, WarrantySummary
from func.src.services.warranty.service import WarrantyService

dummy_user_data = {}
expected_warranty_summary = WarrantySummary(
    available="Pendente de Definição",
)


def test_get_warranty_summary():
    response = WarrantyService.get_warranty_summary(dummy_user_data)
    assert response == expected_warranty_summary


expected_warrantyed_wallet = [Asset(
    ticker="Pendente de Definição",
    mean_price=15.45,
    initial_quantity=10,
    current_quantity="Pendente de Definição",
    spent_value=154.50,
    current_value="Pendente de Definição",
), Asset(
    ticker="Pendente de Definição",
    mean_price=15.45,
    initial_quantity=10,
    current_quantity="Pendente de Definição",
    spent_value=154.50,
    current_value="Pendente de Definição",
)]


def test_get_warrantyed_wallet():
    response = WarrantyService.get_warrantyed_wallet(dummy_user_data)
    assert response == expected_warrantyed_wallet
