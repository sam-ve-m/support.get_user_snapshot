class BlockedAssetsSnapshotRepository:
    @staticmethod
    def snapshot(user_data: dict) -> list:
        blocks = [{"Ativo": None, "Preço Médio": None, "Quantidade": None}]*3
        return blocks
