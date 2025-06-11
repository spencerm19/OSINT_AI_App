'use client'

import { useSelector, useDispatch } from 'react-redux'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Button } from '@/components/ui/button'
import { RootState } from '@/lib/store'
import { toggleSidebar } from '@/lib/features/ui/uiSlice'
import { setSelectedResearch } from '@/lib/features/research/researchSlice'
import { ChevronLeft, ChevronRight, Plus } from 'lucide-react'

export function Sidebar() {
  const dispatch = useDispatch()
  const { sidebarOpen } = useSelector((state: RootState) => state.ui)
  const { items, selectedId } = useSelector((state: RootState) => state.research)

  return (
    <div
      className={`border-r transition-all duration-300 ${
        sidebarOpen ? 'w-64' : 'w-16'
      }`}
    >
      <div className="flex items-center justify-between p-4 border-b">
        {sidebarOpen && <h2 className="text-lg font-semibold">Research</h2>}
        <Button
          variant="ghost"
          size="icon"
          onClick={() => dispatch(toggleSidebar())}
        >
          {sidebarOpen ? <ChevronLeft /> : <ChevronRight />}
        </Button>
      </div>

      {sidebarOpen && (
        <>
          <div className="p-4">
            <Button className="w-full">
              <Plus className="mr-2 h-4 w-4" />
              New Research
            </Button>
          </div>

          <ScrollArea className="h-[calc(100vh-8rem)]">
            <div className="p-4 space-y-2">
              {items.map((item) => (
                <Button
                  key={item.id}
                  variant={selectedId === item.id ? 'secondary' : 'ghost'}
                  className="w-full justify-start"
                  onClick={() => dispatch(setSelectedResearch(item.id))}
                >
                  {item.title}
                </Button>
              ))}
            </div>
          </ScrollArea>
        </>
      )}
    </div>
  )
} 