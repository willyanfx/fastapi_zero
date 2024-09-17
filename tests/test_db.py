from sqlalchemy import select

from app.models import User


def test_create_user(session):
    new_user = User(
        username='marina',
        email='marina@gmail.com',
        password='minha-senha-legal',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'marina'))

    assert user.username == 'marina'
