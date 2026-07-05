"""Supported languages."""

from enum import Enum


class Language(str, Enum):

    ENGLISH = "English"

    HINDI = "Hindi"

    KANNADA = "Kannada"

    TAMIL = "Tamil"

    TELUGU = "Telugu"

    MALAYALAM = "Malayalam"