# Copyright 2016-2023 Geoffrey R. Scheller
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

"""Recursive function module.

* function ackermann_list: eval Ackermann's function simulating recursion with a list
"""

# Computable but not primitively recursive functions

from __future__ import annotations

__all__ = ['ackermann_list']

def ackermann_list(m: int, n:int) -> int:
    """Ackermann function is defined recursively by:

    ```
       ackermann(0,n) = n+1
       ackermann(m,0) = ackermann(m-1,1)
       ackermann(m,n) = ackermann(m-1, ackermann(m, n-1)) for n,m > 0
    ```
    Ackermann's function is an example of a function that is computable
    but not primitively recursive. It quickly becomes computationally
    intractable for relatively small values of `m`.
    """
    # Model a function stack with a list, then
    # evaluate innermost ackermann function first.
    acker = [m, n]

    while len(acker) > 1:
        mm, nn = acker[-2:]
        if mm < 1:
            acker[-1] = acker.pop() + 1
        elif nn < 1:
            acker[-2] = acker[-2] - 1
            acker[-1] = 1
        else:
            acker[-2] = mm - 1
            acker[-1] = mm
            acker.append(nn-1)

    return acker[0]
