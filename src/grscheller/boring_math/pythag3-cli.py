# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Entry points for grscheller.boring_math.pythag3 cli script.

Supports automatically generated OS independent CLI scripts.
"""

from __future__ import annotations

__all__ = ['pythag3_cli']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

import sys
from grscheller.boring_math.pythag3 import Pythag3

# Pythagorean Triples generator script

def pythag3_cli() -> None:
    """Find all primative pythagorian triples up to a given level.

    A pythagorian triple are three integers (a,b,c) such
    that a^2 + b^2 = c^2 where x,y,z > 0 and gcd(a,b,c) = 1

    Usage: pythag3.py n [m]

    Two arguments generate all triples with a <= n and a,b,c <= m
    One argument generates all triples with a <= n
    No arguments generates all triples with 3 <= a <= 100
    """
    pythag3 = Pythag3()

    # Argument processing with some idiot checking
    args = sys.argv[1:]

    if len(args) > 1:
        pythagTriples = pythag3.triples(int(3, args[0]), int(args[1]))
    elif len(args) > 0:
        pythagTriples = pythag3.triples(3, int(args[0]))
    else:
        pythagTriples = pythag3.triples(3, 100)

    # Print out Pythagean Triples
    for triple in pythagTriples:
        print(triple)
