from func.src.domain.validator import BlockSummary, Asset
from func.src.services.blocks.service import BlockService

dummy_user_data = {}
expected_block_summary = BlockSummary(
    block_type="Pendente de Definição",
    description="Pendente de Definição",
    date="Pendente de Definição",
    lawsuit_number="Pendente de Definição",
)


def test_get_block_summary():
    response = BlockService.get_block_summary(dummy_user_data)
    assert response == expected_block_summary


expected_blocked_wallet = [Asset(
    ticker="Pendente de Definição",
    mean_price="Pendente de Definição",
    initial_quantity=10,
    current_quantity=100,
    spent_value=154.50,
    current_value="Pendente de Definição",
), Asset(
    ticker="Pendente de Definição",
    mean_price="Pendente de Definição",
    initial_quantity=10,
    current_quantity=100,
    spent_value=154.50,
    current_value="Pendente de Definição",
)]


def test_get_blocked_wallet():
    response = BlockService.get_blocked_wallet(dummy_user_data)
    assert response == expected_blocked_wallet
