from manager.crud.worker import create_worker, get_worker


def test_create_worker(db, worker):
    worker = create_worker(db=db, worker=worker)

    assert worker.name == "blackprince"


def test_get_worker(db, worker):
    worker = get_worker(db=db, name="blackprince")

    assert worker.name == "blackprince"
