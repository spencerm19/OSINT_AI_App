import { configureStore } from '@reduxjs/toolkit'
import { graphReducer } from './features/graph/graphSlice'
import { researchReducer } from './features/research/researchSlice'
import { uiReducer } from './features/ui/uiSlice'

export const store = configureStore({
  reducer: {
    graph: graphReducer,
    research: researchReducer,
    ui: uiReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch 