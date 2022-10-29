from manager.crud.checker import create_checkin, get_checkin
import datetime

from manager.schema.checkbook import CheckBookCreate


def test_create_checkin(db, checkbook):

    checkin = create_checkin(
        db=db,
        checkin=checkbook
    )

    assert checkin.name == "blackprince"
    assert checkin.checkin_start - checkin.checkin_end == datetime.timedelta(
        hours=2, seconds=30
    )


def test_get_worker(db, worker):
    checkin = get_checkin(db, name="blackprince")

    assert checkin.name == "blackprince"
