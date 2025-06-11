import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { Node, Edge } from 'react-flow-renderer'

interface GraphState {
  nodes: Node[]
  edges: Edge[]
  selectedElements: { nodes: string[]; edges: string[] }
  layout: {
    type: 'force' | 'dagre' | 'circular'
    options: Record<string, any>
  }
  viewport: {
    x: number
    y: number
    zoom: number
  }
}

const initialState: GraphState = {
  nodes: [],
  edges: [],
  selectedElements: { nodes: [], edges: [] },
  layout: {
    type: 'force',
    options: {
      nodeSpacing: 100,
      rankSpacing: 100,
    },
  },
  viewport: {
    x: 0,
    y: 0,
    zoom: 1,
  },
}

const graphSlice = createSlice({
  name: 'graph',
  initialState,
  reducers: {
    setNodes: (state, action: PayloadAction<Node[]>) => {
      state.nodes = action.payload
    },
    setEdges: (state, action: PayloadAction<Edge[]>) => {
      state.edges = action.payload
    },
    addNode: (state, action: PayloadAction<Node>) => {
      state.nodes.push(action.payload)
    },
    addEdge: (state, action: PayloadAction<Edge>) => {
      state.edges.push(action.payload)
    },
    removeNode: (state, action: PayloadAction<string>) => {
      state.nodes = state.nodes.filter((node) => node.id !== action.payload)
      state.edges = state.edges.filter(
        (edge) => edge.source !== action.payload && edge.target !== action.payload
      )
    },
    removeEdge: (state, action: PayloadAction<string>) => {
      state.edges = state.edges.filter((edge) => edge.id !== action.payload)
    },
    setSelectedElements: (
      state,
      action: PayloadAction<{ nodes: string[]; edges: string[] }>
    ) => {
      state.selectedElements = action.payload
    },
    setLayout: (
      state,
      action: PayloadAction<{
        type: GraphState['layout']['type']
        options?: Record<string, any>
      }>
    ) => {
      state.layout = {
        ...state.layout,
        ...action.payload,
      }
    },
    setViewport: (state, action: PayloadAction<Partial<GraphState['viewport']>>) => {
      state.viewport = {
        ...state.viewport,
        ...action.payload,
      }
    },
    resetGraph: (state) => {
      state.nodes = []
      state.edges = []
      state.selectedElements = { nodes: [], edges: [] }
      state.viewport = initialState.viewport
    },
  },
})

export const {
  setNodes,
  setEdges,
  addNode,
  addEdge,
  removeNode,
  removeEdge,
  setSelectedElements,
  setLayout,
  setViewport,
  resetGraph,
} = graphSlice.actions

export const graphReducer = graphSlice.reducer 