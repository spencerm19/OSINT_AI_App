'use client'

import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { Sidebar } from '@/components/ui/sidebar'
import { GraphView } from '@/components/graph/graph-view'
import { fetchResearch } from '@/lib/features/research/researchSlice'

export default function Home() {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchResearch())
  }, [dispatch])

  return (
    <main className="flex h-screen">
      <Sidebar />
      <div className="flex-1 p-4">
        <GraphView />
      </div>
    </main>
  )
} 