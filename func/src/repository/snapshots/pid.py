class PIDSnapshotRepository:
    NOT_FOUND_MESSAGE = "Não encontrado"

    @staticmethod
    def snapshot(user_data: dict) -> dict:
        pid = {
            "Email": user_data.get("email"),
            "Telefone": user_data.get("cel_phone", PIDSnapshotRepository.NOT_FOUND_MESSAGE),
            "Cpf": user_data.get("identifier_document").get("cpf"),
            "Data Nascimento": user_data.get("birth_date", PIDSnapshotRepository.NOT_FOUND_MESSAGE),
            "Possui Vai na Cola?": bool(user_data.get("portfolios", {}).get("vnc", {}).get("br")),
            "RG": user_data.get("identifier_document", {}).get("document_data", {}).get("number", PIDSnapshotRepository.NOT_FOUND_MESSAGE),
            "Nome da Mãe": user_data.get("mother_name", PIDSnapshotRepository.NOT_FOUND_MESSAGE),
            "CEP": user_data.get("address", {}).get("zip_code", PIDSnapshotRepository.NOT_FOUND_MESSAGE),
        }
        return pid
