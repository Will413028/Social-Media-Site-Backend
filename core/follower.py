from fastapi import HTTPException, status
from database.models import Follower
from sqlalchemy.orm.session import Session


def create_follow(db: Session, followee_id: int, user_id: int):
    followee = db.query(Follower).filter(
        Follower.follower_id == user_id, Follower.followee_id == followee_id).first()

    if not followee:
        new_followee = Follower(
            follower_id=user_id,
            followee_id=followee_id
        )
        try:
            db.add(new_followee)
            db.commit()
            db.refresh(new_followee)
            return "Create follower successfully"
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    else:
        return "Already follow!"


def cancel_follow(db: Session, followee_id: int, user_id: int):
    followee = db.query(Follower).filter(
        Follower.follower_id == user_id, Follower.followee_id == followee_id).first()

    if not followee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'followee with followee_id {followee_id} not found')

    if followee.follower_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'You are not allowed to delete this followee')

    try:
        db.delete(followee)
        db.commit()
        return "Delete followee successfully"

    except Exception as e:
        db.rollback()
        raise Exception(str(e))
