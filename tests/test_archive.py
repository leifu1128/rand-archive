import os

import rand_archive as ra
import pytest


def test_archive_double_flush():
    writer = ra.ArchiveWriter(
        'cache/test_pyarchive_double_flush.raa',
        100
    )
    writer.write('dummy', bytes(101))
    writer.write('dummy2', bytes(101))
    writer.close()

    header = ra.Header.read('cache/test_pyarchive_double_flush.raa').inner()
    assert len(header) == 2
    assert 'dummy' in header
    assert 'dummy2' in header
    assert header['dummy'] == {'start': 0, 'end': 101}
    assert header['dummy2'] == {'start': 101, 'end': 202}

    os.remove('cache/test_pyarchive_double_flush.raa')