'use client'

import { Panel as ReactFlowPanel } from 'reactflow'
import { Button } from './ui/button'
import { useDispatch } from 'react-redux'
import { clearGraph } from '@/lib/features/graph/graphSlice'
import { 
  ZoomIn, 
  ZoomOut, 
  Maximize2, 
  Trash2,
  Save,
  Download
} from 'lucide-react'

export function Panel() {
  const dispatch = useDispatch()

  const handleClear = () => {
    if (confirm('Are you sure you want to clear the graph?')) {
      dispatch(clearGraph())
    }
  }

  const handleSave = () => {
    // Implement save functionality
  }

  const handleExport = () => {
    // Implement export functionality
  }

  return (
    <ReactFlowPanel position="top-right" className="bg-card p-2 rounded-lg shadow-lg">
      <div className="flex flex-col gap-2">
        <Button variant="ghost" size="icon" title="Zoom In">
          <ZoomIn className="h-4 w-4" />
        </Button>
        <Button variant="ghost" size="icon" title="Zoom Out">
          <ZoomOut className="h-4 w-4" />
        </Button>
        <Button variant="ghost" size="icon" title="Fit View">
          <Maximize2 className="h-4 w-4" />
        </Button>
        <div className="h-px bg-border my-2" />
        <Button variant="ghost" size="icon" title="Save Graph" onClick={handleSave}>
          <Save className="h-4 w-4" />
        </Button>
        <Button variant="ghost" size="icon" title="Export Graph" onClick={handleExport}>
          <Download className="h-4 w-4" />
        </Button>
        <Button variant="ghost" size="icon" title="Clear Graph" onClick={handleClear}>
          <Trash2 className="h-4 w-4" />
        </Button>
      </div>
    </ReactFlowPanel>
  )
} 