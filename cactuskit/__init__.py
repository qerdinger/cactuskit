"""
The Cactus Library

Licensed under MIT - qerdinger @ 2026
Hosted on GitHub : https://github.com/qerdinger/cactuskit

As a matter of fact, the "cactuize" decorator name comes from an inspiration of @khalidbelk (https://github.com/khalidbelk)
"""

from .cactuskit import (
	ApiMethod,
	ApiProtocol,
	CactusEncoder,
	CactusResponse,
	HttpStatus,
	cactuize,
	make_res,
)

__all__ = [
	"ApiMethod",
	"ApiProtocol",
	"CactusEncoder",
	"CactusResponse",
	"HttpStatus",
	"cactuize",
	"make_res",
]
