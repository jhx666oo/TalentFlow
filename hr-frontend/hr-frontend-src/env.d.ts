/// <reference types="vite/client" />

declare module 'echarts' {
  export interface ECharts {
    setOption(option: any): void
    resize(): void
    dispose(): void
  }

  export function init(element: HTMLElement): ECharts
}
