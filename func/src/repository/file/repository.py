from ...domain.enums import UserFileType
from ...infrastructure.bucket.infrastructure import BucketInfrastructure


class FileRepository:
    infra = BucketInfrastructure

    @classmethod
    async def user_file_exists(
        cls, file_type: UserFileType, unique_id: str, bucket_name: str
    ):
        prefix = cls._resolve_user_path(unique_id=unique_id, file_type=file_type)

        async with cls.infra.get_resource() as s3_resource:
            bucket = await s3_resource.Bucket(bucket_name)
            async for s3_object in bucket.objects.filter(Prefix=prefix):
                return True
        return False

    @staticmethod
    def _resolve_user_path(unique_id: str, file_type: UserFileType) -> str:
        return f"{unique_id}/{file_type.value}/"
