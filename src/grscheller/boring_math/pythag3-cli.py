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

"""Entry points for grscheller.boring_math pythag3 cli script.

The pythag3 script is automatically generated in an OS independent way via
the [project.scripts] section of pyproject.toml.
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
    """Print all possible primative pythagorian triples satifying input
    parameters.

    A pythagorian triple are three integers (a, b, c) such
    that a^2 + b^2 = c^2 where a, b, c > 0 and gcd(a, b, c) = 1

    Usage: pythag3.py [n1 [n2 [n3]]]

      where

      3 arguments print all triples with n1 <= a <= n2 and a,b,c <= n3
      2 arguments print all triples with n1 <= a <= n2
      1 argument prints all triples with a <= n1
      0 arguments print all triples with 3 <= a <= 100
    """
    pythag3 = Pythag3()

    args = sys.argv[1:]

    if len(args) > 2:
        pythagTriples = pythag3.triples(a_start = int(args[0]),
                                          a_max = int(args[1]),
                                            max = int(args[2]))
    elif len(args) == 2:
        pythagTriples = pythag3.triples(a_start = int(args[0]),
                                          a_max = int(args[1]))
    elif leng(args) == 1:
        pythagTriples = pythag3.triples(a_start = 3, a_max = int(args[0]))
    else:
        pythagTriples = pythag3.triples(a_start = 3, a_max = 100)

    # Print out Pythagean Triples
    for triple in pythagTriples:
        print(triple)
