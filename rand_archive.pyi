from typing import Any, Tuple, Union

class Header:
    @classmethod
    def calc_header_size(cls, key_size: int, n_entries: int) -> int: ...
    @classmethod
    def load(cls, path: str) -> 'Header': ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> Tuple[int, int]: ...

class Writer:
    def __new__(cls, path: str, cache_size: int = 100 * 1024 * 1024, max_header_size: int = 1024 * 1024) -> 'Writer': ...
    @classmethod
    def load(cls, path: str, cache_size: int = 100 * 1024 * 1024) -> 'Writer': ...
    def write(self, key: str, value: bytes) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> 'Writer': ...
    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any) -> None: ...

class Reader:
    def __new__(cls) -> 'Reader': ...
    def open_file(self, path: str) -> 'Reader': ...
    def by_size(self, size: int) -> 'Reader': ...
    def by_count(self, count: int) -> 'Reader': ...
    def with_shuffling(self) -> 'Reader': ...
    def with_sharding(self, rank: int, world_size: int) -> 'Reader': ...
    def __iter__(self) -> 'EntryIter': ...

class EntryIter:
    def __iter__(self) -> 'EntryIter': ...
    def __next__(self) -> Union[None, Tuple[str, bytes]]: ...