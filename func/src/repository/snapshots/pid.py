class PIDSnapshotRepository:
    NOT_FOUND_MESSAGE = "Não encontrado"

    @classmethod
    def snapshot(cls, user_data: dict) -> dict:
        pid = {}
        cls._set_email_in_snapshot(pid, "Email", user_data)
        cls._set_telefone_in_snapshot(pid, "Telefone", user_data)
        cls._set_cpf_in_snapshot(pid, "Cpf", user_data)
        cls._set_data_nascimento_in_snapshot(pid, "Data Nascimento", user_data)
        cls._set_possui_vai_na_cola_in_snapshot(pid, "Possui Vai na Cola?", user_data)
        cls._set_rg_in_snapshot(pid, "RG", user_data)
        cls._set_nome_da_mae_in_snapshot(pid, "Nome da Mãe", user_data)
        cls._set_cep_in_snapshot(pid, "CEP", user_data)
        return pid

    @staticmethod
    def _set_email_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        if email := user_data.get("email"):
            snapshot.update({field_label: email})
        else:
            raise Exception("This field is required")

    @staticmethod
    def _set_telefone_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        telefone = user_data.get("cel_phone") or PIDSnapshotRepository.NOT_FOUND_MESSAGE
        snapshot.update({field_label: telefone})

    @staticmethod
    def _set_cpf_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        if cpf := user_data.get("identifier_document").get("cpf"):
            snapshot.update({field_label: cpf})
        else:
            raise Exception("This field is required")

    @staticmethod
    def _set_data_nascimento_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        data_nascimento = user_data.get("birth_date") or PIDSnapshotRepository.NOT_FOUND_MESSAGE
        snapshot.update({field_label: data_nascimento})

    @staticmethod
    def _set_possui_vai_na_cola_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        possui_vai_na_cola = bool(user_data.get("portfolios", {}).get("vnc", {}).get("br"))
        snapshot.update({field_label: possui_vai_na_cola})

    @staticmethod
    def _set_rg_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        rg = user_data.get("identifier_document", {}).get("document_data", {}).get("number") or PIDSnapshotRepository.NOT_FOUND_MESSAGE
        snapshot.update({field_label: rg})

    @staticmethod
    def _set_nome_da_mae_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        nome_da_mae = user_data.get("mother_name") or PIDSnapshotRepository.NOT_FOUND_MESSAGE
        snapshot.update({field_label: nome_da_mae})

    @staticmethod
    def _set_cep_in_snapshot(snapshot: dict, field_label: str, user_data: dict):
        cep = user_data.get("address", {}).get("zip_code") or PIDSnapshotRepository.NOT_FOUND_MESSAGE
        snapshot.update({field_label: cep})
