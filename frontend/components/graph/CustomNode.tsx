'use client'

import { memo } from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { Card } from '../ui/card'
import { Badge } from '../ui/badge'

interface CustomNodeData {
  label: string
  type: string
  properties: Record<string, any>
  confidence?: number
}

function CustomNode({ data, selected }: NodeProps<CustomNodeData>) {
  const { label, type, properties, confidence } = data

  return (
    <Card className={`p-4 min-w-[200px] ${selected ? 'ring-2 ring-primary' : ''}`}>
      <Handle type="target" position={Position.Top} />
      
      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <Badge variant={type === 'Person' ? 'default' : 'secondary'}>
            {type}
          </Badge>
          {confidence && (
            <Badge variant="outline">
              {Math.round(confidence * 100)}%
            </Badge>
          )}
        </div>
        
        <h3 className="font-medium truncate" title={label}>
          {label}
        </h3>
        
        <div className="space-y-1">
          {Object.entries(properties).map(([key, value]) => (
            <div key={key} className="text-xs">
              <span className="text-muted-foreground">{key}:</span>{' '}
              <span className="truncate">{String(value)}</span>
            </div>
          ))}
        </div>
      </div>
      
      <Handle type="source" position={Position.Bottom} />
    </Card>
  )
}

export default memo(CustomNode) 