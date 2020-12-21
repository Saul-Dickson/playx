#!/usr/bin/env python3
"""It is an abstract module for searching songs"""

from playx.youtube import search_youtube


def search(song, disable_kw):
    """Search the song in youtube."""
    try:
        video = search_youtube(song, disable_kw)[0]
    except IndexError:
        return None
    return video
