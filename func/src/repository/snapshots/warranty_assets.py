class WarrantySnapshotRepository:
    _table_name = "Garantia"
    _table_color = "darkblue"

    @classmethod
    def snapshot(cls, user_data: dict) -> dict:
        warrant = {"Disponível em Garantia": None}
        return warrant
