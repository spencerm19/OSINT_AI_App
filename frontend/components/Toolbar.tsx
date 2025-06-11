'use client'

import { Button } from './ui/button'
import {
  Plus,
  Link,
  Unlink,
  Copy,
  Trash,
  LayoutGrid,
  GitFork,
  Share2,
} from 'lucide-react'

export function Toolbar() {
  return (
    <div className="border-b border-border p-2">
      <div className="flex items-center space-x-2">
        <div className="flex items-center space-x-1 border-r border-border pr-2">
          <Button variant="ghost" size="icon" title="Add Node">
            <Plus className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" title="Add Edge">
            <Link className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" title="Remove Connection">
            <Unlink className="h-4 w-4" />
          </Button>
        </div>

        <div className="flex items-center space-x-1 border-r border-border pr-2">
          <Button variant="ghost" size="icon" title="Copy">
            <Copy className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" title="Delete">
            <Trash className="h-4 w-4" />
          </Button>
        </div>

        <div className="flex items-center space-x-1 border-r border-border pr-2">
          <Button variant="ghost" size="icon" title="Auto Layout">
            <LayoutGrid className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" title="Branch">
            <GitFork className="h-4 w-4" />
          </Button>
        </div>

        <div className="flex items-center space-x-1">
          <Button variant="ghost" size="icon" title="Share">
            <Share2 className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  )
} 