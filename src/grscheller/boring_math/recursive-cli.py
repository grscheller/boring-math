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

"""Entry points for grscheller.boring_math.integer_math cli scripts.

Supports automatically generated OS independent CLI scripts.
"""

from __future__ import annotations

__all__ = ['ackermann_cli']
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2023-2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"

import sys
from grscheller.boring_math.recursive import ackermann

# Computable but not primitive recursive functions scripts

def ackermann_cli() -> None:
    """Ackermann function is defined recursively by:

        ackermann(0,n) = n+1
        ackermann(m,0) = ackermann(m-1,1)
        ackermann(m,n) = ackermann(m-1, ackermann(m, n-1)) for n,m > 0

    Usage: ackermann.py m n
    """
    # Argument parsing and checking
    args = sys.argv[1:]
    if len(args) == 2:
        try:
            m = int(args[0])
            n = int(args[1])
            if m < 0 or n < 0:
                print("Error: Negative integer argument given" , file=sys.stderr)
                sys.exit(1)
        except ValueError:
            print("Error: Non-integer argument given", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: ackermann.py takes 2 arguments", file=sys.stderr)
        sys.exit(1)

    # Compute value
    print(ackermann(m, n))