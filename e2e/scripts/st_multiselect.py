# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, List

import streamlit as st
from enum import Enum


class Colors(Enum):
    yellow = 1
    blue = 2


class Shake(Enum):
    VANILLA = "VANILLA"
    CHOCOLATE = "CHOCOLATE"
    COOKIES = "COOKIES"
    MINT = "MINT"


options = ("male", "female")

i1 = st.multiselect("multiselect 1", options)
st.text("value 1: %s" % i1)

i2 = st.multiselect("multiselect 2", options, format_func=lambda x: x.capitalize())
st.text("value 2: %s" % i2)

i3: List[Any] = st.multiselect("multiselect 3", [])
st.text("value 3: %s" % i3)

i4 = st.multiselect("multiselect 4", ["coffee", "tea", "water"], ["tea", "water"])
st.text("value 4: %s" % i4)

i5 = st.multiselect(
    "multiselect 5",
    list(
        map(
            lambda x: f"{x} I am a ridiculously long string to have in a multiselect, so perhaps I should just not wrap and go to the next line.",
            range(5),
        )
    ),
)
st.text("value 5: %s" % i5)

i6 = st.multiselect("multiselect 6", options, disabled=True)
st.text("value 6: %s" % i6)


i7 = st.multiselect("choose colors", list(Colors), Colors.yellow)
st.text("value 7: %s" % i7)

i8 = st.multiselect("choose shakes", list(Shake), Shake.CHOCOLATE)
st.text("value 8: %s" % i8)

if st._is_running_with_streamlit:

    def on_change():
        st.session_state.multiselect_changed = True

    st.multiselect("multiselect 9", options, key="multiselect9", on_change=on_change)
    st.text("value 9: %s" % st.session_state.multiselect9)
    st.text(f"multiselect changed: {'multiselect_changed' in st.session_state}")
