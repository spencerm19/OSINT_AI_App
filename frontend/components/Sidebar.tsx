'use client'

import { useState } from 'react'
import { Button } from './ui/button'
import {
  Search,
  Database,
  Network,
  Bot,
  Settings,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react'

export function Sidebar() {
  const [isCollapsed, setIsCollapsed] = useState(false)

  return (
    <div
      className={`bg-card border-r border-border transition-all duration-300 ${
        isCollapsed ? 'w-16' : 'w-64'
      }`}
    >
      <div className="flex flex-col h-full p-4">
        <div className="flex items-center justify-between mb-8">
          {!isCollapsed && <h2 className="text-xl font-bold">OSINT Buddy</h2>}
          <Button
            variant="ghost"
            size="icon"
            onClick={() => setIsCollapsed(!isCollapsed)}
          >
            {isCollapsed ? (
              <ChevronRight className="h-4 w-4" />
            ) : (
              <ChevronLeft className="h-4 w-4" />
            )}
          </Button>
        </div>

        <nav className="space-y-2">
          <Button
            variant="ghost"
            className="w-full justify-start"
            title="Search"
          >
            <Search className="h-4 w-4 mr-2" />
            {!isCollapsed && 'Search'}
          </Button>
          <Button
            variant="ghost"
            className="w-full justify-start"
            title="Data Sources"
          >
            <Database className="h-4 w-4 mr-2" />
            {!isCollapsed && 'Data Sources'}
          </Button>
          <Button
            variant="ghost"
            className="w-full justify-start"
            title="Graph"
          >
            <Network className="h-4 w-4 mr-2" />
            {!isCollapsed && 'Graph'}
          </Button>
          <Button
            variant="ghost"
            className="w-full justify-start"
            title="AI Assistant"
          >
            <Bot className="h-4 w-4 mr-2" />
            {!isCollapsed && 'AI Assistant'}
          </Button>
        </nav>

        <div className="mt-auto">
          <Button
            variant="ghost"
            className="w-full justify-start"
            title="Settings"
          >
            <Settings className="h-4 w-4 mr-2" />
            {!isCollapsed && 'Settings'}
          </Button>
        </div>
      </div>
    </div>
  )
} 