from manager.crud.checker import create_checkin, get_checkin
import datetime

from manager.schema.checkbook import CheckBookCreate


def test_create_checkin(db, checkbook):

    checkin = create_checkin(
        db=db,
        checkin=checkbook
    )

    assert checkin.name == "blackprince"



def test_get_worker(db, worker):
    checkin = get_checkin(db, name="blackprince")

    assert checkin.name == "blackprince"
