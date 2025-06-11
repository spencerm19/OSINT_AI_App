import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit'

interface Research {
  id: number
  title: string
  description: string | null
  tags: string[]
  created_at: string
  updated_at: string
}

interface ResearchState {
  items: Research[]
  selectedId: number | null
  loading: boolean
  error: string | null
}

const initialState: ResearchState = {
  items: [],
  selectedId: null,
  loading: false,
  error: null,
}

// Async thunks
export const fetchResearch = createAsyncThunk(
  'research/fetchResearch',
  async () => {
    const response = await fetch('http://localhost:8000/api/v1/research')
    const data = await response.json()
    return data
  }
)

export const createResearch = createAsyncThunk(
  'research/createResearch',
  async (research: Omit<Research, 'id' | 'created_at' | 'updated_at'>) => {
    const response = await fetch('http://localhost:8000/api/v1/research', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(research),
    })
    const data = await response.json()
    return data
  }
)

const researchSlice = createSlice({
  name: 'research',
  initialState,
  reducers: {
    setSelectedResearch: (state, action: PayloadAction<number | null>) => {
      state.selectedId = action.payload
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchResearch.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchResearch.fulfilled, (state, action) => {
        state.loading = false
        state.items = action.payload
      })
      .addCase(fetchResearch.rejected, (state, action) => {
        state.loading = false
        state.error = action.error.message || 'Failed to fetch research'
      })
      .addCase(createResearch.fulfilled, (state, action) => {
        state.items.push(action.payload)
      })
  },
})

export const { setSelectedResearch } = researchSlice.actions
export const researchReducer = researchSlice.reducer 