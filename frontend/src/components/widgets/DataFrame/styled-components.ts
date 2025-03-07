/**
 * @license
 * Copyright 2018-2022 Streamlit Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import styled from "@emotion/styled"

interface StyledResizableContainerProps {
  width?: number
  height: number
  maxWidth: number
  minWidth: number
  minHeight: number
  maxHeight: number
}

/**
 * A resizable data grid container component.
 */
export const StyledResizableContainer = styled.div<
  StyledResizableContainerProps
>(({ theme, width, height, minHeight, maxHeight, minWidth, maxWidth }) => ({
  overflow: "auto",
  position: "relative",
  resize: "both",
  display: "inline-block",
  ...(width && { width: `${width}px` }),
  minHeight: `${minHeight}px`,
  maxHeight: `${maxHeight}px`,
  minWidth: `${minWidth}px`,
  maxWidth: `${maxWidth}px`,
  height: `${height}px`,
  border: `1px solid ${theme.colors.fadedText05}`,
  marginTop: theme.spacing.md,

  "> div": {
    height: "100%",
    minWidth: "100%",
  },

  "& .dvn-scroller": {
    scrollbarWidth: "thin",
    ["overflowX" as any]: "overlay !important",
    ["overflowY" as any]: "overlay !important",
  },

  // Hide the resize handle in the right corner. Resizing is still be possible.
  "&::-webkit-resizer": {
    display: "none",
  },
}))
