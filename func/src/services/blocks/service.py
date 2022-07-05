from func.src.domain.validator import Wallet, BlockSummary, Asset


class BlockService:

    @classmethod
    def request_block_summary(cls, user_data: dict) -> BlockSummary:
        block_summary = BlockSummary(
            block_type="Pendente de Definição",
            description="Pendente de Definição",
            date="Pendente de Definição",
            lawsuit_number="Pendente de Definição",
        )
        return block_summary

    @classmethod
    def request_blocked_wallet(cls, user_data: dict) -> Wallet:
        blocked_wallet = [Asset(
            ticker="Pendente de Definição",
            mean_price="Pendente de Definição",
            initial_quantity=10,
            current_quantity=100,
            spent_value=154.50,
            current_value="Pendente de Definição",
        )]*2
        return blocked_wallet
