# Stubs for io

# Based on https://docs.python.org/2/library/io.html

# Only a subset of functionality is included.

from typing import List, BinaryIO, TextIO, IO, overload, Iterator, Iterable, Any, Union, Optional
import _io

from _io import BlockingIOError as BlockingIOError
from _io import BufferedRWPair as BufferedRWPair
from _io import BufferedRandom as BufferedRandom
from _io import BufferedReader as BufferedReader
from _io import BufferedWriter as BufferedWriter
from _io import BytesIO as BytesIO
from _io import DEFAULT_BUFFER_SIZE as DEFAULT_BUFFER_SIZE
from _io import FileIO as FileIO
from _io import IncrementalNewlineDecoder as IncrementalNewlineDecoder
from _io import StringIO as StringIO
from _io import TextIOWrapper as TextIOWrapper
from _io import UnsupportedOperation as UnsupportedOperation
from _io import open as open

def _OpenWrapper(file: Union[str, unicode, int],
         mode: unicode = ..., buffering: int = ..., encoding: unicode = ...,
         errors: unicode = ..., newline: unicode = ...,
         closefd: bool = ...) -> IO[Any]: ...

SEEK_SET = ...  # type: int
SEEK_CUR = ...  # type: int
SEEK_END = ...  # type: int


class IOBase(_io._IOBase): ...

class RawIOBase(_io._RawIOBase, IOBase):
    pass

class BufferedIOBase(_io._BufferedIOBase, IOBase):
    pass

class TextIOBase(_io._TextIOBase, IOBase):  # type: ignore
    pass
