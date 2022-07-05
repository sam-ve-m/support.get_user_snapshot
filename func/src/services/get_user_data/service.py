from func.src.repository.user.repository import UserRepository


class GetUserDataService:
    @staticmethod
    def get_user_data(decoded_jwt) -> dict:
        unique_id = decoded_jwt.get("user").get("unique_id")
        if not (user_data := UserRepository.find_user_by_unique_id(unique_id=unique_id)):
            raise ValueError("Unable to find user")
        return user_data
