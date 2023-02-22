from fastapi import HTTPException, status
from database.models import Follower
from sqlalchemy.orm.session import Session


def create_follower(db: Session, follower_id: int, user_id: int):
    new_follower = Follower(
        follower_id = user_id,
        followee_id = follower_id
    )
    try:
        db.add(new_follower)
        db.commit()
        db.refresh(new_follower)
        return "Create follower successfully"
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
