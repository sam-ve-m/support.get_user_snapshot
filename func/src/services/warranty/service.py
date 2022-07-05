from func.src.domain.validator import Wallet, Asset, WarrantySummary


class WarrantyService:

    @classmethod
    def request_warranty_summary(cls, user_data: dict) -> WarrantySummary:
        warranty_summary = WarrantySummary(
            available="Pendente de Definição",
        )
        return warranty_summary

    @classmethod
    def request_warrantyed_wallet(cls, user_data: dict) -> Wallet:
        warrantyed_wallet = [Asset(
            ticker="Pendente de Definição",
            mean_price=15.45,
            initial_quantity=10,
            current_quantity="Pendente de Definição",
            spent_value=154.50,
            current_value="Pendente de Definição",
        )]*2
        return warrantyed_wallet
