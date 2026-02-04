import os
import re
from importlib.resources import files
from pathlib import Path


def _collect_files(ext: str):
    ext = ext.lower()
    root = files(__name__)

    def walk(trav):
        for p in trav.iterdir():
            if p.is_dir():
                yield from walk(p)
            else:
                name = p.name
                if name.lower().endswith(ext):
                    stem = name[:-len(ext)]
                    if "_temp" not in stem:
                        yield Path(p).resolve()  # full path

    return sorted(set(walk(root)))


def _safe_attr(name: str) -> str:
    # make a valid python identifier for attribute access
    base = os.path.splitext(os.path.basename(name))[0]
    base = re.sub(r"\W+", "_", base)          # replace non-word chars
    if not base:
        base = "file"
    if base[0].isdigit():
        base = "_" + base
    return base


class NetIndex(dict):
    """dict + attribute access for network file paths."""
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            raise AttributeError(item) from e

    def __repr__(self):
        keys = ", ".join(list(self.keys())[:8])
        more = "..." if len(self) > 8 else ""
        return f"NetIndex({len(self)} files: {keys}{more})"


def inp_files():
    paths = _collect_files(".inp")
    m = NetIndex()

    for rel in paths:
        # allow nets["Net2.inp"] exact
        m[os.path.basename(rel)] = rel

        # allow nets["Net2"] and nets.Net2
        key = os.path.splitext(os.path.basename(rel))[0]
        m[key] = rel

        # also safe attribute alias (in case of weird names)
        m[_safe_attr(os.path.basename(rel))] = rel

    return m


def msx_files():
    paths = _collect_files(".msx")
    m = NetIndex()

    for rel in paths:
        m[os.path.basename(rel)] = rel
        key = os.path.splitext(os.path.basename(rel))[0]
        m[key] = rel
        m[_safe_attr(os.path.basename(rel))] = rel

    return m
