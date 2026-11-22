from fastapi import APIRouter

from app.models.schemas import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    # Week 1: ingestion only. Retrieval and grounded answering arrive in Weeks 2-3,
    # so the honest answer for now is to abstain.
    return AskResponse(
        answer="Not implemented yet: retrieval is added in Week 2.",
        abstained=True,
    )


@router.get("/versions")
def versions() -> dict:
    return {"versions": ["v1", "v2"]}  # Placeholder until database-backed in Week 2.
