from sqlalchemy import select

from app.models.pipeline import Pipeline
from app.repo.repo import SQLAlchemyRepo


class PipelineRepo(SQLAlchemyRepo):
    async def get_pipeline_by_id(self, pipeline_id: int) -> Pipeline | None:
        query = await self.session.scalars(
            select(Pipeline).where(Pipeline.id == pipeline_id)
        )
        return query.one() if query else None
