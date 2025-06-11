'use client'

import { useCallback } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  Node,
  Edge,
  Connection,
} from 'react-flow-renderer'
import { RootState } from '@/lib/store'
import {
  addNode,
  addEdge,
  removeNode,
  removeEdge,
  setSelectedElements,
} from '@/lib/features/graph/graphSlice'

const nodeTypes = {
  // Custom node types will be defined here
}

export function GraphView() {
  const dispatch = useDispatch()
  const { nodes, edges, selectedElements, viewport } = useSelector(
    (state: RootState) => state.graph
  )

  const onNodesChange = useCallback(
    (changes: any[]) => {
      // Handle node changes (position, selection, etc.)
      const selectedNodes = changes
        .filter((change) => change.selected)
        .map((change) => change.id)
      dispatch(
        setSelectedElements({
          ...selectedElements,
          nodes: selectedNodes,
        })
      )
    },
    [dispatch, selectedElements]
  )

  const onEdgesChange = useCallback(
    (changes: any[]) => {
      // Handle edge changes (selection, etc.)
      const selectedEdges = changes
        .filter((change) => change.selected)
        .map((change) => change.id)
      dispatch(
        setSelectedElements({
          ...selectedElements,
          edges: selectedEdges,
        })
      )
    },
    [dispatch, selectedElements]
  )

  const onConnect = useCallback(
    (connection: Connection) => {
      dispatch(
        addEdge({
          id: `e${connection.source}-${connection.target}`,
          ...connection,
        })
      )
    },
    [dispatch]
  )

  const onNodeDelete = useCallback(
    (nodes: Node[]) => {
      nodes.forEach((node) => dispatch(removeNode(node.id)))
    },
    [dispatch]
  )

  const onEdgeDelete = useCallback(
    (edges: Edge[]) => {
      edges.forEach((edge) => dispatch(removeEdge(edge.id)))
    },
    [dispatch]
  )

  return (
    <div className="w-full h-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodesDelete={onNodeDelete}
        onEdgesDelete={onEdgeDelete}
        nodeTypes={nodeTypes}
        fitView
        className="bg-background"
      >
        <Background />
        <Controls />
        <MiniMap />
      </ReactFlow>
    </div>
  )
} 