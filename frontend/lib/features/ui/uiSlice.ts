import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface UiState {
  sidebarOpen: boolean
  theme: 'light' | 'dark' | 'system'
  loading: boolean
  error: string | null
}

const initialState: UiState = {
  sidebarOpen: true,
  theme: 'system',
  loading: false,
  error: null,
}

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    toggleSidebar: (state) => {
      state.sidebarOpen = !state.sidebarOpen
    },
    setTheme: (state, action: PayloadAction<'light' | 'dark' | 'system'>) => {
      state.theme = action.payload
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload
    },
  },
})

export const { toggleSidebar, setTheme, setLoading, setError } = uiSlice.actions
export const uiReducer = uiSlice.reducer 