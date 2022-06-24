class PID:
    NOT_FOUND_MESSAGE = "Não encontrado"

    def __init__(self, user_data: dict):
        self.__email = self.__set_email_in_snapshot(user_data)
        self.__cellphone = user_data.get("cel_phone") or self.NOT_FOUND_MESSAGE
        self.__cpf = self.__set_cpf_in_snapshot(user_data)
        self.__birth_date = user_data.get("birth_date") or self.NOT_FOUND_MESSAGE
        self.__has_vai_na_cola = bool(user_data.get("portfolios", {}).get("vnc", {}).get("br"))
        self.__rg = user_data.get("identifier_document", {}).get("document_data", {}).get("number") or self.NOT_FOUND_MESSAGE
        self.__mothers_name = user_data.get("mother_name") or self.NOT_FOUND_MESSAGE
        self.__cep = user_data.get("address", {}).get("zip_code") or self.NOT_FOUND_MESSAGE

    @staticmethod
    def __set_email_in_snapshot(user_data: dict) -> str:
        if not (email := user_data.get("email")):
            raise Exception("This field is required")
        return email

    @staticmethod
    def __set_cpf_in_snapshot(user_data: dict) -> str:
        if not (cpf := user_data.get("identifier_document").get("cpf")):
            raise Exception("This field is required")
        return cpf

    def get_snapshot(self) -> list:
        snapshot = [
            {"value": self.__email, "label": "Email"},
            {"value": self.__cellphone, "label": "Telefone"},
            {"value": self.__cpf, "label": "Cpf"},
            {"value": self.__birth_date, "label": "Data Nascimento"},
            {"value": self.__has_vai_na_cola, "label": "Possui Vai na Cola?"},
            {"value": self.__rg, "label": "RG"},
            {"value": self.__mothers_name, "label": "Nome da Mãe"},
            {"value": self.__cep, "label": "CEP"},
        ]
        return snapshot
